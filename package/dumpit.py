__author__ = 'Anubis'

import os
import subprocess

def dumpit():
    getcwd = os.getcwd()

    command_line = "\\package\\library\\DumpIt\\DumpIt.exe >> C:\\Users\\Forensics\\PycharmProjects\\forensic\\package\\library\\DumpIt\\1.raw"
    command_line = getcwd + command_line
    p = subprocess.Popen(command_line, stdout=subprocess.PIPE, shell=True)
