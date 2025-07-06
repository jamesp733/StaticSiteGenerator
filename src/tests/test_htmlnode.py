import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))





import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_htmlprops(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode("node1","val1",None,props)
        prop_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), prop_output)
    def test_eq2(self):
        node = HTMLNode("node1","val12")
        node2 = HTMLNode("node1","val1")
        self.assertNotEqual(node, node2)
        
    
    def test_None_val_leaf(self):
        node = LeafNode(None,None)
        with self.assertRaises(ValueError):
            node.to_html()
        
    
    def test_no_tag_leaf(self):
        node = LeafNode(None,"val")
        htmlval = node.to_html()
        self.assertEqual(htmlval, node.value)
        
        
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

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
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


        
if __name__ == "__main__":
    unittest.main()

