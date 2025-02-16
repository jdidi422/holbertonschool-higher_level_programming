#!/usr/bin/env python3
import xml.etree.ElementTree as ET
"""serialization and deserialization from and to xml"""


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an xml file"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an xml file to a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {element.tag: element.text for element in root}
