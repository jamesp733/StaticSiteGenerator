from .textnode import TextType, TextNode
from .htmlnode import HTMLNode, LeafNode, ParentNode
from .inline_markdown import text_to_textnodes

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = None, value= text_node.text)
        case TextType.BOLD:
            return LeafNode(tag = "b", value= text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag = "i", value= text_node.text)
        case TextType.CODE:
            return LeafNode(tag = "code", value= text_node.text)
        case TextType.LINK:
            return LeafNode(tag = "a", value= text_node.text, props = {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = "img", value= "", props = {"src":text_node.url, "alt":text_node.text})

def text_to_htmlnodes(text: str)-> list[HTMLNode]:
    textnodes = text_to_textnodes(text)
    html_nodes = []
    for textnode in textnodes:
        html_nodes.append(text_node_to_html_node(textnode))
    return html_nodes