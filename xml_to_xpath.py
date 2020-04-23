import xml.etree.ElementTree as ET
import argparse


def parse_xml_to_xpath(root_element, path):
    attrs = ""
    for name, val in root_element.items():
        attrs += "[@" + name + "=" + val + "]"

    print("Element: " + str(root_element).split()[1])
    print("Xpath: " + path + attrs)
    print()

    tags_counter = {}
    for child_element in root_element:
        tag = child_element.tag
        if tag in tags_counter:
            tags_counter[tag] += 1
            numbered_tag = tag + "[" + str(tags_counter[tag]) + "]"
        else:
            tags_counter[tag] = 0
            numbered_tag = tag

        parse_xml_to_xpath(child_element, path + '/' + numbered_tag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Module that parses a file prints all the element/Xpath pairs from it.")
    parser.add_argument("source", help='Source of a file to parse.')
    args = parser.parse_args()

    file = open(getattr(args, 'source'))
    tree = ET.parse(file)
    root = tree.getroot()

    parse_xml_to_xpath(root, "//" + root.tag)
