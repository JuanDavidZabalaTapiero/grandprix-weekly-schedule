import {
  screenshot,
  changeWeekTimeSlotInstructor,
  changeClass,
} from "./api.js";

// === DESCARGAR IMG ===
export function initScreenshot(button) {
  // DATA
  const url = button.dataset.url;
  const spinner = document.querySelector(".spinner-border");

  // EVENTO
  button.addEventListener("click", async () => {
    try {
      // Deshabilitar botón
      button.disabled = true;

      // Mostrar spinner
      spinner.classList.remove("d-none");
      spinner.classList.add("ms-2");

      const data = await screenshot(url);

      // Descargar img
      if (data.message) {
        const link = document.createElement("a");
        link.href = "/static/screenshots/cronograma.png";
        link.download = "cronograma.png";
        link.click();
      }
    } catch (err) {
      console.error(err);
    } finally {
      // Habilitar botón
      button.disabled = false;

      // Ocultar spinner
      spinner.classList.add("d-none");
      spinner.classList.remove("ms-2");
    }
  });
}

// === CAMBIAR INSTRUCTOR ===
export function initChangeInstructor() {
  const instructors = document.querySelectorAll(".instructor");

  instructors.forEach((instructor) => {
    // SELECT
    const select = instructor.nextElementSibling;

    // INSTRUCTOR: CLICK
    instructor.addEventListener("click", () => {
      instructor.classList.add("d-none"); // Ocultar span
      select.classList.remove("d-none"); // Mostrar select
    });

    // SELECT: CHANGE
    select.addEventListener("change", async (event) => {
      const instructorName =
        event.target.options[event.target.selectedIndex].text;

      const instructorId = event.target.value;

      try {
        const data = {
          week_time_slot_instructor_id:
            instructor.dataset.weekTimeSlotInstructorId,
          instructor_id: instructorId,
        };

        const response = await changeWeekTimeSlotInstructor(
          window.API_URLS.updateTimeSlotInstructor,
          data,
        );

        console.log(response);

        instructor.textContent = instructorName; // Cambiar texto
      } catch (err) {
        console.error(err);
      } finally {
        select.classList.add("d-none"); // Ocultar select
        instructor.classList.remove("d-none"); // Mostrar span
      }
    });
  });
}

// === CAMBIAR CLASE ===
export function initChangeClass() {
  const classes = document.querySelectorAll(".class");

  classes.forEach((classElement) => {
    // SELECT
    const select = classElement.nextElementSibling;

    // TD
    const td = classElement.parentElement;

    // CLASE: CLICK
    classElement.addEventListener("click", () => {
      classElement.classList.add("d-none"); // Ocultar span
      td.className = ""; // Quitar clase td
      select.classList.remove("d-none"); // Mostrar select
    });

    // SELECT: CHANGE
    select.addEventListener("change", async () => {
      // OPTION
      const optionTopic = select.options[select.selectedIndex];

      const topicId = optionTopic.value;
      const topicType = optionTopic.dataset.type;

      try {
        const data = {
          class_id: classElement.dataset.classId,
          topic_id: topicId,
        };

        await changeClass(window.API_URLS.updateClass, data);

        classElement.textContent = optionTopic.textContent; // Cambiar texto
        td.className = topicType; // Cambiar clase td
      } catch (err) {
        console.error(err);
      } finally {
        select.classList.add("d-none"); // Ocultar select
        classElement.classList.remove("d-none"); // Mostrar span
      }
    });
  });
}
