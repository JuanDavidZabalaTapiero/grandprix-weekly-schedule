from app.database import get_connection


def get_note():

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes LIMIT 1")

        return cursor.fetchone()


def update_note(text):

    note = get_note()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (text, note["id"]))
        conn.commit()
