

from tartiflette import Scalar
from bson import ObjectId


@Scalar("Json")
class Json:
    @staticmethod
    def coerce_input(val):
        return val

    @staticmethod
    def coerce_output(val):
        return val
    def parse_literal(self, ast):
        return ast.node