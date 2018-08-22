import os
import sys
import urllib
from subprocess import Popen, PIPE

ROOT_DIR = "."
EXCLUDE_LIST = ["Home.md", ".githooks", ".git", "_Sidebar.md"]

def get_url_of_wikigit():
    popen = Popen("git config --get remote.origin.url", shell=True, stdout=PIPE)
    out, error = popen.communicate()
    out = out.rstrip()
    if out.endswith(".git"):
        out = out[:-4]
    i = out.rfind(".")
    if (i != -1):
        out = out[:i] + "/" + out[i+1:]
    return out

def traversal(root_dir, depth):
    try:
        unsorted_file_list = os.listdir(root_dir)
        sub_dir_list = [] 
        file_list = sorted(unsorted_file_list, key=lambda s: s.lower())

        for file_name in file_list:
            if file_name in EXCLUDE_LIST :
                continue
            
            file_path = os.path.join(root_dir, file_name)
            if os.path.isdir(file_path):
                sub_dir_list.append(file_name)
                continue
            
            name, ext = os.path.splitext(file_name)
            if not (ext == ".md"):
                continue

            for i in range(0,depth): sys.stdout.write("\t")
            abs_url = WIKI_URL + "/" + name
            encoded_url = WIKI_URL + "/" + urllib.quote_plus(name) 
            
            sys.stdout.write("* [" + name + "](" + encoded_url + ")\n")

        for sub_dir_name in sub_dir_list:
            sub_dir_path = os.path.join(root_dir, sub_dir_name)
            
            for i in range(0,depth): sys.stdout.write("\t")
            sys.stdout.write("* [" + sub_dir_name + "]\n")

            traversal(sub_dir_path, depth+1)

    except PermissionErr:
        pass

WIKI_URL = get_url_of_wikigit()
sys.stdout.write("[Home](" + WIKI_URL + "/Home)\n")
traversal(ROOT_DIR, 0)
