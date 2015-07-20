from nameko.rpc import rpc

from dependencies import CacheClient


class HelloWorld(object):
    name = "hello"

    cache = CacheClient()

    @rpc
    def greet(self, friend):
        friend = friend.encode('ascii')  # we recv unicode from RPC entrypoint
        greeting = self.cache.get(friend)

        if greeting is None:
            greeting = "Hello {}!".format(friend)  # expensive
            self.cache.set(friend, greeting)

        return greeting
