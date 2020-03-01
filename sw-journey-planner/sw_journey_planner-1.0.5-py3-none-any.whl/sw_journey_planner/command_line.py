#!/usr/bin/env python3

"""
Program entry point
"""

import sys
import sw_journey_planner.swapi as loader

# Constant for unknown number of  stops
_unknown_string = "Unknown"


def main():

    distance = sys.argv[1]

    # Validate the input
    if not distance.isdigit():
        raise ValueError("Distance should be an integer number")

    # ensure distance is an integer
    distance = int(distance)

    # Loop through the starships and plan their journeys
    for starship in loader.load_starships():
        # Ask the starship to plan the journey
        stops = starship.plan_journey(distance)

        # Print the name of starship and the number of stops required to make the Journey.
        # Print Unknow if the number of stops could not be determined
        print(f"{starship.name}: {_unknown_string if stops is None else stops}")


if __name__ == "__main__":
    main()
