import os
import shutil
from nodefunctions import markdown_to_html_node        

def clear_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

def copy_dir(src, dst):
    src_subdirs = os.listdir(src)
    for subdir in src_subdirs:
        src_subdir_path = os.path.join(src, subdir)
        dst_subdir_path = os.path.join(dst, subdir)
        if os.path.isfile(src_subdir_path):
            shutil.copy(src_subdir_path, dst_subdir_path)
        else:            
            os.mkdir(dst_subdir_path)
            copy_dir(src_subdir_path, dst_subdir_path)

def src_to_public(src, dst):
    if not os.path.exists(src):
        return f'source directory "{src}" does not exist'

    clear_dir(dst)
    copy_dir(src, dst)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line[:2] == "# ":
            return line[2:]
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_node.to_html())
    dest_dir = os.path.dirname(dest_path)
    if not os.path.isdir(dest_dir): 
        os.makedirs(dest_dir)
    dest_html = dest_path.replace(".md", ".html")
    with open(dest_html, "w") as f:
        print(f"writing {dest_html}")
        f.write(html_page)
    
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Searching '{dir_path_content}'.")
    dir_contents = os.listdir(dir_path_content)
    for content in dir_contents:
        content_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        print(f"content: {content_path}")
        print(f"dest_path: {dest_path}")
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, dest_path)
        else:
            generate_page_recursive(content_path, template_path, dest_path)