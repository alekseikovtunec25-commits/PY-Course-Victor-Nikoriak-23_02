import sys
from pathlib import Path

# знайти root проекту
ROOT = Path(__file__).resolve().parents[1]

# додати root у Python path
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
