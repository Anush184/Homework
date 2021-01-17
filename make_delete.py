import os


def make_delete_dirs():
    print(os.getcwd())
    dir_names = ("Dir_1", "Dir_2", "Dir_3", "Dir_4")
    for item in dir_names:
        os.mkdir(item)
        os.chdir(item)
        if item == "Dir_2":
            os.chdir("..")
    print(os.getcwd())
    question = input("Do you want to delete the folders you created? Press Yes or No: ")
    if question == 'Yes':
        for item in dir_names[::-1]:
            if len(os.listdir(os.getcwd())) == 0:
                os.chdir("..")
                os.rmdir(item)
            else:
                os.chdir(".")
                os.rmdir(item)
        print(os.getcwd())


make_delete_dirs()


