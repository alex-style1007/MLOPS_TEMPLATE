.. Documentation_MLOPS documentation master file, created by
   sphinx-quickstart on Wed Sep 11 12:02:24 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation_MLOPS
=================================
.. _introduction:

Introduction
============

Welcome to the documentation for the **{{cookiecutter.Project_name}}** project, developed under the Team Data Science Process (TDSP) methodology with a particular focus on data engineering using the Medallion methodology.

TDSP Methodology
----------------

The project follows the **TDSP** (Team Data Science Process) methodology, a structured approach to developing data science solutions that spans from initial planning to implementation and monitoring. TDSP facilitates collaboration between teams and ensures that all aspects of the data science process are managed effectively.

Medallion Methodology in Data Engineering
------------------------------------------

For data engineering, we have applied the Medallion methodology (`Medallion Architecture <https://www.databricks.com/glossary/medallion-architecture>`_). This methodology organizes data into a system of hierarchical layers (Bronze, Silver, and Gold) to improve data quality, accessibility, and usability:

- **Bronze**: Raw and unprocessed data. This layer is used to store information in its original format.
- **Silver**: Refined and cleaned data. In this layer, data is transformed and enriched to prepare it for analysis.
- **Gold**: Analytical and prepared data. The final layer is used for data that is ready for consumption and advanced analysis.

Contents
--------

In this documentation, you will find detailed information about:

- The TDSP methodology and its application in the project.
- The structure and workflow of the Medallion methodology.
- Technical details and processes used in data engineering.
- Project results and analysis.

We hope that this documentation provides a clear insight into the process and results of our work.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   README.md
   {{cookiecutter.Business_Understanding}}/index.rst

