import json
import os
from unittest.mock import patch

import pandas as pd
import pytest
from pytest import fixture

from proteobench.score.subcellprofile.subcellprofile_scores import (
    Subcellprofile_Scores,
)

dir = os.path.dirname(__file__)


@fixture
def Score_SpatialDataSet():
    """Fixture to return a Subcellprofile_Scores object with valid data."""
    settings = os.path.join(dir, "../data/subcellprofile/domqc_settings_raw_input.json")
    content = os.path.join(dir, "../data/subcellprofile/pg.matrix.tsv")
    settings = json.load(open(settings))
    content = open(content)
    sp_scores = Subcellprofile_Scores()
    sp_scores.generate_SpatialDataSet(content, settings)
    return sp_scores


@fixture
def Score_SpatialDataSetComparison(Score_SpatialDataSet):
    """Fixture to return a Subcellprofile_Scores object with valid data and a SpatialDataSetComparison object."""
    Score_SpatialDataSet.run_SpatialDataSetComparison()
    return Score_SpatialDataSet


def test_generate_SpatialDataset():
    """Test the SpatialDataSet is generated correctly and contains the dictionary with the right experiment name."""
    settings = os.path.join(dir, "../data/subcellprofile/domqc_settings_raw_input.json")
    content = os.path.join(dir, "../data/subcellprofile/pg.matrix.tsv")
    settings = json.load(open(settings))
    content = open(content)
    sp_scores = Subcellprofile_Scores()
    sp_scores.generate_SpatialDataSet(content, settings)
    assert list(sp_scores.sd.analysed_datasets_dict.keys()) == ["AlphaDIA 1.9.2 Lumos_predicted"]


# TODO: Parameterize this for different input formats
def test_run_SpatialDataSetComparison_noerrors(Score_SpatialDataSet: Subcellprofile_Scores):
    """Running the SpatialDataSetComparison should not raise errors with any input."""
    Score_SpatialDataSet.run_SpatialDataSetComparison()


@pytest.mark.skip("requires domaps 1.0.5")
def test_median_profile_reproducibility(Score_SpatialDataSetComparison):
    """Running the method median_profile_reproducibility and assert the cast of the result."""
    medians_test = Score_SpatialDataSetComparison._median_profile_reproducibility()
    assert isinstance(medians_test, float)


def test_complex_scatter_unnormalized_noerrors(Score_SpatialDataSetComparison):
    """Test the complex scatter average is calculated correctly."""
    mean_complex_scatter = Score_SpatialDataSetComparison._complex_scatter_unnormalized()
    assert isinstance(mean_complex_scatter, float)


@patch("domaps.SpatialDataSetComparison.aggregate_cluster_scatter")
def test_get_metrics_dict_keys(mock_aggregate, Score_SpatialDataSetComparison):
    mock_aggregate.return_value = pd.DataFrame({"distance": [1, 2, 3]})

    results = Score_SpatialDataSetComparison.get_metrics()

    key_set = set(results.keys())
    assert len(key_set) == len(results.keys())

    assert set(results.keys()) == set(
        [
            "depth_id_total",
            "depth_profile_total",
            "depth_id_intersection",
            "depth_profile_intersection",
            "median_profile_reproducibility",
            "mean_complex_scatter",
        ]
    )
