import pytest
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo.database

@pytest.fixture
def motor(mongodb: pymongo.database.Database, event_loop):
    ret = AsyncIOMotorClient(*mongodb.client.address, io_loop=event_loop)
    yield ret
    ret.close()

@pytest.fixture
def ctx(motor):
    return {
        'db': motor.playdb,
    }