from textnode import *
from htmlnode import *
from nodefunctions import *
from gen import clear_dir, copy_dir, src_to_public, generate_page_recursive
import os
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    print(basepath)
    src_to_public("./static", "./docs")
    generate_page_recursive("./content", "./template.html", "./docs", basepath)

main()