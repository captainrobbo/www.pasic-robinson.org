""" sort and rename photos by datetime taken


Images tend to be from iphone with names like IMG_0787.jpeg,
but from two different iphones; or from whatsapp with a UUID.

I want them in chrono order.  This renames every image

    Renamed 27d3e99b-0578-432d-b82f-f23979646c1a.jpeg -> 20251219_114151.jpeg
    Renamed IMG_2304.jpeg -> 20250402_124153.jpeg


Repeated runs should be idempotent

If the folder is in git, tell git to forget them first with

    git rm --cached *.jpeg

"""
import glob
import os
import sys

from PIL import Image


def get_timestamped_name(path):
    ext = os.path.splitext(path)[1]
    exif = Image.open(path).getexif()
    if not exif:
        return None
    if 0x0132 not in exif:
        return "????"

    txt = exif[0x0132]
    txt = txt.replace(":", "")
    txt = txt.replace(" ","_")
    return txt + ext

def run():
    if len(sys.argv) != 2:
        print("Usage:  python photosort.py dirname")
        sys.exit(0)
    dirname = sys.argv[1]

    os.chdir(dirname)

    imagelist = glob.glob("*.jp*")


    print(f"found {len(imagelist)} photos")

    fixed = 0
    for oldname in imagelist:
        newname = get_timestamped_name(oldname)
        if newname != oldname:
            os.rename(oldname, newname)
            print(f"Renamed {oldname} -> {newname}")
            fixed += 1
        else:
            print(f"Ignored {oldname}")
    print(f"Renamed {fixed} files in chrono order")



if __name__=='__main__':
    run()
