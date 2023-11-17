class ElasticFields:
    main_mapping = {
        "level": "level.keyword",
        "message": "message.keyword",
        "resource_id": "resource_id.keyword",
        "timestamp": "timestamp",
        "trace_id": "trace_id.keyword",
        "span_id": "span_id.keyword",
        "commit": "commit.keyword",
        "parent_resource_id": "metadata.parentResourceId.keyword"

    }

    SEARCH_FIELDS = [
        "level",
        "message",
        "resource_id",
        "span_id",
        "commit",
        "metadata.parentResourceId"
    ]

    def get_field(self, field):
        return self.main_mapping.get(field)

    def get_search_fields(self):
        return self.SEARCH_FIELDS


field_mapping = ElasticFields()

