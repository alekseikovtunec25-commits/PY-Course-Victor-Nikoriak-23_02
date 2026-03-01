# PY_Curse_Victor-Nikoriak-23_02

# Python Course 23-02-2026 — Repo for Students

Ласкаво просимо 👋  
Цей репозиторій — **матеріали уроків** + **процес здачі домашок через GitHub** (як у реальній команді).

---

# ⚙️ 0. Встановлення Git (ОБОВʼЯЗКОВО)

Перед початком роботи потрібно встановити **Git**.

Git — це система контролю версій, через яку ми здаємо домашні завдання.

---

## 🪟 Windows

👉 Офіційна сторінка встановлення:

https://git-scm.com/install/windows

✅ Пряме завантаження (рекомендовано):

https://github.com/git-for-windows/git/releases/latest

Завантажте:

```

Git for Windows/x64 Setup

````

### Під час встановлення
Можна **всюди натискати Next** (налаштування за замовчуванням підходять).

---

## 🍎 macOS

👉 Інструкція:

https://git-scm.com/install/mac

Найпростіший спосіб:

Відкрийте Terminal і виконайте:

```bash
xcode-select --install
````

macOS автоматично встановить Git.

---

## 🐧 Linux

👉 Інструкція:

[https://git-scm.com/install/linux](https://git-scm.com/install/linux)

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

### Fedora

```bash
sudo dnf install git
```

### Arch Linux

```bash
sudo pacman -S git
```

---

## ✅ Перевірка встановлення

Відкрийте Terminal / Command Prompt:

```bash
git --version
```

Ви повинні побачити приблизно:

```
git version 2.xx.x
```

---

## ✅ Перше налаштування Git (1 раз)

Виконайте:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

⚠️ Використовуйте той email, який прив’язаний до GitHub.

---

---

# 🧭 Як ми працюємо

* **`main`** — це матеріали курсу (оновлюються викладачем)
* Домашка робиться у **власній гілці**
* Здача = **Pull Request (PR)**
* Викладач не додає студентський код у `main`

---

````

---

✅ Тепер у тебе README починається **правильно професійно**:

1. Git install  
2. Git setup  
3. Workflow  

---

💡 Маленька порада (дуже практична):

На першому занятті попроси студентів виконати:

```bash
git --version
````

```markdown
# Python Course 2026 — Repo for Students

Ласкаво просимо 👋  
Цей репозиторій — **матеріали уроків** + **процес здачі домашок через GitHub** (як у реальній команді).

---

## Як ми працюємо

- **`main`** — це **матеріали курсу** (оновлюються викладачем).
- **Домашка** робиться **в окремій гілці** (`homework-XX`).
- **Здача** = **Pull Request (PR)**.
- Викладач **не мерджить** ваш код у `main` (щоб курс залишався чистим).

---

## Швидкий старт (1 раз)

### 1) Fork репозиторію (в браузері GitHub)
1. Відкрийте цей репозиторій на GitHub.
2. Натисніть **Fork** (праворуч вгорі).
3. У вас з’явиться копія: `github.com/<ваш_нік>/python-course-2026`

### 2) Clone у PyCharm
PyCharm → **File → New Project from Version Control**  
Вставте URL **вашого форку**:
```

[https://github.com/](https://github.com/)<ваш_нік>/python-course-2026

````

### 3) Додайте upstream (1 раз)
У PyCharm → Terminal виконайте:
```bash
git remote add upstream https://github.com/<TEACHER_ORG_OR_NICK>/python-course-2026
````

Перевірка:

```bash
git remote -v
```

Очікувано:

* `origin` → ваш репозиторій
* `upstream` → репозиторій викладача

---

## Перед кожним заняттям (оновити матеріали)

У PyCharm → Terminal:

```bash
git checkout main
git pull upstream main
git push origin main
```

> Якщо щось не пішло — див. розділ “Проблеми”.

---

## Домашнє завдання (кожен раз)

### Правило №1: НЕ ПРАЦЮЄМО В `main`

`main` — тільки щоб підтягувати нові уроки.

### Кроки для домашки

1. Створіть гілку під конкретний урок:

```bash
git checkout -b homework-01
```

2. Виконайте завдання (редагуйте потрібні файли/ноутбук).

3. Збережіть зміни (commit):

```bash
git add .
git commit -m "Homework 01"
```

4. Відправте гілку на GitHub:

```bash
git push origin homework-01
```

5. Здайте домашку через Pull Request:

* Відкрийте ваш GitHub репозиторій
* Натисніть **Compare & Pull Request**
* Створіть PR: `homework-01` → `main` (вашого форку або репо викладача — як скаже викладач)

> **PR = здача домашки.**
> Викладач залишить коментарі, ви зробите правки і запушите ще раз у ту саму гілку — PR оновиться автоматично.

---

## Як отримати фідбек і здати повторно

1. Викладач залишив коментарі в PR
2. Ви робите правки **в цій же гілці** (`homework-01`)
3. Комітите і пушите:

```bash
git add .
git commit -m "Fix after review"
git push origin homework-01
```

4. PR оновиться сам

---

## Правила курсу

* ✅ `main` **не чіпати** (не робити домашку в `main`)
* ✅ 1 домашка = 1 гілка (`homework-XX`)
* ✅ Назви гілок: `homework-01`, `homework-02`, ...
* ✅ Коміти з нормальними повідомленнями: `Homework 03`, `Fix after review`
* ❌ Не видаляйте файли уроків без потреби
* ❌ Не мерджте чужі гілки у свій `main`

---

## Часті проблеми

### 1) “Я не бачу нові уроки”

Зробіть оновлення:

```bash
git checkout main
git pull upstream main
```

### 2) “Я зробив домашку в main, що робити?”

Найпростіше: створіть нову гілку з поточного стану і працюйте далі вже правильно:

```bash
git checkout -b homework-XX
```

Потім поверніться в `main`, оновіть його з upstream:

```bash
git checkout main
git pull upstream main
```

### 3) “Permission denied / не можу push”

Причина майже завжди одна:

* ви клонували **репозиторій викладача**, а не **свій форк**.

Рішення:

* клонувати `github.com/<ваш_нік>/python-course-2026`
* або змінити `origin` на ваш репозиторій.

---

## Корисні команди (шпаргалка)

Показати гілки:

```bash
git branch
```

Перейти в гілку:

```bash
git checkout homework-01
```

Створити гілку:

```bash
git checkout -b homework-01
```

Статус змін:

```bash
git status
```

Коміти:

```bash
git log --oneline
```

---

## Контакт / питання

Якщо щось зламалось — кидайте:

* скрін помилки
* вивід `git remote -v`
* вивід `git status`

І ми швидко поправимо 🙂

