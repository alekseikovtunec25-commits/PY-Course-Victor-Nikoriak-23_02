"""
Reusable exam widget for all course lessons.

Usage in a notebook cell:
    from tools.exam_engine import make_exam_widget
    display(make_exam_widget("lesson_04_exam", lambda: STUDENT_NAME, require_student))
"""

import ast, uuid, time, re, html, json, os
import requests
import ipywidgets as widgets
from IPython.display import display, clear_output


# ── API URL ────────────────────────────────────────────────────────────────────

def _load_api_url() -> str:
    cfg = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(cfg, encoding="utf-8") as f:
            return json.load(f)["api_url"]
    except Exception:
        return (
            "https://script.google.com/macros/s/"
            "AKfycbzVDiNm9hDGInd7s_G-iBA2rsw6NF2BCfdzYlZ4WOwRawKQU0LH4oLrVNup3krfJwsM/exec"
                )

_API_URL = _load_api_url()


# ── Syntax highlighting (pygments is bundled with Jupyter) ────────────────────

try:
    from pygments import highlight as _pyg_hl
    from pygments.lexers import PythonLexer as _PyLex
    from pygments.formatters import HtmlFormatter as _HtmlFmt
    _LEXER = _PyLex()
    _FMT   = _HtmlFmt(nowrap=True, style="monokai", noclasses=True)
    _HAS_PYGMENTS = True
except ImportError:
    _HAS_PYGMENTS = False


def _highlight(code: str) -> str:
    """Return syntax-coloured HTML for a Python snippet."""
    if _HAS_PYGMENTS:
        return _pyg_hl(code, _LEXER, _FMT)
    return html.escape(code)


# ── Code formatter ────────────────────────────────────────────────────────────

def _expand_semicolons(code: str) -> list:
    """
    Split 'a; b; c' → ['a', 'b', 'c'].
    Respects quoted strings and escape sequences.
    """
    parts, current, in_str = [], [], None
    i = 0
    while i < len(code):
        ch = code[i]
        if in_str:
            current.append(ch)
            if ch == "\\" and i + 1 < len(code):
                i += 1
                current.append(code[i])
            elif ch == in_str:
                in_str = None
        elif ch in ('"', "'"):
            in_str = ch
            current.append(ch)
        elif ch == ";":
            s = "".join(current).strip()
            if s:
                parts.append(s)
            current = []
        else:
            current.append(ch)
        i += 1
    s = "".join(current).strip()
    if s:
        parts.append(s)
    return parts


def _format_code_py(code: str) -> str:
    """
    Convert compact exam-style code to properly indented Python.

    Pipeline:
      1. Strip trailing '?' (end-of-question punctuation)
      2. Expand semicolons → separate lines
      3. ast.parse() + ast.unparse() for proper indentation
         e.g. 'if x>2: y=1'  →  'if x > 2:\\n    y = 1'
      4. Fallback to semicolon-expanded text on SyntaxError
    """
    code = code.strip().rstrip("?").strip()
    if not code:
        return ""
    lines = _expand_semicolons(code)
    normalized = "\n".join(lines)
    try:
        tree = ast.parse(normalized)
        return ast.unparse(tree)
    except SyntaxError:
        return normalized


# Trigger keywords that precede a code snippet after ":"
# Groups: (1) before+trigger  (2) code  (3) optional "якщо/при..." context  (4) "?"
#
# Examples handled:
#   "Що виведе код: print(x)?"                   → trigger=код
#   "Що буде виведено: x=1; print(x)?"           → trigger=виведено
#   "Що буде виведено: print(x) якщо x=5?"       → trigger=виведено, context=якщо x=5
#   "Який результат: a+b?"                        → trigger=результат
_CODE_TRIGGER = re.compile(
    r"^(.*?(?:\b(?:код(?:у|и|ом|і)?|виведено|результат|вивід|станеться)|(?:який|що)\s+містить))\s*:\s*"
    r"(.+?)"
    r"(\s+(?:якщо|при|коли|після)\b.*)?"
    r"(\?)?$",
    flags=re.I | re.S,
)


def render_question_html(text: str) -> str:
    """
    Return safe HTML for one exam question:
      • question text in <div class='question-text'>
      • syntax-highlighted <pre class='code-block'> when code is detected

    Detection priority:
      1. Ukrainian trigger (код/виведено/результат/вивід) followed by ":"
         Context after "якщо/при/коли" is appended to the question text.
      2. Multi-line text — first line = question, rest = code
      3. Plain text — no code block

    Never raises — always returns valid HTML.
    """
    try:
        raw = (text or "").strip()
        if not raw:
            return "<div class='question-text'>(порожнє питання)</div>"

        m = _CODE_TRIGGER.search(raw)
        if m:
            before    = m.group(1).strip()
            code_src  = m.group(2).strip()
            context   = (m.group(3) or "").strip()  # e.g. "якщо запуск: python s.py a b"
            q_mark    = m.group(4) or ""
            code_fmt  = _format_code_py(code_src)
            code_html = _highlight(code_fmt)
            # Reconstruct readable question: "Що буде виведено, якщо запуск: ...?"
            q_text = f"{before}, {context}{q_mark}" if context else f"{before}{q_mark}"
            return (
                f"<div class='question-text'>{html.escape(q_text)}</div>"
                f"<pre class='code-block'>{code_html}</pre>"
            )

        if "\n" in raw:
            first, rest = raw.split("\n", 1)
            rest = rest.strip()
            if rest:
                code_fmt  = _format_code_py(rest)
                code_html = _highlight(code_fmt)
                return (
                    f"<div class='question-text'>{html.escape(first.strip())}</div>"
                    f"<pre class='code-block'>{code_html}</pre>"
                )

        return f"<div class='question-text'>{html.escape(raw)}</div>"

    except Exception:
        return f"<div class='question-text'>{html.escape(str(text or ''))}</div>"


# ── Level constants ────────────────────────────────────────────────────────────

LEVEL_ORDER = ["bronze", "silver", "gold", "platinum"]
LEVEL_LABELS = {
    "bronze":   "🟢 Bronze",
    "silver":   "🟡 Silver",
    "gold":     "🟠 Gold",
    "platinum": "🔴 Platinum",
}


# ── Internal question widget ───────────────────────────────────────────────────

def _make_question_widget(q: dict, submit_fn) -> widgets.VBox:
    tid   = q.get("id", "")
    qtext = q.get("question", "")
    code  = (q.get("code") or "").strip()
    opts  = [str(o) for o in q.get("options", []) if str(o).strip()]

    # New format: dedicated code field → highlight directly, no regex needed.
    # Legacy format (no code field): fall back to render_question_html() heuristics.
    if code:
        inner = (
            f"<div class='question-text'>{html.escape(qtext)}</div>"
            f"<pre class='code-block'>{_highlight(code)}</pre>"
        )
    else:
        inner = render_question_html(qtext)

    q_w   = widgets.HTML(f"<div class='question-card'>{inner}</div>")
    opt_w = widgets.RadioButtons(options=opts, layout=widgets.Layout(width="100%"))
    btn_w = widgets.Button(description="Перевірити", button_style="primary")
    out_w = widgets.Output()
    _done = [False]

    def _click(_):
        if _done[0]:
            return
        _done[0] = True
        btn_w.disabled = True
        ans = opt_w.value

        with out_w:
            clear_output()
            display(widgets.HTML("<div class='muted'>⏳ Перевірка...</div>"))

        resp = submit_fn(tid, ans)
        prog = resp.get("progress", {})
        ok   = prog.get("correct", False)
        pct  = prog.get("score_pct", "—")
        cnt  = prog.get("correct_count", "—")
        n    = prog.get("answered", "—")

        with out_w:
            clear_output()
            icon = (
                "<div class='correct'>✅ Правильно!</div>"
                if ok else
                "<div class='wrong'>❌ Неправильно</div>"
            )
            display(widgets.HTML(
                f"{icon}<div class='muted'>📊 Загалом: {cnt}/{n} ({pct}%)</div>"
            ))

    btn_w.on_click(_click)
    return widgets.VBox(
        [q_w, opt_w, btn_w, out_w],
        layout=widgets.Layout(margin="0 0 14px 0"),
    )


# ── Public: make_exam_widget ───────────────────────────────────────────────────

def make_exam_widget(
    lesson_id: str,
    get_student_name,
    require_student_fn,
) -> widgets.VBox:
    """
    Build a Voilà-compatible exam widget.

    Args:
        lesson_id:          e.g. "lesson_05_exam"
        get_student_name:   callable → str | None   (returns current STUDENT_NAME)
        require_student_fn: callable → bool          (prints error if not ready)

    Returns:
        widgets.VBox — pass directly to display() in the notebook cell.

    Voilà note:
        Questions are rendered by mutating questions_box.children (not via display()),
        which propagates over the WebSocket without needing an Output context.
    """
    start_btn     = widgets.Button(
        description="▶ Завантажити іспит",
        button_style="success",
        layout=widgets.Layout(width="220px"),
    )
    status_out    = widgets.Output()
    questions_box = widgets.VBox([])

    def _on_start(b):
        if not require_student_fn():
            with status_out:
                clear_output()
                print("⛔ Спочатку представтесь")
            return

        b.disabled    = True
        b.description = "⏳ Завантаження..."

        with status_out:
            clear_output()
            print("⏳ Підключення до сервера...")

        name = get_student_name()

        try:
            sess = requests.get(
                _API_URL,
                params={"name": name, "lesson_id": lesson_id},
                timeout=20,
            ).json()
        except Exception as ex:
            with status_out:
                clear_output()
                print("❌ Помилка з'єднання:", ex)
            b.disabled    = False
            b.description = "▶ Завантажити іспит"
            return

        if not sess.get("ok"):
            with status_out:
                clear_output()
                print("❌ Помилка сесії:", sess.get("error"))
            return

        token = sess["token"]

        try:
            qr = requests.get(
                _API_URL,
                params={"action": "questions", "token": token},
                timeout=20,
            ).json()
        except Exception as ex:
            with status_out:
                clear_output()
                print("❌ Помилка завантаження питань:", ex)
            return

        if not qr.get("ok"):
            with status_out:
                clear_output()
                print("❌ Питання не завантажено:", qr.get("error"))
            return

        questions = qr.get("questions", [])

        with status_out:
            clear_output()
            print(f"✅ Завантажено {len(questions)} питань  |  {name}, починайте!")

        def _submit(task_id, answer):
            try:
                r = requests.post(
                    _API_URL,
                    json={
                        "token":     token,
                        "task_id":   task_id,
                        "result":    {"answer": answer},
                        "nonce":     str(uuid.uuid4()),
                        "client_ts": int(time.time() * 1000),
                    },
                    timeout=20,
                )
                return r.json()
            except Exception as ex:
                return {"ok": False, "error": str(ex)}

        by_level = {}
        for q in questions:
            lvl = (q.get("level") or "").lower().strip()
            by_level.setdefault(lvl, []).append(q)

        children = []
        for lvl in LEVEL_ORDER:
            qs = by_level.get(lvl, [])
            if not qs:
                continue
            label = LEVEL_LABELS.get(lvl, lvl.title())
            children.append(widgets.HTML(
                f"<h2 class='{lvl}' style='margin-top:22px'>{label}</h2>"
            ))
            for q in qs:
                children.append(_make_question_widget(q, _submit))

        # Voilà-compatible: mutate .children instead of calling display()
        questions_box.children = tuple(children)

    start_btn.on_click(_on_start)
    return widgets.VBox([start_btn, status_out, questions_box])
