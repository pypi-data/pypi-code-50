from vector import Vector


if __name__ == "__main__":
    v_1 = Vector(1, 2, 3)
    v_2 = Vector(4, 5, 6)

    print(f"v_1 is {v_1}")
    print(f"v_2 is {v_2}")

    print(f"the norm of {v_1} is {v_1.norm}")
    print(f"the norm of {v_2} is {v_2.norm}")

    print(f"the sum of v_1 and v_2 is {v_1 + v_2}")
    print(f"the dot product of v_1 and v_2 is {v_1 * v_2}")
    print(f"2 * v_1 is {2 * v_1}")

