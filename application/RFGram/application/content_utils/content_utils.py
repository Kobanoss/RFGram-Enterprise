import os
import secrets
from PIL import Image
from pathlib import Path
from application.content_utils.imports import *

OUT_SIZE = {'pfp': (125, 125), 'media': (200, 200)}
ROOT = CONTENT_CONF.ROOT
CONTENT_PATH = CONTENT_CONF.CONTENT_PATH


def save_picture(picture, pic_type):
    if picture is None:
        return

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    pic_fname = random_hex + f_ext
    pic_path = Path(CONTENT_PATH, 'profile_pics/', pic_fname)

    i = Image.open(picture)
    i.thumbnail(OUT_SIZE[pic_type])
    i.save(pic_path)

    print(pic_path)

    return pic_fname


def save_media(picture):
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(picture.filename)
    pic_fname = random_hex + f_ext
    pic_path = Path(CONTENT_PATH, 'media/', pic_fname)

    i = Image.open(picture)

    bwidth = 600
    ratio = bwidth / float(i.size[0])
    height = int((float(i.size[1]) * ratio))
    i = i.resize((bwidth, height), Image.ANTIALIAS)
    i.save(pic_path)

    j = Image.open(picture)

    bwidth = 125
    ratio = bwidth / float(j.size[0])
    height = int((float(j.size[1]) * ratio))
    j = j.resize((bwidth, height), Image.ANTIALIAS)
    thumb_path = Path(CONTENT_PATH, 'media/', 'thumb' + pic_fname)
    j.save(thumb_path)

    k = Image.open(picture)

    bwidth = 500
    ratio = bwidth / float(j.size[0])
    height = int((float(j.size[1]) * ratio))
    k = k.resize((bwidth, height), Image.ANTIALIAS)
    mid_path = Path(CONTENT_PATH, 'media/', 'mid' + pic_fname)
    print(mid_path)
    k.save(mid_path)

    return pic_fname


def get_file_url(f_path):
    url = 'static/' + f_path
    print(url)
    return url


def delete_file(f_path):
    os.remove(Path(CONTENT_PATH, f_path))
