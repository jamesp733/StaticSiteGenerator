from enum import Enum

class TextType(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self , text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self,node2):
        return self.text == node2.text \
        and self.text_type == node2.text_type \
        and self.url == node2.url
        
    def __repr__(self) -> str: 
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    


