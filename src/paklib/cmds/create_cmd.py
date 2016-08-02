import os
import gflags
from textwrap import dedent

import hashlib
import zipfile

from ..exceptions import UsageError

from ..TreeScanner import TreeScanner
from ..PakManifest import PakManifest, PakFile, PakFolder

gflags.DEFINE_string('pkg_version',
    short_name = 'v',
    default = None,
    help="Version to tag this package with",
)
gflags.MarkFlagAsRequired('pkg_version')

gflags.DEFINE_bool(
    'warn_non_file',
    default = False,
    help = "Warn if file objects are found in source that are not directories or files"
)

def help():
    return dedent("""\
        Command Usage: pak create -v 1.0 source_folder/ pkg_name-1.0.pak
        """)


def _print(msg):
    print msg

def run(args):

    if len(args) != 2:
        raise UsageError("Got %d arguments, but I only expected 2 (%s)" % (len(args), ' '.join(args)))
    else:
        source_path, target_filename = args

    # Validate source path
    if not os.path.exists(source_path):
        raise UsageError("Source path doesn't exist: " + source_path)
    if not os.path.isdir(source_path):
        raise UsageError("Source path isn't a directory: " + source_path)

    # Examin target filename
    target = os.path.abspath(target_filename)
    if not os.path.exists(os.path.dirname(target)):
        raise UsageError("Directory doesn't exist for target: " + target)
    if not os.path.isdir(os.path.dirname(target)):
        raise UsageError("Target parent is not a directory: " + os.path.dirname(target))

    # Setup scanner
    scanner = TreeScanner(source_path)
    if gflags.FLAGS.warn_non_file:
        scanner.warn_non_file = lambda path: _print("WARNING: Skipping file object:" + path)

    # Init package file
    pak = zipfile.ZipFile(target, mode='w')

    # Process file objects in source folder
    manifest = PakManifest()
    for source_obj in scanner.scan():

        if source_obj.obj_type == 'folder':

            print '[D]', source_obj

            fold = PakFolder(source_obj.path)
            manifest.dirs[fold.path] = fold

        elif source_obj.obj_type == 'file':

            print '[F]', source_obj

            hash = hashlib.md5()
            hash.upd

            pfile = PakFile(source_obj.path)
            manifest.files[pfile.path] = pfile

            pak.write(source_obj.abs_path, os.path.join('files', pfile.path), zipfile.ZIP_DEFLATED)

    # Add manifest to package
    pak.writestr('manifest.json', manifest.save_string(), zipfile.ZIP_DEFLATED)

    # Clean up
    pak.close()
