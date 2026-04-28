from textnode import *
from htmlnode import *
from nodefunctions import *
from gen import clear_dir, copy_dir, src_to_public

def main():
    src_to_public("./static", "./public")

main()