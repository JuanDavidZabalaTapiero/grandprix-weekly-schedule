from datetime import datetime, timedelta
from collections import defaultdict
from app.services.weeks import get_week
from app.services.time_slots import get_time_slots
from app.services.week_days import get_week_days
from app.services.classes import get_classes_by_week


# ==== FUNCIONES AUXILIARES ====


def group_classes_by_day(classes):
    grouped = defaultdict(list)

    for c in classes:
        grouped[c["week_day_id"]].append(
            {
                "id": c["id"],
                "topic_id": c["topic_id"],
                "topic": c["topic_name"],
                "type": c["topic_type"],
            }
        )

    return grouped


def build_days(days, classes_by_day):
    return [
        {
            "day_name": d["day_name"],
            "day_number": d["day_number"],
            "is_holiday": d["is_holiday"],
            "classes": classes_by_day.get(d["id"], []),
        }
        for d in days
    ]


def serialize_time_slots(slots):
    return [
        {
            "id": t["id"],
            "time_slot": t["label"],
            "instructor_id": t["instructor_id"],
            "instructor": t["instructor_name"],
        }
        for t in slots
    ]


# ==== BUILD COMPLETO ====


def build_schedule(week_id):

    # DATA

    week = get_week(week_id)

    weekday_time_slots = get_time_slots(week_id, "weekday")
    saturday_time_slots = get_time_slots(week_id, "saturday")

    days = get_week_days(week_id)

    all_classes = get_classes_by_week(week_id)

    # GROUPING

    classes_by_day = group_classes_by_day(all_classes)

    weekday_days = [d for d in days if d["day_name"] != "Sábado"]

    saturday_days = [d for d in days if d["day_name"] == "Sábado"]

    # DATES
    week_end_dt = datetime.strptime(week["week_end"], "%Y-%m-%d").date()
    week_end = week_end_dt - timedelta(days=1)

    # FORMATEO: DD-MM-YYYY
    time_period_start = datetime.strptime(week["week_start"], "%Y-%m-%d").strftime(
        "%d-%m-%Y"
    )
    time_period_end = week_end.strftime("%d-%m-%Y")

    # RESPONSE
    return {
        "time_period_start": time_period_start,
        "time_period_end": time_period_end,
        "blocks": {
            "monday-friday": {
                "time_slots": serialize_time_slots(weekday_time_slots),
                "days": build_days(weekday_days, classes_by_day),
            },
            "saturday": {
                "time_slots": serialize_time_slots(saturday_time_slots),
                "days": build_days(saturday_days, classes_by_day),
            },
        },
    }
