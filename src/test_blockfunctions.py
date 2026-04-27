import unittest
from blockfunctions import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_m2b_lines(self):
        md = """
This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_m2b_tabs(self):
        md = """
This is **bolded** paragraph





          This paragraph has two tabs and spaces
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This paragraph has two tabs and spaces",
            ],
        )

    def test_b2bt_header(self):
        h_list = []
        headertext = " TEXT"
        for i in range(1, 7):
            headertext = "#" + headertext
            h_list.append(headertext)

        for text in h_list:
            self.assertEqual(
                block_to_block_type(text),
                BlockType.HEADER
                )

        self.assertEqual(
            block_to_block_type("####### TEXT"),
            BlockType.PARAGRAPH
            )
        
        self.assertEqual(
            block_to_block_type("#######TEXT"),
            BlockType.PARAGRAPH
            )

    def test_b2bt_code(self):
        md = "```\nCode Text```"
        self.assertEqual(
            block_to_block_type(md), BlockType.CODE
        )

        md_multi = """```
        Code Text```"""
        self.assertEqual(
            block_to_block_type(md_multi), BlockType.CODE
        )

    def test_b2bt_quote(self):
        md = """>implying\n>mfw\n>mfw I have no face"""
        self.assertEqual(
            block_to_block_type(md), BlockType.QUOTE
        )

        md2 = """> implying\n> mfw\n> mfw I have no face"""
        self.assertEqual(
            block_to_block_type(md), BlockType.QUOTE
        )

        
        
    def test_b2bt_unordered(self):
        md = "- list\n- list2\n- list3"
        self.assertEqual(
            block_to_block_type(md), BlockType.UNORDERED_LIST
        )

    def test_b2bt_ordered(self):
        md = "1. list\n2. list2\n3. list3"
        self.assertEqual(
            block_to_block_type(md), BlockType.ORDERED_LIST
        )

        md2 = "2. list\n3. list2\n4. list3"
        self.assertEqual(
            block_to_block_type(md2), BlockType.PARAGRAPH
        )

        md3 = "1. list\n1. list2\n1. list3"
        self.assertEqual(
            block_to_block_type(md3), BlockType.PARAGRAPH
        )

    def test_b2bt_mixed_list(self):
        md = "1. list\n2. list2\n- list3"
        self.assertEqual(
            block_to_block_type(md), BlockType.PARAGRAPH
        )