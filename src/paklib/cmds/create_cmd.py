
from textwrap import dedent

from ..exceptions import UsageError

def help():
    return dedent("""\
        Command Usage: pak create source_folder/ pkg_name-1.0.pak -v 1.0
        """)

def run(args):

    if len(args) !=  2:
        