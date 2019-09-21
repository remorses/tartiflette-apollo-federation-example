import os
import urllib.parse
from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers
from tartiflette_plugin_apollo_federation import ApolloFederationPlugin
from .resolvers import *
import asyncio

PORT = 8001

here = os.path.dirname(os.path.abspath(__file__))


def run():
    app = web.Application()
    app = register_graphql_handlers(
        app=app,
        engine_sdl=f"{here}/sdl/",
        engine_modules=[ApolloFederationPlugin(engine_sdl=f"{here}/sdl/")],
        executor_http_endpoint="/graphql",
        executor_http_methods=["POST"],
        graphiql_enabled=True,
    )
    web.run_app(app, port=PORT)


run()
