from textnode import *
from htmlnode import *
from blockfunctions import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text.split(delimiter)
            if not len(node_text) % 2:
                raise Exception(f"{len(node_text)} nodes - Invalid Markdown syntax: no closing delimiter")
            for i in range(len(node_text)):
                if not i % 2:
                    node_text[i] = TextNode(node_text[i], node.text_type)
                else:
                    node_text[i] = TextNode(node_text[i], text_type)
            new_nodes.extend(node_text)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            old_text = node.text
            for image in images:
                image_alt = image[0]
                image_link = image[1]
                split_text = old_text.split(f"![{image_alt}]({image_link})", 1)
                if split_text[0]:
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                old_text = split_text[1]
            if old_text:
                new_nodes.append(TextNode(old_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            old_text = node.text
            for link in links:
                link_text = link[0]
                link_uri = link[1]
                split_text = old_text.split(f"[{link_text}]({link_uri})", 1)
                if split_text[0]:
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_uri))
                old_text = split_text[1]
            if old_text:
                new_nodes.append(TextNode(old_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    clean_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in clean_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            clean = " ".join(block.split("\n"))
            parent = ParentNode('p', text_to_children(clean))
            html_nodes.append(parent)
        elif block_type == BlockType.HEADER:
            header_size = 0
            for c in block[:7]:
                if c == '#':
                    header_size += 1
                else:
                    break
            parent = ParentNode(f"h{header_size}", text_to_children(block[header_size + 1:]))
            html_nodes.append(parent)
        elif block_type == BlockType.QUOTE:
            block_text = block.splitlines()
            clean_lines = []
            for text in block_text:
                clean_lines.append(text[1:].lstrip())
            clean_text = " ".join(clean_lines)
            parent = ParentNode("blockquote", text_to_children(clean_text))
            html_nodes.append(parent)
        elif block_type == BlockType.UNORDERED_LIST:
            block_text = block.splitlines()
            list_lines = []
            for line in block_text:
                clean_text = line.split('- ', 1)[1]
                list_lines.append(ParentNode("li", text_to_children(clean_text)))
            parent = ParentNode("ul", list_lines)
            html_nodes.append(parent)
        elif block_type == BlockType.ORDERED_LIST:
            block_text = block.splitlines()
            list_lines = []
            for line in block_text:
                clean_text = line.split('. ', 1)[1]
                list_lines.append(ParentNode("li", text_to_children(clean_text)))
            parent = ParentNode("ol", list_lines)
            html_nodes.append(parent)
        elif block_type == BlockType.CODE:
            code_text = block[4:-3]
            code_text_node = TextNode(code_text, TextType.CODE)
            code_node = text_node_to_html_node(code_text_node)
            parent = ParentNode("pre", [code_node])
            html_nodes.append(parent)

    return ParentNode("div", html_nodes)