from textnode import *
from htmlnode import *

def main():
    testtextnode = TextNode("Anchor Text", "link", "http://www.boot.dev")
    print(testtextnode)

    testhtmlnode = HtmlNode("bold", "test txt", None, {"href": "https://www.google.com", "target":"_blank",})
    print(testhtmlnode.props_to_html())
    print(testhtmlnode)

main()