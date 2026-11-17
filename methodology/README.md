# Methodology

This directory contains the detailed methodology developed for the geometric and thermal characterization of residential buildings in Álava. The complete workflow is organized into separate folders, each dedicated to a specific methodological stage or processing procedure.

Each folder provides its own documentation (`README.md`), describing the corresponding methodology, input datasets, processing steps, scripts, software requirements, and expected outputs.

The purpose of this structure is to ensure that each stage of the workflow can be understood, executed, reviewed, and validated independently, while maintaining consistency with the overall geometric and thermal characterization process.

## Methodological Structure

The methodology is divided into different folders according to the procedures implemented in the project.

Each folder contains the documentation and resources associated with its corresponding stage. The individual README files provide detailed explanations of the procedures and should be consulted to understand the specific operations performed at each stage.

The folders are intended to cover the different components of the workflow, from the preparation and processing of input datasets to the generation of geometric parameters, thermal modelling, and final energy demand estimation.

## Folder Documentation

The methodological procedures are documented independently within their respective folders.

For each procedure, the corresponding documentation should describe:

- **Objective:** The purpose and role of the procedure within the overall methodology.
- **Input data:** Required datasets, their sources, formats, and relevant characteristics.
- **Processing workflow:** The operations and steps performed, including their execution order.
- **Scripts and tools:** Software, libraries, scripts, and computational resources required.
- **Parameters and assumptions:** Relevant settings, equations, criteria, and methodological assumptions.
- **Output data:** Generated files, variables, formats, and their intended use in subsequent stages.
- **Validation:** Checks required to verify the correct execution and reliability of the procedure.

The individual README files should be considered the primary reference for the technical details of each methodological stage.

## Methodology Validation

The implementation and reliability of the complete workflow are assessed through the **Methodology Validation Checklist** (Section 7).

This checklist covers input data validation, QGIS processing, Python environment configuration, thermal modelling, final output verification, and reproducibility.

Each procedure must be tested and reviewed before being considered validated. The availability of documentation alone does not imply that a procedure has been successfully tested.

Validation status should be updated progressively as the different methodological stages are executed and reviewed.

## Reproducibility and Traceability

The folder-based organization is intended to facilitate:

- Independent execution and verification of individual procedures.
- Traceability between input datasets, processing operations, and final outputs.
- Identification of dependencies between methodological stages.
- Consistent documentation of software versions, scripts, and processing parameters.
- Reproduction and review of the complete geometric and thermal characterization workflow.

For a complete understanding of the methodology, users should consult the README file in each individual folder, following the processing sequence and considering the dependencies between procedures.

