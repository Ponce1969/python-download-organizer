# Organizador Automático de Descargas

Script en Python que organiza automáticamente los archivos de tu carpeta de Descargas en subcarpetas según su tipo.

## 📋 Características

- ✅ Organiza archivos por extensión (PDF, Videos, Imágenes, Documentos, etc.)
- ✅ Configuración externa con archivo TOML
- ✅ Sistema de logging completo
- ✅ Modo dry-run para pruebas
- ✅ Manejo de archivos duplicados
- ✅ Automatización con Task Scheduler

## � Requisitos

- Python 3.11+
- Windows 10/11
- PowerShell 5+
- Entorno virtual en `.venv`

## 📥 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/organizador-descargas.git
   cd organizador-descargas
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
