__author__="Anubis"


import os
import subprocess
from package.volatility import *

#windows7 32 ou 64 bits

def main():
    while 1:
        os.system('CLS')
        try:
            menu_principal = input(
                "   _   _   _   _   _    _   _   _   _  \n"
                "  / \ / \ / \ / \ / \  / \ / \ / \ / \ \n"
                " ( F | 0 | R | E | N )( S | I | C | S | \n"
                "  \_/ \_/ \_/ \_/ \_/  \_/ \_/ \_/ \_/  \n\n"
                "---- Saisir le numero du menu ----\n"
                " 1: Memory Dump\n"
                " 2: Artifact Analysis\n"
                " 3: Registery and Event Log Analysis\n"
                " 4: NTFS Filesystem Analysis \n"
                " 5: Network Support Utilities\n"
                " 6: ALL \n"
                " 7: Quitter le programme\n"
            )
        except:
            print "Saisir le numero du menu, s il vous plait."
            exit()

        if menu_principal == 1:
            while 1:
                try:
                    menu_memory_dump = input("#####################  MENU 1: Memory Dump  #####################\n"
                                             "1: volatility -h : list all available options and their default values.\n"
                                             "2: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_memory_dump == 1:
                    volatility(1)
                elif menu_memory_dump == 2:
                    break

        elif menu_principal == 2:
            while 1:
                try:
                    menu_artifact_analysis = input("#####################  MENU 2: Artifact Analysis  #####################\n"
                                                 "1: A Voir\n"
                                                 "2: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_artifact_analysis == 1:
                    print "A voir"
                elif menu_artifact_analysis == 2:
                    break

        elif menu_principal == 3:
            while 1:
                try:
                    menu_registery_event_log_analysis = input("################  MENU 3: Registery and Event Log Analysis  ################\n"
                                                              " 1: A Voir\n"
                                                              " 2: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_registery_event_log_analysis == 1:
                    print "A Voir"
                elif menu_registery_event_log_analysis == 2:
                    break

        elif menu_principal == 4:
            while 1:
                try:
                    menu_ntfs_filesystem_analysis = input("#####################  MENU 4: NTFS Filesystem Analysis  #####################\n"
                                                              " 1: A Voir\n"
                                                              " 2: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_ntfs_filesystem_analysis == 1:
                    print "A voir"
                elif menu_ntfs_filesystem_analysis == 2:
                    break

        elif menu_principal == 5:
            while 1:
                try:
                    menu_network_support_utilities = input("#####################  MENU 5: Network Support Utilities  #####################\n"
                                                            "1: A Voir\n"
                                                            "2: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_network_support_utilities == 1:
                    print "A voir"
                elif menu_network_support_utilities == 2:
                    break

        elif menu_principal == 6:
            print "ALL"
            volatility(1)

        elif menu_principal == 7:
            print "Bonne journee, a bientot"
            exit()


main()