import sys
import os

from Cheetah.Template import Template
from Cheetah.Compiler import DEFAULT_COMPILER_SETTINGS

from namespaceGenerator import get_namespace

from os.path import join as pj
from os.path import normpath as np

import typing
import argparse

def parse_cl(argc: int, argv: list[str]):
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", type=str, required=True)
    ap.add_argument("--article", type=str)
    ap.add_argument("--out", type=str)
    return ap.parse_args(argv[1:])

def main(argc: int, argv: list[str]) -> int:
    parsedArgs = parse_cl(argc, argv)

    projRoot = pj(os.path.curdir, np("../")) # expected to be ran from /build
    nameSpace = get_namespace(projRoot, parsedArgs)

    with open(parsedArgs.template, 'r', encoding="utf-8") as templateFile:
        templateText = templateFile.read()

    DEFAULT_COMPILER_SETTINGS["encoding"] = "utf-8"
    template = Template(templateText, searchList=[nameSpace])

    with open(parsedArgs.out, 'w', encoding="utf-8") as outFile:
        outFile.write(str(template))

    return 0

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

