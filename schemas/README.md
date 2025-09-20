# Energy Certification Schemas

This directory contains XML schemas for European Certification of Energetic Efficiency of Buildings.

## Available Schemas

Place schema files (XSD) for different energy certification standards here. The parser will automatically 
try to detect and use the appropriate schema based on the XML namespace.

## Schema Naming Convention

It's recommended to name schemas according to their standard or namespace, for example:
- `epbd_schema.xsd` - For European Energy Performance of Buildings Directive schemas
- `cte_schema.xsd` - For Spanish Technical Building Code schemas

## Adding New Schemas

When adding new schemas, make sure to update the `SCHEMA_MAPPINGS` dictionary in the `xml_parser.py` file
to map the XML namespace to the schema file location.

