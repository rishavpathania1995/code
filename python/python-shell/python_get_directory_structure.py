import os

CURR_DIR = os.getcwd()
print("current dir :{}".format(CURR_DIR))

DEST_DIR = '/mnt/wsraid_nfs'

os.chdir(DEST_DIR)

d = {}
list_filename_all = []

for root, dirs, files in os.walk(".", topdown=False):
    for file_name in files:
        list_filename_all.append(os.path.join(root, file_name))
        print(len(list_filename_all))

print(list_filename_all)


