#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 4, 2022
# a program that calculates the area of a rectangle or square


def calc_area(base, height):
    # calculates the area
    area = base * height

    # prints results
    print(f"The area is {area}cm^2.")


def main():
    # getting user input for the base
    base_str = input("Enter the base (cm): ")

    # getting user input for height
    height_str = input("Enter the height (cm): ")

    # exception handling
    try:
        base_int = int(base_str)
        height_int = int(height_str)

    except Exception:
        print("Invalid Input! Please enter positive integer.")

    else:
        if base_int <= 0 or height_int <= 0:
            print("Invalid Input! Please enter positive integer.")

        else:
            # calls function to calculate the area
            calc_area(base_int, height_int)


if __name__ == "__main__":
    main()
