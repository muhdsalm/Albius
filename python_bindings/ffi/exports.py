from ctypes import POINTER, c_char_p, c_int

from ffi import __lib__

from .disk import Disk, Partition


def setup_exports():
    # --------------------------disk_ops---------------------------
    # LocateDisk
    __lib__.LocateDisk.argtypes = [c_char_p]
    __lib__.LocateDisk.restype = POINTER(Disk)

    # Mount
    __lib__.Mount.argtypes = [POINTER(Partition), c_char_p]
    __lib__.Mount.restype = None

    # UmountPartition
    __lib__.UmountPartition.argtypes = [POINTER(Partition)]
    __lib__.UmountPartition.restype = None

    # UmountDirectory
    __lib__.UmountDirectory.argtypes = [c_char_p]
    __lib__.UmountDirectory.restype = None

    # --------------------------file_ops---------------------------
    # Unsquashfs
    __lib__.Unsquashfs.argtypes = [c_char_p, c_char_p, c_int]
    __lib__.Unsquashfs.restype = None

    # ------------------------partitioning-------------------------
    # NewPartition
    __lib__.NewPartition.argtypes = [POINTER(Disk), c_char_p, c_char_p, c_int, c_int]
    __lib__.NewPartition.restype = None

    # RemovePartition
    __lib__.RemovePartition.argtypes = [POINTER(Partition)]
    __lib__.RemovePartition.restype = None

    # ResizePartition
    __lib__.ResizePartition.argtypes = [POINTER(Partition), c_int]
    __lib__.ResizePartition.restype = None
