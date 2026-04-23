from textnode import *
from htmlnode import *

def main():
    testtextnode = TextNode("Anchor Text", "link", "http://www.boot.dev")
    print(testtextnode)

    testhtmlnode = HtmlNode("bold", "test txt", None, {"href": "https://www.google.com", "target":"_blank",})
    print(testhtmlnode.props_to_html())
    print(testhtmlnode)

    testleafnode = LeafNode("p", "Hello World")
    print(testleafnode)
    print(testleafnode.to_html())

    testlinknode = LeafNode("a", "This is a link", {"href": "www.google.com"})
    print(testlinknode.to_html())

    testimgnode = LeafNode("img", "This is an image", {"src": "image-file.jpg", "alt": "alternative text"})
    print(testimgnode.to_html())

main()