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

    # Get command name
    argv = sys.argv[:]
    pak_cmd = os.path.basename(argv[0])
    if len(argv) < 2:
        usage_error("Must pick a command")
    # pak help (command)
    elif len(argv) >= 3 and argv[1] == 'help':
        command_name = argv[2]
        argv = [pak_cmd + ' ' + command_name, '--help'] + argv[3:]
    # pak (command) [options]
    else:
        command_name = argv[1]
        argv = [pak_cmd + ' ' + command_name, ] + argv[2:]

    # Load command
    if command_name == 'create':
        from paklib.cmds import create_cmd
        command_module = create_cmd
    else:
        usage_error("Unknown command: " + command_name)

    # Check command structure
    if 'run' not in dir(command_module):
        abort("Command %s is missing run()" % (command_name))
    if 'help' not in dir(command_module):
        abort("Command %s is missing help()" % (command_name))

    # Handle help
    if '--help' in argv:
        print command_module.help()

    # Parse command line arguments
    try:
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print 'USAGE ERROR: %s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS)
        sys.exit(1)

    # Run command
    command_module.run(argv)

    print "Finished"