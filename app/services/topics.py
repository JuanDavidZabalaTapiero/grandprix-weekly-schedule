from app.database import get_connection


# INDEX
def get_last_index(type):

    setting_key = f"current_{type}_topic_index"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM settings WHERE key = ?", (setting_key,))
        row = cursor.fetchone()

        return int(row["value"])


def update_last_index(type, topic_id):

    setting_key = f"current_{type}_topic_index"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (setting_key, topic_id),
        )
        conn.commit()


# TOPICS
def get_next_topic(type):

    last_topic_id = get_last_index(type)

    with get_connection() as conn:
        cursor = conn.cursor()

        # CONSULTAR

        # siguiente id
        cursor.execute(
            "SELECT id, name FROM topics WHERE type = ? AND id > ? ORDER BY id LIMIT 1",
            (type, last_topic_id),
        )
        topic = cursor.fetchone()

        # volver al inicio
        if not topic:
            cursor.execute(
                "SELECT id, name FROM topics WHERE type = ? ORDER BY id LIMIT 1",
                (type,),
            )

            topic = cursor.fetchone()

        # ACTUALIZAR INDEX
        update_last_index(type, topic["id"])

        return topic


def get_all_topics():

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM topics ORDER BY id")

        return cursor.fetchall()
