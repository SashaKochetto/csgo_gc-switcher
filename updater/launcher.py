
APP_ID = "csgoswitcher"

from os import remove
from os.path import exists as is_exists
from platform import system as get_platform_system
from shutil import unpack_archive
from subprocess import call as subprocess_call

PLATFORM_SYSTEM = get_platform_system()

extension = ".exe"
if PLATFORM_SYSTEM == "Linux":
    extension = ""

update_file = f".{APP_ID}/update.zip"

if is_exists(update_file):
    unpack_archive(update_file)
    remove(update_file)

subprocess_call(f".{APP_ID}/csgo_gc-switcher{extension}")