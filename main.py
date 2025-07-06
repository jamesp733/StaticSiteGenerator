
import os as os
import sys
import shutil as shutil
from copy_directory import copy_directory_to_location
from generate_pages import generate_pages_recursive

BASEPATH = "/StaticSiteGenerator/"
CONTENT_DIR_PATH = "content" 
TEMPLATE_PATH = "template.html"
TARGET_DIR_PATH = "docs"

def main():
    basepath =BASEPATH
    if len(sys.argv)>1:
        basepath = sys.argv[1]
        
    copy_directory_to_location("static","docs")  #move static info to docs and delete docs if it exists
    generate_pages_recursive(CONTENT_DIR_PATH ,TEMPLATE_PATH, TARGET_DIR_PATH, basepath) #generate pages into target dir


if __name__ == "__main__":
    main()