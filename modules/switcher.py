
from urllib.request import urlopen, urlretrieve

from os import remove
from os.path import exists as is_exists, isfile

from shutil import rmtree, copy, unpack_archive

from . import PLATFORM_SYSTEM

def restore(LOADED_MAPS, VANILLA_FOLDER):

    for dir in LOADED_MAPS['mods']:

        if not is_exists(dir):
            continue

        if isfile(dir):
            remove(dir)
            continue

        rmtree(dir)

    for dir in LOADED_MAPS['game']:
        copy(f"{VANILLA_FOLDER}/{dir}", dir)


def download_and_extract(DOWNLOAD_URL, DIST_PATH):

    try:
        urlretrieve(DOWNLOAD_URL, DIST_PATH)
    except:
        return False

    unpack_archive(DIST_PATH)
    remove(DIST_PATH)

    return True