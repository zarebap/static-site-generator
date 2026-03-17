import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def testImage(self):
        markdown = "![alt text](https://example.com/image.png)"
        images = extract_markdown_images(markdown)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][1], "https://example.com/image.png")

    def testLink(self):
        markdown = "[link text](https://example.com)"
        links = extract_markdown_links(markdown)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][1], "https://example.com")

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    unittest.main()
