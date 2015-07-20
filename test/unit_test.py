import mockcache
from mock import call
from nameko.testing.services import worker_factory

from hello_world.service_cache import HelloWorld


def test_greet():

    hello_svc = worker_factory(HelloWorld)

    hello_svc.cache.get.return_value = None

    assert hello_svc.greet("Matt") == "Hello Matt!"
    assert hello_svc.cache.get.call_args_list == [call("Matt")]


def test_greet_with_mockcache():

    fake_cache = mockcache.Client()
    hello_svc = worker_factory(HelloWorld, cache=fake_cache)

    assert hello_svc.greet("Matt") == "Hello Matt!"
    assert fake_cache.get("Matt") == "Hello Matt!"
