from collections import OrderedDict


DEFINITION_REGISTRY = OrderedDict()


def add_definition(definition):
    DEFINITION_REGISTRY[definition.description] = definition
