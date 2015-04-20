import os
import subprocess

def recoverypassword():
    getcwd = os.getcwd()

    command_line = "\\package\\library\\Browser\\LaZagne.exe all -w"
    command_line = getcwd + command_line
    p = subprocess.call(command_line, stdout=subprocess.PIPE, shell=False)

    print "Done!"