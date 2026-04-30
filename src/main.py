from textnode import *
from htmlnode import *
from nodefunctions import *
from gen import clear_dir, copy_dir, src_to_public, generate_page
import os

def main():
    src_to_public("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_page("./content/blog/glorfindel/index.md", "./template.html", "./public/blog/glorfindel/index.html")
    generate_page("./content/blog/tom/index.md", "./template.html", "./public/blog/tom/index.html")
    generate_page("./content/blog/majesty/index.md", "./template.html", "./public/blog/majesty/index.html")
    generate_page("./content/contact/index.md", "./template.html", "./public/contact/index.html")

main()