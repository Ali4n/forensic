__author__ = 'Anubis'

import os, time

#List All Files in DIR + get Size + get Creation
def listfiles():
    folder_path = "C:\\Users"
    print(folder_path)
    try:
        for path, dirs, files in os.walk(folder_path):
            for filename in files:
                print("Nom Long : "+path+"\\"+filename)
                #Taille
                print("Taille: "+str(os.path.getsize(path+"\\"+filename))+" Octets")
                #Date creation
                print("Date de Creation: "+str(time.ctime(os.path.getctime(path+"\\"+filename))))
                #Date Modification
                print("Date de Modification: "+str(time.ctime(os.path.getmtime(path+"\\"+filename))))
    except:
        print("Fail")
        #faire une gestion des erreurs plus avancee

def webhistory():
    folder_path = "C:\\Users"
    print(folder_path)
    try:
        getcwd = os.getcwd()
        command_line = "\\package\\library\\NirSoft\\browsinghistoryview.exe /HistorySource 1 /LoadIE 1 /LoadFirefox 1 /LoadChrome 1 /LoadSafari 1 /stext "C:\\tmp_forensic\web_history\web_history.txt""
        command_line = getcwd + command_line
    except:
        print("Fail")