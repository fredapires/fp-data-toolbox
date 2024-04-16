## Datavault modeling

I want to build a dataware house in GBQ with 'dbt' as the main orchestrator of transformations. I need a diagram that outlines the flow of data from source to final analytics / business insights. This should follow data modeling best practices and would help me to orient myself with the data pipeline.

Here are the steps that each data set should go through between data source and final analytics / business insights:

1. Loading data from 2-3 sources into a GCP storage bucket
2. Copying data from the storage bucket to a raw staging area in GBQ
3. transform the raw staging data into clean staging data in GBQ
4. transform the clean staging data into a normalized data warehouse format (star / snowflake schema)
5. transform the normalized data warehouse into a denormalized data format for various one-big-table servings of data to analytics users

Please help me with an initial iteration of a mermaid diagram that outlines the flow of data for this data model.

```mermaid
graph LR
    DS1[Data Sources] -->|Loading| GSB(
        GCP Storage Bucket
        Data Lake
        )
    DS2[Data Sources] -->|Loading| GSB
    DS3[Data Sources] -->|Loading| GSB
    subgraph SG1 [Google Cloud Platform]
        GSB -->|Copying| RSA(Raw Staging)
        subgraph SG2 [Google BigQuery]
            RSA -->|Data Cleaning| CSD(Clean Staging Data)
            CSD -->|Data Normalization| NDW(Data Warehouse)
            NDW -->|Denormalization| DDA(Denormalized Data for Analytics)
        end
    end
    DDA --> XLA[Excel Analytics]
    DDA --> LSVIZ[Looker Studio Visualizations]
    DDA --> QVIZ[Qlik Visualizations]
    CSD ---->|Data Validity Checks| QAR(Quality Assurance Reporting)
    NDW ---->|Data Validity Checks| QAR

    %% classDef source fill:#f9f,stroke:#333,stroke-width:2px;
    %% classDef storage fill:#bbf,stroke:#333,stroke-width:2px;
    %% classDef process fill:#fdfd96,stroke:#333,stroke-width:2px;
    %% classDef insights fill:#fbb,stroke:#333,stroke-width:2px;

    class DS source;
    class GSB storage;
    class RSA,CSD,NDW,DDA process;
    class BI insights;
```