from aiohttp import web
import aiofiles
import os
import urllib.parse

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

routes.static('/uploads/', path='./uploads/')
