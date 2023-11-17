from elasticsearch_dsl import Q
from app.utility.Elastic import ElasticConnector

class ElasticRepository:

    def get_match_phrase_clause(self, query_field, value, boost):
        return Q('match_phrase', **{query_field: {'query': value, 'boost': boost}})

    def get_term_query(self, query_field, value):
        return Q("term", **{query_field: value}).to_dict()

    def get_multi_term_query(self, query_field, value):
        return Q("terms", **{query_field: value}).to_dict()

    def get_exclude_clause_keyword_query(self, exclude_clause):
        return Q("bool", must_not=exclude_clause).to_dict()



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

    @staticmethod
    def generateTermQuery(field, value):
        if value is None:
            return

        query = Q('term', **{field: value})
        return query.to_dict()

    @staticmethod
    def generateNotTermQuery(field, value):
        if value is None:
            return

        query = ~Q('term', **{field: value})
        return query.to_dict()

    @staticmethod
    def generateExistsQuery(field_name):
        query = Q('exists', field=field_name)
        return query.to_dict()

    @classmethod
    def generateShouldQuery(cls, child_queries):
        child_queries = cls.cleanList(child_queries)
        if not child_queries:
            return

        query = Q('bool', should=child_queries, minimum_should_match=1)
        return query.to_dict()

    @classmethod
    def generateMustQuery(cls, child_queries):
        child_queries = cls.cleanList(child_queries)
        if not child_queries:
            return

        query = Q('bool', must=child_queries)
        return query.to_dict()

    @classmethod
    def generateMustNotQuery(cls, child_queries):
        child_queries = cls.cleanList(child_queries)
        if not child_queries:
            return

        query = Q('bool', must_not=child_queries)
        return query.to_dict()

    @classmethod
    def generateMatchQuery(cls, field, values, condition="or", operator="or"):
        values = cls.cleanList(values)
        if not values:
            return
        queries = []
        for value in values:
            query = {"match": {field: {"query": value, "operator": operator}}}
            queries.append(query)
        if condition == "or":
            match_query = cls.generateShouldQuery(queries)
        elif condition == "and":
            match_query = cls.generateMustQuery(queries)
        else:
            match_query = None

        return match_query

    @classmethod
    def generateMultiMatchQuery(cls, fields, values, condition="or", operator="or", query_type="best_fields"):
        values = cls.cleanList(values)
        if not values:
            return

        queries = []
        for value in values:
            query = Q('multi_match', query=value, fields=fields, operator=operator, type=query_type)
            queries.append(query)

        if condition == "or":
            query = Q('bool', should=queries)
        elif condition == "and":
            query = Q('bool', must=queries)
        else:
            query = None

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

    @classmethod
    def generateTermsQuery(cls, field, terms):
        terms = cls.cleanList(terms)
        if not terms:
            return

        query = Q('terms', **{field: terms})
        return query.to_dict()

    def get_match_phrase_clause(self, query_field, value, boost):
        return {"match_phrase": {query_field: {"query": value, "boost": boost}}}

    def execute_bulk_actions(self, actions):
        ElasticConnector.bulk(actions)
        return

elastic_repo = ElasticRepository()