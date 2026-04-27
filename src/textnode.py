from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text: 
            if self.text_type == other.text_type: 
                if self.url == other.url:
                    return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(Node):
    if Node.text_type == TextType.TEXT:
        return LeafNode(None, Node.text)
    if Node.text_type == TextType.BOLD:
        return LeafNode("b", Node.text)
    if Node.text_type == TextType.ITALIC:
        return LeafNode("i", Node.text)
    if Node.text_type == TextType.CODE:
        return LeafNode("code", Node.text)
    if Node.text_type == TextType.LINK:
        return LeafNode("a", Node.text, {"href": Node.url})
    if Node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": Node.url, "alt": Node.text})