#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 4, 2022
# a program that calculates the area of a triangle


def calc_area(base, height):
    # calculates the area
    area = (base * height) / 2

    # prints results
    print(f"The area is {area:.3}cm^2.")


def main():
    # getting user input for the base
    base_str = input("Enter the base (cm): ")

    # getting user input for height
    height_str = input("Enter the height (cm): ")

    # exception handling
    try:
        base_fl = float(base_str)
        height_fl = float(height_str)

    except Exception:
        print("Invalid Input! Please enter positive integer.")

    else:
        if base_fl <= 0 or height_fl <= 0:
            print("Invalid Input! Please enter positive integer.")

        else:
            # calls function to calculate the area
            calc_area(base_fl, height_fl)


if __name__ == "__main__":
    main()
