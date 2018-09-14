#Created by Kevin Yunqiao Liu, Sept. 14 2018

import os

os.system("cd /Users/kevin.liu/Desktop/GitRepo\ Year\ 9/Year9DesignCS4-PythonKL")
os.system("git status")
os.system("git add .")

str1 = input("Commit Message: ")
commit = "git commit -m " + str1

os.system(commit)
os.system("git push")
