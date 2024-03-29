CREATE OR REPLACE VIEW `analytics-scfinance-thd.TEMP_1DAY.V_A_TABLE_VIEW` (
    -- NAME OPTIONS(description="Field 1")
    FIELD_1  OPTIONS(description="Field 1"),
    -- NAME OPTIONS(description="Field 2")
    FIELD_2 OPTIONS(description="Field 2"),
    -- NAME OPTIONS(description="Field 3")
    FIELD_3  OPTIONS(description="Field 3"),
    -- NAME OPTIONS(description="Field 4")
    FIELD_4  OPTIONS(description="Field 4"),
    -- NAME OPTIONS(description="Field 5")
    FIELD_5  OPTIONS(description="Field 5"),
    -- NAME OPTIONS(description="Field 6")
    FIELD_6  OPTIONS(description="Field 6"),
    -- NAME OPTIONS(description="Field 7")
    FIELD_7  OPTIONS(description="Field 7")

    ) 
    /*
    TABLE OPTIONS (VIEWS ARE A SUBSET OF TABLES)
    1. LABELS -- PROVIDES A LABEL FOR THE PROJECT. THIS METADATA ALLOWS FOR EASY FILTERING OF RESOURCES BASED ON LABELS.
    2. DESCRIPTION -- PROVIDES A DESCRIPTION FOR THE TABLE.
*/
    OPTIONS(
        labels=[("project", "training"), ("example","view")],
        description="A view of A Table"
    )
    AS
    SELECT 
        FIELD_1,
        FIELD_2,
        FIELD_3,
        FIELD_4,
        FIELD_5,
        FIELD_6,
        FIELD_7
    FROM `analytics-scfinance-thd.TEMP_1DAY.A_TABLE`
   
    WHERE 1=1;

     