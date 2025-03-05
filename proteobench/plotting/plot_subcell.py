"""
Module for plotting quantitative proteomics data.
"""

from typing import Dict

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class PlotDataPoint:
    """
    Class for plotting data points.
    """

    @staticmethod
    def plot_metric(
        benchmark_metrics_df: pd.DataFrame,
        metric_x: str = "median_profile_reproducibility",  # or mean_complex_scatter
        metric_y: str = "depth_id_total",  # or depth_profile_total
        software_colors: Dict[str, str] = {
            "DIA-NN": "#8c564b",
            "AlphaDIA": "#4daf4a",
            "Custom": "#7f7f7f",
            "Spectronaut": "#bcbd22",
            "FragPipe (DIA-NN quant)": "#ff7f00",
        },
        mapping: Dict[str, int] = {"old": 10, "new": 20},
        highlight_color: str = "#d30067",
        label: str = "None",
    ) -> go.Figure:
        """
        Plot selected metrics in a scatter plot with Plotly, highlighting specific data points.

        Parameters
        ----------
        benchmark_metrics_df : pd.DataFrame
            The DataFrame containing benchmark metrics data.
        metric_x : str, optional
            The metric to plot, either "median_profile_reproducibility" or "mean_complex_scatter", by default "median_profile_reproducibility".
        metric_y : str, optional
            The metric to plot, either "depth_id_total" or "depth_profile_total", by default "depth_id_total".
        software_colors : Dict[str, str], optional
            A dictionary mapping software names to their colors, by default predefined colors.
        mapping : Dict[str, int], optional
            A dictionary mapping categories to scatter plot sizes, by default {"old": 10, "new": 20}.
        highlight_color : str, optional
            The color used for highlighting certain points, by default "#d30067".
        label : str, optional
            The column name for labeling data points, by default "None".

        Returns
        -------
        go.Figure
            A Plotly figure object representing the scatter plot.
        """

        # TODO: both y metrics seem to be series, logic is missing on which value to plot
        x_values = benchmark_metrics_df[metric_x]
        y_values = benchmark_metrics_df[metric_y].apply(lambda x: x[0])

        # Add hover text with detailed information for each data point
        hover_texts = []
        for idx, _ in benchmark_metrics_df.iterrows():
            datapoint_text = ""
            if benchmark_metrics_df.is_temporary[idx] == True:
                datapoint_text = (
                    f"ProteoBench ID: {benchmark_metrics_df.id[idx]}<br>"
                    + f"Software tool: {benchmark_metrics_df.software_name[idx]} {benchmark_metrics_df.software_version[idx]}<br>"
                )
                if "comments" in benchmark_metrics_df.columns:
                    datapoint_text = (
                        datapoint_text + f"Comment (private submission): {benchmark_metrics_df.comments[idx]}"
                    )
            else:
                # TODO: Determine parameters based on module
                datapoint_text = (
                    f"ProteoBench ID: {benchmark_metrics_df.id[idx]}<br>"
                    + f"Software tool: {benchmark_metrics_df.software_name[idx]} {benchmark_metrics_df.software_version[idx]}<br>"
                    + f"Search engine: {benchmark_metrics_df.search_engine[idx]} {benchmark_metrics_df.search_engine_version[idx]}<br>"
                    + f"FDR psm: {benchmark_metrics_df.ident_fdr_psm[idx]}<br>"
                    + f"MBR: {benchmark_metrics_df.enable_match_between_runs[idx]}<br>"
                    + f"Precursor Tolerance: {benchmark_metrics_df.precursor_mass_tolerance[idx]}<br>"
                    + f"Fragment Tolerance: {benchmark_metrics_df.fragment_mass_tolerance[idx]}<br>"
                    + f"Enzyme: {benchmark_metrics_df.enzyme[idx]} <br>"
                    + f"Missed Cleavages: {benchmark_metrics_df.allowed_miscleavages[idx]}<br>"
                    + f"Min peptide length: {benchmark_metrics_df.min_peptide_length[idx]}<br>"
                    + f"Max peptide length: {benchmark_metrics_df.max_peptide_length[idx]}<br>"
                )
                if "submission_comments" in benchmark_metrics_df.columns:
                    datapoint_text = (
                        datapoint_text + f"Comment (public submission): {benchmark_metrics_df.submission_comments[idx]}"
                    )

            hover_texts.append(datapoint_text)

        scatter_size = [mapping[item] for item in benchmark_metrics_df["old_new"]]
        if "Highlight" in benchmark_metrics_df.columns:
            scatter_size = [
                item * 2 if highlight else item
                for item, highlight in zip(scatter_size, benchmark_metrics_df["Highlight"])
            ]

        # Color plot based on software tool
        colors = [software_colors[software] for software in benchmark_metrics_df["software_name"]]
        if "Highlight" in benchmark_metrics_df.columns:
            colors = [
                highlight_color if highlight else item
                for item, highlight in zip(colors, benchmark_metrics_df["Highlight"])
            ]

        benchmark_metrics_df["color"] = colors
        benchmark_metrics_df["hover_text"] = hover_texts
        benchmark_metrics_df["scatter_size"] = scatter_size

        layout_xaxis_range = [
            min(x_values) - min(x_values) * 0.05,
            max(x_values) + max(x_values) * 0.05,
        ]
        layout_xaxis_title = (
            # TODO: replace by string defined in module
            metric_x
        )

        layout_yaxis_range = [
            min(y_values) - min(max(y_values) * 0.05, 2000),
            max(y_values) + min(max(y_values) * 0.05, 2000),
        ]

        layout_yaxis_title = (
            # TODO: replace by string defined in module
            metric_y
        )

        fig = go.Figure(
            layout_yaxis_range=layout_yaxis_range,
            layout_xaxis_range=layout_xaxis_range,
        )

        # Get all unique color-software combinations (necessary for highlighting)
        color_software_combinations = benchmark_metrics_df[["color", "software_name"]].drop_duplicates()
        benchmark_metrics_df["enable_match_between_runs"] = benchmark_metrics_df["enable_match_between_runs"].astype(
            str
        )
        # plot the data points, one trace per software tool
        for _, row in color_software_combinations.iterrows():
            color = row["color"]
            software = row["software_name"]

            tmp_df = benchmark_metrics_df[
                (benchmark_metrics_df["color"] == color) & (benchmark_metrics_df["software_name"] == software)
            ]
            # to do: remove this line as soon as parameters are homogeneous, see #380
            # tmp_df["enable_match_between_runs"] = tmp_df["enable_match_between_runs"].astype(str)
            fig.add_trace(
                go.Scatter(
                    x=tmp_df[metric_x],
                    y=tmp_df[metric_y].apply(lambda x: x[0]),
                    mode="markers" if label == "None" else "markers+text",
                    hovertext=tmp_df["hover_text"],
                    text=tmp_df[label] if label != "None" else None,
                    marker=dict(color=tmp_df["color"], showscale=False),
                    marker_size=tmp_df["scatter_size"],
                    name=tmp_df["software_name"].iloc[0],
                )
            )

        fig.update_layout(
            width=700,
            height=700,
            xaxis=dict(
                title=layout_xaxis_title,
                gridcolor="white",
                gridwidth=2,
                linecolor="black",
            ),
            yaxis=dict(
                title=layout_yaxis_title,
                gridcolor="white",
                gridwidth=2,
                linecolor="black",
            ),
        )
        fig.update_xaxes(showgrid=True, gridcolor="lightgray", gridwidth=1)
        fig.update_yaxes(showgrid=True, gridcolor="lightgray", gridwidth=1)

        fig.add_annotation(
            x=0.5,
            y=0.5,
            xref="paper",
            yref="paper",
            text="-Beta-",
            font=dict(size=50, color="rgba(0,0,0,0.1)"),
            showarrow=False,
        )

        fig.update_layout(clickmode="event+select")

        return fig
