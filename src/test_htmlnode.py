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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("b", "child2")
        child_node3 = LeafNode(None, "child3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><b>child2</b>child3</div>")

    def test_to_html_with_multiple_grandchildren(self):
        son_node = LeafNode("b", "son")
        daughter_node = LeafNode("i", "daughter")
        niece_node = LeafNode("i", "niece")
        nephew_node = LeafNode("b", "nephew")
        self_node = ParentNode("div", [son_node, daughter_node])
        cousin_node = ParentNode("div", [nephew_node, niece_node])
        parent_node = ParentNode("span", [self_node, cousin_node])
        self.assertEqual(
            parent_node.to_html(),
            "<span><div><b>son</b><i>daughter</i></div><div><b>nephew</b><i>niece</i></div></span>",
        )


if __name__ == "__main__":
    unittest.main()