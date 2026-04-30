import unittest
from gen import extract_title

class gen(unittest.TestCase):
    def test_extract_title(self):
        md = "Placeholder\n# The Title\nEndtext\n"
        self.assertEqual(extract_title(md), "The Title")

    def test_extract_title_h2(self):
        md = "Placeholder\n## The Title\nEndtext\n"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_h2_h1(self):
        md = "Placeholder\n## The Title\n# The Title\nEndtext\n"
        self.assertEqual(extract_title(md), "The Title")
