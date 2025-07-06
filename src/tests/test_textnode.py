import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))





import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_str(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_str = f"TextNode({node.text}, {node.text_type.value}, {node.url})"
        self.assertEqual(str(node),expected_str)
        
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nod", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"testurl")
        self.assertNotEqual(node, node2)
        
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        
if __name__ == "__main__":
    unittest.main()

