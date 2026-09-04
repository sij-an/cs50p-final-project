def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }

    return value * units[from_unit] / units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return value

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15

    return value


def convert_mass(value, from_unit, to_unit):
    units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592,
        "ton": 1000000
    }

    return value * units[from_unit] / units[to_unit]


def convert_area(value, from_unit, to_unit):
    units = {
        "mm2": 0.000001,
        "cm2": 0.0001,
        "m2": 1,
        "km2": 1000000,
        "in2": 0.00064516,
        "ft2": 0.092903,
        "yd2": 0.836127,
        "acre": 4046.856
    }

    return value * units[from_unit] / units[to_unit]


def convert_volume(value, from_unit, to_unit):
    units = {
        "ml": 0.001,
        "l": 1,
        "m3": 1000,
        "tsp": 0.00492892,
        "tbsp": 0.0147868,
        "cup": 0.236588,
        "gal": 3.78541
    }

    return value * units[from_unit] / units[to_unit]


def convert_speed(value, from_unit, to_unit):
    units = {
        "mps": 1,
        "kph": 1000 / 3600,
        "mph": 1609.344 / 3600,
        "knot": 1852 / 3600
    }

    return value * units[from_unit] / units[to_unit]


def convert_time(value, from_unit, to_unit):
    units = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800
    }

    return value * units[from_unit] / units[to_unit]


def main():   
    print("BASIC UNIT CONVERTER MADE BY SIJAN FOR CS50 FINAL PROJECT")
    print("1. Length")
    print("2. Temperature")
    print("3. Mass")
    print("4. Area")
    print("5. Volume")
    print("6. Speed")
    print("7. Time")

    choice = input("Choose a category: ")

    if choice == "1":
        print("Units: mm, cm, m, km, in, ft, yd, mi")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_length(value, from_unit, to_unit)

    elif choice == "2":
        print("Units: C, F, K")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_temperature(value, from_unit, to_unit)

    elif choice == "3":
        print("Units: mg, g, kg, oz, lb, ton")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_mass(value, from_unit, to_unit)

    elif choice == "4":
        print("Units: mm2, cm2, m2, km2, in2, ft2, yd2, acre")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_area(value, from_unit, to_unit)

    elif choice == "5":
        print("Units: ml, l, m3, tsp, tbsp, cup, gal")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_volume(value, from_unit, to_unit)

    elif choice == "6":
        print("Units: mps, kph, mph, knot")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_speed(value, from_unit, to_unit)

    elif choice == "7":
        print("Units: second, minute, hour, day, week")
        value = float(input("Enter value: "))
        from_unit = input("From: ")
        to_unit = input("To: ")
        result = convert_time(value, from_unit, to_unit)

    else:
        print("Invalid choice.")
        return

    print("Result:", result, to_unit)


if __name__ == "__main__":
    main()
    