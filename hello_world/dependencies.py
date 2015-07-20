import memcache

from nameko.extensions import DependencyProvider


class CacheClient(DependencyProvider):
    """ Silly DependencyProvider that returns a new memcache Client
    for every worker.
    """
    def setup(self):
        config = self.container.config
        self.uri = config.get("MEMCACHED_URI", ["127.0.0.1:11211"])

    def get_dependency(self, worker_ctx):
        return memcache.Client(self.uri)
