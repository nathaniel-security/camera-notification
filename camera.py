import os
while True:
    a  = os.system("lsof /dev/video0")
    #print(a)
    #print(type(a))
    if (a != 256):
        import subprocess
        subprocess.Popen(['notify-send', "application trying to access camera"])
        