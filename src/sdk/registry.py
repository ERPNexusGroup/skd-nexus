from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class ComponentRegistry:
    """
    Registry minimalista en JSON para componentes instalados.
    """

    def __init__(self, registry_path: Path):
        self.registry_path = registry_path
        self._data: Dict[str, Dict[str, Any]] = {"components": {}}
        self._load()

    # ------------------------------------------------------------------
    # IO
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if not self.registry_path.exists():
            self._save()
            return

        try:
            raw = self.registry_path.read_text(encoding="utf-8")
            if raw.strip():
                self._data = json.loads(raw)
            else:
                self._data = {"components": {}}
        except json.JSONDecodeError:
            # Archivo corrupto: reiniciar estructura básica
            self._data = {"components": {}}

        if "components" not in self._data:
            self._data["components"] = {}

    def _save(self) -> None:
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = self.registry_path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(self._data, indent=2), encoding="utf-8")
        tmp_path.replace(self.registry_path)

    # ------------------------------------------------------------------
    # API
    # ------------------------------------------------------------------

    def register(self, name: str, payload: Dict[str, Any]) -> None:
        self._data["components"][name] = payload
        self._save()

    def unregister(self, name: str) -> None:
        self._data["components"].pop(name, None)
        self._save()

    def get(self, name: str) -> Optional[Dict[str, Any]]:
        return self._data["components"].get(name)

    def list(self) -> List[Dict[str, Any]]:
        return list(self._data["components"].values())
