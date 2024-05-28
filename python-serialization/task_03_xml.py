
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input XML file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
