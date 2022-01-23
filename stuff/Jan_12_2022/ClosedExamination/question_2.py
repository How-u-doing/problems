import math


def collide(objectA: set, objectB: set) -> bool:
    """Detects if two objects collide.

    Args:
        objectA: A set of tuples of the form (x, y, z, radius) that represents the
            3D coordinates and radius of a sphere.
        objectB: ditto

    Returns:
        True if objectA collides with objectB, False otherwise.

    Raises:
        ValueError: An error occurred when the format of a tuple is invalid.

    Example:
        objA = {(0,0,0,1), {0,1,0,1}}
        objB = {(1,1,1,1)}
        intersect = collide(objA, objB)
    """

    if len(objectA) == 0 or len(objectB) == 0:
        return False
    if objectA == objectB:  # collide with itself
        return True

    for sphere_a in objectA:
        for sphere_b in objectB:
            if collide_sphere(sphere_a, sphere_b):
                return True
    return False


def collide_sphere(sphereA: tuple, sphereB: tuple) -> bool:
    if len(sphereA) != 4 or len(sphereB) != 4:
        raise ValueError("Either/both object(s) has/have a wrong size (not 4)")
    if all(isinstance(x, (float, int)) for x in sphereA) is False or \
            all(isinstance(x, (float, int)) for x in sphereB) is False:
        raise ValueError("Found non-float type element(s) in tuple(s)")
    if sphereA[3] <= 0 or sphereB[3] <= 0:
        raise ValueError("non-positive radius")

    dist2: float = (sphereA[0] - sphereB[0]) * (sphereA[0] - sphereB[0]) + \
                   (sphereA[1] - sphereB[1]) * (sphereA[1] - sphereB[1]) + \
                   (sphereA[2] - sphereB[2]) * (sphereA[2] - sphereB[2])

    # (r1+r2)^2 may overflow, so we comp against their dist instead of dist square
    # sqrt may be expensive though :)
    if (sphereA[3] + sphereB[3]) > math.sqrt(dist2):
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        objA = {(0, 0, 0, -1), (0, 1, 0, 1)}
        objB = {(1, 1, 1, 1)}
        intersect = collide(objA, objB)
        print("object A{(0, 0, 0, 1), (0, 1, 0, 1)} collides with " +
              "object B{(1, 1, 1, 1)}: " + str(intersect))
    except ValueError as verr:
        print(verr)
