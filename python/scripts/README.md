# Python Processing Scripts

This folder contains the Python scripts used for the thermal characterization of the residential building stock of Álava.

## Workflow

The Python workflow uses the geometric and physical parameters generated in QGIS, together with climatic data and trained predictive models, to estimate building base temperatures and annual heating energy demand.

## Main Script

The main processing script is:

`Script_SPYDER.py`

It is executed using Spyder within the configured Python environment.

The script performs the following operations:

- Loads the trained predictive model from `modelo_TB.pkl`.
- Predicts the base temperature of each building.
- Calculates Heating Degree Days (HDD) using the climatic data in `ArchivoClimatico.xlsx`.
- Estimates the annual heating energy demand of each building.

## Requirements

The original methodology uses:

- Python 3.9
- scikit-learn 0.24.2
- XGBoost 1.7
- joblib
- pandas
- numpy
- PyQt5
- xlsxwriter
- openpyxl

See `python/requirements.txt` for the dependency list.

## Outputs

The workflow generates:

- `Parametros_Edificios_TB.csv`
- `Parametros_TB_HDD.xlsx`
- `Predicciones_Edificios.xlsx`

These files contain the predicted base temperatures, calculated Heating Degree Days and estimated annual heating energy demand.

## Notes

- The original trained model and input datasets should be preserved without modification.
- The two geometric parameter datasets must correspond to the same buildings.
- The climate data must have the expected temporal resolution.
- The original scripts should be preserved and documented to ensure reproducibility.
