#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XML Parser for European Certification of Energetic Efficiency of Buildings
"""

import os
import json
import logging
from typing import Dict, Optional, Tuple, Any
from lxml import etree

# %% Setup logging
logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("CTE_Parser")

# %% Constants and Schema mappings
# Common namespaces used in energy certification documents
NAMESPACES = {
	"xsi": "http://www.w3.org/2001/XMLSchema-instance",
	"epbd": "http://data.europa.eu/epbd/",  # Example namespace
	"cte": "http://certificacion.energetica.es/",  # Example namespace
}

# Mapping of namespaces to schema locations
SCHEMA_MAPPINGS = {
	"http://data.europa.eu/epbd/": "schemas/epbd_schema.xsd",
	"http://certificacion.energetica.es/": "schemas/cte_schema.xsd",
	# Add more mappings as needed
}


# %% XML to Dict conversion functions
def _element_to_dict(element: etree._Element) -> Dict[str, Any]:
	"""Convert an XML element to a Python dictionary."""
	result = {}

	# Add element attributes
	for key, value in element.attrib.items():
		result[f"@{key}"] = value

	# Process child elements - using multiple methods for compatibility
	children = []
	# Try different methods to get children, as lxml has changed these APIs over versions
	try:
		# Method 1: Direct iteration (works in some versions)
		children = list(element)
	except TypeError:
		try:
			# Method 2: getchildren() method (deprecated but might work)
			children = element.getchildren()
		except AttributeError:
			# Method 3: XPath method (most compatible)
			children = element.xpath("./*")

	for child in children:
		child_dict = _element_to_dict(child)
		child_tag = child.tag

		# Remove namespace if present
		if '}' in child_tag:
			child_tag = child_tag.split('}', 1)[1]

		if child_tag in result:
			if not isinstance(result[child_tag], list):
				result[child_tag] = [result[child_tag]]
			result[child_tag].append(child_dict)
		else:
			result[child_tag] = child_dict

	# Add text content if element has text and no children
	if element.text and element.text.strip():
		if not result:  # No attributes or children
			return element.text.strip()
		else:
			result["#text"] = element.text.strip()

	return result


def xml_to_dict(root: etree._Element) -> Dict[str, Any]:
	"""Convert an XML document to a Python dictionary."""
	root_tag = root.tag
	if '}' in root_tag:
		root_tag = root_tag.split('}', 1)[1]

	return {root_tag: _element_to_dict(root)}


# %% Schema detection and validation
def detect_schema(xml_root: etree._Element) -> Optional[str]:
	"""Detect the appropriate schema based on XML namespace."""
	# Check for schema location in the XML itself
	xsi_schema_location = xml_root.attrib.get(f"{{{NAMESPACES['xsi']}}}schemaLocation", "")
	if xsi_schema_location:
		parts = xsi_schema_location.split()
		if len(parts) >= 2:
			namespace = parts[0]
			if namespace in SCHEMA_MAPPINGS:
				return SCHEMA_MAPPINGS[namespace]

	# Check namespaces in the root element
	root_ns = None
	if '}' in xml_root.tag:
		root_ns = xml_root.tag.split('}', 1)[0][1:]  # Extract namespace
		if root_ns in SCHEMA_MAPPINGS:
			return SCHEMA_MAPPINGS[root_ns]

	logger.warning(f"Could not detect schema for XML. Root namespace: {root_ns}")
	return None


def validate_xml(xml_tree: etree._ElementTree, schema_path: str) -> Tuple[bool, str]:
	"""Validate XML against a schema."""
	try:
		schema_doc = etree.parse(schema_path)
		schema = etree.XMLSchema(schema_doc)
		is_valid = schema.validate(xml_tree)

		if not is_valid:
			error_log = schema.error_log
			return False, str(error_log)
		return True, "XML document is valid against the schema"
	except Exception as e:
		return False, f"Validation error: {str(e)}"


# %% Main parser function
def parse_energy_certificate_xml(xml_file_path: str, schema_path: str) -> Dict[str, Any]:
	"""
	Parse an XML file for energy certification, validate against schema if available,
	and return as a dictionary.

	Args:
		xml_file_path: Path to the XML file
		schema_path: Path to the schema file for validation

	Returns:
		Dictionary representation of the XML file
	"""
	try:
		# Parse XML
		logger.info(f"Parsing XML file: {xml_file_path}")
		parser = etree.XMLParser(remove_blank_text=True,
		                         dtd_validation=False)
		xml_tree = etree.parse(xml_file_path, parser)
		xml_root = xml_tree.getroot()

		# Detect and validate schema
		logger.info("Detecting and validating schema...")
		if schema_path is None:
			schema_path = detect_schema(xml_root)

		if schema_path and os.path.exists(schema_path):
			is_valid, message = validate_xml(xml_tree, schema_path)
			if is_valid:
				logger.info("XML validation successful")
			else:
				logger.warning(f"XML validation failed: {message}")
		else:
			logger.warning("No schema found or schema file doesn't exist")

		# Convert to dictionary
		# Convert to dictionary
		try:
		    result = xml_to_dict(xml_root)
		except TypeError as e:
		    logger.warning(f"Type error during XML conversion: {str(e)}")
		    # Try alternative conversion approach
		    result = {}
		    for elem in xml_root.xpath("//*"):
		        path = xml_root.getpath(elem)
		        if elem.text and elem.text.strip():
		            result[path] = elem.text.strip()
		        for attr_name, attr_value in elem.attrib.items():
		            result[f"{path}/@{attr_name}"] = attr_value
		    logger.info("Used fallback XML parsing method")
		return result

	except Exception as e:
		logger.error(f"Error parsing XML file: {str(e)}")
		raise


# %% Command line interface
if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Parse European Energy Certification XML files")
	parser.add_argument("xml_file", help="Path to the XML file to parse")
	parser.add_argument("--schema_path", "-s", help="Schema file path for validation (optional)", default=None)
	parser.add_argument("--output", "-o", help="Output JSON file path (default: print to console)")
	parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print JSON output")

	args = parser.parse_args()
	print(args)
	try:
		result_dict = parse_energy_certificate_xml(args.xml_file, schema_path=args.schema_path)
		json_output = json.dumps(result_dict, indent=4 if args.pretty else None, ensure_ascii=False)

		if args.output:
			with open(args.output, 'w', encoding='utf-8') as f:
				f.write(json_output)
			logger.info(f"JSON output written to {args.output}")
		else:
			print(json_output)

	except Exception as e:
		logger.error(f"Error: {str(e)}")
		exit(1)
