import time
from tqdm import tqdm
import subprocess
import os 
txt = ""
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in tqdm(profiles):
    time.sleep(1)
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp850', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            txt += "{:<30}|  {:<}\n".format(i, results[0])
        except IndexError:
            txt += "{:<30}|  {:<}\n".format(i, "index hatası")
    except subprocess.CalledProcessError:
        txt += "{:<30}|  {:<}\n".format(i, "key clear degil")

with open('wifisifre.txt', 'w') as f:
    f.write(txt)

time.sleep(5)
os.startfile("wifisifre.txt")