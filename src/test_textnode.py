import unittest

from textnode import TextNode, TextType

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



if __name__ == "__main__":
    unittest.main()