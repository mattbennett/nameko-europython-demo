from nameko.web.handlers import http


class HelloWorld(object):
    name = "hello"

    @http("GET", "/greet/<string:friend>")
    def greet(self, request, friend):
        return "Hello {}!".format(friend)
