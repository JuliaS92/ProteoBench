# Subcellular profile DOM LFQ - protein level - DIA

This module uses subcellular fractionation to assess the sensitivity and quantification accuracy for data acquired with data-independent acquisition (DIA) on a Thermo Exploris 480.
This module is work in progress.

**We are working on the documentation: more information comming soon.**

Users can load their data and inspect the results privately. They can also make their outputs public by providing the associated parameter file and submitting the benchmark run to ProteoBench. By doing so, their workflow output will be stored alongside all other benchmark runs in ProteoBench and will be accessible to the entire community.

**This module is not designed to compare later-stages post-processing of quantitative data such as missing value replacement, and we advise users to publically upload data without replacement of missing values and without manual filtering.**

We think that this module is more suited to evaluate the impact of (non exhaustive list):
-

Other modules will be more suited to explore further post-pocessing steps.

## Data set

A subset of the Thermo Exploris 480 mass spectrometer (Thermo Fisher) data independent acquisition (DIA) data described by [Schessner et al., 2023](https://www.nature.com/articles/s41467-023-41000-7) was used as a benchmark dataset. Here, only the 18 runs from the short gradient series (named “20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5*”) was used, including three technical replicates of 6 fractions derived from subcellular fractionation by centrifugation of HeLa cells.

Please refer to the original publication for the full description of sample preparation and data acquisition parameters ([Schessner et al., 2023](https://www.nature.com/articles/s41467-023-41000-7).

The files can be downloaded from the proteomeXchange repository [PXD034971](https://www.ebi.ac.uk/pride/archive/projects/PXD034971), make sure that you download the following raw files:

- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5_Map2_3K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5_Map2_3K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_1K_20210131142601.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_1K_20210131142601.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_3K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_3K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_6K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_6K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_12K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_12K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_24K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_24K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_80K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map1_80K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_1K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_1K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_6K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_6K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_12K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_12K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_24K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_24K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_80K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map2_80K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_1K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_1K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_3K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_3K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_6K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_6K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_12K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_12K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_24K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_24K.raw)
- [20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_80K.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2023/08/PXD034971/20210131_EXPL4_ViAl_SA_HeLa_Evosep_21min_DIA_120k_15k_1-5s_Map3_80K.raw)

Alternatively, you can download them from the ProteoBench server here: [proteobench.cubimed.rub.de/datasets/raw_files/subcellprofile/](To be uploaded)

**It is imperative not to rename the files once downloaded!**

Download the zipped FASTA file here: <a href="https://datashare.biochem.mpg.de/s/IaZH252kMCs8yY2" download>FileShare</a>.
The fasta file provided for this module contains human proteins and contaminant proteins
([Frankenfield et al., JPR](https://pubs.acs.org/doi/10.1021/acs.jproteome.2c00145))

## Metric calculation

In this module, the performance of the workflow is evaluated on three metrics.
TBD: which proteins are used and why

1) Profile depth: Number of proteins for which a profile could be calculated. Only proteins with 4 or more quantification values in **consecutive** runs are used.
2) Reproducibility: Coefficients of Variation
3) Complex scatter: Mean (?) of the mean (?) manhattan distance of protein profiles to the average (?) protein profile per complex

## How to use

### Input data for private visualisation of your benchmark run(s)

The module is flexible in terms of what workflow the participants can run. However, to ensure a fair comparison of the different processing tools, we suggest using the parameters listed in Table 1.

|Parameter|Value|
|---------|-----|
|Maximum number of missed cleavages|1|
|PSM FDR|0.01|
|Protein FDR|0.01|
|Precursor m/z range|350-1400|
|Fragment ion m/z range|361-1033|
|Endopeptidase|Trypsin/P|
|Fixed modifications|Carbamidomethylation (C)|
|Variable modifications|Oxidation (M), Acetyl (Protein N-term)|


### Submit your run for public usage

When you have successfully uploaded and visualized a benchmark run, we strongly encourage you to add the result to the online repository. This way, your run will be available to the entire community and can be compared to all other uploaded benchmark runs. By doing so, your workflow outputs, parameters and calculated metrics will be stored and publicly available.

To submit your run for public usage, you need to upload the parameter file associated to your run in the field `Meta data for searches`. Currently, we accept outputs from DIA-NN, AlphaDIA, FragPipe, and Spectronaut (see bellow for more tool-specific details). Please fill the `Comments for submission` if needed, and confirm that the metadata is correct (corresponds to the benchmark run) before checking the button `I confirm that the metadata is correct`. Then the button
`I really want to upload it` will appear to trigger the submission.

Table 2 provides an overview of the required input files for public submission. More detailed instructions are provided for each individual tool in the following section.

**Table 2. Overview of input files required for metric caluclation and public submission**
|Tool|Input file|Parameter File|
|---------|-----|-|
|AlphaDIA|pg_matrix.tsv|log.txt|
|DIA-NN|report.pg_matrix.tsv|*report.log.txt|
|FragPipe (DIA-NN quant)|report.pg_matrix.tsv|fragpipe.workflow|
|Spectronaut|output name with “(normal)”|*.txt|


After upload, you will get a link to a Github pull request associated with your data. Please copy it and save it. With this link, you can get the unique identifier of your run (for example `Proline__20240106_141919`), and follow the advancement of your submission and add comments to communicate with the ProteoBench maintainers. If everything looks good, your submission will be reviewed and accepted (it will take a few working days). Then, your benchmark run will be added to the public runs of this module and plotted alongside all other benchmark runs in the figure.

## Important Tool-specific settings

### [DIA-NN](https://github.com/vdemichev/DiaNN)
1. Import Raw files
2. Add FASTA but do not select "Contaminants" since these are already included in the FASTA file
3. Turn on FASTA digest for library-free search / library generation (automatically activates deep-learning based spectra, RTs, and IMs prediction).
4. Do not set verbosity/Log Level higher than 1, otherwise parameter parsing will not work correctly.
5. The input files for Proteobench are "report.pg_matrix.tsv" (main report for the protein quantities) and "*report.log.txt*" (parameter files).

### [AlphaDIA](https://github.com/MannLabs/alphadia)
1. Select FASTA and import .raw files in "Input files"
2. In "Method settings" you need to define your search parameters
3. Turn on "Predict Library"
4. The input files for ProteoBench are "pg_matrix.tsv" (protein quantification) and "log.txt" (parameter files)

### [FragPipe - DIA-NN](https://github.com/Nesvilab/FragPipe)
1. Load the DIA_SpecLib_Quant workflow
2. Following import of raw files, assign experiments "by File Name" right above the list of raw files.
3. **Make sure contaminants are not added when you add decoys to the database**.
4. Upload “report.pg_matrix.tsv” in order for Proteobench to calculate the ion ratios. For public submission, please provide the parameter file “fragpipe.workflow” that correspond to your search.

### [Spectronaut](https://biognosys.com/software/spectronaut/?gad_source=1&gclid=CjwKCAjwreW2BhBhEiwAavLwfBvsoFvzw54UAATBCaHN6kn8T0vmcdo1ZLhPUH0t90yM-XGo9_fNOhoCsuUQAvD_BwE) (work in progress)


### Custom format

Work in progress

## toml file description (work in progress)

Each software tool produces specific output files formats. We made ``.toml`` files that describe where to find the information needed in each type of input. These can be found in `proteobench/modules/dia_quant/io_parse_settings`:

(TBD)


## Result Description

After uploading an output file, a table is generated that contains the following columns:

(TBD)

  ## Define Parameters

To make the results available to the entire community, you need to provide the parameter file that corresponds to
your analysis. You can upload it in the drag and drop area in the "Add results to online repository" section (under Download calculated ratio's).
See [here](#important-tool-specific-settings)
for all compatible parameter files.
In this module, we keep track of the following parameters, if you feel
that some important information is missing, please add it in the
`Comments for submission` field.
  - software tool name and version
  - search engine name and version (if different from software tool)
  - FDR threshold for PSM, peptide and protein level
  - match between run (or not)
  - Precursor and fragment m/z range
  - precursor and fragment mass tolerance
  - enzyme (although for these data it should be Trypsin)
  - maximum number of missed-cleavages
  - minimum and maximum peptide length
  - fixed and variable modifications
  - maximum number of modifications
  - minimum and maximum precursor charge

Once you confirm that the metadata is correctly parsed (and corresponds to the
table you uploaded before generating the plot), a button will appear.
Press it to submit.

**If some parameters are not in your parameter file, it is important that
you provide them in the "comments" section.**

Once submitted, you will see a weblink that will prompt you to a
pull request on the github repository of the module. Please write down
its number to keep track of your submission. If it looks good, one of
the reviewers will accept it and make your data public.

Please contact us if you have any issue. To do so, you can create an
[issue](https://github.com/Proteobench/ProteoBench/issues/new) on our
github, or [send us an email](mailto:proteobench@eubic-ms.org?subject=ProteoBench_query).