import collections
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from tartiflette import Resolver
import pymongo
from datetime import datetime
from typing import NamedTuple, Union




@Resolver('Query.stuff')
async def revolve_stuff(_, args, ctx, info):
    return {
        'ciao': 'sdasd',
        'cosa': 86
    }

@Resolver('Query.others')
async def revolve_others(_, args, ctx, info):
    print(args)
    return args['input']

@Resolver('Query.campaign')
async def revolve_campaign(_, args, ctx, info):
    print(args)
    return args['_id']

@Resolver('Query.something')
async def revolve_some(_, args, ctx, info):
    return {
        '_id': 'xxx',
        'ciao': 'asd'
    }
@Resolver('Query.bo')
async def revolve_bo(_, args, ctx, info):
    return {
        '_id': 'vvv',
        'cose': 'asd'
    }