# 5. Results and Outputs

## 5.1. Overview

The methodology produces a set of geometric, physical and thermal parameters for the residential building stock of Álava.

The results are generated through two main stages:

1. Geometric characterization using QGIS.
2. Thermal characterization and energy demand estimation using Python.

## 5.2. Geometric Characterization Outputs

The QGIS processing workflow generates building-level datasets containing the geometric and physical parameters required by the predictive models.

The main output files are:

- `Parametros_Edificios.csv`
- `Parametros_Edificios_2.csv`

These datasets are used as inputs for the Python workflow.

## 5.3. Thermal Characterization Outputs

The Python workflow generates the following main files:

| File | Description |
|---|---|
| `Parametros_Edificios_TB.csv` | Predicted building base temperatures. |
| `Parametros_TB_HDD.xlsx` | Heating Degree Days calculated for each building. |
| `Predicciones_Edificios.xlsx` | Final estimated annual heating energy demand. |

## 5.4. Main Result Variables

The final prediction dataset includes the following variables:

| Variable | Description |
|---|---|
| `CodEdifici` | Unique building identifier. |
| `TB Model Prediction (ºC)` | Predicted building base temperature. |
| `UA + ρVcp (kW/K)` | Building thermal parameter. |
| `HDD (ºC·days)` | Heating Degree Days. |
| `Prediction (kWh)` | Estimated annual heating energy demand. |

## 5.5. Interpretation of Results

The results provide an estimate of the annual heating energy demand associated with each building.

They can be used to analyse the geometric and thermal characteristics of the residential building stock and to support spatial assessments at different territorial scales.

The results should be interpreted in accordance with the assumptions, input data quality and limitations of the methodology.

## 5.6. Future Result Visualization

Maps, figures and statistical summaries can be added to this section as the results are generated and validated.

Potential outputs include:

- Spatial distribution of estimated heating energy demand.
- Comparison of building characteristics across municipalities.
- Statistical summaries of predicted thermal parameters.
- Identification of spatial patterns in the residential building stock.
