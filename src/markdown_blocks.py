from enum import Enum
from .htmlnode import HTMLNode, LeafNode, ParentNode
from .inline_markdown import text_to_textnodes, TextNode, TextType
from .textnode_to_htmlnode import text_node_to_html_node, text_to_htmlnodes
class BlockType(Enum):
    paragraph = "p"
    heading = "h"
    code = "pre<code>"
    quote = "blockquote"
    unordered_list = "ul"
    ordered_list = "o1"



def text_to_htmlnodes(text: str)-> list[HTMLNode]:
    textnodes = text_to_textnodes(text)
    html_nodes = []
    for textnode in textnodes:
        html_nodes.append(text_node_to_html_node(textnode))
    return html_nodes

def markdown_to_html_node(markdown) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    main_blocks = []
    
    for block in blocks:
        if block == "": continue #base case if recursion
        block_type = block_to_block_type(block)
        
        
        
        block_val = block  #default case for a paragraph where theres nothing else
        node = HTMLNode()
        block_tag =""
        

        match block_type:
            case BlockType.paragraph:
                block_tag = "p" 
                p_lines = block_val.split("\n")
                p_line = " ".join(p_lines)
                html_nodes = text_to_htmlnodes(p_line)
                node = ParentNode(block_tag,children=html_nodes)
                
            case BlockType.heading:
                split_input = block.split()
                if split_input[0].count("#") >6:
                    raise ValueError
                h_count = split_input[0].count("#") #should floor this to 6, but number of h's
                block_tag = f"h{h_count}" #Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
                block_val = " ".join(split_input[1::]) # [0] is just the ###'s.
                
                html_nodes = text_to_htmlnodes(block_val)
                node = ParentNode(block_tag,children=html_nodes)
                
            case BlockType.code:
                block_tag = "pre"
                block_val = block_val[3:-3] #starts and ends with '''
                if block_val.startswith("\n"):
                    block_val = block_val[1::]
                if not block_val.endswith("\n"):
                    block_val += "\n"
                node = ParentNode(block_tag ,children = [LeafNode("code",block_val)])
                
            case BlockType.quote:
                block_tag = "blockquote" 
                
                
                quote_lines = block_val.split("\n")
                quoted_line =""
                for line in quote_lines:
                    quoted_line+=line[1:].strip() +"\n"
                    
                html_nodes = text_to_htmlnodes(quoted_line)
                
                node = ParentNode(block_tag,children=html_nodes)
                
                
            case BlockType.unordered_list:
                split_input = block.split("- ")
                block_tag = "ul" 
                children = []
                for line in split_input:
                    line = line.strip()
                    if line =="": continue
                    html_nodes = text_to_htmlnodes(line)
                    children.append(ParentNode("li",children = html_nodes))
                node = ParentNode(block_tag,children=children)
                
                
            case BlockType.ordered_list:
                split_input = block.split("\n")
                block_tag = "ol" 
                children = []
                for line in split_input:
                    line = line[2:].lstrip() #remove the starting number e.g. 1. or 2. 
                    if line == "": continue
                    html_nodes = text_to_htmlnodes(line)
                    children.append(ParentNode("li",children = html_nodes))
                node = ParentNode(block_tag,children=children)
        
        main_blocks.append(node)
    return ParentNode("div",children = main_blocks)
        
        
def markdown_to_blocks(markdown: str) -> list[str]:
    markdown_blocks =markdown.split("\n\n")
    stripped_blocks = []
    for block in markdown_blocks:
        stripped_block = block.strip()
        if len(stripped_block) !=0:  
            stripped_blocks.append(stripped_block)
    return stripped_blocks

def block_to_block_type(block: str) -> BlockType:
    split_block = block.split("\n")
    
    if block.partition(" ")[0].count("#") ==  len(block.partition(" ")[0]) and len(block.partition(" ")[0]) <7:
        return BlockType.heading
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    if len([line for line in split_block if line.startswith(">")]) == len(split_block):
        return BlockType.quote
    if all(block.startswith("- ") for block in split_block):
        return BlockType.unordered_list
    if all(block.startswith(f"{i+1}. ") for i,block in enumerate(split_block)):
        return BlockType.ordered_list
    return BlockType.paragraph


print(HTMLNode("str"))