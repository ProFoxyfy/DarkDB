import os
from tkinter.filedialog import askdirectory
import requests
import language
from os import system, name
current_lang = 1


def clear():
    # Dummy function bc it doesnt actually work
    return

def langIdToKey(id):
    if id == 1:
        return "german"
    else:
        return "english"

def get_lang_key(key):
    return language.lang_strings.get(langIdToKey(current_lang)).get(key)

def download_file(path,url):
    file = open(path,"wb")
    print(get_lang_key("download_start").replace("%",url))
    download = requests.get(url)
    file.write(download.content)
    print(get_lang_key("download_end"))

def get_file_from_branch(file,branch):
    repos = "https://raw.githubusercontent.com/ProFoxyfy/DarkDB/%TARGETBRANCH%/src/%TARGETFILE%"
    return repos.replace("%TARGETBRANCH%",branch).replace("%TARGETFILE%",file)

def install(branch):
    path = askdirectory()
    print(get_lang_key("folder_create"))
    darkdbPath = path
    download_file(darkdbPath + "\darkdb.py",get_file_from_branch("darkdb.py",branch))
    download_file(darkdbPath + "\\reader.py", get_file_from_branch("reader.py", branch))
    print(get_lang_key("install_end"))


def __main__():
    global current_lang
    print("Please select Language:")
    print("[1] Deutsch")
    print("[2] English")
    if input("Enter Selection:") == "1":
        current_lang = 1
    else:
        current_lang = 2
    clear()
    print(get_lang_key("select_branch"))
    if input(">>> ") == "1":
        clear()
        install("production")
    else:
        clear()
        install("experimental")

if __name__ == '__main__':
    __main__();
