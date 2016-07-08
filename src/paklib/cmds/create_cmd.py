
from textwrap import dedent

def help():
    return dedent("""\
        Command Usage: pak create source_folder/ pkg_name-1.0.pak -v 1.0
        """)


def run(argv):
    print "HIT", ' '.join(argv)