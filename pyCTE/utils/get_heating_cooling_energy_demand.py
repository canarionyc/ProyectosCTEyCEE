import sqlite3

def get_total_annual_energy_demand(db_path, project_name):
    """
    Connects to a SQLite database to calculate the total annual heating and cooling energy demand for a given project.

    The demand is calculated as the sum of the absolute value of annual heating demand 
    and the annual cooling demand, in kWh/m2.

    Args:
        db_path (str): The full path to the SQLite database file.
        project_name (str): The name of the project to look up.

    Returns:
        float: The total annual energy demand in kWh/m2, or None if not found.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
            SELECT abs(annual_heating_kwh_m2) + annual_cooling_kwh_m2
            FROM results_building_summary
            WHERE project_name = ?
        """
        
        cursor.execute(query, (project_name,))
        result = cursor.fetchone()
        
        conn.close()

        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    # Note: You might need to update this path to the correct database file.
    db_file = r"C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\EjemploI_2526_Option1_Config1\NewBDL_O.sqlite"
    project = 'EjemploI_2526_Option1_Config1'
    
    total_demand_per_m2 = get_total_annual_energy_demand(db_file, project)

    if total_demand_per_m2 is not None:
        print(f"Total annual energy demand for project '{project}': {total_demand_per_m2:.2f} kWh/m2")
        # If you have the building's reference area, you can calculate the total demand in kWh.
        # For example, if the area is 64 m2:
        area_m2 = 64
        total_demand_kwh = total_demand_per_m2 * area_m2
        print(f"Total annual energy demand for a {area_m2} m2 building: {total_demand_kwh:.2f} kWh")
    else:
        print(f"Could not retrieve energy demand for project '{project}'.")
