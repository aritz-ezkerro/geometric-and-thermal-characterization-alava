# 7. Methodology Validation Checklist

## 7.1. Input Data Validation

- [ ] Confirm that all required input datasets are available.
- [ ] Verify that filenames match those expected by the processing scripts.
- [ ] Check that all shapefile companion files are present.
- [ ] Verify the coordinate reference systems of the spatial datasets.
- [ ] Confirm that the digital surface model rasters cover the study area.
- [ ] Check the structure and variables of `ArchivoClimatico.xlsx`, including the `OutTemp` column.

## 7.2. QGIS Processing Validation

- [ ] Confirm compatibility with QGIS 3.42.3.
- [ ] Verify that all processing scripts are available.
- [ ] Confirm that `Script_QGIS.py` executes the processing workflow correctly.
- [ ] Check that building identifiers (`CodEdifici`) are generated consistently.
- [ ] Verify the geometric and physical parameters generated during processing.
- [ ] Confirm that the following output files are created:
  - `Parametros_Edificios.csv`
  - `Parametros_Edificios_2.csv`

## 7.3. Python Environment Validation

- [ ] Confirm that Python 3.9 is available.
- [ ] Install the required Python libraries.
- [ ] Verify compatibility of scikit-learn and XGBoost with the trained model.
- [ ] Confirm that `Script_SPYDER.py` executes without errors.
- [ ] Verify that `modelo_TB.pkl` can be loaded correctly.

## 7.4. Thermal Modelling Validation

- [ ] Confirm that the geometric parameters are correctly imported.
- [ ] Verify that the predictive model generates building base temperature estimates.
- [ ] Check that the climate dataset is read correctly.
- [ ] Verify the calculation of Heating Degree Days (HDD).
- [ ] Confirm that the thermal parameters and HDD are combined using the intended calculation.
- [ ] Check the units and interpretation of the resulting energy demand estimates.

## 7.5. Final Output Validation

- [ ] Confirm that the expected output files are generated.
- [ ] Verify that building identifiers remain consistent across processing stages.
- [ ] Check for missing or duplicated building records.
- [ ] Identify missing, invalid or implausible predicted values.
- [ ] Confirm that annual heating energy demand is expressed in kWh.
- [ ] Verify that the results can be linked to the corresponding building geometries in QGIS.

## 7.6. Reproducibility

- [ ] Document the software versions and dependencies.
- [ ] Record the input datasets and their sources.
- [ ] Document any modifications to the original scripts.
- [ ] Record relevant processing parameters and assumptions.
- [ ] Preserve the original input data and trained model.
- [ ] Document known limitations and potential sources of uncertainty.

## 7.7. Validation Status

The checklist will be progressively completed as the methodology is tested and reviewed.

A completed checklist should indicate that the corresponding procedure has been tested, not simply that its documentation is available.
