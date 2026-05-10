# Volumen 2 — Anexo A1: Git

> **Recursos para el anexo "Git: Control de Versiones para Proyectos de Drones"**  
> **Nivel:** Principiante

---

## 📦 Contenido

Este anexo contiene la referencia rápida de Git aplicada al contexto de proyectos ROS2 y Python de drones.

```
VOLUMEN-2/Anexos/A1-Git/
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
git init mi-paquete-ros2

# 2. Ver estado de archivos
git status

# 3. Añadir cambios al área de preparación
git add src/mi_nodo.cpp
git add .                   # todos los archivos

# 4. Guardar snapshot (commit)
git commit -m "feat: añadir nodo publicador de telemetría"

# 5. Ver historial
git log --oneline
```

### Estructura recomendada para paquetes ROS2
```bash
mi_paquete_ros2/
├── README.md
├── .gitignore
├── package.xml
├── CMakeLists.txt          # (C++) o setup.py (Python)
├── src/
│   └── mi_nodo.cpp
├── launch/
│   └── mi_launch.py
└── config/
    └── parametros.yaml
```

### .gitignore recomendado para ROS2
```
build/
install/
log/
__pycache__/
*.pyc
*.egg-info/
.venv/
```

### Trabajar con ramas (branches)
```bash
# Crear rama para experimento de navegación
git checkout -b nav2-experimento

# Listar ramas
git branch

# Fusionar cuando el experimento funcione
git checkout main
git merge nav2-experimento
```

### Repositorio remoto (GitHub)
```bash
# Clonar este repositorio de scripts del curso
git clone https://github.com/DroneBooks/DronesAutonomos.git

# Descargar actualizaciones
git pull
```

---

## 📖 Referencia al Libro

Este anexo acompaña el **Volumen 2, Anexo A1: Git** del libro  
*Drones Autónomos II: Robótica, Visión Artificial e IA Embarcada*.

Temas del anexo en el libro:
- Instalación de Git en Ubuntu, macOS y Windows
- Gestión de ramas para proyectos ROS2
- Colaboración en equipos de robótica
- Integración con VS Code (GitLens)

---

**Última actualización:** Abril 2026 | DroneBooks
