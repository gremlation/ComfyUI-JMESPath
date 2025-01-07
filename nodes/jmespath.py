from json import loads
from typing import Tuple, Any

import jmespath


class JMESPath:
    """
    Runs a JMESPath query against input JSON and outputs the result.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"defaultInput": True}),
                "expression": ("STRING", {"default": "@"}),
            },
        }

    RETURN_TYPES = ("*", "STRING", "INT", "FLOAT")
    RETURN_NAMES = ("any", "string", "int", "float")
    FUNCTION = "execute"

    CATEGORY = "utils"

    def execute(self, json_string: str, expression: str) -> Tuple[Any, str, int | None, float | None]:
        result = jmespath.search(expression, loads(json_string))
        result_int = None
        try:
            result_int = int(result)
        except (TypeError, ValueError):
            pass
        result_float = None
        try:
            result_float = float(result)
        except (TypeError, ValueError):
            pass
        return (result, str(result), result_int, result_float)
