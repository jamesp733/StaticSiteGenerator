from __future__ import annotations

class HTMLNode:
    def __init__(self,tag: str = None,value:str = None,children: list[HTMLNode] = None,props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError 
    
    def props_to_html(self) -> str:
        html_attr = ""
        for key,val in self.props.items():
            html_attr += f" {key}=\"{val}\""
        return html_attr
    def __repr__(self) -> str:
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
    
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag = tag, value = value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag = tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("no children")
        children_html_tag = ""
        for child in self.children:
            children_html_tag+= child.to_html()

        return f"<{self.tag}>{children_html_tag}</{self.tag}>"