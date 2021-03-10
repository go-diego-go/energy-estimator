import re
from src.command import Command

"""
I'm using a regular expression here for 3 main reasons:
1) I find them fun and interesting
2) I get both parsing and validation out of the box
3) The strings themselves are pretty short (or so they are so far),
   so the performance should still be ok
"""
TIMESTAMP = r"[1-9]\d*"
FRACTIONAL_VALUE = r"(0\.\d+)"
ONE = r"(1(\.0+)?)"
DELTA_COMMAND = fr"(Delta (?P<sign>\+|\-)(?P<value>{FRACTIONAL_VALUE}|{ONE}))"
TURNOFF_COMMAND = "(TurnOff)"
INPUT_PARSER = re.compile(
    (
        # timestamp component
        fr"^(?P<timestamp>{TIMESTAMP}) "
        # command component (either TurnOff or Delta)
        fr"({TURNOFF_COMMAND}|{DELTA_COMMAND})$"
    )
)


class Parser:
    @staticmethod
    def parse_command(input: str) -> Command:
        matches = INPUT_PARSER.match(input)

        if not matches:
            raise ValueError("Invalid input. Please try again.")

        timestamp = int(matches.group("timestamp"))

        # I'm assuming that if the regex matched, I either got:
        # a) A Delta command (with a corresponding value)
        # b) A TurnOff command (with no value, which defaults to 0.0)
        value = matches.group("value") or "0.0"
        sign = matches.group("sign")
        delta = float(value) * (-1 if sign == "-" else 1)

        return Command(timestamp, delta)
