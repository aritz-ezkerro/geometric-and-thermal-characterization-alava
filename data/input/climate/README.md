# Climatic Input Data

This folder contains the climatic information required for the thermal characterization of residential buildings.

## Required File

The Python workflow reads the following Excel file:

`ArchivoClimatico.xlsx`

## Main Variable

The file must contain the outdoor temperature variable:

`OutTemp`

This variable is used to calculate Heating Degree Days (HDD) for each building, based on its predicted base temperature.

## Data Preparation

Before running the Python workflow:

- Use the exact filename `ArchivoClimatico.xlsx`.
- Ensure that the `OutTemp` column is available.
- Check the temperature units and temporal resolution.
- Preserve the original climatic dataset.

The complete data structure and original climatic data source will be documented after reviewing the file and the Python script.
