import os
import sys
import gflags
from textwrap import dedent

USAGE = dedent("""\
            Usage: pak (command)

            Valid commands:
                create - Create a new package

            View help as:
                pak help (command)
            """)

def usage_error(msg):
    print "Usage Error:", msg
    print USAGE
    sys.exit(1)


def abort(msg):
    print "ERROR:", msg
    print "ABORTING"
    sys.exit(2)


if __name__ == '__main__':

    # Get command
    if len(sys.argv) < 2:
        usage_error("Must pick a command")
    command_name = sys.argv[1]

    # Handle help
    help_command = None
    if command_name == 'help':
        if len(sys.argv) < 3:
            print USAGE
            sys.exit(1)
        elif len(sys.argv) > 3:
            usage_error("Too many arguments for help")
        help_command = command_name
        command_name = sys.argv[2]

    # Load command
    if command_name == 'create':
        from paklib.cmds import create_cmd
        command = create_cmd
    else:
        usage_error("Unknown command: " + command_name)

    # Check command structure
    if 'go' not in dir(command):
        abort("Command %s is missing go()" % (command_name))
    if 'help' not in dir(command):
        abort("Command %s is missing help()" % (command_name))

    # Parse command line arguments
    try:
        argv = [sys.argv, ] + sys.argv[2:]
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print 'USAGE ERROR: %s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS)
        sys.exit(1)

    # Handle help
    if help_command is not None:
        print command.help()
        sys.exit(1)

    # Run command
    command.go(argv)

    print "Finished"