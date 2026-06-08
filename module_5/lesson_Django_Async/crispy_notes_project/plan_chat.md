╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
 Plan: crispy_notes_project — груповий чат (Django Channels + WebSocket)

 Контекст

 Попередня задача виконана — async views для Notes (143 тести проходять, README
 готовий).

 Нова задача: додати real-time груповий чат між членами Django Group.
 Мета — показати студентам РЕАЛЬНИЙ use case async: WebSocket = persistent
 connections, один event loop тримає тисячі відкритих з'єднань.

 Студент бачить що /groups/<pk>/chat/ — це сторінка зі звичайним HTTP (GET → HTML),
 але під капотом JavaScript відкриває WebSocket ws://host/ws/groups/<pk>/chat/ і всі
 повідомлення приходять миттєво без перезавантаження.

 Поточний стан проєкту

 - Django 5.2, SQLite, Bootstrap 5.3.3 dark theme, Bootstrap Icons 1.11.3
 - Groups: вбудована django.contrib.auth.models.Group, members через
 group.user_set.all()
 - base.html має {% block extra_css %} і {% block extra_js %}
 - Static: hello_app/static/hello_app/css/app.css (є), JS-директорії немає
 - hello_project/asgi.py → application = get_asgi_application() (треба замінити)
 - requirements.txt → uvicorn вже є, channels немає

 ---
 Нові файли (створити)

 hello_project/routing.py                              ← WebSocket URL patterns
 hello_app/consumers.py                                ← AsyncWebsocketConsumer
 hello_app/static/hello_app/js/group_chat.js           ← JS WebSocket клієнт
 hello_app/templates/hello_app/group_chat.html         ← Bootstrap 5 chat UI

 Модифіковані файли

 requirements.txt                     — додати channels>=4.0
 hello_project/settings.py            — INSTALLED_APPS + CHANNEL_LAYERS
 hello_project/asgi.py                — ProtocolTypeRouter (HTTP + WebSocket)
 hello_app/models.py                  — ChatMessage model
 hello_app/views.py                   — group_chat HTTP view
 hello_app/urls.py                    — /groups/<pk>/chat/ URL
 hello_app/templates/hello_app/group_detail.html — кнопка "Відкрити чат"
 hello_app/static/hello_app/css/app.css           — chat bubble styles

 ---
 Порядок виконання

 Крок 1 — requirements.txt

 Додати рядок channels>=4.0 (після uvicorn, з навчальним коментарем).
 channels-redis і daphne НЕ потрібні — використовуємо InMemoryChannelLayer.

 Крок 2 — hello_project/settings.py

 a) INSTALLED_APPS — додати "channels" після "debug_toolbar", перед "hello_app":
     "channels",    # Django Channels — WebSocket підтримка

 b) CHANNEL_LAYERS — новий блок після DB config:
 CHANNEL_LAYERS = {
     "default": {
         "BACKEND": "channels.layers.InMemoryChannelLayer",
         # InMemoryChannelLayer: зберігає повідомлення в RAM процесу.
         # Тільки для розробки (один процес). Production → RedisChannelLayer.
     }
 }
 Великий навчальний коментар: що таке channel layer, як group_send доставляє
 повідомлення всім subscriber-ам.

 Крок 3 — hello_app/models.py

 Додати ChatMessage після останньої моделі (перед class Meta файлу):
 class ChatMessage(models.Model):
     group     = models.ForeignKey(Group, on_delete=models.CASCADE,
 related_name='chat_messages')
     author    = models.ForeignKey(User, on_delete=models.CASCADE,
 related_name='chat_messages')
     content   = models.TextField()
     timestamp = models.DateTimeField(auto_now_add=True)

     class Meta:
         ordering = ['timestamp']
         indexes = [models.Index(fields=['group', 'timestamp'],
 name='chat_group_ts_idx')]
 Міграція: python manage.py makemigrations && python manage.py migrate

 Крок 4 — hello_project/routing.py (новий файл)

 from django.urls import re_path
 from hello_app import consumers

 websocket_urlpatterns = [
     re_path(r'^ws/groups/(?P<group_pk>\d+)/chat/$',
 consumers.GroupChatConsumer.as_asgi()),
 ]
 Коментар: чому re_path (не path) — Channels URLRouter потребує іменовану групу для
 scope['url_route']['kwargs'].

 Крок 5 — hello_project/asgi.py

 Замінити application = get_asgi_application() на ProtocolTypeRouter:
 django_asgi_app = get_asgi_application()  # ПЕРЕД імпортом consumers!

 from channels.routing import ProtocolTypeRouter, URLRouter
 from channels.auth import AuthMiddlewareStack
 from hello_project.routing import websocket_urlpatterns

 application = ProtocolTypeRouter({
     "http": django_asgi_app,
     "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
 })
 КРИТИЧНО: get_asgi_application() має бути викликаний ДО from hello_app import
 consumers — інакше AppRegistryNotReady.
 Зберегти весь наявний навчальний docstring, додати коментарі про ProtocolTypeRouter і
 AuthMiddlewareStack.

 Крок 6 — hello_app/consumers.py (новий файл)

 GroupChatConsumer(AsyncWebsocketConsumer) з 4 методами:

 connect():
 - self.user = self.scope['user'] (AuthMiddlewareStack вже заповнив)
 - якщо not self.user.is_authenticated → await self.close(); return
 - self.group_pk = int(self.scope['url_route']['kwargs']['group_pk'])
 - await self.check_membership(group_pk, user) → якщо False → await self.close();
 return
 - self.room_group_name = f"chat_group_{self.group_pk}"
 - await self.channel_layer.group_add(self.room_group_name, self.channel_name)
 - await self.accept()
 - messages = await self.load_history(self.group_pk) → надіслати кожне type='history'

 disconnect(close_code):
 - await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
 якщо room_group_name існує

 receive(text_data):
 - data = json.loads(text_data), content = data.get('content','').strip()
 - msg = await self.save_message(group_pk, user, content)
 - await self.channel_layer.group_send(room_group_name, {'type': 'chat_message',
 'author': username, 'content': content, 'timestamp': msg.timestamp.isoformat(),
 'message_id': msg.id})

 chat_message(event):
 - await self.send(text_data=json.dumps({...event data..., 'type': 'message'}))

 DB helpers (декоратор @database_sync_to_async):
 - check_membership(group_pk, user) —
 Group.objects.get(pk).user_set.filter(pk=user.pk).exists()
 - load_history(group_pk) —
 list(ChatMessage.objects.filter(group_id=group_pk).select_related('author').order_by(
 '-timestamp')[:50].values('id','author__username','content','timestamp')) →
 .reverse() → повернути list
 - save_message(group_pk, user, content) — ChatMessage.objects.create(...)

 КРИТИЧНО в load_history: .values(...) + list() виконує SQL IN the thread і повертає
 plain Python dict — безпечно передавати між потоками. Lazy QuerySet НЕ повертати.

 Великий навчальний docstring на початку файлу: що таке consumer, HTTP flow vs
 WebSocket flow, channel layer pub/sub.

 Крок 7 — hello_app/views.py

 Додати group_chat view (sync, @login_required):
 @login_required
 def group_chat(request, pk):
     group = get_object_or_404(Group, pk=pk)
     if not group.user_set.filter(pk=request.user.pk).exists():
         messages.error(request, 'Ти не є членом цієї групи.')
         return redirect('hello_app:group_list')
     return render(request, 'hello_app/group_chat.html', {'group': group})
 Коментар: ця view тільки рендерить HTML-сторінку. Реальний чат відбувається через
 WebSocket.

 Крок 8 — hello_app/urls.py

 Додати в секцію Groups:
 path('groups/<int:pk>/chat/', views.group_chat, name='group_chat'),

 Крок 9 — hello_app/templates/hello_app/group_detail.html

 Додати картку "Груповий чат" у праву колонку (col-md-6), між "Додати учасника" і
 "Небезпечна зона":
 <div class="card shadow-sm mb-3 border-primary">
   <div class="card-body d-flex justify-content-between align-items-center">
     <div>
       <h6 class="fw-semibold mb-1">
         <i class="bi bi-chat-dots me-2 text-primary"></i>Груповий чат
       </h6>
       <small class="text-muted">Реальний час · WebSocket · Django Channels</small>
     </div>
     <a href="{% url 'hello_app:group_chat' group.pk %}" class="btn btn-primary">
       <i class="bi bi-chat-dots me-1"></i>Відкрити чат
     </a>
   </div>
 </div>

 Крок 10 — hello_app/templates/hello_app/group_chat.html (новий файл)

 Структура:
 {% extends 'layouts/dashboard.html' %}
 {% load static %}

 {% block topbar_title %}Чат групи: {{ group.name }}{% endblock %}

 {% block content %}
   <!-- Status bar: "з'єднуємось..." / "підключено" / "відключено" -->
   <!-- Message feed: div#chat-messages — scrollable, flex-grow-1 -->
   <!-- Input bar: form#chat-form з text input + кнопка Send -->
   <!-- data-config: div#chat-config data-group-pk data-username (hidden) -->
 {% endblock %}

 {% block extra_js %}
 <script src="{% static 'hello_app/js/group_chat.js' %}"></script>
 {% endblock %}
 Не використовувати inline <script> з {{ group.pk }} всередині — передавати дані через
 data-атрибути прихованого div.

 Крок 11 — hello_app/static/hello_app/js/group_chat.js (новий файл)

 IIFE (function() { 'use strict'; ... }()) з:
 1. Читання data-group-pk і data-username з #chat-config
 2. const wsUrl = \${protocol}://${location.host}/ws/groups/${GROUP_PK}/chat/``
 3. connect() → new WebSocket(wsUrl) → onopen/onmessage/onerror/onclose
 4. onmessage → appendMessage(data) для type='history' і type='message'
 5. formEl.addEventListener('submit', ...) → socket.send(JSON.stringify({content}))
 6. appendMessage(data) → Bootstrap flex bubble, isMine → justify-content-end
 7. escapeHtml(str) → захист від XSS (&, <, >, ", ')
 8. Автопідключення при onclose коди не 1000 (setTimeout(connect, 3000))

 Великий навчальний коментар: HTTP flow vs WebSocket flow, WebSocket API браузера.

 Крок 12 — hello_app/static/hello_app/css/app.css

 Додати розділ /* 9. CHAT BUBBLES */ в кінець файлу:
 .chat-bubble { max-width: 70%; padding: .5rem .85rem; border-radius: 14px; ... }
 .chat-mine   { background: var(--accent); color: #fff; border-bottom-right-radius:
 4px; }
 .chat-other  { background: var(--card-bg); border: 1px solid var(--card-border); ...
 }
 .chat-author { font-size: .75rem; font-weight: 600; color: var(--text-secondary); }
 .chat-time   { font-size: .7rem; color: rgba(255,255,255,.55); text-align: right; }
 .chat-other .chat-time { color: var(--text-secondary); }

 ---
 Навчальна архітектура — ключові концепції для коментарів у коді

 Browser                Django (ASGI / uvicorn)
 ──────                 ──────────────────────
 GET /groups/7/chat/ ──► group_chat(view) ──► group_chat.html (HTML + JS)
                                                   │
 ws://host/ws/groups/7/chat/ ══════════════► GroupChatConsumer.connect()
                                                   │
                                             channel_layer.group_add("chat_group_7",
 self.channel_name)
                                                   │
 JS: socket.send({content}) ══════════════► GroupChatConsumer.receive()
                                                   │ save_message() → DB
                                             channel_layer.group_send("chat_group_7",
 {...})
                                                   │
                                      ┌────────────┴────────────┐
                               consumer A                  consumer B
                           chat_message()            chat_message()
                                │                         │
                           socket.send()            socket.send()
                                │                         │
                           Browser A                Browser B
                        (Viktor бачить)          (Oля бачить)

 ---
 Верифікація

 # 1. Встановити channels
 pip install "channels>=4.0"

 # 2. Міграція
 python manage.py makemigrations hello_app
 python manage.py migrate

 # 3. Перевірка конфігурації
 python manage.py check

 # 4. Запустити ASGI-сервер (обов'язково uvicorn — runserver не підтримує WebSocket)
 uvicorn hello_project.asgi:application --reload --port 8001

 # 5. Ручне тестування:
 #    - Зайти на http://127.0.0.1:8001/groups/ → відкрити групу → кнопка "Відкрити
 чат"
 #    - Відкрити той самий чат у двох вкладках браузера
 #    - Написати повідомлення в одній → воно з'являється в іншій МИТТЄВО
 #    - Перезавантажити сторінку → повідомлення збереглись (history з DB)

 # 6. Тести (143 існуючих не повинні зламатись)
 python manage.py test hello_app -v 1

 Перевірка WebSocket вручну в DevTools:
 // F12 → Console на http://127.0.0.1:8001/groups/7/chat/
 ws = new WebSocket('ws://127.0.0.1:8001/ws/groups/7/chat/')
 ws.onmessage = e => console.log(JSON.parse(e.data))
 ws.send(JSON.stringify({content: 'тест'}))
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌