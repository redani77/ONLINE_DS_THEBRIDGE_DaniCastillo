import pandas as pd
import numpy as np
import re

def parse_memory(memory_str):
    # Diccionario base
    components = {
        "primary_capacity_gb": np.nan,
        "primary_type": np.nan,
        "has_secondary": 0,
        "secondary_capacity_gb": np.nan,
        "secondary_type": np.nan,
        "total_capacity_gb": np.nan
    }
    
    # Expresión regular para extraer capacidad y tipo
    pattern = r"(\d+\.?\d*)(TB|GB|MB)\s*(\w+\s*\w*)"
    
    # Separar combinaciones (ej: "256GB SSD + 1TB HDD")
    drives = re.split(r"\s*\+\s*", memory_str)
    
    # Procesar cada disco
    capacities = []
    types = []
    
    for drive in drives:
        match = re.search(pattern, drive)
        if match:
            value, unit, drive_type = match.groups()
            value = float(value)
            
            # Convertir todo a GB
            multiplier = 1000 if unit == "TB" else 1 if unit == "GB" else 0.001
            capacity_gb = value * multiplier
            
            capacities.append(capacity_gb)
            types.append(drive_type.strip())
    
    if capacities:
        # Primario
        components["primary_capacity_gb"] = capacities[0]
        components["primary_type"] = types[0]
        
        # Secundario (si existe)
        if len(capacities) > 1:
            components["has_secondary"] = 1
            components["secondary_capacity_gb"] = capacities[1]
            components["secondary_type"] = types[1]
        
        # Capacidad total
        components["total_capacity_gb"] = sum(capacities)
    
    return components
    