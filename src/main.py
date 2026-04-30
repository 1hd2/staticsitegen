from textnode import *
from htmlnode import *
from nodefunctions import *
from gen import clear_dir, copy_dir, src_to_public, generate_page_recursive
import os

def main():
    src_to_public("./static", "./public")
    generate_page_recursive("./content", "./template.html", "./public")

main()