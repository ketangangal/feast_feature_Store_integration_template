from datetime import timedelta
from feast import Entity, FeatureService, Field, FileSource, ValueType, FeatureView
from feast.types import Float32, Int64, String

caseid = Entity(name="case_id", value_type=ValueType.STRING, description="Case id for visa")

feature_source = FileSource(path=f"data/features.parquet", timestamp_field ="event_timestamp")
 
target_source = FileSource(path=f"data/target.parquet", timestamp_field ="event_timestamp")

feature_view = FeatureView(name="features",
    ttl=timedelta(seconds=86400*2),
    entities=[caseid],
    schema=[
        Field(name="continent_Africa", dtype=Int64),
        Field(name="continent_Asia", dtype=Int64),
        Field(name="continent_Europe", dtype=Int64),
        Field(name="continent_North America", dtype=Int64),
        Field(name="continent_Oceania", dtype=Int64),
        Field(name="continent_South America", dtype=Int64),
        Field(name="unit_of_wage_Hour", dtype=Int64),
        Field(name="unit_of_wage_Month", dtype=Int64),
        Field(name="unit_of_wage_Week", dtype=Int64),
        Field(name="unit_of_wage_Year", dtype=Int64),
        Field(name="region_of_employment_Island", dtype=Int64),
        Field(name="region_of_employment_Midwest", dtype=Int64),
        Field(name="region_of_employment_Northeast", dtype=Int64),
        Field(name="region_of_employment_South", dtype=Int64),
        Field(name="region_of_employment_West", dtype=Int64),
        Field(name="has_job_experience", dtype=Int64),
        Field(name="requires_job_training", dtype=Int64),
        Field(name="full_time_position", dtype=Int64),
        Field(name="education_of_employee", dtype=Int64),
        Field(name="no_of_employees", dtype=Float32),
        Field(name="company_age", dtype=Float32),
        Field(name="prevailing_wage", dtype=Float32)
    ],
    source=feature_source,
    online=True)


target_view = FeatureView(name="target",
    ttl=timedelta(seconds=86400*2),
    entities=[caseid],
    schema=[
        Field(name="case_status", dtype=String)
    ],
    source=target_source,
    online=True)

## Feature Service
features_service_1 = FeatureService(
    name="features_service_1",
    features=[
        feature_view
    ],
)


## Experimental
exp_feature_source = FileSource(path=f"data/features_exp.parquet", timestamp_field ="event_timestamp")
 
exp_target_source = FileSource(path=f"data/target_exp.parquet", timestamp_field ="event_timestamp")


exp_feature_view = FeatureView(name="exp_features",
    ttl=timedelta(seconds = 10000),
    entities=[caseid],
    schema=[
        Field(name="continent_Africa", dtype=Int64),
        Field(name="continent_Asia", dtype=Int64),
        Field(name="continent_Europe", dtype=Int64),
        Field(name="continent_North America", dtype=Int64),
        Field(name="continent_Oceania", dtype=Int64),
        Field(name="continent_South America", dtype=Int64),
        Field(name="unit_of_wage_Hour", dtype=Int64),
        Field(name="unit_of_wage_Month", dtype=Int64),
        Field(name="unit_of_wage_Week", dtype=Int64),
        Field(name="unit_of_wage_Year", dtype=Int64),
        Field(name="region_of_employment_Island", dtype=Int64),
        Field(name="region_of_employment_Midwest", dtype=Int64),
        Field(name="region_of_employment_Northeast", dtype=Int64),
        Field(name="region_of_employment_South", dtype=Int64),
        Field(name="region_of_employment_West", dtype=Int64),
        Field(name="has_job_experience", dtype=Int64),
        Field(name="requires_job_training", dtype=Int64),
        Field(name="full_time_position", dtype=Int64),
        Field(name="education_of_employee", dtype=Int64),
        Field(name="no_of_employees", dtype=Float32),
        Field(name="company_age", dtype=Float32),
        Field(name="prevailing_wage", dtype=Float32)
    ],
    source=exp_feature_source,
    online=True)

exp_target_view = FeatureView(name="exp_target",
    ttl=timedelta(seconds=400),
    entities=[caseid],
    schema=[
        Field(name="case_status", dtype=String)
    ],
    source=exp_target_source,
    online=True)