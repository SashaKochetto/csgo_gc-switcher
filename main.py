
from config import (
    APP_NAME,
    APP_ID,
    APP_VERSION_STRING,
    VANILLA_FOLDER,
)

from os import mkdir
from shutil import rmtree, copy
from os.path import exists as is_exists, isfile
from json import load as j_load

from modules import (
    PLATFORM_SYSTEM,
    autoupdate,
    switcher,
    map_generator,
)

LOADED_MAPS = None
APP_FOLDER = f".{APP_ID}"
VANILLA_FOLDER = f"{APP_FOLDER}/csgo_vanilla"

is_csgo_folder = True
extension = ".exe"
if PLATFORM_SYSTEM != 'windows':
    extension = "_linux64"

if not is_exists("csgo") or not isfile(f"csgo{extension}"):
    print("It looks like this isn't the 'csgo legacy' folder.")
    is_csgo_folder = ( input("Are you sure you want to continue? [y/n]: ").lower() == 'y' )

if not is_exists(APP_FOLDER):
    mkdir(APP_FOLDER)
    LOADED_MAPS = map_generator.make_map_file()

else:
    if not is_exists(f"{APP_FOLDER}/map.json"):
        LOADED_MAPS = map_generator.make_map_file()
    else:
        with open(f"{APP_FOLDER}/map.json", "r") as f:
            LOADED_MAPS = j_load(f)

if is_csgo_folder and autoupdate.update():
    while True:
        print(f"{APP_NAME} v{APP_VERSION_STRING}\n\nSelect an action:\n[1] Create a vanilla CSGO dump\n[2] Switch to Project446\n[3] Switch to Mikkokko's csgo_gc\n[4] Restore the vanilla version\n[5] Quit\n")
        user_option = input("> ")

        if user_option == "1":

            print("\nWARNING!\nBefore creating a dump, ensure that no mods are currently installed!")
            user_option = input("Continue? [y/n]: ")

            if user_option.lower() != 'y':
                continue

            if is_exists(VANILLA_FOLDER):
                print("\nThe vanilla dump has already been created!")
                overwrite = input('Overwrite? [y/n]: ')

                if overwrite.lower() != 'y':
                    continue

                rmtree(VANILLA_FOLDER)

            mkdir(VANILLA_FOLDER)

            print("\nCreating dump...")

            for path in LOADED_MAPS['game']:
                dirs = path.split("/")

                if isfile(path):

                    if len(dirs) == 1:
                        copy(path, f"{VANILLA_FOLDER}/{path}")
                        continue

                    target = dirs.pop()
                    path = "/".join(dirs)

                    current_path = VANILLA_FOLDER

                    for dir in dirs:

                        current_path += f"/{dir}"
                        if is_exists(current_path):
                            continue

                        mkdir(current_path)

                    current_path += f"/{target}"

                    full_path = f"{path}/{target}"
                    copy(full_path, current_path)

            print("\nDump created!")
            _ = input("Press Enter to return to the main menu...\n")
            continue

        elif user_option == "2":

            print("\nThis action will result in the complete deletion of the modded by csgo_gc binaries (inventory.txt, etc. will be saved)!")
            user_option = input("Do you want to continue? [y/n]: ")

            if user_option.lower() != 'y':
                continue

            print("Preparing files...")

            switcher.restore(LOADED_MAPS, VANILLA_FOLDER)

            url_mod = "https://project446.com/api/download/zip"
            archive_name = "Project446-Client.zip"
            if PLATFORM_SYSTEM == 'linux':
                url_mod = "https://project446.com/api/download/linux64"
                archive_name = "Project446-Client-Linux-x64.tar.gz"

            print("Downloading mod...")

            is_successful = switcher.download_and_extract(url_mod, archive_name)

            message = "The mod has been installed successfully!"
            if not is_successful:
                message = "Something went wrong...\nTry downloading and installing it manually"

            print(message)
            _ = input("Press Enter to return to the main menu...\n")

            continue

        elif user_option == "3":

            print("\nThis action will result in the complete deletion of the modded by csgo_gc binaries (inventory.txt, etc. will be saved)!")
            user_option = input("Do you want to continue? [y/n]: ")

            if user_option.lower() != 'y':
                continue

            print("Preparing files...")

            switcher.restore(LOADED_MAPS, VANILLA_FOLDER)

            url_mod = "https://github.com/Mikkokko/csgo_gc/releases/latest/download/csgo_gc-windows-latest.zip"
            archive_name = "csgo_gc-windows-latest.zip"
            if PLATFORM_SYSTEM == 'linux':
                url_mod = "https://github.com/Mikkokko/csgo_gc/releases/latest/download/csgo_gc-ubuntu-latest.zip"
                archive_name = "csgo_gc-ubuntu-latest.zip"

            print("Downloading mod...")

            is_successful = switcher.download_and_extract(url_mod, archive_name)

            message = "The mod has been installed successfully!"
            if not is_successful:
                message = "Something went wrong...\nTry downloading and installing it manually"

            print(message)
            _ = input("Press Enter to return to the main menu...\n")

            continue


        elif user_option == "4":

            print("\nThis action will result in the complete deletion of the modded by csgo_gc binaries (inventory.txt, etc. will be saved)!")
            user_option = input("Do you want to continue? [y/n]: ")

            if user_option.lower() != 'y':
                continue

            print("Restoring game files...")

            switcher.restore(LOADED_MAPS, VANILLA_FOLDER)

            print("\nGame files restored!")
            _ = input("Press Enter to return to the main menu...\n")
            continue


        elif user_option == "5":
            break

        print("\nUnknown command.\n")