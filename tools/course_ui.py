from IPython.display import HTML, display

def activate():
    display(HTML("""
<style>

/* ------------------------
GLOBAL LAYOUT
------------------------ */

.jp-Notebook {
    font-size:20px !important;
    line-height:1.6;
}

.jp-Notebook .jp-Cell {
    max-width:900px;
    margin:auto;
}

/* ------------------------
HEADINGS
------------------------ */

h1 {font-size:42px !important;}
h2 {font-size:32px !important;}
h3 {font-size:26px !important;}

/* ------------------------
QUESTION CARD
------------------------ */

.question-card{
    max-width:720px;
    background:white;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:24px;
    margin:20px 0;
    box-shadow:0 3px 8px rgba(0,0,0,0.05);
}

/* ------------------------
QUESTION TEXT
------------------------ */

.question-text{
    font-size:20px;
    margin-bottom:12px;
}

/* ------------------------
RADIO OPTIONS
------------------------ */

.widget-radio-box{
    display:flex;
    flex-direction:column;
    gap:8px;
    margin-left:4px !important;
}

.widget-radio-box label{
    font-size:18px !important;
}

/* ------------------------
RADIO SIZE
------------------------ */

input[type="radio"]{
    transform:scale(1.4);
    margin-right:10px;
}

/* ------------------------
INPUT FIELD
------------------------ */

.widget-text input{
    font-size:18px !important;
    padding:8px !important;
    height:38px !important;
}

/* ------------------------
BUTTONS
------------------------ */

.widget-button{
    font-size:16px !important;
    padding:10px 22px !important;
    min-height:40px !important;
    border-radius:10px !important;
    margin-top:12px !important;
}

/* ------------------------
LEVEL TITLES
------------------------ */

.bronze{
font-size:28px;
font-weight:700;
color:#cd7f32;
}

.silver{
font-size:28px;
font-weight:700;
color:#9aa0a6;
}

.gold{
font-size:28px;
font-weight:700;
color:#f4b400;
}

.code-block {
    background:#1e1e1e;
    color:#d4d4d4;
    padding:14px 16px;
    border-radius:8px;
    font-family:"Fira Code", monospace;
    font-size:15px;
    margin:10px 0;
    white-space:pre;
}

/* ------------------------
RESULT TEXT
------------------------ */

.correct{
color:#16a34a;
font-size:20px;
font-weight:600;
}

.wrong{
color:#dc2626;
font-size:20px;
font-weight:600;
}

/* ------------------------
PROGRESS BAR
------------------------ */

.progress{
width:100%;
height:12px;
background:#e5e7eb;
border-radius:10px;
overflow:hidden;
margin:12px 0;
}

.progress-bar{
height:100%;
background:#22c55e;
}

/* ------------------------
TASK BLOCK SPACING
------------------------ */

.task{
margin-bottom:30px;
}

</style>
"""))
