# 📂 Python Download Organizer | Organizador Automático de Descargas

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-type--hints-brightgreen.svg)

**[English](#english) | [Español](#español)**

---

## English

A professional Python script that automatically organizes your Downloads folder by file type. Features configuration via TOML, comprehensive logging, dry-run mode, and Windows Task Scheduler integration.

### ✨ Features

- 🗂️ **Smart Organization**: Automatically sorts files by extension into categorized folders
- ⚙️ **TOML Configuration**: External configuration file for easy customization
- 📊 **Comprehensive Logging**: Detailed logs of all operations
- 🧪 **Dry-Run Mode**: Test without moving files
- 🔄 **Duplicate Handling**: Intelligent renaming for duplicate files
- ⏰ **Task Automation**: Windows Task Scheduler integration scripts included
- 🐍 **Modern Python**: Type hints, pathlib, and Python 3.12+ features

### 📋 Requirements

- Python 3.12+
- Windows 10/11
- PowerShell 5+
- UV package manager (recommended) or pip

### 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ponce1969/python-download-organizer.git
   cd python-download-organizer
   ```

2. **Create virtual environment:**
   ```bash
   uv venv --python 3.12
   ```

3. **Activate the environment:**
   ```bash
   .venv\Scripts\activate
   ```

4. **Configure the script:**
   ```bash
   copy src\config.example.toml src\config.toml
   ```
   
5. **Edit `src\config.toml`** to customize folders and extensions

6. **Run the script:**
   ```bash
   cd src
   python script_descargas.py
   ```

### 📁 Default Folder Structure

The script creates these folders in your Downloads directory:

- `PDF/` - PDF documents
- `Videos/` - Video files (mp4, avi, mkv, etc.)
- `Imagenes/` - Images (jpg, png, gif, etc.)
- `Documentos/` - Office documents and text files
- `Comprimidos/` - Compressed files (zip, rar, 7z)
- `Programas/` - Executables (exe, msi)
- `Audio/` - Audio files (mp3, wav, flac)
- `Otros/` - Unrecognized files

### ⏰ Automated Scheduling

**Run as Administrator:**

```powershell
cd C:\Users\YourUser\path\to\project\src
.\crear_tarea_automatica.ps1
```

This creates a scheduled task that runs every Sunday at 8:00 PM.

**Test the task:**
```powershell
schtasks /run /tn "OrganizarDescargas"
```

**Remove the task:**
```powershell
.\eliminar_tarea_automatica.ps1
```

### 🛠️ Configuration

Edit `src/config.toml`:

```toml
[general]
dry_run = false  # true = simulate only, false = move files
downloads_folder = "Downloads"

[folders]
pdf = "PDF"
mp4 = "Videos"
jpg = "Imagenes"
# ... add more extensions

[others]
folder = "Otros"  # For unrecognized files
```

### 📝 Logging

All operations are logged to `src/ordenar_descargas.log` with timestamps and details.

### 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Español

Script profesional en Python que organiza automáticamente tu carpeta de Descargas por tipo de archivo. Incluye configuración TOML, logging completo, modo de prueba y scripts de automatización para Windows Task Scheduler.

### 📋 Características

- 🗂️ **Organización Inteligente**: Ordena archivos por extensión en carpetas categorizadas
- ⚙️ **Configuración TOML**: Archivo de configuración externo fácil de personalizar
- 📊 **Logging Completo**: Registros detallados de todas las operaciones
- 🧪 **Modo Dry-Run**: Prueba sin mover archivos
- 🔄 **Manejo de Duplicados**: Renombrado inteligente para archivos duplicados
- ⏰ **Automatización**: Scripts de integración con Task Scheduler incluidos
- 🐍 **Python Moderno**: Type hints, pathlib y características de Python 3.12+

### 📋 Requisitos

- Python 3.12+
- Windows 10/11
- PowerShell 5+
- UV package manager (recomendado) o pip

### 📥 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Ponce1969/python-download-organizer.git
   cd python-download-organizer
   ```

2. **Crea el entorno virtual:**
   ```bash
   uv venv --python 3.12
   ```

3. **Activa el entorno:**
   ```bash
   .venv\Scripts\activate
   ```

4. **Copia y configura el archivo de configuración:**
   ```bash
   copy src\config.example.toml src\config.toml
   ```
   
5. **Edita `src\config.toml`:**
   - Ajusta las rutas y extensiones según tus necesidades
   - Configura `dry_run = true` para la primera prueba

## 🚀 Uso Manual

### Modo normal (mueve archivos)

```bash
python script_descargas.py
```

### Modo prueba (solo simula)

Edita `config.toml` y configura:
```toml
dry_run = true
```

Luego ejecuta:
```bash
python script_descargas.py
```

## ⏰ Configurar Automatización (Recomendado)

### Crear tarea automática (Domingos a las 20:00)

**IMPORTANTE: Debes ejecutar como Administrador**

1. Presiona `Win + X` y selecciona **"Windows PowerShell (Administrador)"** o **"Terminal (Administrador)"**
2. Navega a la carpeta del script:
   ```powershell
   cd C:\Users\cerra\codigo\Scripts\src
   ```
3. Ejecuta:
   ```powershell
   .\crear_tarea_automatica.ps1
   ```

**Nota:** El script usa el Python del entorno virtual `.venv` para garantizar que siempre use las dependencias correctas.

### Probar la tarea manualmente

```powershell
schtasks /run /tn "OrganizarDescargas"
```

### Ver la tarea en el Programador

```powershell
taskschd.msc
```

### Eliminar la tarea automática

```powershell
.\eliminar_tarea_automatica.ps1
```

## ⚙️ Configuración

Edita `config.toml` para personalizar:

- **dry_run**: `true` para simular, `false` para mover archivos realmente
- **downloads_folder**: Nombre de tu carpeta de descargas
- **[folders]**: Mapeo de extensiones a carpetas
- **[others]**: Carpeta para archivos no reconocidos

## 📁 Estructura de Carpetas

El script crea estas carpetas en tu directorio de Descargas:

- `PDF/` - Archivos PDF
- `Videos/` - Videos (mp4, avi, mkv, etc.)
- `Imagenes/` - Imágenes (jpg, png, gif, etc.)
- `Documentos/` - Documentos de Office y texto
- `Comprimidos/` - Archivos ZIP, RAR, 7z
- `Programas/` - Ejecutables (exe, msi)
- `Otros/` - Archivos no reconocidos

## 📝 Logs

Los logs se guardan en `ordenar_descargas.log` con información de cada ejecución.

## 🔧 Modificar Horario

Para cambiar el horario de ejecución, edita `crear_tarea_automatica.ps1`:

```powershell
# Ejemplo: Todos los días a las 22:00
$Trigger = New-ScheduledTaskTrigger -Daily -At 22:00

# Ejemplo: Lunes y Viernes a las 18:00
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday,Friday -At 18:00
```

Luego vuelve a ejecutar el script de creación.

## 🐞 Problemas Comunes

### La tarea no se ejecuta

- ✅ Verifica que se creó como Administrador
- ✅ Revisa los logs en `ordenar_descargas.log`
- ✅ Comprueba que la tarea existe: `taskschd.msc`
- ✅ Verifica la próxima ejecución: `schtasks /query /tn "OrganizarDescargas"`

### Error de permisos

- ✅ Ejecuta PowerShell como Administrador
- ✅ Verifica que tienes permisos en la carpeta de Descargas

### El script no encuentra archivos

- ✅ Verifica la ruta en `config.toml` (sección `downloads_folder`)
- ✅ Asegúrate de que la carpeta existe
- ✅ Revisa los logs para ver mensajes de error

### Python no encontrado

- ✅ Verifica que el entorno virtual existe en `.venv`
- ✅ Comprueba la ruta: `.venv\Scripts\python.exe`
- ✅ Recrea el entorno si es necesario: `uv venv --python 3.12`

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
