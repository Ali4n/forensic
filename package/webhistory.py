__author__ = 'lorisg91'

import os, time

#List all files from all Web Browsers History
def webhistory():
    folder_path = "C:\\tmp_forensic\\web_history\\"
    try:
        getcwd = os.getcwd()
        file = folder_path + "web_history.txt"
        print (file)
        command_line = getcwd + "\\package\\library\\NirSoft\\browsinghistoryview.exe /HistorySource 1 /LoadIE 1 /LoadFirefox 1 /LoadChrome 1 /LoadSafari 1 /stext " + file
        p = subprocess.Popen(command_line, stdout=subprocess.PIPE, shell=True)
        print ("Export de l'historique dans " + file + " reussi !")
    except:
        print("L'historique n'a pas ete exporte !\n\n")