"""CSV implementation of Nguza's SQL function for mapping waves"""

import argparse
import pandas as pd
import numpy as np


def process_csv(input_path, output_path):
    try:
        df = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    locality_cols = [
        "sq_onb_localitycluj",
        "sq_onb_localitydambovita",
        "sq_onb_localitydolj",
        "sq_onb_localitygalati",
        "sq_onb_localitygiurgiu",
        "sq_onb_localityiasi",
        "sq_onb_localityolt",
        "sq_onb_localityteleorman",
        "sq_onb_localityvalcea",
        "sq_onb_localityvaslui",
    ]

    # Mapping keys are lowercase for case-insensitive matching
    WAVE_MAPPING = {
        "mociu": "Wave 2",
        "apahida": "Wave 1",
        "vânătorii mici": "Wave 2",
        "mănești": "Wave 1",
        "pechea": "Wave 2",
        "valea marului": "Wave 1",
        "cosmesti": "Wave 2",
        "bucesti": "Wave 1",
        "vădastra": "Wave 1",
        "grecești": "Wave 2",
        "breasta": "Wave 2",
        "seaca de padure": "Wave 2",
        "runcu": "Wave 2",
        "pesceana": "Wave 1",
        "stoilești": "Wave 1",
        "traian": "Wave 1",
        "botoșești-paia": "Wave 1",
        "scundu": "Wave 2",
        "parpanița": "Wave 1",
        "todirești": "Wave 2",
        "tătărani": "Wave 1",
        "pogonești": "Wave 2",
        "golăiești": "Wave 1",
        "vlădeni": "Wave 2",
    }

    # Create a temporary copy of the locality columns to find the first valid entry
    # .strip() handles whitespace, and treat 'NA' or empty strings as nulls
    temp_localities = df[locality_cols].copy()
    for col in locality_cols:
        temp_localities[col] = temp_localities[col].astype(str).str.strip()
        temp_localities[col] = temp_localities[col].replace(
            ["NA", "nan", "None", ""], np.nan
        )

    # Grab the first non-null value across the specified columns
    df["locality"] = temp_localities.bfill(axis=1).iloc[:, 0]

    # Apply mapping
    # Normalize the extracted locality to lowercase and stripped for the lookup
    lookup_val = df["locality"].astype(str).str.lower().str.strip()
    df["recruitment"] = lookup_val.map(WAVE_MAPPING)

    df.to_csv(output_path, index=False)
    print(f"Success! Processed {len(df)} rows.")
    print(f"Results saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Map Romanian localities to Waves via CSV."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV")
    parser.add_argument("--output", "-o", required=True, help="Path to output CSV")

    args = parser.parse_args()
    process_csv(args.input, args.output)


if __name__ == "__main__":
    main()
