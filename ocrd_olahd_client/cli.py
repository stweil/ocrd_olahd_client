import click
from ocrd.decorators import ocrd_cli_options, ocrd_cli_wrap_processor

from .processor import OlaHdClientProcessor

@click.command()
@ocrd_cli_options
def cli(*args, **kwargs):
    return ocrd_cli_wrap_processor(OlaHdClientProcessor, *args, **kwargs)
