#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

# Constants for Soylent and HLTH Code
SOYLENT_CALORIES_PER_PORTION = 1200 / 9
SOYLENT_DRY_GRAMS_PER_PORTION = 270 / 9
SOYLENT_WATER_FL_OZ_PER_PORTION = 36 / 9

HLTH_CODE_CALORIES_PER_PORTION = 800 / 9
HLTH_CODE_DRY_GRAMS_PER_PORTION = 156 / 9
HLTH_CODE_WATER_FL_OZ_PER_PORTION = 16 / 9

# Conversion factor from fluid ounces to grams (approximate)
FL_OZ_TO_GRAMS = 28.3495231


def main():
    parser = argparse.ArgumentParser(
        description="Calculate portions of Soylent and HLTH Code."
    )
    parser.add_argument(
        "total_calories", type=int, help="Total number of calories."
    )
    parser.add_argument(
        "final_portions", type=int, help="Final number of portions."
    )
    args = parser.parse_args()

    # Calculate number of Soylent and HLTH Code portions needed
    soylent_portions = min(
        args.total_calories // SOYLENT_CALORIES_PER_PORTION, args.final_portions
    )
    hlth_calories = args.total_calories - (
        soylent_portions * SOYLENT_CALORIES_PER_PORTION
    )
    hlth_code_portions = hlth_calories / HLTH_CODE_CALORIES_PER_PORTION

    # Calculate total mass of each ingredient
    # We round the numbers because our ability to measure out the final
    # portions is limited.
    total_soylent_dry = round(soylent_portions * SOYLENT_DRY_GRAMS_PER_PORTION)
    total_hlth_code_dry = round(
        hlth_code_portions * HLTH_CODE_DRY_GRAMS_PER_PORTION
    )
    soylent_water_fl_oz = soylent_portions * SOYLENT_WATER_FL_OZ_PER_PORTION
    hlth_water_fl_oz = hlth_code_portions * HLTH_CODE_WATER_FL_OZ_PER_PORTION
    total_water_fl_oz = soylent_water_fl_oz + hlth_water_fl_oz
    total_water = round(total_water_fl_oz * FL_OZ_TO_GRAMS)

    # Calculate total mass and mass per portion
    total_mass = total_soylent_dry + total_hlth_code_dry + total_water
    mass_per_portion = round(total_mass / args.final_portions)

    # Print results
    print(f"Soylent dry mass: {total_soylent_dry} g")
    print(f"HLTH Code dry mass: {total_hlth_code_dry} g")
    print(f"Total water mass: {total_water} g")
    print(f"Total mass: {total_mass} g")
    print(f"mass per portion: {mass_per_portion} g")


if __name__ == "__main__":
    main()
