from yams.buildobjs import EntityType, String


class NamedThing(EntityType):
    name = String(maxsize=42, required=True)


class TitledThing(EntityType):
    title = String(maxsize=42, required=True)
