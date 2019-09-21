from typing import Any, Callable, Dict, Optional, NamedTuple
import time
from tartiflette import Directive
from tartiflette.types.field import GraphQLField






class RequireInput(NamedTuple):
    equalTo: str
    arg: str = None
    field: str = None

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
        if not directive_args.arg in args:
            raise Exception(f'in Query.{info.query_field.name}: {directive_args.arg} not in args')
        if not getattr(ctx['req'], 'user', None):
            raise Exception(f'no session available required in Query.{info.query_field.name}')
        if args[directive_args.arg] != ctx['req'].user.get(directive_args.equalTo):
            raise Exception(f'in Query.{info.query_field.name}: argument {args[directive_args.arg]} does not satisfy requirement {directive_args.arg} == {directive_args.equalTo}')
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
        # args = field_definition.arguments
        print('value:', value)
        print('info:', info.query_field.name)
        # print('args:', args)

        if not directive_args.field in value:
            raise Exception(f'in Query.{info.query_field.name}: @require field {directive_args.field} not in output')
        if value[directive_args.field] != ctx['req'].user.get(directive_args.equalTo):
            raise Exception(f'in Query.{info.query_field.name}: field {directive_args.field} does not satisfy requirement {directive_args.field} == session.{directive_args.equalTo}')
        else:
            return await next_directive(value, field_definition, ctx, info)




@Directive("needsLogin")
class NeedsLogin:
    @staticmethod
    async def on_field_execution(
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        if not getattr(ctx['req'], 'user', None):
            raise Exception(f'no required session available')
        else:
            return await next_resolver(parent_result, args, ctx, info)

