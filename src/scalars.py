

from tartiflette import Scalar


@Scalar("Json")
class CapitalizedString:
    @staticmethod
    def coerce_input(val):
        return val

    @staticmethod
    def coerce_output(val):
        return val