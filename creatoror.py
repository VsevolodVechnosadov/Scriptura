import os
from pathlib import Path


def create_dir(url: str) -> str:
    tokens = url.split('/')
    dirname = tokens[5]
    parent_dir = Path.cwd()
    path = os.path.join(parent_dir, dirname)
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    return path
