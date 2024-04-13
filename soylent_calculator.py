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
FL_OZ_TO_GRAMS = 29.5735


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
    args.total_calories -= soylent_portions * SOYLENT_CALORIES_PER_PORTION
    hlth_code_portions = min(
        args.total_calories // HLTH_CODE_CALORIES_PER_PORTION,
        args.final_portions - soylent_portions,
    )

    # Calculate total weight of each ingredient
    total_soylent_dry = soylent_portions * SOYLENT_DRY_GRAMS_PER_PORTION
    total_hlth_code_dry = hlth_code_portions * HLTH_CODE_DRY_GRAMS_PER_PORTION
    total_water = (
        soylent_portions * SOYLENT_WATER_FL_OZ_PER_PORTION
        + hlth_code_portions * HLTH_CODE_WATER_FL_OZ_PER_PORTION
    ) * FL_OZ_TO_GRAMS

    # Calculate total weight and weight per portion
    total_weight = total_soylent_dry + total_hlth_code_dry + total_water
    weight_per_portion = total_weight / args.final_portions

    # Print results
    print(f"Soylent dry weight: {total_soylent_dry} g")
    print(f"HLTH Code dry weight: {total_hlth_code_dry} g")
    print(f"Total water weight: {total_water} g")
    print(f"Total weight: {total_weight} g")
    print(f"Weight per portion: {weight_per_portion} g")


if __name__ == "__main__":
    main()
