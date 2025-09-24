def calculate_weight(earth_weight, planet_number):
    gravity_factors = {
        1: 0.38,    # Mercury
        2: 0.91,    # Venus
        3: 0.38,    # Mars
        4: 2.34,    # Jupiter
        5: 1.06,    # Saturn
        6: 0.92,    # Uranus
        7: 1.19     # Neptune
    }
    planet = {
        1: 'Mercury',
        2: 'Venus',
        3: 'Mars',
        4: 'Jupiter',
        5: 'Saturn',
        6: 'Uranus',
        7: 'Neptune'
    }
    if planet_number in gravity_factors:
        return earth_weight * gravity_factors[planet_number],planet[planet_number]
    else:
        return None

planet = 5  # For example: Jupiter
weight_on_earth = 150
weight_on_planet, planet_name= calculate_weight(weight_on_earth, planet)

if weight_on_planet is not None:
    print("Your weight on planet number", planet_name, "is", round(weight_on_planet, 2))
else:
    print("Invalid planet number! Choose between 1 and 7.")