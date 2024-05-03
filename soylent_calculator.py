#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

# Constants for Soylent and HLTH Code
SOYLENT_CALORIES_PER_PORTION = 400 * 3 / 9
SOYLENT_DRY_GRAMS_PER_PORTION = 90 * 3 / 9
SOYLENT_WATER_FL_OZ_PER_PORTION = 12 * 3 / 9
SOYLENT_CARBS_GRAMS_PER_PORTION = 36 * 3 / 9

HLTH_CODE_CALORIES_PER_PORTION = 800 / 9
HLTH_CODE_DRY_GRAMS_PER_PORTION = 156 / 9
HLTH_CODE_WATER_FL_OZ_PER_PORTION = 16 / 9
HLTH_CODE_CARBS_GRAMS_PER_PORTION = 0 / 9

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
    # Recommended water is from:
    # https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/water/art-20044256
    parser.add_argument(
        "--min-water",
        type=int,
        default=2800,
        help=(
            "Minimum number of grams of water. Default is 2800, "
            "3700 g/2700 g are the recommended amount of "
            "water per day for an adult male/female.)"
        ),
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
    total_water_g = round(total_water_fl_oz * FL_OZ_TO_GRAMS)
    total_water = max(args.min_water, total_water_g)

    # Calculate total carbs
    total_carbs = (
        soylent_portions * SOYLENT_CARBS_GRAMS_PER_PORTION
        + hlth_code_portions * HLTH_CODE_CARBS_GRAMS_PER_PORTION
    )
    carbs_per_portion = round(total_carbs / args.final_portions, 1)

    # Calculate total mass and mass per portion
    total_mass = total_soylent_dry + total_hlth_code_dry + total_water
    mass_per_portion = round(total_mass / args.final_portions)

    # Calculate minimum mass for next level of carbs
    next_level_of_carbs = int(carbs_per_portion) + 0.5
    min_mass_for_next_level_of_carbs = round(
        mass_per_portion * next_level_of_carbs / carbs_per_portion
    )

    # Print results
    print(f"Soylent dry mass: {total_soylent_dry} g")
    print(f"HLTH Code dry mass: {total_hlth_code_dry} g")
    print(f"Total water mass: {total_water} g")
    print(f"Total mass: {total_mass} g")
    print(f"Mass per portion: {mass_per_portion} g")
    print(f"Carbs per portion: {carbs_per_portion} g")
    print(
        f"Min mass for {next_level_of_carbs} g"
        f"carbs: {min_mass_for_next_level_of_carbs} g"
    )


if __name__ == "__main__":
    main()
