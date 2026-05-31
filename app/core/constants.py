import holidays
from pathlib import Path

# PATH RAÍZ
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# DÍAS FESTIVOS
CO_HOLIDAYS = holidays.CO()

# DÍAS DE LA SEMANA
DAY_NAMES = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo",
}

# DB
DB_PATH = BASE_DIR / "db" / "app.db"

# TIME-SLOT INSTRUCTOR
DEFAULT_WEEK_TIME_SLOT_INSTRUCTORS = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 2),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
]
