"""
Solar Doomsday
Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum
antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.
Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have
one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar
Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12
square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would
leave 3 square yards, so you can turn those into three 1x1 square solar panels.
Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar
panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make
out of those panels, starting with the largest squares first. So, following the example above, solution(12) would
return [9, 1, 1, 1].
"""


import math


def solution_forloop(area: int) -> list:
    result = []
    while area > 0:
        biggest_panel = int(math.sqrt(area)) ** 2
        result.append(biggest_panel)
        area -= biggest_panel
    return result


def solution_recursive(area: int, current_result: list = None) -> list:
    current_result = current_result or []

    if not area:
        return current_result

    biggest_panel = int(math.sqrt(area)) ** 2
    current_result.append(biggest_panel)

    return solution_recursive(area - biggest_panel, current_result)


def main():
    for x in (12, 127, 332, 982, 4372, 11467):
        print(f"Panels for {x} (forloop):", solution_forloop(x))
        print(f"Panels for {x} (recursive):", solution_recursive(x))
        print("")


if __name__ == "__main__":
    main()
