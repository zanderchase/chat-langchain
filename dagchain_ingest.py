"""Load html from files, clean up, split, ingest into Weaviate."""
from dagchain.loader_logic.dag_abstractions import DagChainBaseLoader, SetDefinitions
from langchain.document_loaders import ReadTheDocsLoader

# Readdocs loader
loader = ReadTheDocsLoader("langchain.readthedocs.io/en/latest/")
read_dagchain = DagChainBaseLoader("read", [loader], 'daily')
read_job, read_schedule = read_dagchain.setup_job()


# Defs to output
defs = SetDefinitions(
    jobs=[read_job],
    schedules=[read_schedule],
)