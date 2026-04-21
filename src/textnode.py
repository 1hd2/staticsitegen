from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
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

    def __eq__(other):
        if self.text == other.text: 
            if self.text_type == other.text_type: 
                if self.url == other.url:
                    return True
        
    def __repr__(node):
        return f"TextNode({node.text}, {node.text_type}, {node.url})"