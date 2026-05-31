from datetime import date, timedelta, datetime
from app.database import get_connection
from app.utils.dates import days_in_between, get_day_name, get_day_number, is_holiday
from app.services.week_days import register_week_day
from app.services.week_time_slot_instructors import (
    register_default_week_time_slot_instructor,
)
from app.services.classes import register_week_classes


def register_week(week_start, week_end):

    # REGISTRAR SEMANA
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weeks (week_start, week_end) VALUES (?, ?)",
            (week_start.isoformat(), week_end.isoformat()),
        )
        conn.commit()

        week_id = cursor.lastrowid

    # REGISTRAR DÍAS
    for day in days_in_between(week_start, week_end):
        register_week_day(
            week_id, day, get_day_name(day), get_day_number(day), is_holiday(day)
        )

    # REGISTRAR INSTRUCTOR-TIMESLOT DEFAULT
    register_default_week_time_slot_instructor(week_id)

    # REGISTRAR CLASES
    register_week_classes(week_id)

    return week_id


def register_current_week():
    today = date.today()

    # LUNES
    week_start = today - timedelta(days=today.weekday())

    # DOMINGO
    week_end = week_start + timedelta(days=6)

    return register_week(week_start, week_end)


def register_next_week(current_monday):

    # CONVERTIR A DATETIME
    current_monday = datetime.strptime(current_monday, "%Y-%m-%d").date()

    week_start = current_monday + timedelta(days=7)
    week_end = week_start + timedelta(days=6)

    return register_week(week_start, week_end)


def get_week(id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weeks WHERE id = ?", (id,))

        return cursor.fetchone()


def get_current_week():
    # YYYY-MM-DD
    today = date.today().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM weeks WHERE ? BETWEEN week_start AND week_end", (today,)
        )

        return cursor.fetchone()


def get_next_week(current_week_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM weeks WHERE id > ? ORDER BY id LIMIT 1", (current_week_id,)
        )

        return cursor.fetchone()
