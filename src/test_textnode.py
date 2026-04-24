import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_type(self):
        node = TextNode("Sample text", TextType.ITALIC, "http://boot.dev")
        node2 = TextNode("Sample text", TextType.BOLD, "http://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Sample text", TextType.CODE)
        node2 = TextNode("Sample text", TextType.CODE, None)
        self.assertEqual(node, node2)

    def test_eq_quotes(self):
        node = TextNode('Sample text', TextType.LINK, "http://boot.dev")
        node2 = TextNode("Sample text", TextType.LINK, "http://boot.dev")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link_to_html(self):
        node = TextNode("This is a link", TextType.LINK, "http://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "http://www.google.com"})
        self.assertEqual(html_node.to_html(), '<a href="http://www.google.com">This is a link</a>')

if __name__ == "__main__":
    unittest.main()