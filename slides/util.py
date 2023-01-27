from jsonschema import validators
from typing import Optional, Type


def extend_with_default(validator_class: Type) -> Type:
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(validator, properties, instance, schema):
            yield error

    return validators.extend(validator_class, {"properties": set_defaults})


def apply_defaults_and_validate(instance: dict, schema: dict, cls: Optional[Type] = None) -> dict:
    """
    Apply defaults and validate the instance against the schema.
    """
    cls = cls or validators.validator_for(schema)
    cls = extend_with_default(cls)
    cls(schema).validate(instance)
    return instance
