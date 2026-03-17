import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode(
            tag="div", value="Hello World", children=None, props={"class": "my-div"}
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "my-div"})
        self.assertEqual(node.props_to_html(), ' class="my-div"')
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=div, value=Hello World, children=None, props={'class': 'my-div'})",
        )

    def test_htmlnode_empty(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=None, value=None, children=None, props=None)",
        )

    def test_htmlnode_no_props(self):
        node = HTMLNode(tag="span", value="Hello", children=None, props=None)
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=span, value=Hello, children=None, props=None)",
        )


if __name__ == "__main__":
    unittest.main()
