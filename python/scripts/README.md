# Python Processing Scripts

This folder contains the Python scripts used for the thermal characterization of the residential building stock of Álava.

## Workflow

The Python workflow uses the geometric and physical parameters generated in QGIS, together with climatic data and trained predictive models, to estimate building base temperatures and annual heating energy demand.

## Main Script

The main processing script is:

`Script_SPYDER.py`

It is executed using Spyder within the configured Python environment.

## Requirements

The original methodology uses:

- Python 3.9
- scikit-learn 0.24.2
- XGBoost 1.7
- joblib
- pandas
- xlsxwriter
- openpyxl

## Outputs

The workflow generates building-level thermal parameters, Heating Degree Days (HDD) and estimated annual heating energy demand.

## Notes

The original scripts will be added after reviewing their contents and confirming their dependencies.
