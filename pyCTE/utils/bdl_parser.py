# Key Things to Know When Parsing
# Encoding: These files often use latin-1 or mbcs encoding (common in older Windows software like CALENER), not UTF-8. If you get decode errors, switch the encoding.
# Line Continuation: In strict BDL, logical lines can be broken across physical lines. The script above assumes properties generally stay on one line or uses basic regex matching. For production use, you might need to concatenate lines before matching.
# Units: The header $UNITS METRIC tells you the data values (conductivity, density, etc.) are in metric units (SI).

import re
import json

def parse_bdl_library(file_content):
    """
    Parses a CALENER/DOE-2 BDL library file content into a list of dictionaries.
    """
    entries = []
    current_entry = {}
    
    # Regex to capture the header line: $LIBRARY-ENTRY "Name" Type Category
    # It handles names with or without quotes
    header_pattern = re.compile(r'^\$LIBRARY-ENTRY\s+(?:"([^"]+)"|([^\s]+))\s+([^\s]+)\s+(.*)$')
    
    # Regex to capture properties: KEY = VALUE or KEY = ( ... )
    # This is a simplified regex; complex nested structures might need a full state machine
    property_pattern = re.compile(r'([A-Z0-9\-]+)\s*=\s*(\([^\)]*\)|[^(\s]+)')

    lines = file_content.splitlines()
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check for new entry start
        header_match = header_pattern.match(line)
        if header_match:
            # If we were building an entry, save it (unless it's the first one)
            if current_entry:
                entries.append(current_entry)
            
            # Start new entry
            name = header_match.group(1) or header_match.group(2)
            obj_type = header_match.group(3)
            category = header_match.group(4)
            
            current_entry = {
                "name": name,
                "type": obj_type,
                "category": category,
                "properties": {}
            }
            continue

        # Skip comments (lines starting with $ but NOT $LIBRARY-ENTRY)
        if line.startswith('$'):
            continue

        # Check for end of entry
        if line.endswith('..'):
            line = line[:-2] # Remove the dots to parse the last property if present

        # Parse properties in the line
        # We merge lines to handle multi-line lists roughly
        # (For a robust parser, you'd accumulate lines until a full statement is closed)
        props = property_pattern.findall(line)
        if current_entry:
            for key, value in props:
                # Clean up value (remove quotes if simple string, handle numbers)
                if value.startswith('(') and value.endswith(')'):
                    # It's a list, try to parse elements
                    inner = value[1:-1].replace(',', ' ').split()
                    clean_list = []
                    for i in inner:
                        if i.replace('"','').strip():
                            clean_list.append(i.replace('"',''))
                    current_entry['properties'][key] = clean_list
                else:
                    # It's a single value
                    try:
                        current_entry['properties'][key] = float(value)
                    except ValueError:
                        current_entry['properties'][key] = value

    # Append the last entry
    if current_entry:
        entries.append(current_entry)
        
    return entries

if __name__ == "__main__":
    # Assuming 'file_content' is the string string you provided
    input_file = r"C:\ProgramasCTEyCEE\CALENER-GT-348\DOE-2\Bdllib.dat"
    with open(input_file, 'r', encoding='latin-1') as f:
        file_content = f.read()

    parsed_data = parse_bdl_library(file_content)
    print(json.dumps(parsed_data[0:2], indent=2)) # Print first 2 entries