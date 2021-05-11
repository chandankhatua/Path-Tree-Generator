import os
from pathlib import Path
import sys

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


def getFiles(fileName):
    basePath = Path(fileName)
    files = [en for en in basePath.iterdir()]
    return files


def _gen_tree(files, prefix=""):
    l = len(files)
    for i, e in enumerate(files):
        connector = ELBOW if i == l - 1 else TEE
        if (e.is_dir()):
            print(f"{prefix}{connector} {e.name}{os.sep}")
            if (i != l - 1):
                pre = prefix + PIPE_PREFIX
            else:
                pre = prefix + SPACE_PREFIX

            dirname = getFiles(e)
            _gen_tree(dirname, pre)
            if(i != l - 1):
                print(f"{PIPE}")

        else:
            print(f"{prefix}{connector} {e.name}")


def main():

    if len(sys.argv) == 2:
        input_path = sys.argv[1]
        root_dir = Path(input_path)
        files = getFiles(root_dir)
        print(f"{root_dir}{os.sep}")
        print(PIPE)
        _gen_tree(files)
    else:
        print("Invalid argument")
        sys.exit(1)


if __name__ == "__main__":
    main()
