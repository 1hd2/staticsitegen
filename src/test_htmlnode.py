import unittest

from htmlnode import HtmlNode

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
        

if __name__ == "__main__":
    unittest.main()