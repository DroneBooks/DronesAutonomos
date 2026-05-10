# Volumen 1 — Anexo A1: Git

> **Recursos para el anexo "Git: Control de Versiones para Proyectos de Drones"**  
> **Nivel:** Principiante

---

## 📦 Contenido

Este anexo no requiere scripts adicionales — Git es la herramienta en sí misma.  
Aquí encontrarás una referencia rápida de los comandos usados en el libro.

```
VOLUMEN-1/Anexos/A1-Git/
└── README.md    # Esta guía de referencia rápida
```

---

## 🔧 Comandos Esenciales del Libro

### Configuración inicial (una sola vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Flujo básico de trabajo
```bash
# 1. Inicializar repositorio
git init mi-proyecto-drone

# 2. Ver estado de archivos
git status

# 3. Añadir cambios al área de preparación
git add archivo.py          # archivo específico
git add .                   # todos los archivos

# 4. Guardar snapshot (commit)
git commit -m "descripción del cambio"

# 5. Ver historial
git log --oneline
```

### Trabajar con ramas (branches)
```bash
# Crear y cambiar a nueva rama
git checkout -b experimento-pid

# Listar ramas
git branch

# Volver a la rama principal
git checkout main

# Fusionar rama
git merge experimento-pid
```

### Repositorio remoto (GitHub)
```bash
# Clonar repositorio de scripts del curso
git clone https://github.com/DroneBooks/DronesAutonomos.git

# Descargar actualizaciones
git pull

# Subir cambios propios (si tienes permisos)
git push origin main
```

### Deshacer cambios
```bash
# Ver diferencias antes de guardar
git diff

# Descartar cambios en un archivo
git restore archivo.py

# Volver a un commit anterior (sin borrar historial)
git revert HEAD
```

---

## 🗂️ Estructura Recomendada para Proyectos de Drones

```
mi-drone-proyecto/
├── README.md               # Descripción del proyecto
├── .gitignore              # Archivos a ignorar
├── scripts/
│   ├── vuelo_autonomo.py
│   └── telemetria.py
├── tests/
│   └── test_waypoints.py
└── docs/
    └── configuracion.md
```

### .gitignore recomendado para Python
```
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.log
*.csv
*.bag
```

---

## 📖 Referencia al Libro

Este anexo acompaña el **Volumen 1, Anexo A1: Git** del libro  
*Drones Autónomos I: Hardware, Ardupilot y MAVLink*.

Temas del anexo en el libro:
- Instalación de Git en Ubuntu, macOS y Windows
- Flujo de trabajo con ramas para experimentos de vuelo
- Colaboración en proyectos de robótica
- Integración con VS Code (GitLens)

---

**Última actualización:** Abril 2026 | DroneBooks
