from app.constants.ElasticFields import field_mapping
from app.repository.Elastic import elastic_repo



class Filters:
    @classmethod
    def addFilters(cls, filters):
        filter_list = []

        if filters.get("level") is not None:
            cls.AddLevelFilters(filters.get("level"), filter_list)

        if filters.get("message") is not None:
            cls.AddMessageFilters(filters.get("message"), filter_list)

        if filters.get("resource_id") is not None:
            cls.AddResource_idFilters(filters.get("resource_id"), filter_list)

        if filters.get("timestamp") is not None:
            cls.AddtimestampFilters(filters.get("timestamp"), filter_list)

        if filters.get("trace_id") is not None:
            cls.AddTrace_idFilters(filters.get("trace_id"), filter_list)

        if filters.get("spanId") is not None:
            cls.AddspanIdFilters(filters.get("spanId"), filter_list)

        if filters.get("commit") is not None:
            cls.AddcommitIdFilters(filters.get("commit"), filter_list)

        if filters.get("parent_resource_id") is not None:
            cls.AddParentResourceIdFilters(filters.get("parent_resource_id"), filter_list)

        return filter_list


    @staticmethod
    def AddLevelFilters(level_values, filter_list):
        if isinstance(level_values, list) and len(level_values):
            field = field_mapping.get_field('level')
            level_values_filter = elastic_repo.get_multi_term_query(field, level_values)
            filter_list.append(level_values_filter)

    @staticmethod
    def AddMessageFilters(message_values, filter_list):
        if isinstance(message_values, list) and len(message_values):
            field = field_mapping.get_field('message')
            message_filter = elastic_repo.get_multi_term_query(field, message_values)
            filter_list.append(message_filter)

    @staticmethod
    def AddResource_idFilters(resource_id_values, filter_list):
        if isinstance(resource_id_values, list) and len(resource_id_values):
            field = field_mapping.get_field('resource_id')
            resource_id_filter = elastic_repo.get_multi_term_query(field, resource_id_values)
            filter_list.append(resource_id_filter)

    @staticmethod
    def AddtimestampFilters(timestamp_filter_values, filter_list):
        if timestamp_filter_values:
            field = field_mapping.get_field("timestamp")
            start_time = timestamp_filter_values.get("start_time")
            end_time = timestamp_filter_values.get("end_time")
            if start_time is not None or end_time is not None:
                time_stamp_filter = elastic_repo.generateRangeQuery(field, start_time, end_time, True)
                filter_list.append(time_stamp_filter)

    @staticmethod
    def AddTrace_idFilters(trace_id_values, filter_list):
        if trace_id_values:
            field = field_mapping.get_field('trace_id')
            trace_id_filter = elastic_repo.get_multi_term_query(field, trace_id_values)
            filter_list.append(trace_id_filter)

    @staticmethod
    def AddspanIdFilters(span_id_values, filter_list):
        if span_id_values:
            field = field_mapping.get_field('span_id')
            span_id_filter = elastic_repo.get_multi_term_query(field, span_id_values)
            filter_list.append(span_id_filter)

    @staticmethod
    def AddcommitIdFilters(commit_id_values, filter_list):
        if commit_id_values:
            field = field_mapping.get_field('commit')
            commit_id_filter = elastic_repo.get_multi_term_query(field, commit_id_values)
            filter_list.append(commit_id_filter)

    @staticmethod
    def AddParentResourceIdFilters(parent_resource_id_values, filter_list):
        if parent_resource_id_values:
            field = field_mapping.get_field('parent_resource_id')
            parent_resource_id_filter = elastic_repo.get_multi_term_query(field, parent_resource_id_values)
            filter_list.append(parent_resource_id_filter)





