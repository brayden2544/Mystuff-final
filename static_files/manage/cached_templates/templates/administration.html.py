# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396975212.221696
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/administration.html'
_template_uri = 'administration.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 21
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<u><h1>Administration Options</h1></u>\n<div class="pull-left">\n\t<h3>Setup Options</h3>\n\t<a class="btn btn-default" href="/manage/Setup_Default_Store/">Setup Default Store</a>\n\t<a class="btn btn-danger" href="/manage/Remove_All/">Delete All From Database</a><br>\n\n\t<br>\n\t<h3>Monthly Setup</h3>\n\t<a class="btn btn-default" href="/manage/new_month/">Setup Accounts for New Month</a><br>\n</div>\t\n\n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


