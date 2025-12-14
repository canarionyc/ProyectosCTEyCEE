import os

def safe_read_and_print(file_path):
    """
    Reads a file in binary mode and decodes it to UTF-8 with error handling,
    then prints the content to the console.
    """
    print(f"\n--- Safely reading file: {file_path} ---\n")
    try:
        with open(file_path, 'rb') as f:
            raw_content = f.read()
        
        # Decode using UTF-8, replacing any characters that cause errors
        # This helps to see the content even if it's not perfectly clean
        content = raw_content.decode('utf-8', errors='replace')
        
        print("--- File Content (decoded with error replacement) ---")
        print(content)
        print("----------------------------------------------------")

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # The path to the file we want to inspect
    target_file = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/NewBDL_O.res'
    safe_read_and_print(target_file)
