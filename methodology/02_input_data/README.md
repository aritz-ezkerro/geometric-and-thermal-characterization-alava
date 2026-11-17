# Input Data

## 2.1. Overview

The geometric and thermal characterization methodology requires three main types of input data:

- Cadastral information.
- Digital surface models.
- Climatic data.

These datasets are used to derive the geometric characteristics of buildings and estimate their thermal performance and annual heating energy demand.

All input files must be prepared according to the naming conventions and formats expected by the QGIS and Python scripts.

## 2.2. Cadastral Data

### 2.2.1. Data Source

Cadastral information is obtained from the Álava Cadastre.

The methodology uses cadastral vector information and associated attribute tables to identify buildings and their internal divisions.

### 2.2.2. Required Files

The following files are required:

| File | Description |
|---|---|
| `edificio.shp` | Building geometries. |
| `division_altura.shp` | Geometries representing building divisions by height. |
| `Edificios_XXX.csv` | Attribute table associated with the cadastral buildings. |

The `XXX` suffix identifies the corresponding municipality or dataset, following the naming convention expected by the scripts.

### 2.2.3. File Preparation

The cadastral layers must be placed in the input data folder.

When using ESRI Shapefiles, all associated files must be kept together. These may include:

- `.shp`: geometric information.
- `.shx`: geometry index.
- `.dbf`: attribute table.
- `.prj`: coordinate reference system information.

Other associated files should also be preserved when present.

The methodology allows the use of cadastral information from different municipalities. These datasets can be combined or filtered to define the study area, provided that the resulting files maintain consistent identifiers and coordinate reference systems.

## 2.3. Digital Surface Models

### 2.3.1. Data Source

The methodology uses digital surface model information from the MDSnE2 2.5 second coverage provided by the National Geographic Information Centre of Spain (CNIG).

These raster datasets provide surface elevation information required for the geometric characterization of buildings.

### 2.3.2. Required Files

The input raster files must follow this naming convention:

`NDSM-EDIFICIOS-XXX.tif`

Multiple raster files can be supplied when the study area covers more than one raster tile.

### 2.3.3. File Preparation

The raster files must be placed in the corresponding input folder.

During QGIS processing, the methodology combines the required raster information according to the geographical extent of the building layer (`edificio.shp`).

The resulting surface model is used in subsequent geometric processing operations.

## 2.4. Climatic Data

### 2.4.1. Purpose

Climatic data are required for the thermal characterization of buildings and the estimation of annual heating energy demand.

The Python workflow uses outdoor temperature data (`OutTemp`) to calculate Heating Degree Days (HDD) based on the predicted building base temperature.

The resulting HDD values are subsequently combined with the thermal parameters of each building to estimate annual heating energy demand.

### 2.4.2. Required File

The required climatic input file is:

`ArchivoClimatico.xlsx`

The file is read by the Python processing script using Excel format.

It must contain the outdoor temperature information required for the HDD calculation, including the `OutTemp` variable.

### 2.4.3. Data Preparation

Before running the Python workflow, ensure that:

- The file is named exactly `ArchivoClimatico.xlsx`.
- The file is stored in the climatic input data folder.
- The `OutTemp` column is available.
- The temperature values use the units and temporal structure expected by the Python script.

The complete column structure, temperature units, temporal resolution and original climatic data source should be documented after verification against the script and the original dataset.

## 2.5. Input Data Organization

The input datasets should be organized as follows:

```text
data/
└── input/
    ├── cadastral/
    │   ├── edificio.shp
    │   ├── edificio.shx
    │   ├── edificio.dbf
    │   ├── edificio.prj
    │   ├── division_altura.shp
    │   ├── division_altura.shx
    │   ├── division_altura.dbf
    │   ├── division_altura.prj
    │   └── Edificios_XXX.csv
    │
    ├── surface_models/
    │   └── NDSM-EDIFICIOS-XXX.tif
    │
    └── climate/
        └── ArchivoClimatico.xlsx
```

The climate filename shown above is provisional and must be checked against the actual script.

## 2.6. Data Preparation Considerations

Before starting the processing workflow, the following aspects should be checked:

1. All required input files are available.
2. File names follow the conventions expected by the scripts.
3. Shapefile components are stored together.
4. Cadastral datasets cover the intended study area.
5. Digital surface model rasters provide sufficient spatial coverage.
6. The climatic dataset has the structure expected by the Python script.
7. The input data are accessible from the folders selected during execution.

## 2.7. Data Licensing and Availability

The methodology uses information obtained from external public data providers.

Before redistributing input datasets through this repository, users should check the applicable terms of use, attribution requirements and redistribution conditions of each source.

In particular, the availability of cadastral information and digital surface models does not automatically mean that all downloaded files can be redistributed freely.

Where redistribution is not permitted or practical, this repository should provide information about the original data source and instructions for obtaining the required datasets instead of including restricted copies.

Large raster datasets and complete cadastral datasets should generally not be uploaded directly to GitHub. Small example datasets may be provided when their use and redistribution are permitted.

## 2.8. Summary

The methodology requires cadastral vector data, digital surface model rasters and climatic information.

Correct file preparation and naming are essential for the QGIS and Python scripts to execute successfully.

The exact climatic file format and structure remain to be verified against the current version of the Python workflow.
