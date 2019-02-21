import os
import psutil
import subprocess
import pathlib
import shutil



def kill_process(pid):
    #print(type(pid))
    try:
        proc = psutil.Process(int(pid))
        proc.kill()
    except:
        print("Not able to kill")

def make_output(dirname):
    try:
        if dirname not in os.listdir(os.getcwd()):
            os.mkdir(dirname)
            print("dir created with dirname:{dirname}".format(dirname))

    except:
        print("Not able to create Dir")


def copy_to_current():
    shutil.copy2("src", "dest")


if __name__  == '__main__':
    process_name = input("enter process name")
    try:
        process_pid = subprocess.check_output(['pidof', process_name])

    except:
        print("PID not Found")

    kill_process(process_pid.decode('utf-8').split(" ")[0])
    make_output("test_dir")
    copy_to_current()
