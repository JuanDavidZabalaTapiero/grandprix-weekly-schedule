import random
from app.database import get_connection
from app.services.week_days import get_week_day, get_week_days
from app.services.topics import get_next_topic


def register_class(week_day_id, topic_id):

    # VALIDAR SI ES FESTIVO
    week_day = get_week_day(week_day_id)

    if week_day["is_holiday"]:
        return

    # REGISTRAR
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO classes (week_day_id, topic_id) VALUES (?, ?)",
            (week_day_id, topic_id),
        )
        conn.commit()

        return cursor.lastrowid


def register_week_day_classes(week_day_id, workshop_position=None):

    # A
    if workshop_position == "A":
        topic_a = get_next_topic("workshop")
    else:
        topic_a = get_next_topic("theory")

    # B
    if workshop_position == "B":
        topic_b = get_next_topic("workshop")
    else:
        topic_b = get_next_topic("theory")

    # C
    topic_c = get_next_topic("theory")

    # REGISTRAR
    structure = [
        topic_a["id"],
        topic_b["id"],
        topic_a["id"],
        topic_b["id"],
        topic_c["id"],
    ]

    for topic_id in structure:
        register_class(week_day_id, topic_id)


def register_saturday_classes(week_day_id):

    structure = [
        get_next_topic("theory")["id"],
        get_next_topic("theory")["id"],
        get_next_topic("theory")["id"],
        get_next_topic("theory")["id"],
    ]

    for topic_id in structure:
        register_class(week_day_id, topic_id)


def register_week_classes(week_id):

    week_days = get_week_days(week_id)

    # == LUNES - VIERNES ==
    monday_to_friday = week_days[:5]

    # WORKSHOP

    # Elegir 3 días aleatorios
    workshop_days = random.sample([day["id"] for day in monday_to_friday], 3)

    # Para cada día workshop: elegir aleatoriamente A o B como workshop
    workshop_positions = {}

    for week_day_id in workshop_days:
        workshop_positions[week_day_id] = random.choice(["A", "B"])

    # REGISTRAR CLASES
    for week_day in monday_to_friday:
        week_day_id = week_day["id"]

        register_week_day_classes(week_day_id, workshop_positions.get(week_day_id))

    # == SÁBADO ==
    saturday = week_days[5]
    register_saturday_classes(saturday["id"])


def get_classes_by_week(week_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                c.id,
                c.week_day_id,
                c.topic_id,
                t.name AS topic_name,
                t.type AS topic_type
            FROM classes c
            JOIN week_days wd ON c.week_day_id = wd.id
            JOIN topics t ON c.topic_id = t.id
            WHERE wd.week_id = ?
            ORDER BY c.week_day_id
            """,
            (week_id,),
        )

        return cursor.fetchall()


def update_class_topic(id, topic_id):

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE classes SET topic_id = ? WHERE id = ?", (topic_id, id))
        conn.commit()
