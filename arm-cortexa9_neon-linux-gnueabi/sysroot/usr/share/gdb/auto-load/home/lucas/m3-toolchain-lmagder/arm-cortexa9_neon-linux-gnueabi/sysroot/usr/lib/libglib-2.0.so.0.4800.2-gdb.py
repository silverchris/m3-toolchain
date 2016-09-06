import sys
import gdb

# Update module path.
dir_ = '/home/lucas/m3-toolchain-lmagder/arm-cortexa9_neon-linux-gnueabi/sysroot/usr/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib import register
register (gdb.current_objfile ())
