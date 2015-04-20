__author__="Anubis"


import os
import subprocess
from package.volatility import *
from package.listfiles import *
from package.dumpit import *
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
                " 3: Registry Analysis\n"
                " 4: Event Log Analysis\n"
                " 5: NTFS Filesystem Analysis\n"
                " 6: Network Support Utilities\n"
                " 7: ALL\n"
                " 8: Quitter le programme\n"
            )
        except:
            print "Saisir le numero du menu, s il vous plait."
            exit()

        if menu_principal == 1:
            while 1:
                try:
                    menu_memory_dump = input("#####################  MENU 1: Memory Dump  #####################\n"
                                             "1: DumpIt\n"
                                             "2: Volatility\n"
                                             "3: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_memory_dump == 1:
                    dumpit()
                elif menu_memory_dump == 2:
                    volatility(1)
                    break

        elif menu_principal == 2:
            while 1:
                try:
                    menu_artifact_analysis = input("#####################  MENU 2: Artifact Analysis  #####################\n"
                                                 "1: Prefech \n"
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
                    menu_registery_event_log_analysis = input("################  MENU 3: Registry Analysis  ################\n"
                                                              " 1: Base SAM\n"
                                                              " 2: Security Policy"
                                                              " 3: Get NTUSER.DAT infos"
                                                              " 4: Retour au menu principal\n"
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
                    menu_registery_event_log_analysis = input("################  MENU 4: Event Log Analysis  ################\n"
                                                              " 1: Base SAM\n"
                                                              " 4: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_registery_event_log_analysis == 1:
                    print "A Voir"
                elif menu_registery_event_log_analysis == 2:
                    break

        elif menu_principal == 5:
            while 1:
                try:
                    menu_ntfs_filesystem_analysis = input("#####################  MENU 5: NTFS Filesystem Analysis  #####################\n"
                                                              " 1: List Personal Files\n"
                                                              " 2: List Web Browsers History\n"
                                                              " 3: Retour au menu principal\n"
                    )
                except:
                    print "Saisir le numero du menu, s il vous plait."
                    exit()

                if menu_ntfs_filesystem_analysis == 1:
                    listfiles()
                elif menu_ntfs_filesystem_analysis == 2:
                    webhistory()
                elif menu_ntfs_filesystem_analysis == 3:
                    break

        elif menu_principal == 6:
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

        elif menu_principal == 7:
            print "ALL"
            volatility(1)

        elif menu_principal == 8:
            print "Bonne journee, a bientot"
            exit()


main()