import os
import urllib.parse
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient
import aiohttp_cors
from tartiflette_aiohttp import register_graphql_handlers
import src.resolvers
import src.scalars
import aiofiles 
import asyncio
from .routes import routes
import src.directive


@web.middleware
async def middleware(request, handler):
        request.user = {}
        response = await handler(request)
        return response
    



here = os.path.dirname(os.path.abspath(__file__))

def run():
    app = web.Application(middlewares=[middleware])
    db = AsyncIOMotorClient().playdb
    app = register_graphql_handlers(
        app=app,
        engine_sdl=f'{here}/sdl/',
        executor_context={
            'db': db,
        },
        executor_http_endpoint='/graphql',
        executor_http_methods=['POST'],
        graphiql_enabled=True
    )
    app.add_routes(routes)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    
    # app.on_startup.append(start_background_tasks)
    # app.on_cleanup.append(cleanup_background_tasks)
    web.run_app(app, port=8090,)

run()