
from . import PLATFORM_SYSTEM
from config import APP_ID
from json import dump as j_dump

def generate():

    if PLATFORM_SYSTEM == 'linux':
        return {
            'game': [
                'bin/linux64/libtogl_client.so',
                'bin/linux64/panorama_client.so',
                'bin/linux64/panorama_gl_client.so',
                'csgo/bin/linux64/client_client.so',
                'csgo/maps/soundcache/_master.cache',
                'csgo/panorama/code.pbin',
                'csgo/steam.inf',
                'csgo/modelsounds.cache',
                'csgo_linux64'
            ],
            'mods': [
                'licenses',
                'README.md',
                'srcds_linux',
                'csgo_gc/release.txt',
                'csgo_gc/linux64',
                'csgo/panorama/localization',
                'csgo/resource/csgo_gc_english.txt',
                'csgo/resource/csgo_gc_russian.txt',
                'csgo/resource/flash/econ'
            ]
        }

    return {
        'game': [
            'bin/panorama.dll',
            'csgo/bin/client.dll',
            'csgo/panorama/code.pbin',
            'csgo.exe'
        ],
        'mods': [
            'licenses',
            'README.md',
            'gc_log.txt',
            'csgo.exe.old',
            'csgo_gc/release.txt',
            'csgo_gc/csgo_gc.dll',
            'csgo_gc/.update_lock',
            'csgo_gc/csgo_gc_27015.env',
            'csgo/cfg/project446_sdr_relay.txt',
            'csgo/panorama/localization',
            'csgo/resource/csgo_gc_english.txt',
            'csgo/resource/csgo_gc_russian.txt',
            'csgo/resource/flash/econ'
        ]
    }

def make_map_file():

    MAPS = generate()

    with open(f".{APP_ID}/map.json", "w") as f:
        j_dump(MAPS, f)

    return MAPS