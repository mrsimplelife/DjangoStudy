class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # return "%04d" % value
        return str(value)


class MonthConverter(YearConverter):
    regex = r"^0?[1-9]$|^1[0-2]$"


class DayConverter(YearConverter):
    regex = r"^0?[1-9]$|^[1-2]\d$|^3[01]$"
