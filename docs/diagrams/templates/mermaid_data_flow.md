# data_flow_diagram

| Type           | Description                                  | Color       |
|----------------|----------------------------------------------|-------------|
| Process Nodes  | Nodes that represent processing steps       | 🟩 Green     |
| Custom Type 1  | Description for custom type 1 (e.g., Input) | 🟧 Orange    |
| Data Stored    | Nodes that represent data storage           | 🟨 Yellow    |
| Custom Type 3  | Description for custom type 3 (e.g., Flow)  | 🟦 Blue      |
| Analysis Nodes | Nodes that represent analysis operations    | 🟥 Red       |
| Custom Type 2  | Description for custom type 2 (e.g., Output)| 🟪 Purple    |

```mermaid
graph BT;
%%%% Define Nodes

collect(Data Collection):::process
actuals_raw[Raw Actuals Data]:::data_stored
subgraph initial_processing [Initial Processing]
    preprocess(Preprocessing):::process
    transform(Data Transformation):::process
end

train(Model Training):::process

prediction[Future Predictions]:::data_stored
actuals_analysis[Analysis Actuals Data]:::data_stored
reporting_actuals_data[Reporting Actuals Data]:::data_stored
reporting_data[Full Reporting Data]:::data_stored
analytics_data[Full Analytics Data]:::data_stored
subgraph insights [Insights]
    analyze_adhoc[Adhoc Analysis]:::analysis
    reporting_analytics[Analytics Reporting]:::reporting
    reporting_full[Full Report]:::reporting
end

%%%% Define connections
collect --> actuals_raw
actuals_raw --> preprocess
preprocess --> transform
transform --> actuals_analysis
actuals_analysis --> train
actuals_analysis --> reporting_actuals_data
reporting_actuals_data --> reporting_data
train --> prediction
prediction --> analytics_data
actuals_analysis --> analytics_data
analytics_data --> analyze_adhoc
analytics_data --> reporting_analytics
prediction --> reporting_data
reporting_data --> reporting_full

%%%% Define the styling for the diagram
classDef default fill:#C2C2C2,stroke:#333,stroke-width:2px,color:black,font-weight:bold;
%%%%
classDef data_interim fill:#F97316,stroke:#333,stroke-width:2px,color:black;
classDef data_stored fill:#FCDC3B,stroke:#333,stroke-width:2px,color:black;
classDef process fill:#3FBF3F,stroke:#333,stroke-width:2px,color:black;
classDef reporting fill:#60A5FA,stroke:#333,stroke-width:2px,color:black;
classDef analysis fill:#F93822,stroke:#333,stroke-width:2px,color:black;
```
