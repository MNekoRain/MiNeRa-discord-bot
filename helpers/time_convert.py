from datetime import datetime
from lang.language import get_lang


def devideInt(string: str) -> tuple[int, str]:
        ints = []
        strs = [] 
        for symbol in string:
            try:
                ints.append(int(symbol))
            except TypeError:
                strs.append(symbol)
            except ValueError:
                strs.append(symbol)
        return int("".join(map(str, ints))), "".join(strs)


def to_seconds(duration__: str) -> int | None:
    """
    Convert a time to seconds\n
    Example:\n
      > to_seconds("1 day")\n
      86400\n
      > to_seconds("2m")\n
      120\n
      > to_seconds("3hours")\n
      6400
      > to_seconds("60")
      60
    """
    if duration__.isdigit():
        return duration__
    duration_, time_ = devideInt(duration__)
    if time_[0].lower() in ["m", "м"]:
        return duration_ * 60
    elif time_[0].lower() in ["h", "ч"]:
        return duration_ * 60 * 60
    elif time_[0].lower() in ["d", "д"]:
        return duration_ * 60 * 60 * 24
    elif time_[0].lower() in ["w", "н"]:
        return duration_ * 60 * 60 * 24 * 7
    else:
        return None


class TimeConvert:
    def __init__(self, lang):
        self.mouth: dict[str, str] = {
            "01": get_lang(lang, "timeconverter.mouth0"),
            "02": get_lang(lang, "timeconverter.mouth1"),
            "03": get_lang(lang, "timeconverter.mouth2"),
            "04": get_lang(lang, "timeconverter.mouth3"),
            "05": get_lang(lang, "timeconverter.mouth4"),
            "06": get_lang(lang, "timeconverter.mouth5"),
            "07": get_lang(lang, "timeconverter.mouth6"),
            "08": get_lang(lang, "timeconverter.mouth7"),
            "09": get_lang(lang, "timeconverter.mouth8"),
            "10": get_lang(lang, "timeconverter.mouth9"),
            "11": get_lang(lang, "timeconverter.mouth10"),
            "12": get_lang(lang, "timeconverter.mouth11")
        }
        self.week: dict[str, str] = {
            "0": get_lang(lang, "timeconverter.week0"),
            "1": get_lang(lang, "timeconverter.week1"),
            "2": get_lang(lang, "timeconverter.week2"),
            "3": get_lang(lang, "timeconverter.week3"),
            "4": get_lang(lang, "timeconverter.week4"),
            "5": get_lang(lang, "timeconverter.week5"),
            "6": get_lang(lang, "timeconverter.week6")
        }

    def time_name(self) -> tuple[str, str]:
        """
        Returns a now week and mouth name
        """
        now = datetime.now()
        return self.week[now.strftime('%w')], self.mouth[now.strftime('%m')]

    def mouth_name(self) -> str:
        """
        Returns a now mouth name
        """
        now = datetime.now()
        return self.mouth[now.strftime('%m')]

    def week_name(self) -> str:
        """
        Returns a now week name
        """
        now = datetime.now()
        return self.week[now.strftime('%w')]
