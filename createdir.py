import os

print(os.getcwd())
os.mkdir("Dir_1")
os.chdir("Dir_1")
os.mkdir("Dir_2")
os.chdir("Dir_2")
print(os.getcwd())
os.chdir("..")
os.mkdir("Dir_3")
os.chdir("Dir_3")
os.mkdir("Dir_4")
os.chdir("Dir_4")
print(os.getcwd())

question = input("Do you want to delete the folders you created? Press Yes or No: ")

if question == "Yes":
    os.chdir("..")
    os.rmdir("Dir_4")
    os.chdir("..")
    os.rmdir("Dir_3")
    os.rmdir("Dir_2")
    os.chdir("..")
    os.rmdir("Dir_1")
    print(os.getcwd())
