from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADER = "header"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(markdown):
    if markdown[0] == '#':
        for c in markdown[:7]:
            if c == ' ':
                return BlockType.HEADER
            if c != '#':
                break
    
    if markdown[:4] == "```\n":
        if markdown[-3:] == "```":
            return BlockType.CODE
    
    markdown_lines = markdown.splitlines()
    
    for l in range(len(markdown_lines)):
        if markdown_lines[l][0] != '>':
            break
        if l == len(markdown_lines) -1 :
            return BlockType.QUOTE

    for l in range(len(markdown_lines)):
        if markdown_lines[l][:2] != "- ":
            break
        if l == len(markdown_lines) - 1:
            return BlockType.UNORDERED_LIST
        
    for l in range(len(markdown_lines)):
        if markdown_lines[l][:3] != f"{l+1}. ":
            break
        if l == len(markdown_lines) - 1:
            return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i]:
            clean_blocks.append(blocks[i])
    return clean_blocks