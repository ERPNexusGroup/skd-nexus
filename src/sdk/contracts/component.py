from dataclasses import dataclass
from typing import Optional


@dataclass
class ModuleComponent:

    technical_name: str
    display_name: Optional[str] = None
    component_type: str = "module"
    package_type: str = "extension"
    domain: str = "custom"
