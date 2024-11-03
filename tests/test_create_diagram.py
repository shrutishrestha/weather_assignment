import unittest
import os
from diagram.create_diagram import create_mermaid_diagram

class TestCreateDiagram(unittest.TestCase):
    """
    Unit test case for the create_mermaid_diagram function, verifying file creation and content.
    """
    def test_create_mermaid_diagram(self):
        """
        Test create_mermaid_diagram function with sample data and verify file output.

        This test:
        - Defines sample data to pass to the create_mermaid_diagram function.
        - Calls the function, specifying an output file path.
        - Checks if the file was created successfully at the specified location.
        - Reads the file content to ensure it contains the expected "mermaid" keyword.
        - Cleans up by removing the generated file after the test.
        """
        
        # Sample data to be converted into a diagram by create_mermaid_diagram
        data = {"weather": "sunny", "temperature": 23}
        
        # Call the function and specify a test output file path
        file_path = create_mermaid_diagram(data, "test_output.html")
        
        # Assert that the output file was created at the specified location
        self.assertTrue(os.path.exists(file_path))
        
        # Open the generated file to verify its content
        with open(file_path, "r") as file:
            content = file.read()
            
            # Check if "mermaid" is present in the file content, indicating correct diagram generation
            self.assertIn("mermaid", content)

        # Remove the generated file after test completion to keep the test environment clean
        os.remove(file_path)

# Run the test suite
if __name__ == '__main__':
    unittest.main()