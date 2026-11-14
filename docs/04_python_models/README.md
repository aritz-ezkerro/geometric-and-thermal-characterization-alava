# 4. Thermal Characterization Using Python

## 4.1. Overview

The thermal characterization stage uses Python to estimate the thermal properties and annual heating energy demand of residential buildings.

It combines the geometric and physical parameters generated during the QGIS processing stage with predictive models and climatic data.

## 4.2. Software Requirements

The original workflow uses the following software and libraries:

- Anaconda
- Python 3.9
- Spyder
- scikit-learn 0.24.2
- XGBoost 1.7
- joblib
- pandas
- xlsxwriter
- openpyxl

The specified versions are recommended to maintain compatibility with the original scripts and trained model.

## 4.3. Input Data

The Python workflow requires:

- `Parametros_Edificios.csv`: building parameters generated during QGIS processing.
- `Parametros_Edificios_2.csv`: additional geometric and physical parameters.
- `ArchivoClimatico.xlsx`: climatic data containing the `OutTemp` variable.
- `modelo_TB.pkl`: previously trained predictive model.

These files must be available in the folders selected when executing the Python script.

## 4.4. Predictive Modelling

The workflow loads the trained model using the `joblib` library.

The model predicts the building base temperature using the parameters generated during the QGIS stage.

The predictions are exported to:

`Parametros_Edificios_TB.csv`

## 4.5. Heating Degree Days Calculation

The predicted building base temperatures are combined with outdoor temperature data (`OutTemp`) to calculate Heating Degree Days (HDD).

The workflow calculates HDD for each building and exports the resulting values to:

`Parametros_TB_HDD.xlsx`

## 4.6. Annual Heating Energy Demand

The final stage combines the HDD values with the building thermal parameter:

`UA + ρVcp (kW/K)`

The methodology uses these values to estimate annual heating energy demand.

The final results are exported to:

`Predicciones_Edificios.xlsx`

The output includes the building identifier, predicted base temperature, thermal parameter, HDD and estimated heating demand.

## 4.7. Execution Notes

The Python processing script is executed in Spyder.

Before running the workflow, verify that:

- The required input files are available.
- The trained model is in the correct folder.
- The Python environment contains the required dependencies.
- The input filenames match those expected by the script.

Detailed explanations of the model, equations, data units and script parameters will be added after reviewing the original Python code.
