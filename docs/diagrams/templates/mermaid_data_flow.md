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
graph LR;
%%%% Define Nodes
subgraph initial_processing [Initial Processing]
    collect(Data Collection):::process
    preprocess(Preprocessing):::process
    transform(Data Transformation):::process
end

train(Model Training):::process
predict(Make Predictions):::process
analysis_data[Analysis Dataset]:::data_stored

subgraph insights [Insights]
    analyze_adhoc[Adhoc Analysis]:::analysis
    report[Analysis Report]:::reporting
end

%%%% Define connections
collect --> preprocess
preprocess --> transform;
transform --> analysis_data;
analysis_data --> analyze_adhoc;
analysis_data --> train;
analysis_data --> report;
train --> predict;

%%%% Define the styling for the diagram
classDef default fill:#C2C2C2,stroke:#333,stroke-width:2px,color:black,font-weight:bold;
%%%%
classDef data_interim fill:#F97316,stroke:#333,stroke-width:2px,color:black;
classDef data_stored fill:#FCDC3B,stroke:#333,stroke-width:2px,color:black;
classDef process fill:#3FBF3F,stroke:#333,stroke-width:2px,color:black;
classDef reporting fill:#60A5FA,stroke:#333,stroke-width:2px,color:black;
classDef analysis fill:#F93822,stroke:#333,stroke-width:2px,color:black;
```
