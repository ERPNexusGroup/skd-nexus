from pathlib import Path

from sdk.validation import ComponentValidator
from sdk.dependency import DependencyResolver

components = {}

validator = ComponentValidator()

for path in Path("modules").iterdir():
    if path.is_dir():
        meta = validator.validate_component(path)
        components[meta.technical_name] = meta

resolver = DependencyResolver(components)

resolver.build_graph()

order = resolver.resolve_install_order()

print(order)
