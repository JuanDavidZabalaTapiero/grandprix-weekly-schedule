from app.database import get_connection


def get_time_slots(week_id, block_type):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                wtsi.id AS id,
                ts.label,
                i.id AS instructor_id,
                i.full_name AS instructor_name
            FROM time_slots ts
            LEFT JOIN week_time_slot_instructors wtsi ON ts.id = wtsi.time_slot_id AND wtsi.week_id = ?
            LEFT JOIN instructors i ON wtsi.instructor_id = i.id
            WHERE ts.block_type = ?
            ORDER BY ts.id
            """,
            (week_id, block_type),
        )

        return cursor.fetchall()
