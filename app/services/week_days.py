from app.database import get_connection


def register_week_day(week_id, date, day_name, day_number, is_holiday):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO week_days (week_id, date, day_name, day_number, is_holiday) VALUES (?, ?, ?, ?, ?)",
            (week_id, date, day_name, day_number, is_holiday),
        )
        conn.commit()

        return cursor.lastrowid


def get_week_day(week_day_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM week_days WHERE id = ?", (week_day_id,))

        return cursor.fetchone()


def get_week_days(week_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM week_days WHERE week_id = ?", (week_id,))

        return cursor.fetchall()
