from src.command import Command
from typing import Dict

from src.parser import Parser

LIGHT_CONSUMPTION = 5


class Solver:
    def __init__(self) -> None:
        """
        I'm using a dictionary rather than a simple list
        in order to optimize for duplicate handling
        This still lets me do O(1) insertions
        I could also use something like a BST to keep the structure sorted at all times
        but then the insertion time turns into O(logn)
        Although the sort is O(nlogn) so in the end you could say they're technically
        equivalent overall
        Still, the tree gives you an advantage from having the structure sorted at all
        times
        E.g. it's cheaper to check if a new command overflows the dimmer value at
        insertion time
        """
        self._storage: Dict[int, Command] = {}

    def add_command(self, input: str) -> None:
        command = Parser.parse_command(input)
        self._storage[command.timestamp] = command

    def run(self) -> float:
        # sort entries to accomodate for unordered positions
        sorted_timestamps = sorted(self._storage.keys())

        total = 0.0
        current_start = 0
        current_end = 0
        current_rate = 0.0

        def get_rate_for_period() -> float:
            return (
                (current_end - current_start) / 3600 * current_rate * LIGHT_CONSUMPTION
            )

        for timestamp in sorted_timestamps:
            command = self._storage[timestamp]

            current_end = command.timestamp

            total += get_rate_for_period()

            current_start = command.timestamp
            current_rate += command.delta

        total += get_rate_for_period()

        return total
