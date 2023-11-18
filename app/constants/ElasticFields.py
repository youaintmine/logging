class ElasticFields:
    main_mapping = {
        "level": "level.keyword",
        "message": "message.keyword",
        "resource_id": "resourceId.keyword",
        "timestamp": "timestamp",
        "trace_id": "traceId.keyword",
        "span_id": "spanId.keyword",
        "commit": "commit.keyword",
        "parent_resource_id": "metadata.parentResourceId.keyword"

    }

    SEARCH_FIELDS = [
        "level",
        "message",
        "resourceId",
        "spanId",
        "commit",
        "metadata.parentResourceId",
        "traceId"
    ]

    def get_field(self, field):
        return self.main_mapping.get(field)

    def get_search_fields(self):
        return self.SEARCH_FIELDS


field_mapping = ElasticFields()
