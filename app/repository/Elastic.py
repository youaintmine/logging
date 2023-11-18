from elasticsearch_dsl import Q
from app.utility.Elastic import ElasticConnector


class ElasticRepository:

    def get_multi_term_query(self, query_field, value):
        return Q("terms", **{query_field: value}).to_dict()

    @staticmethod
    def cleanList(unclean_list):
        if unclean_list is None:
            return []
        clean_list = []
        for list_item in unclean_list:
            if list_item is not None:
                clean_list.append(list_item)
        return clean_list

    @staticmethod
    def generateRangeQuery(field, gte, lt, is_upper_limit_inclusive=False):
        query = {"range": {field: dict()}}
        if gte is not None and gte != "":
            query["range"][field]["gte"] = gte
        if lt is not None and lt != "":
            if is_upper_limit_inclusive:
                query["range"][field]["lte"] = lt
            else:
                query["range"][field]["lt"] = lt
        return query

    @classmethod
    def generateShouldQuery(cls, child_queries):
        child_queries = cls.cleanList(child_queries)
        if not child_queries:
            return

        query = Q('bool', should=child_queries, minimum_should_match=1)
        return query.to_dict()

    @classmethod
    def generateMatchPhraseQuery(cls, field, values, condition="or", boost=1):
        values = cls.cleanList(values)
        if not values:
            return

        queries = []
        for value in values:
            query = Q('match_phrase', **{field: {"query": value, "boost": boost}})
            queries.append(query)

        if condition == "or":
            match_query = Q('bool', should=queries, minimum_should_match=1)
        elif condition == "and":
            match_query = Q('bool', must=queries)
        else:
            match_query = None

        return match_query.to_dict()

    def execute_bulk_actions(self, actions):
        ElasticConnector.bulk(actions)
        return


elastic_repo = ElasticRepository()
