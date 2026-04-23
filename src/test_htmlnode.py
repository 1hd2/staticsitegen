import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode()
        node2 = HtmlNode()
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props(self):
        node = HtmlNode("bold", "test txt", None, {"href": "https://www.google.com", "target":"_blank",})
        p2html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), p2html)

    def test_repr(self):
        node = str(HtmlNode("bold", None, None, None))
        repr = 'HtmlNode(tag=bold, value=None, children=None, props=None)'
        self.assertEqual(node, repr)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_link_to_html(self):
        node = LeafNode("img", "image", {"src": "image.jpg"})
        self.assertEqual(node.to_html(), '<img src="image.jpg">image</img>')

    def test_htmlnode_no_tag(self):
        node = LeafNode(None, "No tag")
        self.assertEqual(node.to_html(), 'No tag')

    def test_htmlnode_no_value(self):
        node = LeafNode("b", "")
        self.assertEqual(node.to_html(), '<b></b>')

if __name__ == "__main__":
    unittest.main()