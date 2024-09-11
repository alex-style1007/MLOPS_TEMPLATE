# What is TDSP?

TDSP is an agile, iterative data science methodology that you can use to efficiently deliver predictive analytics solutions and AI applications. TDSP improves team collaboration and learning by recommending optimal ways for team roles to work together. TDSP incorporates best practices and frameworks from Microsoft and other industry leaders to help your team effectively implement data science initiatives. TDSP enables you to reap the benefits of your data science program.

## Data Science Life Cycle

The TDSP provides a lifecycle that you can use to structure the development of your data science projects.The TDSP lifecycle consists of five main phases that the team executes iteratively. These phases include:

1. Business awareness
2. Data acquisition and understanding
3. Modeling
4. Implementation
5. Customer acceptance

![Ciclo_de_vida](https://learn.microsoft.com/es-es/azure/architecture/data-science-process/media/lifecycle/tdsp-lifecycle2.png)

The following diagram shows the tasks (in blue) and artifacts (in green) corresponding to each phase of the lifecycle (shown on the horizontal axis) and for the roles (shown on the vertical axis).

![Roles](https://learn.microsoft.com/es-es/azure/architecture/data-science-process/media/overview/tdsp-tasks-by-roles.png)


# What is a medallion architecture?

A medallion architecture is a data design pattern used to logically organize data in a lakehouse, with the goal of incrementally and progressively improving the structure and quality of data as it flows through each layer of the architecture (from Bronze ⇒ Silver ⇒ Gold layer tables). Medallion architectures are sometimes also referred to as "multi-hop" architectures.

![Architecture](https://www.databricks.com/sites/default/files/inline-images/building-data-pipelines-with-delta-lake-120823.png?v=1702318922)

## Bronze layer (raw data)

The Bronze layer is where we land all the data from external source systems. The table structures in this layer correspond to the source system table structures "as-is," along with any additional metadata columns that capture the load date/time, process ID, etc. The focus in this layer is quick Change Data Capture and the ability to provide an historical archive of source (cold storage), data lineage, auditability, reprocessing if needed without rereading the data from the source system.

## Silver layer (cleansed and conformed data)

In the Silver layer of the lakehouse, the data from the Bronze layer is matched, merged, conformed and cleansed ("just-enough") so that the Silver layer can provide an "Enterprise view" of all its key business entities, concepts and transactions. (e.g. master customers, stores, non-duplicated transactions and cross-reference tables).

The Silver layer brings the data from different sources into an Enterprise view and enables self-service analytics for ad-hoc reporting, advanced analytics and ML. It serves as a source for Departmental Analysts, Data Engineers and Data Scientists to further create projects and analysis to answer business problems via enterprise and departmental data projects in the Gold Layer.

In the lakehouse data engineering paradigm, typically the ELT methodology is followed vs. ETL - which means only minimal or "just-enough" transformations and data cleansing rules are applied while loading the Silver layer. Speed and agility to ingest and deliver the data in the data lake is prioritized, and a lot of project-specific complex transformations and business rules are applied while loading the data from the Silver to Gold layer. From a data modeling perspective, the Silver Layer has more 3rd-Normal Form like data models. Data Vault-like, write-performant data models can be used in this layer.

## Gold layer (curated business-level tables)

Data in the Gold layer of the lakehouse is typically organized in consumption-ready "project-specific" databases. The Gold layer is for reporting and uses more de-normalized and read-optimized data models with fewer joins. The final layer of data transformations and data quality rules are applied here. Final presentation layer of projects such as Customer Analytics, Product Quality Analytics, Inventory Analytics, Customer Segmentation, Product Recommendations, Marking/Sales Analytics etc. fit in this layer. We see a lot of Kimball style star schema-based data models or Inmon style Data marts fit in this Gold Layer of the lakehouse.

So you can see that the data is curated as it moves through the different layers of a lakehouse. In some cases, we also see that lot of Data Marts and EDWs from the traditional RDBMS technology stack are ingested into the lakehouse, so that for the first time Enterprises can do "pan-EDW" advanced analytics and ML - which was just not possible or too cost prohibitive to do on a traditional stack. (e.g. IoT/Manufacturing data is tied with Sales and Marketing data for defect analysis or health care genomics, EMR/HL7 clinical data markets are tied with financial claims data to create a Healthcare Data Lake for timely and improved patient care analytics.

### References

1. [Documentation of TDSP](https://learn.microsoft.com/es-es/azure/architecture/data-science-process/overview)-What is TDSP?
2.[Documentation of Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)-What is a medallion architecture?


