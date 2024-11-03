def create_mermaid_diagram(data: dict, file_path="output.html") -> str:
    """
    Generate a Mermaid diagram from a dictionary and save it as an HTML file.
    
    Args:
        data (dict): Data to represent in the diagram.
        file_path (str): Path to save the HTML file.

    Returns:
        str: Path of the saved HTML file.
    """
    mermaid_template = (
        "<html>\n"
        "<head><script type=\"module\" src=\"https://unpkg.com/mermaid@9.1.1/dist/mermaid.esm.min.mjs\"></script></head>\n"
        "<body>\n"
        "<div class=\"mermaid\">\n"
        "{mermaid_code}\n"
        "</div>\n"
        "</body>\n"
        "</html>\n"
    )

    # Write template to file
    with open(file_path, "w") as file:
        file.write(mermaid_template)
    return file_path

