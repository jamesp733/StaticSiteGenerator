
import os as os
import shutil as shutil
from src import markdown_blocks


def extract_title(markdown: str):
    return markdown.split("# ")[1].split("\n")[0]  #title is after first # so will be second entry in first list, and will be the first line in second list

def generate_page(from_path: str, template_path: str, dest_path: str, basepath:str):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f: #read in markdown
        mkdown_str = f.read()
    with open(template_path, "r") as f: #read in template
        template_str = f.read()
    mkdown_html = markdown_blocks.markdown_to_html_node(mkdown_str).to_html() #convert mkdown in file to html
    
    
    title = extract_title(mkdown_str)
    template_str = template_str.replace("{{ Title }}",title,1) #add title
    template_str = template_str.replace("{{ Content }}",mkdown_html,1) #add content
    template_str = template_str.replace('href="/',f'href="{basepath}') #correct basepath
    template_str = template_str.replace('src="/',f'src="{basepath}') #correct basepath
    with open(dest_path,"w") as f: #write html to destination
        os.makedirs(os.path.dirname(dest_path),exist_ok=True)
        f.write(template_str)
    return

def generate_pages_recursive(dir_path_content,template_path, dest_dir_path,basepath):
    with os.scandir(dir_path_content) as entries: #get items in the source directory
        for entry in entries:
            target_path = os.path.join(dest_dir_path, entry.name)  #this is the path where we're writing to
            if entry.path.endswith(".md"):
                target_path = target_path[:-2] +"html" #replace md with html file extension
                generate_page(entry.path, template_path, target_path,basepath)
            if entry.is_dir():
                os.makedirs(target_path,exist_ok=True) #makedir if needed
                generate_pages_recursive(entry.path, template_path, target_path,basepath)


