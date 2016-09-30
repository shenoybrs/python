import os
def rename_files():
    file_list = os.listdir(r"D:\python-projects\alphabet\alphabet")
    print(file_list)
    current_dir = os.curdir
    os.chdir(r"D:\python-projects\alphabet\alphabet")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(current_dir)
rename_files()
