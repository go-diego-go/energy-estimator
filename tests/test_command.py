from src.command import Command


def test_class_properties() -> None:
    command = Command(12345, -0.5)
    assert command.delta == -0.5
    assert command.timestamp == 12345

    assert Command(123, 0.2) == Command(123, 0.2)
    assert Command(123, 0.2) != Command(12, 0.2)
    assert Command(123, 0.2) != Command(123, 0.1)
    assert Command(123, 0.5) != "not a command"

    assert hash(Command(123, 0.5)) == hash(Command(123, 0.5))
