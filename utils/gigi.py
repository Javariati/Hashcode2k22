import os
import zipfile
import time


def zippoh(path):
    print(banner())
    time.sleep(3)
    print("\n[ 0 ] - Starting zipping :DDDDDDDDD - [ 0 ]\n")
    zipf = zipfile.ZipFile(f"{path}/Submission.zip", 'w', zipfile.ZIP_DEFLATED)

    for dirname, subdirs, files in os.walk("/Users/andrearighi/Documents/GitHub/Hashcode2k22"):
        paths = ["/Users/andrearighi/Documents/GitHub/Hashcode2k22/.git/", "/Users/andrearighi/Documents/GitHub/Hashcode2k22/output/", "/Users/andrearighi/Documents/GitHub/Hashcode2k22/venv/"]

        to_continue = False

        for path in paths:
            if dirname.startswith(path):
                to_continue = True
                break

        if to_continue:
            continue

        zipf.write(dirname)
        for filename in files:
            zipf.write(os.path.join(dirname, filename))

    zipf.close()
    time.sleep(2)
    print("\n")
    print("FINISHED ZIIPPPING 8=====D\n")


def zip_dir(dir, path):
    print("[ ! ] - your zipping request has been sent to Trenitalia - [ ! ]\n")
    time.sleep(1)
    print("[ ! ] - Ciuf ciuf, train is coming xD - [ ! ]\n")
    print("""
        ───▄▄▄
        ─▄▀░▄░▀▄
        ─█░█▄▀░█
        ─█░▀▄▄▀█▄█▄▀
        ▄▄█▄▄▄▄███▀
    """)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file != "Submission.zip":
                dir.write(os.path.join(root, file),os.path.relpath(os.path.join(root, file),os.path.join(path, '..')))


def banner():
    return ("""
   ___ ___ ___ ___   _   _          ___      _   _               _____                    
  / __|_ _/ __|_ _| | |_| |_  ___  | _ \_  _| |_| |_  ___ _ _   |_  (_)_ __ _ __  ___ _ _ 
 | (_ || | (_ || |  |  _| ' \/ -_) |  _/ || |  _| ' \/ _ \ ' \   / /| | '_ \ '_ \/ -_) '_|
  \___|___\___|___|  \__|_||_\___| |_|  \_, |\__|_||_\___/_||_| /___|_| .__/ .__/\___|_|  
                                        |__/                          |_|  |_|            
    """) + f"""
    ╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┐┌ ┬┬    ╔═╗┌─┐┌─┐┌┬┐┬ ┬┌─┐┬─┐┌─┐┬ ┬┌─┐┬ ┬┌─┐┌─┐    ╦┌┐┌┌─┐
    ║║║├─┤ │ ├┤ │ ││││ ││    ╚═╗│ │├┤  │ │││├─┤├┬┘├┤ ├─┤│ ││ │└─┐├┤     ║││││  
    ╩ ╩┴ ┴ ┴ └─┘└─┘┘└┘└┘┴────╚═╝└─┘└   ┴ └┴┘┴ ┴┴└─└─┘┴ ┴└─┘└─┘└─┘└─┘────╩┘└┘└─┘
    """
