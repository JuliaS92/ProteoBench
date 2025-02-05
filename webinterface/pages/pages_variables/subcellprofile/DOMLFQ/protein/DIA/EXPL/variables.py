from dataclasses import dataclass, field
from typing import List, Type

from pages.texts.generic_texts import WebpageTexts


@dataclass
class VariablesSubcellprofileDOMLFQ:
    all_datapoints: str = "all_datapoints_subcell_domlfq"
    all_datapoints_submission: str = "all_datapoints_submission_subcell_domlfq"
    input_df_submission: str = "input_df_submission_subcell_domlfq"
    result_performance_submission: str = "result_performance_submission_subcell_domlfq"
    submit: str = "submit_subcell_domlfq"
    fig_logfc: str = "fig_logfc_subcell_domlfq"
    fig_metric: str = "fig_metric_subcell_domlfq"
    fig_cv: str = "fig_CV_violinplot_subcell_domlfq"
    result_perf: str = "result_perf_subcell_domlfq"
    meta_data: str = "meta_data_subcell_domlfq"
    input_df: str = "input_df_subcell_domlfq"
    meta_file_uploader_uuid: str = "meta_file_uploader_uuid_subcell_domlfq"
    comments_submission_uuid: str = "comments_submission_uuid_subcell_domlfq"
    check_submission_uuid: str = "check_submission_uuid_subcell_domlfq"
    meta_data_text: str = "comments_for_submission_subcell_domlfq"
    check_submission: str = "heck_submission_subcell_domlfq"
    button_submission_uuid: str = "button_submission_uuid_subcell_domlfq"
    df_head: str = "df_head_subcell_domlfq"
    placeholder_fig_compare: str = "placeholder_fig_compare_subcell_domlfq"
    placeholder_table: str = "placeholder_table_subcell_domlfq"
    placeholder_slider: str = "placeholder_slider_subcell_domlfq"
    placeholder_downloads_container: str = "placeholder_downloads_container_subcell_domlfq"
    highlight_list: List[str] = field(default_factory=list)
    first_new_plot: bool = True
    default_val_slider: int = 3
    beta_warning: bool = True
    github_link_pr: str = "github.com/Proteobot/Results_quant_ion_DIA.git"
    selectbox_id_submitted_uuid: str = "selectbox_id_submitted_subcell_domlfq"
    selectbox_id_uuid: str = "selectbox_id_subcell_domlfq"
    slider_id_submitted_uuid: str = "slider_id_submitted_subcell_domlfq"
    slider_id_uuid: str = "slider_id_subcell_domlfq"
    download_selector_id_uuid: str = "download_selector_id_subcell_domlfq"
    table_id_uuid: str = "table_id_subcell_domlfq"

    additional_params_json: str = "../webinterface/configuration/subcell_domlfq.json"

    description_module_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/introduction.md"
    description_files_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/file_description.md"
    description_input_file_md: str = (
        "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/input_file_description.md"
    )
    description_slider_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/slider_description.md"
    description_table_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/table_description.md"
    description_results_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/result_description.md"
    description_submission_md: str = "pages/markdown_files/subcellprofile/DOMLFQ/protein/DIA/EXPL/submit_description.md"

    all_datapoints_submitted: str = "all_datapoints_submitted_subcell_domlfq"
    placeholder_table_submitted: str = "placeholder_table_submitted_subcell_domlfq"
    placeholder_slider_submitted: str = "placeholder_slider_submitted_subcell_domlfq"
    highlight_list_submitted: List[str] = field(default_factory=list)

    parse_settings_dir: str = "../proteobench/io/parsing/io_parse_settings/Quant/lfq/ion/DIA/AIF"

    texts: Type[WebpageTexts] = WebpageTexts
    doc_url: str = (
        "https://proteobench.readthedocs.io/en/latest/available-modules/6-subcellprofile-domlfq-protein-DIA-expl/"
    )

    title: str = "Subcellular protein profiling - DOMLFQ"

    additional_params_json: str = "../proteobench/io/params/json/Quant/lfq/ion/DIA/fields.json"
    prefix_params: str = "lfq_ion_dia_aif_quant_"
    params_json_dict: str = "params_json_dict_lfq_ion_dda_aif_quant"
    params_file_dict: str = "params_file_dict_lfq_ion_dia_aif_quant"
