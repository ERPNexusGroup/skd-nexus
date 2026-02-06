# Ejemplos de Manifiestos

## module.json

```json
{
  "name": "mod_hotel_reservations",
  "version": "1.0.0",
  "description": "Módulo para gestión de reservas de hotel",
  "author": "Nexus Corp",
  "email": "dev@nexus.com",
  "keywords": ["hospitalidad", "reservas"],
  "dependencies": {
    "mod_core": "^1.0.0"
  }
}
```

## app.json

```json
{
  "name": "app_front_desk",
  "version": "1.0.0",
  "description": "Aplicación de recepción",
  "parent_module": "mod_hotel_reservations",
  "dependencies": {}
}
```
