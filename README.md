# Feast Feature Store Integration Template
The top-level namespace within Feast is a project. Users define one or more feature views within a project. Each feature view contains one or more features that relate to a specific entity. A feature view must always have a data source, which in turn is used during the generation of training datasets and when materializing feature values into the online store.

![image](https://user-images.githubusercontent.com/40850370/202990403-d11a5bf8-a674-4060-b2bc-d97311f19201.png)

Projects provide complete isolation of feature stores at the infrastructure level. It is not possible to retrieve features from multiple projects in a single request. We recommend having a single feature store and a single project per environment (dev, staging, prod).
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

**Feast Registry:** Path to the registry [ object store (GCS, S3) ] where feature definiation will be stored by feast.

**Provider:**  Enviorment where data is stored.

**Online Store:** The online store is a database that stores only the latest feature values for low letency inference.

**Offline Store:** The offline store persists batch data that has been ingested into Feast. This data is used for producing training datasets. For feature retrieval and materialization, Feast does not manage the offline store directly, but runs queries against it. 

```yaml
# Initial Configuration File 
project: feature_store
registry: /path/to/registry.db
provider: local
online_store:
    path: /path/to/online_store.db
entity_key_serialization_version: 2
```

```yaml
# Updated Configuration File  
project: feature_store
registry: feature_store/feature_repo/data/feature_definition.db
provider: local
online_store:
    path: feature_store/feature_repo/data/feature_inference.db
entity_key_serialization_version: 2
```
## Components of feast Store

## Data Configurations 


## References
1. Getting started with Feast, an open source feature store running on AWS Managed Services **:** [Blog Link](https://aws.amazon.com/blogs/opensource/getting-started-with-feast-an-open-source-feature-store-running-on-aws-managed-services/) 