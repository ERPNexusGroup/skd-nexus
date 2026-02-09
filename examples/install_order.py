from pathlib import Path
from sdk.dependency import DependencyResolver

resolver = DependencyResolver()

BASE_DIR = Path(__file__).resolve().parent

resolver.load_component(BASE_DIR / "modules" / "base")
resolver.load_component(BASE_DIR / "modules" / "sales")
resolver.load_component(BASE_DIR / "modules" / "inventory")

plan = resolver.resolve()

print(plan)
