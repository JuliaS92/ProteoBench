import os
from unittest.mock import patch

import pandas as pd
import pytest

from proteobench.modules.subcellprofile.domlfq.protein.DIA.subcellprofile_domlfq_protein_DIA_EXPL import (
    SubcellprofileDomlfqProteinDIAEXPLModule,
)

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), "../data/subcellprofile")
TESTDATA_FILES = {
    "DIA-NN": os.path.join(TESTDATA_DIR, "TRIMMED_DIANN_1-9-2_report.pg_matrix.tsv"),
    "FragPipe (DIA-NN quant)": os.path.join(TESTDATA_DIR, "TRIMMED_FragPipe_DIANNquant_2-0_report.pg_matrix.tsv"),
    "AlphaDIA": os.path.join(TESTDATA_DIR, "TRIMMED_AlphaDIA_1-9-2_pg.matrix.tsv"),
    "Spectronaut": os.path.join(TESTDATA_DIR, "TRIMMED_Spectronaut_19-5_20250130_154210_Proteobench-newdataset_DIA_Exploris_compartiments_ProteinPivot_Report.tsv"),  # noqa: E501; fmt: skip
}


class TestSubcellprofileDomlfqProteinDIAEXPLModule:
    @pytest.fixture(autouse=True)
    @patch("proteobench.github.gh.GithubProteobotRepo.clone_repo")
    @patch("proteobench.github.gh.GithubProteobotRepo.read_results_json_repo")
    def _init(self, mock_read_results_json_repo, mock_clone_repo):
        self.user_input = {
            "software_name": "MaxQuant",
            "software_version": "1.0",
            "search_engine_version": "1.0",
            "search_engine": "MaxQuant",
            "ident_fdr_psm": 0.01,
            "ident_fdr_peptide": 0.05,
            "ident_fdr_protein": 0.1,
            "enable_match_between_runs": 1,
            "precursor_mass_tolerance": "0.02 Da",
            "fragment_mass_tolerance": "0.02 Da",
            "enzyme": "Trypsin",
            "allowed_miscleavages": 1,
            "min_peptide_length": 6,
            "max_peptide_length": 30,
            # "comments_for_plotting": "" -> Doesn't seem to be required for the test"
        }
        mock_clone_repo.return_value = None
        mock_read_results_json_repo.return_value = pd.DataFrame()
        all_datapoints, _ = SubcellprofileDomlfqProteinDIAEXPLModule("").benchmarking(
            TESTDATA_FILES["DIA-NN"], "DIA-NN", self.user_input, None
        )
        self.one_datapoint = all_datapoints

    @patch("proteobench.github.gh.GithubProteobotRepo.clone_repo")
    @patch("proteobench.github.gh.GithubProteobotRepo.read_results_json_repo")
    def test_benchmarking_return_types_are_correct(self, mock_read_results_json_repo, mock_clone_repo):
        mock_clone_repo.return_value = None
        mock_read_results_json_repo.return_value = pd.DataFrame()
        all_datapoints, input_df = SubcellprofileDomlfqProteinDIAEXPLModule("").benchmarking(
            TESTDATA_FILES["DIA-NN"], "DIA-NN", self.user_input, None
        )
        assert isinstance(all_datapoints, pd.DataFrame)
        assert isinstance(input_df, pd.DataFrame)

    @patch("proteobench.github.gh.GithubProteobotRepo.clone_repo")
    @patch("proteobench.github.gh.GithubProteobotRepo.read_results_json_repo")
    def test_all_metric_columns_present_in_all_datapoints(self, mock_read_results_json_repo, mock_clone_repo):
        mock_clone_repo.return_value = None
        mock_read_results_json_repo.return_value = pd.DataFrame()
        all_datapoints, _ = SubcellprofileDomlfqProteinDIAEXPLModule("").benchmarking(
            TESTDATA_FILES["DIA-NN"], "DIA-NN", self.user_input, None
        )
        expected_metrics_columns = [i[0] for i in SubcellprofileDomlfqProteinDIAEXPLModule.metrics]
        assert all(column in all_datapoints.columns for column in expected_metrics_columns)

    @patch("proteobench.github.gh.GithubProteobotRepo.clone_repo")
    def test_new_datapoint_is_added_to_existing_ones(self, mock_clone_repo):
        mock_clone_repo.return_value = None

        # Change hash of existing datapoint to allow addition of the new datapoint with identical data
        self.one_datapoint["intermediate_hash"] = "unique_hash"

        all_datapoints, _ = SubcellprofileDomlfqProteinDIAEXPLModule("").benchmarking(
            TESTDATA_FILES["DIA-NN"], "DIA-NN", self.user_input, self.one_datapoint
        )
        assert len(all_datapoints) == 2

    @patch("proteobench.github.gh.GithubProteobotRepo.clone_repo")
    def test_new_datapoint_already_present_in_datapoints_is_not_added(self, mock_clone_repo):
        """This test requires that exactly the same input data is used for the new datapoint as for
        `self.one_datapoint` in the fixture.
        """
        mock_clone_repo.return_value = None
        all_datapoints, _ = SubcellprofileDomlfqProteinDIAEXPLModule("").benchmarking(
            TESTDATA_FILES["DIA-NN"], "DIA-NN", self.user_input, self.one_datapoint
        )
        assert len(all_datapoints) == 1
