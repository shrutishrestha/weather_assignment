def create_mermaid_diagram(data: dict, file_path="output.html") -> str:
    """
    Generate a Mermaid diagram from a dictionary and save it as an HTML file.
    
    Args:
        data (dict): Data to represent in the diagram.
        file_path (str): Path to save the HTML file.

    Returns:
        str: Path of the saved HTML file.
    """


    def generate_mermaid_code(data, parent_name="data"):
        """
        Recursively generates Mermaid syntax lines for visualizing nested data structures.

        Args:
            data (dict or list): The input data to visualize, which can be a nested dictionary or list.
            parent_name (str): The base name for nodes in the diagram, used to create unique identifiers.

        Returns:
            list: A list of strings, each representing a line of Mermaid syntax for a node 
                or connection in the data structure.
        """
        lines = []
        if isinstance(data, dict):
            for key, value in data.items():
                node_name = f"{parent_name}_{key}"
                lines.append(f"{parent_name} --> {node_name}")
                if isinstance(value, (dict, list)):
                    lines.extend(generate_mermaid_code(value, node_name))
                else:
                    value_node = f"{node_name}_value"
                    lines.append(f"{node_name} --> {value_node}[{value}]")
        elif isinstance(data, list):
            for index, item in enumerate(data):
                node_name = f"{parent_name}_{index}"
                lines.append(f"{parent_name} --> {node_name}")
                if isinstance(item, (dict, list)):
                    lines.extend(generate_mermaid_code(item, node_name))
                else:
                    value_node = f"{node_name}_value"
                    lines.append(f"{node_name} --> {value_node}[{item}]")

        lines = [line.replace("data_", "") for line in lines]
        return lines
    
    mermaid_code = ["graph TD"] + generate_mermaid_code(data)
    mermaid_code_str = "\n".join(mermaid_code)
    
    mermaid_template = (
        "<html>\n"
        "<head><script type=\"module\" src=\"https://unpkg.com/mermaid@9.1.1/dist/mermaid.esm.min.mjs\"></script></head>\n"
        "<body>\n"
        "<div class=\"mermaid\">\n"
        f"{mermaid_code_str}\n"
        "</div>\n"
        "</body>\n"
        "</html>\n"
    )

    # Write template to file
    with open(file_path, "w") as file:
        file.write(mermaid_template)
    return file_path

