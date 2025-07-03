# Sistema Web de Gestión Académica

Este proyecto es un ejemplo básico de una aplicación web para la gestión de estudiantes y cursos. Está pensado para instituciones educativas con recursos limitados y utiliza Python y Flask.

## Requisitos

- Python 3
- Paquetes del archivo `requirements.txt`

Instalar dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar la aplicación:

```bash
python app.py
```

2. Acceder a las rutas principales:

- `GET /students` — Lista de estudiantes.
- `POST /students` — Crear estudiante (enviar JSON con `name`).
- `GET /courses` — Lista de cursos.
- `POST /courses` — Crear curso (enviar JSON con `name`).
- `GET /enrollments` — Inscripciones.
- `POST /enrollments` — Registrar inscripción (enviar JSON con `student_id` y `course_id`).

Los datos se almacenan en `data.json`.
