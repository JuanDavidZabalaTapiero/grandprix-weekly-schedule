import subprocess
from flask import Blueprint, render_template, url_for, jsonify, request
from app.services.weeks import (
    get_week,
    get_current_week,
    register_current_week,
    get_next_week,
    register_next_week,
)
from app.services.topics import get_all_topics
from app.services.instructors import get_all_instructors
from app.services.notes import get_note, update_note
from app.services.week_time_slot_instructors import update_week_time_slot_instructor
from app.services.classes import update_class_topic
from app.utils.build import build_schedule

core_bp = Blueprint("core", __name__)


# INICIO
@core_bp.get("/")
def home():

    # VERFIFICAR REGISTRO DE LA SEMANA ACTUAL
    current_week = get_current_week()

    if not current_week:
        current_week_id = register_current_week()
        current_week = get_week(current_week_id)

    # VERIFICAR REGISTRO DE LA PRÓXIMA SEMANA
    next_week = get_next_week(current_week["id"])

    if not next_week:
        next_week_id = register_next_week(current_week["week_start"])
        next_week = get_week(next_week_id)

    return render_template(
        "home.html", current_week_id=current_week["id"], next_week_id=next_week["id"]
    )


# CRONOGRAMA
@core_bp.route("/<int:week_id>/schedule", methods=["GET", "POST"])
def week_schedule(week_id):

    # FORM
    if request.method == "POST":
        new_note = request.form.get("note")
        update_note(new_note)

    # DATA
    schedule = build_schedule(week_id)
    note = get_note()
    topics = get_all_topics()
    instructors = get_all_instructors()

    return render_template(
        "schedule.html",
        week_id=week_id,
        schedule=schedule,
        note=note,
        topics=topics,
        instructors=instructors,
    )


# CAMBIAR INSTRUCTOR
@core_bp.put("/time-slot/instructor")
def update_time_slot_instructor():

    # DATA
    data = request.get_json()

    # CAMBIO
    update_week_time_slot_instructor(
        data["week_time_slot_instructor_id"], data["instructor_id"]
    )

    return jsonify({"message": "Cambio de instructor realizado"})


# CAMBIAR TEMA
@core_bp.put("/class")
def update_class():

    # DATA
    data = request.get_json()

    # CAMBIO
    update_class_topic(data["class_id"], data["topic_id"])

    return jsonify({"message": "Cambio de clase realizado"})


# GENERAR IMG
@core_bp.get("/<int:week_id>/schedule/screenshot")
def screenshot(week_id):
    url = url_for("core.week_schedule", week_id=week_id, _external=True)

    subprocess.run(["node", "scripts/screenshot.js", url, "#schedule"], check=True)

    return jsonify({"message": "Captura de pantalla exitosa"})
