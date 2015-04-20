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
