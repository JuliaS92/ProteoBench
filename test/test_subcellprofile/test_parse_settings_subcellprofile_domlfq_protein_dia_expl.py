import os

import pytest

from proteobench.io.parsing.parse_proteins import load_input_file
from proteobench.io.parsing.parse_settings import ParseSettingsBuilder

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), "../data/subcellprofile_domlfq_protein_DIA_EXPL")
TESTDATA_FILES = {
    "DIA-NN": os.path.join(TESTDATA_DIR, "DIA-NN_example_domlfq_report.pg_matrix.tsv"),
    "FragPipe (DIA-NN quant)": os.path.join(TESTDATA_DIR, "FragPipe-DIA-NN_example_domlfq_report.pg_matrix.tsv"),
    "AlphaDIA": os.path.join(TESTDATA_DIR, "AlphaDIA_example_domlfq_report.pg.matrix.tsv"),
}
SUPPORTED_SOFTWARE_TOOLS = ("DIA-NN", "FragPipe (DIA-NN quant)", "AlphaDIA")
PARSE_SETTINGS_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "proteobench",
        "io",
        "parsing",
        "io_parse_settings",
        "subcellprofile",
        "domlfq",
        "protein",
        "DIA",
    )
)


def load_file(format_name: str):
    """Method used to load the input file."""
    input_df = load_input_file(TESTDATA_FILES[format_name], format_name)
    return input_df


class TestOutputFileReading:
    """Simple tests for reading csv input files."""

    def test_if_module_supports_search_tool(self):
        """Test whether all software tools supported by the module are actually tested."""
        parse_settings = ParseSettingsBuilder(
            parse_settings_dir=PARSE_SETTINGS_DIR, module_id="subcellprofile_domlfq_protein_DIA_EXPL"
        )
        for parsed_software_tool in parse_settings.INPUT_FORMATS:
            assert parsed_software_tool in SUPPORTED_SOFTWARE_TOOLS

    @pytest.mark.parametrize("software_tool", SUPPORTED_SOFTWARE_TOOLS)
    def test_valid_and_supported_search_tool_settings_exists(self, software_tool):
        """Test whether valid settings files exist for the tested software tools."""
        parse_settings = ParseSettingsBuilder(
            parse_settings_dir=PARSE_SETTINGS_DIR, module_id="subcellprofile_domlfq_protein_DIA_EXPL"
        )
        assert software_tool in parse_settings.INPUT_FORMATS

    @pytest.mark.parametrize("software_tool", SUPPORTED_SOFTWARE_TOOLS)
    def test_input_file_loading(self, software_tool):
        """Test whether the inputs input are loaded successfully."""
        input_df = load_file(software_tool)
        assert not input_df.empty

    @pytest.mark.parametrize("software_tool", SUPPORTED_SOFTWARE_TOOLS)
    def test_creation_of_parser_settings_instance(self, software_tool):
        """Test whether the input files are loaded successfully."""

        parse_settings_builder = ParseSettingsBuilder(
            module_id="subcellprofile_domlfq_protein_DIA_EXPL", parse_settings_dir=PARSE_SETTINGS_DIR
        )
        parse_settings = parse_settings_builder.build_parser(software_tool)
        assert parse_settings is not None

    @pytest.mark.parametrize("software_tool", SUPPORTED_SOFTWARE_TOOLS)
    def test_input_file_initial_parsing(self, software_tool):
        """Test the initial parsing of the input file."""

        parse_settings_builder = ParseSettingsBuilder(
            module_id="subcellprofile_domlfq_protein_DIA_EXPL", parse_settings_dir=PARSE_SETTINGS_DIR
        )

        input_df = load_file(software_tool)
        parse_settings = parse_settings_builder.build_parser(software_tool)
        prepared_df, replicate_to_raw = parse_settings.convert_to_standard_format(input_df)

        assert not prepared_df.empty
        assert replicate_to_raw != {}

    @pytest.mark.parametrize("software_tool", SUPPORTED_SOFTWARE_TOOLS)
    def test_correct_number_of_rawfiles_present_in_parsed_input_file(self, software_tool):
        """Test whether the correct number of rawfiles are present in the parsed input file."""
        parse_settings_builder = ParseSettingsBuilder(
            module_id="subcellprofile_domlfq_protein_DIA_EXPL", parse_settings_dir=PARSE_SETTINGS_DIR
        )

        input_df = load_file(software_tool)
        parse_settings = parse_settings_builder.build_parser(software_tool)
        prepared_df, replicate_to_raw = parse_settings.convert_to_standard_format(input_df)

        parsed_rawfiles = sorted(prepared_df["Raw file"].unique())
        expected_rawfiles = sorted(parse_settings.run_mapper.keys())
        assert parsed_rawfiles == expected_rawfiles
