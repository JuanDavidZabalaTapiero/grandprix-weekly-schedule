from app.core.constants import DEFAULT_WEEK_TIME_SLOT_INSTRUCTORS
from app.database import get_connection


def register_default_week_time_slot_instructor(week_id):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO week_time_slot_instructors (week_id, time_slot_id, instructor_id) VALUES (?, ?, ?)",
            [
                (week_id, time_slot_id, instructor_id)
                for time_slot_id, instructor_id in DEFAULT_WEEK_TIME_SLOT_INSTRUCTORS
            ],
        )

        conn.commit()


def update_week_time_slot_instructor(id, instructor_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE week_time_slot_instructors SET instructor_id = ? WHERE id = ?",
            (instructor_id, id),
        )
        conn.commit()
