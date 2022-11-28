# Feast Feature Store Integration Template
Feast is the leading open source feature store that automates the last mile in your production ML data pipelines. It allows data teams to serve features consistently for offline training and online inference.
![Screenshot 2022-11-24 161109](https://user-images.githubusercontent.com/117065034/204229179-949bcb64-cf15-46e4-9d35-b7d0436cc8bd.png)


## Components of feast Store
1. Offline Store: The offline store persists batch data that has been ingested into Feast. This data is used for producing training datasets. The feast does not manage the offline store directly but runs queries against it.
2. Online Store: The online store is a database that stores only the latest feature values for each entity.
3. Feast Registry: An object store (GCS, S3) based registry used to persist feature definitions that are registered with the feature store.
4. SDK: Manage version-controlled feature definitions, Materialize (load), Build and retrieve training datasets, and Retrieve online features.
5. Feast UI

## Initialize the Project

```bash
feast init -m dev
```
## Configure Your Feature Store

**STEP 1:** Create data folder under feature_store/feature_repo

```bash
mkdir dev/feature_repo/data
```

**STEP 2:** Configure feature_store.yaml

```yaml
# Initial Configuration File 
project: feature_store

# Path to the registry [ object store (GCS, S3) ] where feature definiation will be stored by feast.
registry: /path/to/registry.db

# Enviorment where data is stored.
provider: local

# The online store is a database that stores only the latest feature values for low latency inference.
online_store:
    path: /path/to/online_store.db

# The offline store persists batch data that has been ingested into Feast. This data is used for producing training datasets. For feature retrieval and materialization, Feast does not manage the offline store directly, but runs queries against it. 
    # offline_store:
    #     type: redshift
    #     cluster_id: [SET YOUR CLUSTER ID]
    #     region: us-west-2
    #     user: admin
    #     database: dev
    #     s3_staging_location: [SET YOUR BUCKET]
    #     iam_role: [SET YOUR ARN]

entity_key_serialization_version: 2
```

```yaml
# Updated Configuration File  
project: dev
registry: data/registry.db
provider: local
online_store:
    type: sqlite
    path: data/online_store.db

entity_key_serialization_version: 2
```
## Feature Definition
### Python file
1. Define The source of the features 
2. Define Entity for the feature schema 
3. Define Feature Schema [*Entity and source will be utilised*]
4. Define Feature Service 

### Integration Code flow
1. Define the Entity Dataframe [ Df will contain target, Entity, Timestamp]
2. Get the Historical Features using entity dataframe [ Feature retrieval ]
3. Save the data which will be used for model training
4. Materialization [ For inferencing real time ]

## References
1. Getting started with Feast, an open source feature store running on AWS Managed Services **:** [Blog Link](https://aws.amazon.com/blogs/opensource/getting-started-with-feast-an-open-source-feature-store-running-on-aws-managed-services/) 