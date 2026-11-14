# QGIS Scripts

## 1. Overview

This directory contains the Python scripts used to automate the geometric characterization of the residential building stock of Álava using QGIS.

The main entry point is `Script_QGIS.py`, which executes the individual processing scripts stored in the `0.Códigos` directory.

## 2. Software Requirements

- QGIS 3.42.3
- Python environment integrated into QGIS
- PyQt5 (included in the QGIS Python environment)

## 3. Script Organization

The original methodology includes 25 individual `.txt` scripts:

| Script group | Scripts | Purpose |
|---|---|---|
| Normal processing | a1–a22 | Geometric characterization workflow |
| Cleanup and reset | a23–a25 | Removal and reset of generated files and temporary data |

Scripts are executed in numerical order to ensure that processing operations follow the required sequence.

## 4. Main Execution Script

`Script_QGIS.py` is responsible for:

1. Opening a folder-selection dialog to locate the processing scripts.
2. Identifying the available `.txt` files.
3. Sorting scripts numerically.
4. Checking that all 25 scripts are present and consecutively numbered.
5. Selecting the execution group according to the configured mode.
6. Executing the selected scripts sequentially.
7. Reporting the total execution time.

## 5. Execution Modes

The execution mode is configured in `Script_QGIS.py`:

- `MODE = "normal"`: executes scripts a1–a22 and performs the geometric characterization workflow.
- `MODE = "reset"`: executes scripts a23–a25 and performs cleanup/reset operations.

The default configuration is `MODE = "normal"`.

## 6. Input Data

The processing workflow uses the following input datasets:

- `edificio.shp`: cadastral building geometries.
- `division_altura.shp`: building subdivision and height information.
- `Edificios_XXX.csv`: additional cadastral attributes.
- `NDSM-EDIFICIOS-XXX.tif`: normalized digital surface model rasters.

All shapefile companion files must be preserved.

## 7. Main Outputs

The geometric characterization workflow generates intermediate and final datasets, including:

- `Parametros_Edificios.csv`
- `Parametros_Edificios_2.csv`

These files are subsequently used by the Python thermal characterization workflow.

## 8. Execution Notes

- Run `Script_QGIS.py` from the QGIS Python Console.
- Ensure that all input datasets are available before starting.
- Do not run cleanup/reset operations during normal processing.
- Preserve the original input data.
- Check the generated outputs before proceeding to the Python modelling stage.

## 9. Further Documentation

Detailed descriptions of individual processing scripts, their parameters, intermediate datasets and outputs will be documented as part of the methodological workflow.
