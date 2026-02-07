# ERP NEXUS SDK

SDK puro Python para definir, validar e instalar componentes (módulos, aplicaciones y librerías) compatibles con el ecosistema ERP NEXUS.

## Características

- **Cero dependencias de framework**: Funciona standalone sin Django, FastAPI, etc.
- **Validación estricta**: Schemas Pydantic para garantizar la integridad de los manifiestos.
- **Instalación transaccional**: Garantiza rollback automático si falla la instalación.
- **Resolución de dependencias**: Soporte para Semantic Versioning.
- **Tipado estático**: Código 100% tipado y compatible con mypy.
- **Gestión moderna**: Optimizado para el uso con [uv](https://docs.astral.sh/uv/).

## Instalación

Este proyecto utiliza **uv** para la gestión de paquetes y entornos virtuales, reemplazando a pip/poetry en el flujo de trabajo.

### Agregar a tu proyecto

```bash
uv add erp-nexus-sdk
```

### Instalación en entorno virtual existente

```bash
uv pip install erp-nexus-sdk
```

## Desarrollo

Para contribuir al desarrollo del SDK, sigue estos pasos:

1. **Sincronizar entorno**:
   Instala las dependencias definidas en `pyproject.toml`.
   ```bash
   uv sync
   ```

2. **Ejecutar pruebas**:
   ```bash
   uv run pytest
   ```

3. **Verificar tipado**:
   ```bash
   uv run mypy src
   ```

## Uso Básico

### Validación de un Módulo

```python
from pathlib import Path
from erp_nexus_sdk.validator import ComponentValidator

validator = ComponentValidator()
try:
    schema = validator.validate_manifest(Path("./mod_ventas/__meta__.py"))
    print(f"Módulo válido: {schema.name} v{schema.version}")
except Exception as e:
    print(f"Error: {e}")
```

### Instalación Transaccional

```python
from erp_nexus_sdk.installer import TransactionalInstaller
from erp_nexus_sdk.contracts import StorageBackend

# Implementa tu backend de almacenamiento (ej: sistema de archivos local)
class MyStorage(StorageBackend):
    ...

installer = TransactionalInstaller(MyStorage())
installer.install(source_path=Path("./mod_ventas"), target_path=Path("/opt/nexus/modules/mod_ventas"))
```

## Estructura del Proyecto

- `src/erp_nexus_sdk`: Código fuente del SDK.
- `docs/`: Documentación y especificaciones.
- `tests/`: Pruebas unitarias.

## Licencia

[MIT](LICENSE)
