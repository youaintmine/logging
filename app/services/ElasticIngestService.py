from app.repository.Elastic import elastic_repo
from app.utility.Elastic import ElasticConnector


class IngestService:
    def insert_logs_into_es(self, logs, index_name):
        if logs and len(logs):
            try:
                actions = []
                for log in logs:
                    actions.append(convert_to_index_action(log, 'log_system'))
                elastic_repo.execute_bulk_actions(actions)
                print(f"Inserted {len(logs)} Logs")
            except Exception as e:
                print(f"Insertion to elastic search failed with exception: {e}")


def convert_to_index_action(log, index_name):
    return {"_op_type": "index", "_index": index_name, "_source": log}


ElasticIngester = IngestService()
