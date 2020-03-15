#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

from scriptgen import BlockBuilder, IndentType, StringBuilder, timestamp


class CSharpBlockBuilder(BlockBuilder):

    default_semicolon_end: bool = False

    def __init__(
            self,
            header: str = "",
            semicolon_end: bool = None,
            indent_len: int = None,
            indent_space_len: int = None,
            indent_type: IndentType = None,
            rstrip: bool = None
    ) -> None:
        semicolon_end = semicolon_end if semicolon_end is not None else CSharpBlockBuilder.default_semicolon_end
        BlockBuilder.__init__(
            self,
            indent_len=indent_len,
            indent_space_len=indent_space_len,
            indent_type=indent_type,
            rstrip=rstrip
        )
        self.header = f"{header}{self.new_line}{{{self.new_line}" if header else f"{{{self.new_line}"
        self.footer = f"}}{';' if semicolon_end else ''}{self.new_line}"


def csharp_autogen() -> StringBuilder:
    return csharp_comment(f"Auto-generated: {timestamp()}")


def csharp_block() -> StringBuilder:
    return CSharpBlockBuilder()


def csharp_class(
        class_name: str,
        access_modifier: str = "public",
        base_class_name: str = None,
        interface_names: List[str] = None
) -> StringBuilder:
    interface_names = interface_names if interface_names is not None else []
    inheritance = []
    if base_class_name:
        inheritance.append(base_class_name)
    if interface_names:
        inheritance.extend(interface_names)
    inheritance_str = f" : {', '.join(inheritance)}" if inheritance else ""
    header = f"{access_modifier} class {class_name}{inheritance_str}"
    csb = CSharpBlockBuilder(
        header=header
    )
    return csb


def csharp_comment(*args: str) -> StringBuilder:
    sb = StringBuilder()
    for arg in args:
        sb.wl(f"// {arg}")
    return sb


def csharp_constructor(
        class_name: str,
        access_modifier: str = "public",
        parameters: List[str] = None
) -> StringBuilder:
    parameters_str = csharp_parameters(parameters)
    header = f"{access_modifier} {class_name}({parameters_str})"
    csb = CSharpBlockBuilder(
        header=header
    )
    return csb


def csharp_doc(*args: str) -> StringBuilder:
    sb = StringBuilder()
    sb.wl("/// <summary>")
    for arg in args:
        sb.wl(f"/// {sb.indent}{arg}")
    sb.wl("/// </summary>")
    return sb


def csharp_for_loop(
        var_name: str = "i",
        initial_val: str = "0",
        condition_max: str = None,
        condition_stmt: str = None,
        step_stmt: str = None,
        var_type: str = None
) -> StringBuilder:
    var_type = var_type if var_type else "var"
    condition_stmt = condition_stmt if condition_stmt else f"{var_name} < {condition_max}"
    step_stmt = step_stmt if step_stmt else f"++{var_name}"
    csb = CSharpBlockBuilder(
        header=f"for ({var_type} {var_name} = {initial_val}; {condition_stmt}; {step_stmt})"
    )
    return csb


def csharp_foreach_loop(
        enumerable_name: str,
        var_name: str = "v",
        var_type: str = None
) -> StringBuilder:
    var_type = var_type if var_type else "var"
    csb = CSharpBlockBuilder(
        header=f"foreach ({var_type} {var_name} in {enumerable_name})"
    )
    return csb


def csharp_method(
        method_name: str,
        access_modifier: str = "public",
        return_type: str = "void",
        parameters: List[str] = None
) -> StringBuilder:
    parameters_str = csharp_parameters(parameters)
    header = f"{access_modifier} {return_type} {method_name}({parameters_str})"
    csb = CSharpBlockBuilder(
        header=header
    )
    return csb


def csharp_namespace(namespace_name: str) -> StringBuilder:
    csb = CSharpBlockBuilder(
        header=f"namespace {namespace_name}"
    )
    return csb


def csharp_parameters(parameters: List[str]) -> StringBuilder:
    parameters = parameters if parameters else []
    parameters_len = len(parameters)
    sb = StringBuilder()
    if parameters_len > 1:
        sb.nl()
        for i, p in enumerate(parameters):
            sb.wt(p, addtl_indent_len=1)
            sb.wl("," if i < parameters_len - 1 else "")
    elif parameters_len == 1:
        p = parameters[0]
        sb.wt(p)
    return sb


def csharp_region(region_name: str) -> StringBuilder:
    bb = BlockBuilder(
        indent_len=0,
        header=f"#region {region_name}{StringBuilder.new_line * 2}",
        footer=f"{StringBuilder.new_line}#endregion {region_name}{StringBuilder.new_line}",
    )
    return bb


def csharp_try_catch(
        catch_var_name: str = "Exception ex"
) -> (StringBuilder, StringBuilder, StringBuilder):
    sb = StringBuilder()
    csb_try = CSharpBlockBuilder("try")
    sb.wb(csb_try)
    csb_catch = CSharpBlockBuilder(f"catch ({catch_var_name})")
    sb.wb(csb_catch)
    return sb, csb_try, csb_catch


def csharp_usings(
        *args: str,
        **kwargs: str
) -> StringBuilder:
    sb = StringBuilder()
    for arg in args:
        sb.wl(f"using {arg};")
    for k, v in kwargs.items():
        sb.wl(f"using {k} = {v};")
    return sb
