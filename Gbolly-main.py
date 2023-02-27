import os
import sys
import time 
from time import sleep


#### colours ####
# B='\033[1;94m'
# R='\033[1;91m'
# G='\033[1;92m'
# W='\033[1;97m'
# S='\033[1;96m'
# P='\033[1;95m'
# Y='\033[1;93m'
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'



Gbolly ="""\033[1;97m

\033[1;91m$$\      $$\ $$\                  $$\                                                      $$$$$$\                               $$\       
\033[1;92m$$ | $\  $$ |$$ |                 $$ |                                                    $$  __$$\                              $$ |      
\033[1;93m$$ |$$$\ $$ |$$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\          $$ /  \__| $$$$$$\  $$$$$$\   $$$$$$$\ $$$$$$$\  
\033[1;94m$$ $$ $$\$$ |$$  __$$\  \____$$\\_$$  _|  $$  _____| \____$$\ $$  __$$\ $$  __$$\ $$$$$$\ $$ |      $$  __$$\ \____$$\ $$  _____|$$  __$$\ 
\033[1;95m$$$$  _$$$$ |$$ |  $$ | $$$$$$$ | $$ |    \$$$$$$\   $$$$$$$ |$$ /  $$ |$$ /  $$ |\______|$$ |      $$ |  \__|$$$$$$$ |\$$$$$$\  $$ |  $$ |
\033[1;96m$$$  / \$$$ |$$ |  $$ |$$  __$$ | $$ |$$\  \____$$\ $$  __$$ |$$ |  $$ |$$ |  $$ |        $$ |  $$\ $$ |     $$  __$$ | \____$$\ $$ |  $$ |
\033[1;97m$$  /   \$$ |$$ |  $$ |\$$$$$$$ | \$$$$  |$$$$$$$  |\$$$$$$$ |$$$$$$$  |$$$$$$$  |        \$$$$$$  |$$ |     \$$$$$$$ |$$$$$$$  |$$ |  $$ |
\033[1;92m\__/     \__|\__|  \__| \_______|  \____/ \_______/  \_______|$$  ____/ $$  ____/          \______/ \__|      \_______|\_______/ \__|  \__|
                                                              $$ |      $$ |                                                               
                                                              $$ |      $$ |                                                               
                                                              \__|      \__|                                                        \033[1;91mVersion 2.5

   
                                                                                                                

                                                  \033[1;93mThis is a whatsapp crash toolkit

                                                                                                                      
                                                  \033[1;92mCoded by Omotosho Gbolahan Hammed                                                                      
                                                  \033[1;96mGithub: https://github.com/Gbolahanomotosho                                                          
                                                  \033[1;95mFacebook: Facebok.com/Gbolahanomotosho
                                                  \033[1;93mInstagram: _lord_of_hacker        
                                                  \033[1;91mWhatsapp: 08022648626                                                                                 
                                                  \033[1;94mThis tools is very dangerous 
                                                  \033[1;94mPls use it wisely
                                                   






      
         \033[1;91m[1] Crash WhatsApp number                          
         \033[1;96m[2] Crash WhatsApp Group 
         \033[1;94m[3] Report a bug                        
         \033[1;92m[4] Contact the developer and check for new update 
                




                                                                                                                                                               \033[1;97m"""






for i in Gbolly:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)



try:
        menu = int(input("\033[1;93mEnter an option: "))
except ValueError:
        print("\033[1;92mEnter the correct number")
        time.sleep(3)
        loop()



if menu == 1:


    if os.path.exists('Gbolahan-whatsapp-crash.py'):

        os.system("python3 Gbolahan-whatsapp-crash.py")


elif menu == 2:

    if os.path.exists('Group-whatsapp-crash.py'):

        os.system("python3 Group-whatsapp-crash.py")


elif menu == 3:
    if os.path.exists('Report.py'):

        os.system("python3 Report.py")


elif menu == 4:
    os.system("xdg-open https://github.com/Gbolahanomotosho")
    time.sleep(2)
    os.system("xdg-open https://facebook.com/gbolahan.omotosho.73")
    time.sleep(2)
    os.system("xdg-open https://wa.me/08022648626")



