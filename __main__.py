import os
import random
import subprocess

wallpapers_dir = "/usr/share/backgrounds/Dynamic_Wallpapers"
wallpapers = [f for f in os.listdir(wallpapers_dir) if f.endswith(".xml")]
random_wallpaper = random.choice(wallpapers)

subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{wallpapers_dir}/{random_wallpaper}"])
