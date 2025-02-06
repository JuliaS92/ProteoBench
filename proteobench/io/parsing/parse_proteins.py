from pathlib import Path

import pandas as pd


def load_input_file(input_csv: str, input_format: str) -> pd.DataFrame:
    """
    Loads a dataframe from a CSV file depending on its format.

    Args:
        input_csv (str): The path to the CSV file.
        input_format (str): The format of the input file (e.g., "MaxQuant", "AlphaPept", etc.).

    Returns:
        pd.DataFrame: The loaded dataframe.
    """

    if input_format == "DIA-NN":
        input_data_frame = pd.read_csv(input_csv, low_memory=False, sep="\t")

        # Remove the whole filepath in *.pg_matrix and the extension of the filenames
        rename_path_to_file = {c: Path(c.replace("/", "\\").split("\\")[-1]).stem for c in input_data_frame.columns[4:]}
        input_data_frame = input_data_frame.rename(columns=rename_path_to_file)
    elif input_format == "FragPipe (DIA-NN quant)":
        input_data_frame = pd.read_csv(input_csv, low_memory=False, sep="\t")

        # Remove the whole filepath in *.pg_matrix and the extension of the filenames
        rename_path_to_file = {c: Path(c.replace("/", "\\").split("\\")[-1]).stem for c in input_data_frame.columns[5:]}
        input_data_frame = input_data_frame.rename(columns=rename_path_to_file)
    elif input_format == "AlphaDIA":
        input_data_frame = pd.read_csv(input_csv, low_memory=False, sep="\t")
    elif input_format == "Spectronaut":
        input_data_frame = pd.read_csv(input_csv, low_memory=False, sep="\t")
        rename_header_to_file = dict()
        for column in input_data_frame.columns:
            if column.endswith(".PG.Quantity"):
                rename_header_to_file[column] = Path(column[: -len(".PG.Quantity")].split(" ", 1)[-1]).stem

        input_data_frame = input_data_frame.rename(columns=rename_header_to_file)

    return input_data_frame
