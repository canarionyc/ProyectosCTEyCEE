import os

def convert_file_to_utf8(file_path):
    """
    Attempts to read a file with 'latin-1' encoding and overwrites it with 'utf-8'.
    Returns True if conversion was successful, False otherwise.
    """
    try:
        # Read with latin-1
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
        
        # Write back with utf-8
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True
    except UnicodeDecodeError:
        # This can happen if the file is not truly latin-1 or is a binary file.
        print(f"  - Skipping (not latin-1): {os.path.basename(file_path)}")
        return False
    except Exception as e:
        print(f"  - Error converting {os.path.basename(file_path)}: {e}")
        return False

def convert_directory_to_utf8(directory_path):
    """
    Recursively walks through a directory and converts all text files from latin-1 to utf-8.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    print(f"\n--- Starting UTF-8 conversion for directory: {directory_path} ---\n")
    converted_count = 0
    skipped_count = 0

    for root, _, files in os.walk(directory_path):
        for filename in files:
            # You can add more extensions to skip if needed (e.g., .dll, .exe, .png)
            if filename.endswith(('.sqlite', '.db', '.bin', '.jpg', '.png', '.exe', '.dll')):
                print(f"  - Skipping (binary file): {filename}")
                skipped_count += 1
                continue

            file_path = os.path.join(root, filename)
            
            if convert_file_to_utf8(file_path):
                print(f"  - Converted: {filename}")
                converted_count += 1
            else:
                skipped_count += 1
    
    print("\n--- Conversion Summary ---")
    print(f"Successfully converted: {converted_count} files")
    print(f"Skipped: {skipped_count} files")
    print("--------------------------")

if __name__ == '__main__':
    # --- IMPORTANT ---
    # Set the target directory here.
    # For example, to convert all files in the 'EjemploI_2526_Option1_Config1' project:
    target_dir = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1'
    
    convert_directory_to_utf8(target_dir)
