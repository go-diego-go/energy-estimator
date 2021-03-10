from src.command import Command
from pytest import raises

from src.parser import Parser


def test_valid_inputs() -> None:
    assert Parser.parse_command("1544206562 TurnOff") == Command(1544206562, 0.0)
    assert Parser.parse_command("1544206563 Delta +0.5") == Command(1544206563, 0.5)
    assert Parser.parse_command("1544206563 Delta -0.25") == Command(1544206563, -0.25)
    assert Parser.parse_command("1544206563 Delta -1.0") == Command(1544206563, -1.0)
    assert Parser.parse_command("1544206563 Delta +1.00") == Command(1544206563, 1.0)


def test_invalid_inputs() -> None:
    do_invalid_input_test("bla")
    do_invalid_input_test("1.12345 TurnOff")
    do_invalid_input_test("1.12345 Delta +0.5")
    do_invalid_input_test("1234123 Turnoff")
    do_invalid_input_test("12345 Delta")
    do_invalid_input_test("54321 Delta 0")
    do_invalid_input_test("38838 TurnOff +0.5")
    do_invalid_input_test("12345 Delta +1.5")
    do_invalid_input_test("12345 Delta -1.4")
    do_invalid_input_test("12345 Delta -0..4")
    do_invalid_input_test("Delta -0.4")


def do_invalid_input_test(input: str) -> None:
    with raises(ValueError) as excinfo:
        Parser.parse_command(input)
    assert str(excinfo.value) == "Invalid input. Please try again."
