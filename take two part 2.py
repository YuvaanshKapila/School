import math

def cube():
    side_length = 0
    volume_known = input("Do you know the volume or surface area of the cube? ").lower() == 'volume'
    if volume_known:
        volume = float(input("Enter the volume: "))
        side_length = volume ** (1/3)
    else:
        surface_area = float(input("Enter the surface area: "))
        side_length = math.sqrt(surface_area / 6)

    print(f"The side length of the cube is: {side_length}\n")

def sphere():
    radius = 0
    volume_known = input("Do you know the volume or surface area of the sphere? ").lower() == 'volume'
    if volume_known:
        volume = float(input("Enter the volume: "))
        radius = (volume * 3 / (4 * math.pi)) ** (1/3)
    else:
        surface_area = float(input("Enter the surface area: "))
        radius = math.sqrt(surface_area / (4 * math.pi))

    print(f"The radius of the sphere is: {radius}\n")



def cylinder():
    radius = 0
    height = 0

    known_dimension = ""
    surface_area_or_volume = input("Do you know the surface area or volume of the cylinder? ").lower()

    if surface_area_or_volume == 'surface area':
        known_dimension = input("Do you know the radius or height of the cylinder? ").lower()
        if known_dimension == 'radius':
            surface_area = float(input("Enter the surface area: "))
            radius = float(input("Enter the radius: "))
            height = (surface_area / (2 * math.pi * radius)) - radius
        elif known_dimension == 'height':
            surface_area = float(input("Enter the surface area: "))
            height = float(input("Enter the height: "))
            radius = 0.5 * ((height ** 2) + 2 * (surface_area / math.pi)) ** 0.5
        else:
            print("Invalid input. Please specify 'radius' or 'height'.")
    elif surface_area_or_volume == 'volume':
        known_dimension = input("Do you know the radius or height of the cylinder? ").lower()
        if known_dimension == 'radius':
            volume = float(input("Enter the volume: "))
            radius = float(input("Enter the radius: "))
            height = volume / (math.pi * radius ** 2)
        elif known_dimension == 'height':
            volume = float(input("Enter the volume: "))
            height = float(input("Enter the height: "))
            radius = (volume / (math.pi * height)) ** 0.5
        else:
            print("Invalid input. Please specify 'radius' or 'height'.")
    else:
        print("Invalid input. Please specify 'surface area' or 'volume'.")

    print(f"The radius of the cylinder is: {radius}")
    print(f"The height of the cylinder is: {height}\n")

def rectangular_prism():
    length = 0
    width = 0
    height = 0

    volume_known = input("Do you know the volume or surface area of the rectangular prism? ").lower() == 'volume'

    if volume_known:
        known_dims = input("Do you know the length, width, or height of the rectangular prism? (e.g., 'length width'): ").lower().split()
        if len(known_dims) != 2 or set(known_dims) - {'length', 'width', 'height'}:
            print("Invalid dimensions. Please enter two out of 'length', 'width', 'height'.")
            return

        known_values = {}
        for dim in known_dims:
            known_values[dim] = float(input(f"Enter the {dim}: "))

        volume = float(input("Enter the volume: "))

        if 'length' not in known_values:
            length = volume / (known_values['width'] * known_values['height'])
        elif 'width' not in known_values:
            width = volume / (known_values['length'] * known_values['height'])
        elif 'height' not in known_values:
            height = volume / (known_values['length'] * known_values['width'])
    else:
        known_dims = input("Do you know the length, width, or height of the rectangular prism? (e.g., 'length width'): ").lower().split()
        if len(known_dims) != 2 or set(known_dims) - {'length', 'width', 'height'}:
            print("Invalid dimensions. Please enter two out of 'length', 'width', 'height'.")
            return

        known_values = {}
        for dim in known_dims:
            known_values[dim] = float(input(f"Enter the {dim}: "))

        surface_area = float(input("Enter the surface area: "))

        if 'length' not in known_values:
            length = (surface_area - 2 * known_values['width'] * known_values['height']) / (2 * known_values['height'] + 2 * known_values['width'])
        elif 'width' not in known_values:
            width = (surface_area - 2 * known_values['length'] * known_values['height']) / (2 * known_values['height'] + 2 * known_values['length'])
        elif 'height' not in known_values:
            height = (surface_area - 2 * known_values['length'] * known_values['width']) / (2 * known_values['length'] + 2 * known_values['width'])

    print(f"The length of the rectangular prism is: {length}")
    print(f"The width of the rectangular prism is: {width}")
    print(f"The height of the rectangular prism is: {height}\n")

def square_pyramid():
    base_side = 0
    height = 0
    slant_height = 0
    volume = 0
    surface_area = 0

    known_property = input("Do you know the volume or surface area of the square-based pyramid? ").lower()

    if known_property == 'volume':
        volume = float(input("Enter the volume: "))
        height_known = input("Do you know the height? (yes or no): ").lower()

        if height_known == 'yes':
            height = float(input("Enter the height: "))
            base_side = math.sqrt((volume * 3) / height)  # Calculate base side using volume and height
        else:
            base_side = float(input("Enter the base side length: "))
            height = (volume * 3) / (base_side**2)  # Calculate height using volume and base side

    elif known_property == 'surface area':
        surface_area = float(input("Enter the surface area: "))
        slant_height = float(input("Enter the slant height: "))
        base_side = math.sqrt((surface_area - (2 * base_side * slant_height)) / 2)  # Corrected formula to calculate base side using surface area and slant height

    else:
        print("Invalid input. Please specify 'volume' or 'surface area'.")
        return

    # Calculate volume and surface area using the known values
    volume = (base_side**2 * height) / 3
    surface_area = base_side**2 + 2 * base_side * slant_height

    print(f"The volume of the square-based pyramid is: {volume}")
    print(f"The surface area of the square-based pyramid is: {surface_area}")
    print(f"The base side length of the square-based pyramid is: {base_side}")
    print(f"The height of the square-based pyramid is: {height}")
    print(f"The slant height of the square-based pyramid is: {slant_height}")

def triangular_prism():
    a = 0
    b = 0
    c = 0
    h = 0
    L = 0
    volume = 0
    surface_area = 0

    known_property = input("Do you know the volume or surface area of the triangular prism? ").lower()

    if known_property == 'volume':
        volume_known = float(input("What is the volume? "))
        a_known = input("Do you know side a? ").lower() == 'yes'
        b_known = input("Do you know side b? ").lower() == 'yes'
        c_known = input("Do you know side c? ").lower() == 'yes'
        h_known = input("Do you know the height? ").lower() == 'yes'
        l_known = input("Do you know side l? ").lower() == 'yes'

        known_values = {'a': a_known, 'b': b_known, 'c': c_known, 'h': h_known, 'l': l_known}

        if sum(known_values.values()) != 4:
            print("Invalid input. Please specify exactly 4 known values.")
            return

        if not a_known:
            b = float(input("Enter the value for side b: "))
            c = float(input("Enter the value for side c: "))
            h = float(input("Enter the value for height: "))
            l = float(input("Enter the value for side l: "))
            a = (2 * volume_known) / (b * l)

        elif not b_known:
            l = float(input("Enter the value for side l: "))
            h = float(input("Enter the value for height: "))
            b = (2 * volume_known) / (l * h)
        elif not c_known:
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            h = float(input("Enter the value for height: "))
            l = float(input("Enter the value for side l: "))
            c = (2 * volume_known) / (a * l)
        elif not l_known:
            b = float(input("Enter the value for side b: "))
            h = float(input("Enter the value for height: "))
            l = (2 * volume_known) / (b * h)
        elif not h_known:
            b = float(input("Enter the value for side b: "))
            l = float(input("Enter the value for side l: "))
            h = (2 * volume_known) / (b * l)

    elif known_property == 'surface area':
        surface_area_known = float(input("What is the surface area? "))
        a_known = input("Do you know side a? ").lower() == 'yes'
        b_known = input("Do you know side b? ").lower() == 'yes'
        c_known = input("Do you know side c? ").lower() == 'yes'
        h_known = input("Do you know the height? ").lower() == 'yes'
        l_known = input("Do you know side l? ").lower() == 'yes'

        known_values = {'a': a_known, 'b': b_known, 'c': c_known, 'h': h_known, 'l': l_known}

        if sum(known_values.values()) != 4:
            print("Invalid input. Please specify exactly four known values.")
            return

        if not a_known:
            b = float(input("Enter the value for side b: "))
            c = float(input("Enter the value for side c: "))
            h = float(input("Enter the value for height: "))
            l = float(input("Enter the value for side l: "))
            a = (surface_area_known - b * h - c * h) / l
        elif not b_known:
            a = float(input("Enter the value for side a: "))
            c = float(input("Enter the value for side c: "))
            h = float(input("Enter the value for height: "))
            l = float(input("Enter the value for side l: "))
            b = (surface_area_known - a * h - c * h) / l
        elif not c_known:
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            h = float(input("Enter the value for height: "))
            l = float(input("Enter the value for side l: "))
            c = (surface_area_known - a * l - b * h) / h
        elif not h_known:
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            c = float(input("Enter the value for side c: "))
            l = float(input("Enter the value for side l: "))
            h = (surface_area_known - a * l - b * l - c * l) / (a + b + c)
        elif not l_known:
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            c = float(input("Enter the value for side c: "))
            h = float(input("Enter the value for height: "))
            L = math.sqrt(h**2 + (b - c)**2)

    else:
        print("Invalid input. Please specify 'volume' or 'surface area'.")
        return

    print(f"The value of side a is: {a}")
    print(f"The value of side b is: {b}")
    print(f"The value of side c is: {c}")
    print(f"The value of height is: {h}")
    print(f"The value of slant height (L) is: {l}")
def cone():
    radius = 0
    height = 0
    volume = 0
    surface_area = 0

    known_property = input("Do you know the volume or surface area of the cone? ").lower()

    if known_property == 'volume':
        volume_known = float(input("What is the volume? "))
        radius_known = input("Do you know the radius? ").lower() == 'yes'
        height_known = input("Do you know the height? ").lower() == 'yes'

        known_values = {'radius': radius_known, 'height': height_known}

        if sum(known_values.values()) != 1:
            print("Invalid input. Please specify exactly one known value.")
            return

        if not radius_known:
            height = float(input("Enter the value for height: "))
            radius = math.sqrt((3 * volume_known) / (math.pi * height))
        elif not height_known:
            radius = float(input("Enter the value for radius: "))
            height = (3 * volume_known) / (math.pi * radius**2)

        surface_area = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))

        missing_dimension = [dim for dim, known in known_values.items() if not known][0]
        dimensions = {'radius': radius, 'height': height}
        missing_value = dimensions[missing_dimension]
        print(f"The missing dimension of the cone is: {missing_value}")

    elif known_property == 'surface area':
        surface_area_known = float(input("What is the surface area? "))
        radius_known = input("Do you know the radius? ").lower() == 'yes'
        height_known = input("Do you know the height? ").lower() == 'yes'

        known_values = {'radius': radius_known, 'height': height_known}

        if sum(known_values.values()) != 1:
            print("Invalid input. Please specify exactly one known value.")
            return

        if not radius_known:
            height = float(input("Enter the value for height: "))
            radius = (surface_area_known / (math.pi * (1 + math.sqrt(1 + (height**2 / surface_area_known**2)))))**0.5
        elif not height_known:
            radius = float(input("Enter the value for radius: "))
            height = ((surface_area_known / math.pi) - radius) * math.sqrt(radius**2 / ((surface_area_known / math.pi) - radius)**2)

        volume = (1 / 3) * math.pi * radius**2 * height

        missing_dimension = [dim for dim, known in known_values.items() if not known][0]
        dimensions = {'radius': radius, 'height': height}
        missing_value = dimensions[missing_dimension]
        print(f"The missing dimension of the cone is: {missing_value}")

    else:
        print("Invalid input. Please specify 'volume' or 'surface area'.")
        return
def rectangle():
    length = 0
    width = 0

    known_property = input("What is known (area or perimeter) for the rectangle? ").lower()

    if known_property == 'area':
        width = float(input("Enter the width: "))
        area = float(input("Enter the area: "))
        length = area / width
        perimeter = 2 * (length + width)
        print(f"The length of the rectangle is: {length}")
        print(f"The perimeter of the rectangle is: {perimeter}")
    elif known_property == 'perimeter':
        length_known = input("Do you know the length? ").lower() == 'yes'

        if length_known:
            length = float(input("Enter the length: "))
            perimeter = float(input("Enter the perimeter: "))
            width = (perimeter - 2 * length) / 2
        else:
            width = float(input("Enter the width: "))
            perimeter = float(input("Enter the perimeter: "))
            length = (perimeter - 2 * width) / 2

        area = length * width
        print(f"The length of the rectangle is: {length}")
        print(f"The width of the rectangle is: {width}")
        print(f"The area of the rectangle is: {area}")
    else:
        print("Invalid input. Please specify 'area' or 'perimeter'.")

def square():
    side_length = 0

    known_property = input("What is known (area or perimeter) for the square? ").lower()

    if known_property == 'area':
        area = float(input("Enter the area: "))
        side_length = area ** 0.5  # Calculate side length from area
        perimeter = 4 * side_length
        print(f"The side length of the square is: {side_length}")
        print(f"The perimeter of the square is: {perimeter}")
    elif known_property == 'perimeter':
        perimeter = float(input("Enter the perimeter: "))
        side_length = perimeter / 4  # Calculate side length from perimeter
        area = side_length ** 2
        print(f"The side length of the square is: {side_length}")
        print(f"The area of the square is: {area}")
    else:
        print("Invalid input. Please specify 'area' or 'perimeter'.")


def trapezoid():
    known_dimensions = input("Enter the known dimensions (base1, base2, height, area, perimeter) separated by spaces: ").lower().split()

    if len(known_dimensions) != 4 or set(known_dimensions) - {'base1', 'base2', 'height', 'area', 'perimeter'}:
        print("Invalid input. Please enter four out of 'base1', 'base2', 'height', 'area', 'perimeter'.")
        return

    known_values = {}
    for dim in known_dimensions:
        known_values[dim] = float(input(f"Enter the {dim}: "))

    if 'area' in known_values:
        height = (2 * known_values['area']) / (known_values['base1'] + known_values['base2'])
        perimeter = known_values['base1'] + known_values['base2'] + 2 * math.sqrt(known_values['area']**2 - (known_values['base1'] - known_values['base2'])**2) / (known_values['base1'] + known_values['base2'])
        print(f"The missing dimension of the trapezoid is = {height}, perimeter = {perimeter}")

    elif 'perimeter' in known_values:
        base2 = (known_values['perimeter'] - known_values['base1']) / 2
        height = math.sqrt(known_values['area']**2 - (known_values['base1'] - base2)**2) / (known_values['base1'] + base2)
        print(f"The missing dimension of the trapezoid is = {base2}, height = {height}")

    elif 'height' in known_values:
        base2 = (known_values['perimeter'] - known_values['base1']) / 2
        area = 0.5 * (known_values['base1'] + base2) * known_values['height']
        print(f"The missing dimension of the trapezoid is = {base2}, area = {area}")

    elif 'base1' in known_values:
        base2 = (known_values['perimeter'] - known_values['base1']) / 2
        height = math.sqrt(known_values['area']**2 - (known_values['base1'] - base2)**2) / (known_values['base1'] + base2)
        print(f"The missing dimension of the trapezoid is: base2 = {base2}, height = {height}")

    elif 'base2' in known_values:
        base1 = known_values['perimeter'] - 2 * known_values['base2']
        height = (2 * known_values['area']) / (base1 + known_values['base2'])
        print(f"The missing dimension of the trapezoid is: {base1}, height = {height}")

    else:
        print("Invalid input. Please specify 'area', 'perimeter', 'height', 'base1', or 'base2'.")
def circle():
    radius = 0

    known_property = input("What is known (area or circumference) for the circle? ").lower()

    if known_property == 'area':
        radius = float(input("Enter the radius: "))
        area = float(input("Enter the area: "))
        circumference = 2 * math.pi * radius
        print(f"The radius of the circle is: {radius}")
        print(f"The circumference of the circle is: {circumference}")
    elif known_property == 'circumference':
        circumference = float(input("Enter the circumference: "))
        radius = circumference / (2 * math.pi)
        area = math.pi * radius**2
        print(f"The radius of the circle is: {radius}")
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid input. Please specify 'area' or 'circumference'.")

def triangle():
    known_property = input("What is known (area or perimeter) for the triangle? ").lower()

    if known_property == 'area':
        base_known = input("Do you know the base? (yes or no): ").lower() == 'yes'
        height_known = input("Do you know the height? (yes or no): ").lower() == 'yes'

        if base_known and height_known:
            print("All dimensions are known. No calculation needed.")
            return

        area = float(input("Enter the area: "))

        if not base_known:
            height = float(input("Enter the value for height: "))
            base = 2 * area / height
            print(f"The missing dimension of the triangle is: base = {base}")
        elif not height_known:
            base = float(input("Enter the value for base: "))
            height = area / base
            print(f"The missing dimension of the triangle is: height = {height}")

    elif known_property == 'perimeter':
        side_a_known = input("Do you know side a? (yes or no): ").lower() == 'yes'
        side_b_known = input("Do you know side b? (yes or no): ").lower() == 'yes'
        side_c_known = input("Do you know side c? (yes or no): ").lower() == 'yes'

        if side_a_known and side_b_known and side_c_known:
            print("All dimensions are known. No calculation needed.")
            return

        perimeter = float(input("Enter the perimeter: "))

        if not side_a_known:
            side_b = float(input("Enter the value for side b: "))
            side_c = float(input("Enter the value for side c: "))
            side_a = perimeter - side_b - side_c
            print(f"The missing dimension of the triangle is: side a = {side_a}")
        elif not side_b_known:
            side_a = float(input("Enter the value for side a: "))
            side_c = float(input("Enter the value for side c: "))
            side_b = perimeter - side_a - side_c
            print(f"The missing dimension of the triangle is: side b = {side_b}")
        elif not side_c_known:
            side_a = float(input("Enter the value for side a: "))
            side_b = float(input("Enter the value for side b: "))
            side_c = perimeter - side_a - side_b
            print(f"The missing dimension of the triangle is: side c = {side_c}")

    else:
        print("Invalid input. Please specify 'area' or 'perimeter'.")
def parallelogram():
    base = 0
    height = 0
    slant = 0  
    area = 0
    perimeter = 0

    known_property = input("What is known (area or perimeter) for the parallelogram? ").lower()

    if known_property == 'area':
        height_known = input("Do you know the height? (yes or no): ").lower()

        if height_known == 'yes':
            height = float(input("Enter the height: "))
            area = float(input("Enter the area: "))
            base = area / height
            print(f"The missing dimension of the parallelogram is: base length = {base}")
        elif height_known == 'no':
            area = float(input("Enter the area: "))
            base = float(input("Enter the base length: "))
            height = area / base
            print(f"The missing dimension of the parallelogram is: height = {height}")
        else:
            print("Invalid input. Please specify 'yes' or 'no' for knowing the height.")
            return

    elif known_property == 'perimeter':
        slant_known = input("Do you know the slant (s)? (yes or no): ").lower()

        if slant_known == 'yes':
            slant = float(input("Enter the slant (s): "))
            perimeter = float(input("Enter the perimeter: "))
            base = perimeter / 2 - slant
            print(f"The missing dimension of the parallelogram is: base length = {base}")
        elif slant_known == 'no':
            base = float(input("Enter the base length: "))
            perimeter = float(input("Enter the perimeter: "))
            slant = perimeter / 2 - base
            print(f"The missing dimension of the parallelogram is: slant (s) = {slant}")
        else:
            print("Invalid input. Please specify 'yes' or 'no' for knowing the slant.")
            return

    else:
        print("Invalid input. Please specify 'area' or 'perimeter'.")


def run_again():
    return input("Do you want to run again? (yes/no): ").lower() == 'yes'

def main():
    while True:
        dimension_type = input("Do you want to work with 2D or 3D shapes? ").lower()
        if dimension_type == '2d':
            shape = input("Enter the 2D shape (rectangle, square, circle, triangle, trapezoid, parallelogram) or 'exit' to end: ").lower()
            if shape == 'exit':
                break
            elif shape == 'rectangle':
                rectangle()
                square()
            elif shape == 'circle':
                circle()
            elif shape == 'triangle':
                triangle()
            elif shape == 'parallelogram':
                parallelogram()
            elif shape == 'trapezoid':
                trapezoid()
            else:
                print("Invalid shape. Please try again.")

        elif dimension_type == '3d':
            shape = input("Enter the 3D shape (cube, sphere, cylinder, rectangular prism, triangular prism, cone, square pyramid) or 'exit' to end: ").lower()
            if shape == 'exit':
                break
            elif shape == 'cube':
                cube()
            elif shape == 'sphere':
                sphere()
            elif shape == 'cylinder':
                cylinder()
            elif shape == 'rectangular prism':
                rectangular_prism()
            elif shape == 'triangular prism':
                triangular_prism()
            elif shape == 'cone':
                cone()
            elif shape == 'square pyramid':
                square_pyramid()
            else:
                print("Invalid shape. Please try again.")
        else:
            print("Invalid input. Please specify '2d' or '3d'.")

        if not run_again():
            break

if __name__ == "__main__":
    main()


