from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")
        else:
            children_html = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
