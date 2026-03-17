from textnode import TextType, TextNode


def main():
    text = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.bootdev.com",
    )
    print(text)


main()
