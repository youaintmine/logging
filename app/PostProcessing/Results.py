from app.utility.Elastic import ElasticConnector


class Results:

    def get_logs(self, es_query, index_name):
        es_results = ElasticConnector.get_result(index_name, es_query)
        logs = []

        for log in es_results["responses"][0]["hits"]["hits"]:
            logs.append(log)

        return logs


Results = Results()
