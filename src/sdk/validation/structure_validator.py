from pathlib import Path


class StructureValidator:

    REQUIRED_FILES = [
        "__meta__.py",
    ]

    def validate_structure(self, component_path: Path) -> None:

        if not component_path.exists():
            raise FileNotFoundError(f"Componente no encontrado: {component_path}")

        for file in self.REQUIRED_FILES:
            if not (component_path / file).exists():
                raise ValueError(f"Falta archivo obligatorio: {file}")
