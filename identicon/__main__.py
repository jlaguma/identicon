import io

import click

from identicon import __version__
from .decorators import add_custom_help
from .lambdas import md5, get_color, get_random_string, get_random_color
from .identicon import Identicon


@click.command()
@click.version_option(__version__, "-V", "--version", message="%(version)s")
@click.option(
    '--key',
    '-k',
    help='Key string to generate Identicon from.',
)
@click.option(
    '--rand',
    '-r',
    is_flag=True,
    help='Generate random Identicon.',
)
@click.option(
    '--show',
    '-s',
    is_flag=True,
    help='Show generated Identicon.',
)
@click.option(
    '--write',
    '-w',
    help='File name to write to in PNG format.',
)
@add_custom_help
def main(key, rand, show, write):
    identicon = Identicon(key, rand)
    if show:
        identicon.show()

    if write:
        with open(write, 'wb') as f:
            f.write(identicon.byte_array())


if __name__ == '__main__':
    main()
