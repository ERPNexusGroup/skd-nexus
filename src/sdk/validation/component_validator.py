from pathlib import Path

from ..utils.meta_parser import parse_meta_file
from ..schemas.meta_schema import BaseMetaSchema
from .structure_validator import StructureValidator
from .dependency_validator import DependencyValidator


class ComponentValidator:

    def __init__(self):
        self.structure_validator = StructureValidator()
        self.dependency_validator = DependencyValidator()

    def validate_component(self, component_path: Path) -> BaseMetaSchema:

        meta_path = component_path / "__meta__.py"

        metadata = parse_meta_file(meta_path)

        # validar schema pydantic
        meta_model = BaseMetaSchema(**metadata)

        # validar estructura
        self.structure_validator.validate_structure(component_path)

        # validar dependencias (solo formato por ahora)
        self.dependency_validator.validate_dependencies(meta_model)

        return meta_model
