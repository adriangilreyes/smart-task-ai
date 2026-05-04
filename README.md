# 🧠 Smart Task AI

> Gestor de tareas inteligente con interfaz de terminal — construido con Python y Rich.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Rich](https://img.shields.io/badge/Rich-terminal%20UI-purple?style=flat-square)
![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow?style=flat-square)

---

## 📋 ¿Qué es?

**Smart Task AI** es un gestor de tareas que se ejecuta en la terminal. Permite añadir, organizar y eliminar tareas con categorías y niveles de prioridad, con una interfaz visual y colorida gracias a la librería `Rich`.

El proyecto está en constante evolución — el objetivo es integrar IA real para categorizar y priorizar tareas automáticamente.

---

## ✨ Funcionalidades

- ➕ **Añadir tareas** con título, categoría y prioridad
- 🗑️ **Eliminar tareas** por ID
- 📋 **Listar tareas** en una tabla con colores por prioridad y categoría
- 🎨 **Interfaz de terminal** con paneles, colores y validación de inputs

### Categorías disponibles
| Categoría | Color |
|-----------|-------|
| Trabajo   | 🔵 Cyan |
| Estudio   | 🟣 Magenta |
| Personal  | 💙 Azul |

### Niveles de prioridad
| Prioridad | Color |
|-----------|-------|
| Alta      | 🔴 Rojo |
| Media     | 🟡 Amarillo |
| Baja      | 🟢 Verde |

---

## 🚀 Instalación

**1. Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/smart-task-ai.git
cd smart-task-ai
```

**2. Instala las dependencias**
```bash
pip install rich
```

**3. Ejecuta el programa**
```bash
python smart_task.py
```

---

## 🖥️ Uso

Al iniciar, verás el menú principal:

```
╭─────────────────────────────╮
│     Smart Task AI           │
│                             │
│  1. Añadir tarea            │
│  2. Eliminar tarea          │
│  3. Listar tareas           │
│  4. Salir                   │
╰─────────────────────────────╯
```

Las tareas se muestran en tabla con colores:

```
╭────┬──────────────────────┬────────────┬───────────╮
│ ID │ Título               │ Categoría  │ Prioridad │
├────┼──────────────────────┼────────────┼───────────┤
│  1 │ Estudiar Python      │  Estudio   │   Alta    │
│  2 │ Reunión con cliente  │  Trabajo   │   Media   │
│  3 │ Hacer deporte        │  Personal  │   Baja    │
╰────┴──────────────────────┴────────────┴───────────╯
```

---

## 🗂️ Estructura del proyecto

```
smart-task-ai/
│
├── smart_task.py     # Archivo principal
└── README.md         # Este archivo
```

> La estructura irá creciendo conforme se añadan módulos de IA y persistencia.

---

## 🛣️ Roadmap

- [x] Estructura base con diccionario
- [x] Interfaz de terminal con Rich
- [ ] Persistencia de datos con JSON
- [ ] Estado de tarea (pendiente / completada)
- [ ] Fecha de creación automática
- [ ] **IA para categorizar y priorizar automáticamente**
- [ ] Separación en módulos (`tasks.py`, `ai.py`, `ui.py`)
- [ ] Interfaz web con Flask

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas o mejoras:

1. Haz un fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Abre un Pull Request

---

## 📄 Licencia

MIT License — siéntete libre de usar y modificar este proyecto.

---

<p align="center">Hecho con 🐍 Python y mucho café ☕</p>
