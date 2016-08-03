import os
import gflags
from textwrap import dedent

import hashlib
import zipfile

from ..exceptions import UsageError

from ..Bunch import Bunch
from ..TreeScanner import TreeScanner
from ..PakManifest import PakManifest, PakFile, PakFolder

def help():
    return dedent("""\
        Command Usage: pak install pkg_name-1.0.pak /target/path
        """)


def run(args):

    if len(args) != 2:
        raise UsageError("Got %d arguments, but I only expected 2 (%s)" % (len(args), ' '.join(args)))
    else:
        pak_path, target_path = args

    # Validate target_path path
    target_path = os.path.abspath(target_path)
    if not os.path.exists(target_path):
        raise UsageError("Target path doesn't exist: " + target_path)
    if not os.path.isdir(target_path):
        raise UsageError("Target path isn't a directory: " + target_path)

    # Examine pak path
    pak_path = os.path.abspath(pak_path)
    if not os.path.exists(pak_path):
        raise UsageError("Package doesn't exist: " + pak_path)
    if not os.path.isfile(pak_path):
        raise UsageError("Package path is not a file: " + pak_path)

    # Open package
    pak = zipfile.ZipFile(pak_path, 'r')

    # Get manifest
    manifest = PakManifest()
    with pak.open('manifest.json', 'r') as fh:
        manifest.load_string(fh.read())

    # List files in target
    existing = Bunch(
        files = dict(),
        dirs = dict(),
        paths = set(),
        scanner = TreeScanner(target_path),
    )
    for target_obj in existing.scanner.scan():
        existing.paths.add(target_obj.path)

        if target_obj.obj_type == 'folder':
            existing.dirs[target_obj.path] = target_obj

        elif target_obj.obj_type == 'file':
            existing.files[target_obj.path] = target_obj




