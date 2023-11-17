import json
import os

from elasticsearch import Elasticsearch
from elasticsearch.client.indices import IndicesClient
from elasticsearch.exceptions import RequestError
from elasticsearch.helpers import bulk
from elasticsearch.helpers.errors import BulkIndexError
from elasticsearch_dsl import Search

from app.config.Elastic import Credentials

env = os.environ.get("env")


def create_es_connection(hosts, user, password):
    try:
        if user is not None and password is not None:
            return Elasticsearch(hosts, maxsize=25, timeout=120, http_auth=(user, password))
        else:
            return Elasticsearch(hosts, maxsize=25, timeout=120)
    except Exception as error:
        print(error)

class EsConnector:
    hosts = []
    es_user = None
    es_password = None
    es_client = None
    index_list = ["log_system"]

    def __init__(self, hosts, user, password):
        self.hosts = hosts
        self.es_user = user
        self.es_password = password
        self.es_client = create_es_connection(hosts, user, password)

    def get_result(self, index, queries):
        multi_search_query = []
        for query in queries:
            multi_search_query += [{"index": index}, query]
        return self.es_client.msearch(body=multi_search_query)

    def initializeESIndicesClient(self):
        return IndicesClient(self.es_client)


    def close_connection(self):
        self.es_client.transport.close()

    def bulk(self, data):
        try:
            result = bulk(self.es_client, data, refresh=Credentials.refresh)
            print(f"indexing result {result}")
        except BulkIndexError as e:
            print(f"bulk indexing error: {e}")
        except Exception as e:
            print(f"Failed to index with error: {e}")


ElasticConnector = EsConnector(Credentials.hosts, Credentials.user, Credentials.password)
