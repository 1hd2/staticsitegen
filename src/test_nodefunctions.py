import unittest

from nodefunctions import *
from textnode import *

class TestNodeFunctions(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            ])

    def test_italics(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            ])

    def test_code(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
            ])

    def test_multi_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        node2 = TextNode("This is second **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This is second ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            ])

    def test_multi_tag(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        node2 = TextNode("This is _italic_ text", TextType.TEXT)
        node3 = TextNode("This is `code` text", TextType.TEXT)
        bold_nodes = split_nodes_delimiter([node, node2, node3], "**", TextType.BOLD)
        italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
        code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
        self.assertEqual(code_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
            ])

    def test_multi_tag_node(self):
        node = TextNode("This is **bold** text followed by _italic_ text", TextType.TEXT)
        bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
        code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
        self.assertEqual(code_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text followed by ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            ])

    def test_edge_tag(self):
        node = TextNode("`code` This is **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.TEXT),
            ])
        
    def test_edge_tag(self):
        node = TextNode("`code` This is **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.TEXT),
            ])
        
    def test_missing_delimiter(self):
        node = TextNode("This is **bold", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        not_matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertNotEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], not_matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        not_matches = extract_markdown_images(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertNotEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], not_matches)

    def test_extract_markdown(self):
        text = "This is text with a [linkcom](www.example.com) and an ![jpg image](image.jpg), and both [linknet](www.example.net)![png image](image.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertListEqual([("linkcom", "www.example.com"), ("linknet", "www.example.net")], links)
        self.assertListEqual([("jpg image", "image.jpg"), ("png image", "image.png")], images)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [dot net link](example.net) and another [dot com link](example.com)!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("dot net link", TextType.LINK, "example.net"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("dot com link", TextType.LINK, "example.com"),
                TextNode("!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_edge_link(self):
        node = TextNode(
            "[first edge link](example.net) and [last edge link](example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first edge link", TextType.LINK, "example.net"),
                TextNode(" and ", TextType.TEXT),
                TextNode("last edge link", TextType.LINK, "example.com"),
            ],
            new_nodes,
        )

    def test_split_no_image(self):
        node = TextNode(
            "There is no ![image] here",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("There is no ![image] here", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_bold(self):
        node = TextNode(
            "bold text",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("bold text", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_split_multi_node(self):
        node1 = TextNode(
            "[first edge link](example.net) and [second edge link](example.com)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[third edge link](example.org) and [last edge link](example.dev)!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("first edge link", TextType.LINK, "example.net"),
                TextNode(" and ", TextType.TEXT),
                TextNode("second edge link", TextType.LINK, "example.com"),
                TextNode("third edge link", TextType.LINK, "example.org"),
                TextNode(" and ", TextType.TEXT),
                TextNode("last edge link", TextType.LINK, "example.dev"),
                TextNode("!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_ignore_image(self):
        node = TextNode(
            "![ignore this image](image.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("![ignore this image](image.jpg)", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_ignore_plaintext(self):
        node = TextNode("Ignore plaintext", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Ignore plaintext", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_text_to_nodes(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], 
            new_nodes,
        )

    def test_text_to_nodes_adjacent_edges(self):
        node = "**This is all bold** _now all italic_`code block`![image1](image1.jpeg)![image2](image2.jpeg)[link](https://boot.dev)   "
        new_nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("This is all bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("now all italic", TextType.ITALIC),
                TextNode("code block", TextType.CODE),
                TextNode("image1", TextType.IMAGE, "image1.jpeg"),
                TextNode("image2", TextType.IMAGE, "image2.jpeg"),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode("   ", TextType.TEXT)
            ], 
            new_nodes,
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_minimum_string(self):
        node = markdown_to_html_node("")
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_link_image(self):
        node = markdown_to_html_node("Check [this](example.com) and ![pic](image.png)")
        html = node.to_html()
        self.assertEqual(
        html,
        '<div><p>Check <a href="example.com">this</a> and <img src="image.png" alt="pic"></img></p></div>'
        )