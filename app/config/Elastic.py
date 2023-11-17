import os


class Elastic:
    hosts = []
    user = None
    password = None

    def set_elastic_credentials(self):
        elastic_hosts = os.environ.get("ES_HOSTS").split(",")
        for host in elastic_hosts:
            self.hosts.append(host)
        return None

    def __init__(self):
        self.user = os.environ.get("ES_USER")
        self.password = os.environ.get("ES_PASSWORD")
        self.set_elastic_credentials()


Credentials = Elastic()
