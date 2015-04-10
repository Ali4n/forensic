__author__ = 'Anubis'
import os
import subprocess

def volatility(number):
    number = str(number)
    print(number)
    if number == "1":
        getcwd = os.getcwd()

        command_line = "\\package\\library\\Volatility\\volatility.exe --help"
        command_line = getcwd + command_line

        p = subprocess.Popen(command_line, stdout=subprocess.PIPE, shell=True)
        out = p.stdout.readlines()
        out = ''.join(out)

        file = open('volatility_-h.txt', 'w+')

        file.write(out)
        file.close()
        print "Done!"

    if number == "2":
        print "deux"