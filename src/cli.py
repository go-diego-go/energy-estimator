import click

from src.solver import Solver


@click.command()
def estimator() -> None:
    solver = Solver()
    while True:
        try:
            command = click.prompt(text="", prompt_suffix=click.style("> ", fg="green"))
            solver.add_command(command)
        except ValueError as excinfo:
            click.echo(click.style(str(excinfo), fg="red"))
        except click.Abort:
            click.echo(click.style("EOF", fg="red"))
            click.echo(
                click.style(f"Estimated energy used: {solver.run()} Wh", fg="blue")
            )
            break
