from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.extend(node)
        else:
            splitted_text = node.text.split(delimiter)
            for i, text in enumerate(splitted_text):
                print(f"i: {i}, text: {text}")
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.TEXT.value))
                else:
                    new_nodes.append(TextNode(text, text_type))

    if len(new_nodes) % 2 == 0:
        raise ValueError("Invalid Markdown syntax: no closing delimiter found")
