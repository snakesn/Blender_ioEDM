#!/usr/bin/env blender

import sys
import os

import bpy
import addon_utils

def _main(args):
  print("Writing", args)

  default, state = addon_utils.check("io_EDM")
  if not state:
    import io_EDM
    io_EDM.register()

  try:
    myArgumentIndex = next(i for i, v in enumerate(sys.argv) if v == "--")
    args = args[myArgumentIndex+1:]
  except StopIteration:
    pass
  filepath = args[0] if args else "test.edm"
  # Call the import operator
  bpy.ops.export_mesh.edm(filepath=filepath)

if __name__ == "__main__":
  if _main(sys.argv) == -1:
    sys.exit()