from dataclasses import dataclass
import xml.etree.ElementTree as ET
from datetime import datetime

@dataclass
class AnnotationParser:
    """ Class for converting annotation from passed XML to format specified in provided template. """    
    source_xml: str
    date_format: str = "%Y-%m-%dT%H:%M:%S"

    def __post_init__(self):
        self.root = ET.fromstring(self.source_xml)

    def parse(self, template:dict) -> str:
            """ Parse XML file and return different XML in format specified in provided template """
            if len(template.keys()) > 1:
                raise Exception("Template root contains more than one key")
            
            root_key = list(template.keys())[0]

            parsed_xml = ET.Element(root_key)
            self._parse_schema(parsed_xml, template[root_key])            

            return ET.tostring(parsed_xml, encoding="unicode", method="xml", xml_declaration=True)

    def _parse_schema(self, root_element: ET.Element, schema:dict, source:ET.Element = None) -> ET.Element:
        """ Go through schema and parse xml recursively """
        if source is None:
            source = self.root

        # Go through keys and values of current level in the schema
        for key, value in schema.items():  
            if key.startswith("#"):
                continue
            
            # If the element last in the tree (has source)
            source_id = value.get("#source_id")             
            if source_id is not None:
                final_source_el = self._find_element_in_source_by_id(source_id, source)
                if final_source_el is None:
                    continue
                
                e = ET.SubElement(root_element, key)
                if final_source_el.attrib["type"] == "date":
                    e.text = datetime.strptime(final_source_el.text, "%Y-%m-%d").strftime(self.date_format)
                else:
                    e.text = final_source_el.text
                
                continue

            # If there can be multiple elements of the same tag
            list_element = value.get("#list")
            if list_element is not None:
                list_element
                for element in self._find_elements_in_source(list_element, source):
                    self._parse_schema(ET.SubElement(root_element, key), value, element)
                continue
            
            # Otherwise just dive deeper in the tree
            self._parse_schema(ET.SubElement(root_element, key), value, source)            



    @staticmethod
    def _find_element_in_source_by_id(id:str, root_element:ET.Element) -> ET.Element:
        return root_element.find(f".//*[@schema_id='{id}']")

    @staticmethod
    def _find_elements_in_source(id:str, root_element:ET.Element) ->list:
        if id.startswith("@"):
            return root_element.findall(f".//*[@schema_id='{id[1:]}']")
        else:
            return root_element.findall(f".//{id}")
        






