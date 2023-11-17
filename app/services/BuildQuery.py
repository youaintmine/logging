from app.constants.ElasticFields import field_mapping
from app.repository.Elastic import elastic_repo
from app.services.Filter.Filters import Filters


class BuildQuery:
    def get_search_query(self, request_form):
        if request_form.get('filters') is not None:
            filter_list = Filters.addFilters(request_form.get('filters'))

        if request_form.get("query") is not None:
            query_block = self.get_query_block(queries=request_form.get("query"))

        page_start = request_form.get("page_start", 0)
        page_size = request_form.get("page_size", 20)

        query = {"query": {"bool":{}}}

        query["query"]["bool"]["should"] = query_block
        query["query"]["bool"]["filter"] = filter_list
        query["from"] = page_start
        query["size"] = page_size

        return query

    def get_query_block(self, queries):
        should_clause = None
        clauses = []
        if queries is not None:
            query_words = queries.split(",")
            search_fields = field_mapping.get_search_fields()

            for field in search_fields:
                should_clause = elastic_repo.generateMatchPhraseQuery(field, query_words)
                clauses.append(should_clause)
        should_query = elastic_repo.generateShouldQuery(clauses)
        return should_query


BuildQuery = BuildQuery()