from typing import List
from src.solver import Solver


def test_e2e() -> None:
    run_test(["1544206562 TurnOff", "1544206563 Delta +0.5", "1544210163 TurnOff"], 2.5)
    run_test(
        [
            "1544206562 TurnOff",
            "1544206563 Delta +0.5",
            "1544210163 Delta -0.25",
            "1544211963 Delta +0.75",
            "1544211963 Delta +0.75",
            "1544213763 TurnOff",
        ],
        5.625,
    )


def run_test(inputs: List[str], result: float) -> None:
    solver = Solver()
    for input in inputs:
        solver.add_command(input)
    assert solver.run() == result
