from slides import util


def test_default_validator() -> None:
    instance = {"foo": None, "bar": 1}
    schema = {
        "type": "object",
        "properties": {
            "foo": {
                "type": ["string", "null"],
                "default": "foo_default",
            },
            "bar": {
                "type": "integer",
                "default": 42,
            },
            "baz": {
                "type": "object",
                "default": {
                    "child": "of baz",
                }
            }
        }
    }
    assert util.apply_defaults_and_validate(instance, schema) == {
        "foo": None,
        "bar": 1,
        "baz": {
            "child": "of baz",
        }
    }
