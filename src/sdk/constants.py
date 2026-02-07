# Constantes globales del SDK

MODULE_PREFIX = "mod_"
APP_PREFIX = "app_"
LIB_PREFIXES = ("lib_", "pkg_")

MANIFEST_FILES = {
    "module": "__meta__.py",
    "app": "app.json",
    "lib": "lib.json"
}

REQUIRED_MODULE_FIELDS = ["name", "version", "description", "author", "email"]
REQUIRED_APP_FIELDS = ["name", "version", "description", "parent_module"]
REQUIRED_LIB_FIELDS = ["name", "version", "description"]
