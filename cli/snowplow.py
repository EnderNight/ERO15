#
# cli/snowplow.py
#

import typer

app = typer.Typer(
    no_args_is_help=True,
    help="Snowplow related computing.",
)

from typing import Annotated, Optional
from rich.console import Console
from rich.table import Table

import snowplow.clear
import cli.log as log

console = Console()
err_console = Console(stderr=True)


@app.command()
def clear(
    id: Annotated[
        int,
        typer.Argument(
            help="The id of the snow data generated by the drone."
        ),
    ] = 0
) -> None:
    """
    Start the snowplows.
    """
    snowplow.clear.clear(id)
