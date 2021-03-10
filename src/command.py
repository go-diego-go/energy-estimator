class Command:
    def __init__(self, timestamp: int, delta: float):
        self._delta = delta
        self._timestamp = timestamp

    @property
    def delta(self) -> float:
        return self._delta

    @property
    def timestamp(self) -> int:
        return self._timestamp

    # I'm only implementing these two methods for the purposes of easier testing
    # Especially __eq__
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Command):
            return False

        return self.delta == other.delta and self.timestamp == other.timestamp

    def __hash__(self) -> int:
        return hash((self.timestamp, self.delta))
