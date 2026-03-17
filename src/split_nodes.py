from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        text = old_node.text
        images = extract_markdown_images(text)
        if images:
            for image in images:
                new_node = old_node.copy()
                new_node.text = image
                new_nodes.append(new_node)
        else:
            new_nodes.append(old_node)


def split_nodes_link(old_node):
    return
