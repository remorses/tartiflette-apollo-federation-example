import collections
from prtty import pretty
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from tartiflette import Resolver
from tartiflette.types.argument import ResolveInfo

import pymongo
from datetime import datetime
from typing import NamedTuple, Union




@Resolver('Query.me')
async def revolve_stuff(_, args, ctx, info):
    pretty(info)
    return {
        'name': 'sdasd', 
    }

