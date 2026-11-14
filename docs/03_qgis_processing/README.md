# 3. Geometric Characterization Using QGIS

## 3.1. Overview

The geometric characterization stage uses Geographic Information Systems (GIS) to process cadastral information and digital surface models.

The objective is to derive the geometric and physical parameters required for the subsequent thermal characterization of residential buildings.

The processing workflow is implemented in QGIS using a set of Python scripts.

## 3.2. Software Requirements

The original methodology was developed using:

- QGIS 3.42.3
- Python integrated into the QGIS environment

Using the specified QGIS version is recommended to reduce potential compatibility issues.

## 3.3. Input Data

The QGIS workflow requires the following datasets:

- `edificio.shp`: cadastral building geometries.
- `division_altura.shp`: cadastral information describing building divisions and heights.
- `Edificios_XXX.csv`: additional cadastral attributes.
- `NDSM-EDIFICIOS-XXX.tif`: digital surface model data.

All input files must be stored in the corresponding input folders and retain the filenames expected by the scripts.

## 3.4. Processing Workflow

The geometric characterization workflow consists of several processing stages:

1. **Data preparation:** removal of previously loaded layers and temporary files.
2. **Geometry correction:** correction of building geometries and preparation of raster data.
3. **Raster integration:** combination of the available digital surface model tiles.
4. **Building identification:** creation of a unique building identifier (`CodEdifici`).
5. **Spatial processing:** generation of centroids and spatial association between building divisions and building geometries.
6. **Attribute processing:** integration of cadastral attributes and calculation of additional parameters.

The processing scripts are executed sequentially through the QGIS Python console.

## 3.5. Main Outputs

The QGIS workflow generates intermediate datasets and building-level parameters for the Python modelling stage.

The main outputs include:

- `Parametros_Edificios.csv`
- `Parametros_Edificios_2.csv`

These files contain geometric and physical information used as input for the subsequent thermal characterization.

## 3.6. Execution Notes

Before starting a new processing run, check that the input data are correctly organized and that previous intermediate files will not interfere with the new execution.

The original methodology includes scripts to remove temporary and modified files before restarting the workflow.

Large study areas may require substantial computational resources. Processing the territory in smaller sections may help manage these limitations.

## 3.7. Further Documentation

Detailed descriptions of the individual processing scripts, their parameters and their outputs will be added as the workflow is reviewed and documented.
