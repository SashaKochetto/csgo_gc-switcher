
from urllib.request import urlopen, urlretrieve

from time import sleep

from . import PLATFORM_SYSTEM
from config import APP_VERSION_STRING, APP_ID

DOWNLOAD_URL = f"https://github.com/SashaKochetto/csgo_gc-switcher/releases/latest/download/update_pack-{PLATFORM_SYSTEM}.zip"
VERSION_URL = "https://raw.githubusercontent.com/SashaKochetto/csgo_gc-switcher/master/.service/version.txt"

def update():

    try:
        latest_version = urlopen(VERSION_URL).read().decode('utf8').splitlines()[0]
    except:
        print("\nUnable to check for updates.\n")
        return True

    if APP_VERSION_STRING == latest_version:
        return True

    print(f'Update available!\nNew version: {latest_version}\n')
    user_answer = input('Update now? [y/n]: ')
    if user_answer.lower() == 'y':
        print("\nDownloading update...")

        try:
            urlretrieve(DOWNLOAD_URL, f".{APP_ID}/update.zip")
        except:
            print("Something went wrong...\nUpdate failed!")
            return True

        print("To apply the update, you need to reopen the application.\nThe application will close automatically in 3 seconds...")
        sleep(3)

        return False