# Geometric and Thermal Characterization of the Residential Building Stock of Álava

## 1. Introduction

This repository presents a methodology for the geometric and thermal characterization of the residential building stock of Álava (Spain).

The methodology combines Geographic Information Systems (GIS), cadastral information, digital surface models, climatic data and predictive models developed in Python to characterize residential buildings and estimate their annual heating energy demand.

The workflow is divided into two main stages:

- **Geometric characterization:** processing cadastral and geospatial data using QGIS to obtain relevant building parameters.
- **Thermal characterization:** applying predictive models and climatic data in Python to estimate building thermal characteristics and annual heating energy demand.

The methodology builds on previous research conducted in Bizkaia and has been adapted to the specific cadastral characteristics of Álava.

## 2. Objectives

The main objectives are:

- To characterize the geometry of residential buildings using cadastral and geospatial information.
- To derive relevant building parameters through GIS-based processing.
- To estimate building thermal characteristics using predictive models.
- To calculate the estimated annual heating energy demand of residential buildings.
- To provide a reproducible methodology that can be applied to a wider geographical area.

## 3. Methodology

The methodology consists of two main stages:

1. **Geometric characterization using QGIS:** processing cadastral information and digital surface models to derive the geometric and physical parameters required for the analysis.
2. **Thermal characterization using Python:** applying predictive models and climatic data to estimate building base temperatures, Heating Degree Days (HDD) and annual heating energy demand.

## 4. Repository Structure

The repository is organized as follows:

```text
├── docs/          # Methodology documentation
├── qgis/          # QGIS processing scripts
├── python/        # Python scripts and predictive models
├── data/          # Input, intermediate and output data
├── examples/      # Example datasets and results
├── results/       # Maps, figures and tables
├── references/    # Bibliography and data sources
├── README.md
├── CHANGELOG.md
└── CITATION.cff
```

## 5. Software Requirements

The original methodology uses:

- QGIS 3.42.3
- Python 3.9
- Anaconda
- Spyder
- scikit-learn 0.24.2
- XGBoost 1.7
- joblib
- pandas
- xlsxwriter
- openpyxl

The specified versions are recommended to maintain compatibility with the original workflow.

## 6. Outputs

The methodology generates building-level geometric and thermal parameters, including:

- Building geometric and physical characteristics.
- Predicted building base temperatures.
- Heating Degree Days (HDD).
- Estimated annual heating energy demand, expressed in kWh.

The final results can be used for spatial analysis and characterization of the residential building stock.

## 7. Limitations

The applicability and computational performance of the methodology depend on the availability and quality of the input data, software compatibility, predictive model assumptions and the size of the study area.

