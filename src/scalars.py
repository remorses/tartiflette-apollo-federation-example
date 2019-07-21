

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

@Scalar("Url")
class Url:
    @staticmethod
    def coerce_input(val):
        return str(val)

    @staticmethod
    def coerce_output(val):
        return str(val)



@Scalar("ObjectId")
class ObjectIdScalar:
    @staticmethod
    def coerce_input(val):
        return ObjectId(val)

    @staticmethod
    def coerce_output(val):
        return str(val)