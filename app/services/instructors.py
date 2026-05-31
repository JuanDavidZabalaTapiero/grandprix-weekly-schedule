from app.database import get_connection


def get_all_instructors():

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM instructors ORDER BY id")

        return cursor.fetchall()
