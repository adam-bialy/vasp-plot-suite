"""
VASP-DOS-tools - library for processing electronic density of states (eDOS) from VASP calculations \n
Requires DOSCAR, POSCAR and PROCAR files present in the directory \n
AG, 2022 \n
"""


import numpy as np
from dos.vaspdostools.dostypes import RawDos, Dos, DosPlot


def extract(directory):
    """
    Reads DOS from VASP output \n
    See DOS class for more information \n
    :param directory:
    :return: DOS
    """
    return RawDos(directory)


def open_file(path, name=None):
    """
    Reads DOS from previously saved .csv \n
    :param str path: location
    :param str name: name for the system
    :return: Dos
    """
    dos_array = np.genfromtxt(path, delimiter=',', dtype=np.float64)
    if name is None:
        name = path.split(".")[-1]
    return Dos(dos_array, name)