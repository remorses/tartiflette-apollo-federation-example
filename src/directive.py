from typing import Any, Callable, Dict, Optional, NamedTuple
import time
from tartiflette import Directive
from tartiflette.types.field import GraphQLField




@Directive("Test")
class Test:
    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        print('parent_result:', parent_result)
        print('next_resolver:', next_resolver)
        return await next_resolver(parent_result, args, ctx, info)


class RequireInput(NamedTuple):
    arg: str
    equalTo: str
    inside: str


@Directive("require")
class Require:
    @staticmethod
    async def on_field_execution(
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        directive_args = RequireInput(**directive_args)
        if directive_args.inside == 'SESSION':
            if not directive_args.arg in args:
                raise Exception(f'{directive_args.arg} not in args')
            if not getattr(ctx['req'], 'user', None):
                raise Exception(f'no session available')
            if args[directive_args.arg] != ctx['req'].user[directive_args.equalTo]:
                raise Exception(f'argument {args[directive_args.arg]} does not satisfy requirement {directive_args.arg} == {directive_args.equalTo}')
            else:
                return await next_resolver(parent_result, args, ctx, info)
        else:
            return await next_resolver(parent_result, args, ctx, info)

    @staticmethod
    async def on_pre_output_coercion(
        directive_args: Dict[str, Any],
        next_directive: Callable,
        value: Any,
        field_definition: "GraphQLField",
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        directive_args = RequireInput(**directive_args)
        args = field_definition.arguments
        print('value:', value)
        print('args:', args)
        if directive_args.inside == 'OUTPUT':
            if not directive_args.arg in args:
                raise Exception(f'{directive_args.arg} not in args')
            if not directive_args.equalTo in value:
                raise Exception(f'{directive_args.equalTo} not in OUTPUT')
            if args[directive_args.arg] != ctx['req'].user[directive_args.equalTo]:
                raise Exception(f'argument {args[directive_args.arg]} does not satisfy requirement {directive_args.arg} == {directive_args.equalTo}')
            else:
                return await next_directive(value, field_definition, ctx, info)
        else:
            return await next_directive(value, field_definition, ctx, info)
