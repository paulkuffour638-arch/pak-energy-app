def calculate_pressure(force, area):

    try:
        force = float(force)
        area = float(area)

        if area == 0:
            return "Area cannot be zero"

        pressure = force / area

        return f"Pressure = {pressure:.2f} Pa"

    except:
        return "Enter valid numbers"



def calculate_hydrostatic(density, depth):

    try:
        density = float(density)
        depth = float(depth)

        gravity = 9.81

        pressure = density * gravity * depth

        return f"Hydrostatic Pressure = {pressure:.2f} Pa"

    except:
        return "Enter valid numbers"



def calculate_porosity(pore_volume, bulk_volume):

    try:
        pore_volume = float(pore_volume)
        bulk_volume = float(bulk_volume)

        if bulk_volume == 0:
            return "Bulk volume cannot be zero"

        porosity = (pore_volume / bulk_volume) * 100

        return f"Porosity = {porosity:.2f}%"

    except:
        return "Enter valid numbers"



def calculate_permeability(flow_rate, pressure_difference):

    try:
        flow_rate = float(flow_rate)
        pressure_difference = float(pressure_difference)

        if pressure_difference == 0:
            return "Pressure difference cannot be zero"

        permeability = flow_rate / pressure_difference

        return f"Permeability = {permeability:.4f}"

    except:
        return "Enter valid numbers"



def calculate_water_cut(water, total):

    try:
        water = float(water)
        total = float(total)

        if total == 0:
            return "Total production cannot be zero"

        water_cut = (water / total) * 100

        return f"Water Cut = {water_cut:.2f}%"

    except:
        return "Enter valid numbers"