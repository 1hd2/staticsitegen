from textnode import *
from htmlnode import *
from nodefunctions import *

def main():
    testtextnode = TextNode("Anchor Text", "link", "http://www.boot.dev")
    print("-----TextNode: Anchor Text, link, www.boot.dev")
    print(testtextnode)

    testhtmlnode = HtmlNode("bold", "test txt", None, {"href": "https://www.google.com", "target":"_blank",})
    print("-----HtmlNode: bold, test, None, href=...")
    print(testhtmlnode.props_to_html())
    print(testhtmlnode)

    testleafnode = LeafNode("p", "Hello World")
    print("-----LeafNode: p, Hello World")
    print(testleafnode)
    print(testleafnode.to_html())

    testlinknode = LeafNode("a", "This is a link", {"href": "www.google.com"})
    print("-----LinkNode: a, This is a Link...")
    print(testlinknode.to_html())

    testimgnode = LeafNode("img", "This is an image", {"src": "image-file.jpg", "alt": "alternative text"})
    print("-----ImageNode: img, This is a Link...")
    print(testimgnode.to_html())

    testchildnode = LeafNode("span", "child")
    testparentnode = ParentNode("div", [testchildnode])
    print("-----ChildNode and ParentNode")
    print(testchildnode)
    print(testchildnode.to_html())
    print(testparentnode)
    print(testparentnode.to_html())

    testimagetext = "This is an image: ![alt-text](image.jpg)![alt-text-2](image2.jpg)."
    print("-----image markdown extract")
    print(extract_markdown_images(testimagetext))

    testlinktext = "This is a link: [link text](link.com) This is an image: ![alt-text-2](image2.jpg)."
    print("-----link markdown extract")
    print(extract_markdown_links(testlinktext))

    

main()