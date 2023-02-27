#!/usr/bin/python3
#coding=utf-8
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

Report="""

                        \033[1;91mYou can report any bug you notice on this tools to the developer with a screenshot of the bug

                        \033[1;91mWhere do you want to report the bug?


                        \033[1;95mThrough:


\033[1;96m[1] \033[1;94mFacebook


\033[1;93m[2] \033[1;92mWhatsapp



\033[1;95m[3] \033[1;97mGithub



"""



for i in Report:
        time.sleep(0.01)
        print(i, end='',flush=True)


answer = int(input("\033[1;97mChoose: "))


if answer == 1:


    os.system("xdg-open https://facebook.com/gbolahan.omotosho.73")
    time.sleep(2)
    os.system("xdg-open https://facebook.com/gbolahan.omotosho.73")
elif answer == 2:



    os.system("xdg-open https://wa.me/08022648626")
    time.sleep(2)
    os.system("xdg-open https://wa.me/08022648626")
elif answer == 3:



    os.system("xdg-open https://github.com/Gbolahanomotosho")
    time.sleep(2)
    os.system("xdg-open https://github.com/Gbolahanomotosho")
