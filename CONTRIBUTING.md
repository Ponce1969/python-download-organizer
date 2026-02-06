# Guía de Contribución

¡Gracias por tu interés en contribuir! 🎉

## Cómo Contribuir

1. **Fork el repositorio**
2. **Crea una rama** para tu feature o bugfix:
   ```bash
   git checkout -b feature/mi-nueva-funcionalidad
   ```
3. **Haz tus cambios** siguiendo las guías de estilo
4. **Prueba tus cambios** localmente
5. **Commit** con mensajes descriptivos:
   ```bash
   git commit -am 'Agrega soporte para nuevas extensiones'
   ```
6. **Push** a tu fork:
   ```bash
   git push origin feature/mi-nueva-funcionalidad
   ```
7. **Abre un Pull Request** con una descripción clara de los cambios

## Guías de Estilo

### Python

- Usa **type hints** en todas las funciones
- Sigue **PEP 8**
- Usa **docstrings** para funciones complejas
- Mantén las funciones pequeñas y enfocadas

### Commits

- Usa mensajes claros y descriptivos
- Formato: `Verbo en presente + descripción`
- Ejemplos:
  - ✅ `Agrega soporte para archivos .epub`
  - ✅ `Corrige error en manejo de duplicados`
  - ❌ `fix bug`
  - ❌ `cambios varios`

## Reportar Bugs

Usa el sistema de Issues de GitHub e incluye:

- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Versión de Python y sistema operativo
- Logs relevantes

## Sugerir Features

Abre un Issue con:

- Descripción de la funcionalidad
- Caso de uso
- Ejemplo de cómo se usaría

## Preguntas

Si tienes preguntas, abre un Issue con la etiqueta `question`.
