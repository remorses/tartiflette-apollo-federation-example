import pytest
from src.resolvers import resolve_campaigns, resolve_recipes

from .support import pretty




@pytest.mark.asyncio
async def test_1(ctx):
    # pretty(await ctx['db'].campaigns.find({}).to_list(10))
    args = {
        'pagination': {
            'first': 1,
            'after': -1
        },
        'orderBy': {
            'field': 'userId',
            'direction': 'ASC',
        }
    }
    result = await resolve_campaigns({}, args, ctx, {})
    pretty(result)
    assert result['nodes']

@pytest.mark.asyncio
async def test_2(ctx):
    # pretty(await ctx['db'].campaigns.find({}).to_list(10))
    args = {
        'pagination': {
            'last': 2,
            'before': 7
        },
        'orderBy': {
            'field': 'userId',
            'direction': 'ASC',
        }

    }
    result = await resolve_campaigns({}, args, ctx, {})
    pretty(result)
    assert result['nodes']

@pytest.mark.asyncio
async def test_3(ctx):
    # pretty(await ctx['db'].campaigns.find({}).to_list(10))
    args = {
        'pagination': {
            'after': 2,
            'before': 7
        },
        'orderBy': {
            'field': 'userId',
            'direction': 'ASC',
        }

    }
    result = await resolve_campaigns({}, args, ctx, {})
    pretty(result)
    assert result['nodes']




@pytest.mark.asyncio
async def test_4(ctx):
    # pretty(await ctx['db'].campaigns.find({}).to_list(10))
    args = {
        'pagination': {
            'after': 9,
            'before': 7
        },
        'orderBy': {
            'field': 'userId',
            'direction': 'ASC',
        }

    }
    result = await resolve_campaigns({}, args, ctx, {})
    pretty(result)
    assert not len(result['nodes'])