class SDKAdapter:

    def extend_meta_schema(self):
        pass

    def extend_meta_generation(self, context):
        return context

    def extend_validation(self, meta):
        pass

    def extend_scaffold(self, component_path):
        pass
