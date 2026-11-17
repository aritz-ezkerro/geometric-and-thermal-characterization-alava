# Introduction

## 1.1. Background

The residential building stock plays an important role in understanding energy consumption and assessing the energy performance of the built environment.

A detailed characterization of buildings requires information about their geometric properties, thermal characteristics and local climatic conditions.

This project presents a methodology to estimate these parameters using publicly available geospatial information, Geographic Information Systems (GIS) and predictive models developed in Python.

## 1.2. Project scope

The methodology focuses on the residential building stock of Álava (Spain).

It combines cadastral information, digital surface models and climatic data to derive building parameters and estimate annual heating energy demand.

The workflow is divided into two main stages:

- **Geometric characterization:** processing cadastral and geospatial data using QGIS.
- **Thermal characterization:** applying predictive models and climatic calculations using Python.

## 1.3. Methodological background

The methodology builds upon previous research conducted in Bizkaia, adapting the approach to the specific cadastral characteristics of Álava.

The processing workflow has been developed to obtain the geometric parameters required for subsequent thermal characterization.

## 1.4. Main objectives

The main objectives are:

- To characterize the geometry of residential buildings.
- To process cadastral and geospatial information.
- To estimate building thermal characteristics using predictive models.
- To calculate annual heating energy demand.
- To provide a reproducible workflow that can be applied to the residential building stock of Álava.

## 1.5. Workflow overview

The methodology follows these main steps:

1. Collection and preparation of cadastral information.
2. Preparation of digital surface models.
3. Geometric processing using QGIS.
4. Estimation of building thermal parameters using Python.
5. Calculation of heating degree days using climatic data.
6. Estimation of annual heating energy demand.
7. Export and analysis of the results.

## 1.6. Expected outputs

The methodology generates building-level information, including geometric parameters, predicted base temperatures, thermal parameters and estimated annual heating energy demand.

Detailed descriptions of the input data, processing scripts and generated outputs are provided in the following documentation sections.

