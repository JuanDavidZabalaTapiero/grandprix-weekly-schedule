from app.core.constants import CO_HOLIDAYS, DAY_NAMES
from datetime import timedelta


def is_holiday(date):
    return date in CO_HOLIDAYS


def days_in_between(date_start, date_end):
    total_days = (date_end - date_start).days + 1
    return [
        date_start + timedelta(days=i)
        for i in range(total_days)
        if (date_start + timedelta(days=i)).weekday() != 6  # IGNORAR SÁBADO
    ]


def get_day_name(date):
    return DAY_NAMES[date.weekday()]


def get_day_number(date):
    return date.day
