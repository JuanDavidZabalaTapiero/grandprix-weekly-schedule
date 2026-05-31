schedule = {
    "time_period_start": "2026-05-18",
    "time_period_end": "2026-05-23",
    "blocks": {
        "monday-friday": {
            "time_slots": [
                {"time_slot": "7:00 AM - 9:00 AM", "instructor": "Pablo"},
                {"time_slot": "9:00 AM - 11:00 AM", "instructor": "Pablo"},
                {"time_slot": "4:00 PM - 6:00 PM", "instructor": "Pablo"},
                {"time_slot": "6:00 PM - 8:00 PM", "instructor": "Pablo"},
                {"time_slot": "8:00 PM - 10:00 PM", "instructor": "Daniel"},
            ],
            "days": [
                {
                    "day_name": "Lunes",
                    "day_number": 18,
                    "is_holiday": True,
                    "classes": [],
                },
                {
                    "day_name": "Martes",
                    "day_number": 19,
                    "is_holiday": False,
                    "classes": [
                        {"topic": "Documentos obligatorios", "type": "theory"},
                        {"topic": "Equipo de prevención", "type": "workshop"},
                        {"topic": "Documentos obligatorios", "type": "theory"},
                        {"topic": "Equipo de prevención", "type": "workshop"},
                        {"topic": "Accidentes de tránsito", "type": "theory"},
                    ],
                },
            ],
        },
        "saturday": {
            "time_slots": [
                {"time_slot": "8:00 AM - 10:00 AM", "instructor": "Pablo"},
                {"time_slot": "10:00 AM - 12:00 PM", "instructor": "Pablo"},
                {"time_slot": "12:00 PM - 2:00 PM", "instructor": "Pablo"},
                {"time_slot": "2:00 PM - 4:00 PM", "instructor": "Pablo"},
            ],
            "days": [
                {
                    "day_name": "Sábado",
                    "day_number": 23,
                    "is_holiday": False,
                    "classes": [
                        {"topic": "Procedimientos técnicos", "type": "theory"},
                        {"topic": "Clasificación de vehículo", "type": "theory"},
                        {"topic": "Modificaciones al vehículo", "type": "theory"},
                        {"topic": "Restricciones especiales", "type": "theory"},
                    ],
                },
            ],
        },
    },
}
