import math


def centreOfMass(spheres: set) -> tuple:
    """Computes the position of the centre of mass of a set of spheres.

    The centre of mass C = (C_x, C_y, C_z)' is computed by:
        C_x = \frac{ \sum_{i=1}^{N} x_i \, m_i } { \sum_{i=1}^{N} m_i }
    ditto C_y / C_z.
    And the mass m_i of sphere S_i is given by the formula:
        m_i = \frac{4}{3} \mu_i \pi r_i^3  (i.e., unitMass * volume)

    Args:
        spheres: A set of tuples, where each one represents the info of
            a given sphere of the form (x, y, z, radius, unitMass).

    Returns:
        A tuple (C_x, C_y, C_z) representing the position of the centre
        of mass of a set of spheres.

    Raises:
        ValueError: An error occurred when
            - the set ``spheres`` is empty,
            - the radius of a sphere is less or equal to 0,
            - the unit mass of a sphere is less or equal to 0.

    Example of Usage:
        spheres = {(1, -2, 3, 1, 1), (-4, 1, 0, 1, 2), (1, 0, 0, 2, 1)}
        C = centreOfMass(spheres)
    """

    if len(spheres) == 0:
        raise ValueError("The set spheres is empty")

    mass = c_x = c_y = c_z = 0
    for sphere in spheres:
        if sphere[3] <= 0 or sphere[4] <= 0:  # radius or unitMass <= 0
            raise ValueError("The radius and/or unit mass of a sphere: " +
                             tuple2str(sphere) + " are/is less than 0")

        volume = 4.0 / 3 * math.pi * math.pow(sphere[3], 3)
        mass_i = volume * sphere[4]
        mass += mass_i
        c_x += sphere[0] * mass_i
        c_y += sphere[1] * mass_i
        c_z += sphere[2] * mass_i

    c_x /= mass
    c_y /= mass
    c_z /= mass

    return c_x, c_y, c_z


def tuple2str(tup: tuple) -> str:
    string = ','.join(map(str, tup))
    return '(' + string + ')'


if __name__ == '__main__':
    try:
        spheres = {(1, -2, 3, 1, 1), (-4, 1, 0, 1, 2), (1, 0, 0, 2, 1)}
        C = centreOfMass(spheres)
        print(C)
    except ValueError as verr:
        print(verr)
