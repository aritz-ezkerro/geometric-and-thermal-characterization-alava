# 6. Limitations and Recommendations

## 6.1. Overview

The methodology provides a systematic approach to the geometric and thermal characterization of the residential building stock of Álava.

However, the reliability of the results depends on the quality of the input datasets, the compatibility of the software environment and the assumptions used by the predictive models.

## 6.2. Input Data Limitations

The methodology relies on cadastral information, digital surface models and climatic data.

Potential limitations include:

- Incomplete or outdated cadastral information.
- Missing or inconsistent building attributes.
- Differences in spatial resolution or coverage between raster datasets.
- Errors or inconsistencies in building geometries.
- Limitations in the temporal coverage or representativeness of climatic data.

Input datasets should be checked before processing.

## 6.3. Software and Computational Limitations

The original workflow was developed using specific software versions and Python libraries.

Changes in software versions may cause compatibility issues, particularly when loading previously trained predictive models.

The QGIS processing stage can also require significant computational resources when working with large study areas.

For large datasets, processing the territory in smaller sections may help reduce memory requirements and improve workflow management.

## 6.4. Predictive Model Limitations

The thermal characterization relies on previously trained predictive models.

Their performance depends on the representativeness of the training data and the similarity between the original study context and the residential building stock of Álava.

Predicted values should therefore be interpreted as model-based estimates rather than direct measurements of building performance.

Model validation and uncertainty assessment should be considered when interpreting the results.

## 6.5. Recommendations

The following recommendations are proposed:

- Verify all input datasets before starting the workflow.
- Preserve the original input files.
- Use the recommended software versions.
- Keep intermediate and final outputs clearly organized.
- Document any changes made to the original scripts.
- Validate predictions against independent information whenever possible.
- Record the limitations and assumptions associated with each analysis.

## 6.6. Future Improvements

Future development of the methodology could include:

- More detailed documentation of individual processing scripts.
- Additional validation of predictive model performance.
- Assessment of uncertainty in the estimated heating energy demand.
- Integration of updated cadastral and climatic datasets.
- Improved automation and computational efficiency.
- Extension of the methodology to other territorial contexts.
