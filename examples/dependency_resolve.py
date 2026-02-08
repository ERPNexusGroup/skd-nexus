from sdk.dependency import DependencyResolver, VersionResolver

components = load_components_meta()

version_resolver = VersionResolver(components)
version_resolver.validate_versions()

resolver = DependencyResolver(components)
resolver.build_graph()

order = resolver.resolve_install_order()

print(order)
