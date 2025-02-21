from __future__ import annotations

import os
from io import StringIO
from typing import Optional, Tuple

import pandas as pd
from pandas import DataFrame

from proteobench.datapoint.subcellprofile_datapoint import SubcellprofileDatapoint
from proteobench.exceptions import (
    ConvertStandardFormatError,
    DatapointAppendError,
    DatapointGenerationError,
    ParseError,
    ParseSettingsError,
)
from proteobench.io.parsing.parse_proteins import load_input_file
from proteobench.io.parsing.parse_settings import ParseSettingsBuilder
from proteobench.modules.subcellprofile.subcellprofile_base_module import (
    SubcellprofileBaseModule,
)
from proteobench.score.subcellprofile.subcellprofile_scores import (
    Subcellprofile_Scores,
)

METRICS: list[tuple[str, str, str]] = [
    ("depth_id_total", "Protein IDs total", "Total number of protein groups identified in any replicate"),
    ("depth_profile_total", "", ""),
    ("depth_id_intersection", "Protein IDs all replicates", "Number of protein groups identified in all replicates"),
    ("depth_profile_intersection", "", ""),
    ("median_profile_reproducibility", "", ""),
    ("mean_complex_scatter", "", ""),
]
"""Main metrics of subcellprofile module for plotting.
[(column_name, short_description, full_description), ...]
"""

DOMAPS_SETTINGS = {
    "filename": "standard_format",  # TODO: Replace with original filename but no FILEENDING, so the file buffer is read as a csv file by `domaps`
    "expname": "standard_format",  # TODO: Replace with something more descriptive
    "source": "custom",
    "acquisition": "custom",
    "level": "proteins",
    "orientation": "long",
    "original_protein_ids": "Proteins",
    "genes": "Proteins",
    "sets": {"Abundance": "Intensity"},
    "name_pattern": ".*_(?P<rep>Map.)_(?P<frac>.*K).*",
    "fractions": ["1K", "3K", "6K", "12K", "24K", "80K"],
    "fraction_mapping": {"1K": "1K", "3K": "3K", "6K": "6K", "12K": "12K", "24K": "24K", "80K": "80K"},
    "columns_annotation": [],
    "samples": "Raw file",
    "organism": "Homo sapiens",
    "reannotate": False,
    "reannotation_source": "Homo sapiens - uniprot reference_swissprot",
    "organelles": "Homo sapiens - Uniprot",
    "complexes": "Homo sapiens - Uniprot",
    "input_invert": False,
    "input_logged": False,
    "input_samplenormalization": None,
    "quality_filter": ["consecutive"],
    "consecutive": 4,
    "column_filters": {},
    "comment": "Settings for ProteoBench standardized output.",
    "domaps_settings_version": "1.0.4",
}


# class DIAQuantIonModule(QuantModule):
class SubcellprofileDomlfqProteinDIAEXPLModule(SubcellprofileBaseModule):
    """DIA Quantification Module for Ion level Quantification."""

    metrics: list[tuple[str, str, str]] = METRICS
    """Main metrics for plotting.
    [(column_name, short_description, full_description), ...]
    """

    def __init__(
        self,
        token: str,
        proteobot_repo_name: str = "Proteobot/Results_subcellprofile_DOMLFQ_protein_DIA_EXPL",
        proteobench_repo_name: str = " Proteobench/Results_subcellprofile_DOMLFQ_protein_DIA_EXPL",
        parse_settings_dir: str = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "..",
                "..",
                "..",
                "io",
                "parsing",
                "io_parse_settings",
                "subcellprofile",
                "domlfq",
                "protein",
                "DIA",
            )
        ),
        module_id: str = "subcellprofile_domlfq_protein_DIA_EXPL",
    ):
        """
        DIA Quantification Module for Ion level Quantification.

        Args:
            token (str): GitHub token for the user.
            proteobot_repo_name (str): Name of the repository for pull requests and where new points are added.
            proteobench_repo_name (str): Name of the repository where the benchmarking results will be stored.
            parse_settings_dir (str): Directory containing parsing settings.
            module_id (str): Module identifier for configuration.
        """
        super().__init__(
            token,
            proteobot_repo_name=proteobot_repo_name,
            proteobench_repo_name=proteobench_repo_name,
            parse_settings_dir=parse_settings_dir,
            module_id=module_id,
        )

    def is_implemented(self) -> bool:
        """Returns whether the module is fully implemented."""
        return False

    def benchmarking(
        self,
        input_file: str,
        input_format: str,
        user_input: dict,
        all_datapoints: Optional[pd.DataFrame],
    ) -> Tuple[DataFrame, DataFrame]:
        """
        Main workflow of the module for benchmarking workflow results.

        Args:
            input_file (str): Path to the workflow output file.
            input_format (str): Format of the workflow output file.
            user_input (dict): User-provided parameters for plotting.
            all_datapoints (Optional[pd.DataFrame]): DataFrame containing all data points from the repo.

        Returns:
            Tuple[DataFrame, DataFrame]: DataFrame containing all data points, dataframe of the input file
        """
        try:
            input_df = load_input_file(input_file, input_format)
        except pd.errors.ParserError as e:
            raise ParseError(
                f"Error parsing {input_format} file, please ensure the format is correct and the correct software tool is chosen: {e}"
            )
        except Exception as e:
            raise ParseSettingsError(f"Error parsing the input file: {e}")

        try:
            parse_settings = ParseSettingsBuilder(
                parse_settings_dir=self.parse_settings_dir, module_id=self.module_id
            ).build_parser(input_format)
        except KeyError as e:
            raise ParseSettingsError(f"Error parsing settings file for parsing, settings missing: {e}")
        except FileNotFoundError as e:
            raise ParseSettingsError(f"Could not find the parsing settings file: {e}")
        except Exception as e:
            raise ParseSettingsError(f"Error parsing settings file for parsing: {e}")

        try:
            standardized_table, replicate_to_raw = parse_settings.convert_to_standard_format(input_df)
        except KeyError as e:
            raise ConvertStandardFormatError(f"Error converting to standard format, key missing: {e}")
        except Exception as e:
            raise ConvertStandardFormatError(f"Error converting to standard format: {e}")

        domaps_settings = DOMAPS_SETTINGS
        standardized_table_file_buffer = StringIO(standardized_table.to_csv(sep=",", index=False))

        quant_score = Subcellprofile_Scores()
        quant_score.generate_SpatialDataSet(content=standardized_table_file_buffer, settings=domaps_settings)
        quant_score.run_SpatialDataSetComparison()
        metrics: dict[str, float] = quant_score.get_metrics()

        try:
            current_datapoint = SubcellprofileDatapoint.generate_datapoint(metrics, input_format, user_input)
        except Exception as e:
            raise DatapointGenerationError(f"Error generating datapoint: {e}")

        try:
            all_datapoints = self.add_current_data_point(current_datapoint, all_datapoints=all_datapoints)
        except Exception as e:
            raise DatapointAppendError(f"Error adding current data point: {e}")

        return (
            all_datapoints,
            input_df,
        )
