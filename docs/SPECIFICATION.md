# Especificación del SDK ERP NEXUS

Este documento define las especificaciones técnicas para el desarrollo de componentes compatibles con ERP NEXUS.

## Estructura de Componentes

### Módulos (`mod_*`)
Los módulos son las unidades funcionales principales.
- **Prefijo**: `mod_`
- **Estructura**: Debe contener un archivo `module.json`.

### Aplicaciones (`app_*`)
Las aplicaciones extienden o utilizan módulos.
- **Prefijo**: `app_`
- **Estructura**: Debe contener un archivo `app.json`.

### Librerías (`lib_*` / `pkg_*`)
Librerías de utilidad reutilizables.
- **Prefijo**: `lib_` o `pkg_`
- **Estructura**: Debe contener un archivo `lib.json`.

## Manifests

Todos los componentes deben incluir un archivo JSON de manifiesto que describa sus metadatos y dependencias.
