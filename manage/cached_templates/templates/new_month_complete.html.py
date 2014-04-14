# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396998173.171687
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/new_month_complete.html'
_template_uri = 'new_month_complete.html'
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
        month = context.get('month', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        year = context.get('year', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 17
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        month = context.get('month', UNDEFINED)
        def content():
            return render_content(context)
        year = context.get('year', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> New Month Creation Complete</h1><br>\n<h2> New Accounts have been created for ')
        # SOURCE LINE 9
        __M_writer(str( month))
        __M_writer(' ')
        __M_writer(str( year))
        __M_writer('</h2><br>\n\n<u><h2>Summary<h2></u>\n<h3>Revenue Account ')
        # SOURCE LINE 12
        __M_writer(str( month))
        __M_writer(' ')
        __M_writer(str( year))
        __M_writer(': $0<h3>\n<h3>Comissions Expense ')
        # SOURCE LINE 13
        __M_writer(str( month))
        __M_writer(' ')
        __M_writer(str( year))
        __M_writer(': $0<h3>\n<h3>Sales Tax Payable ')
        # SOURCE LINE 14
        __M_writer(str( month))
        __M_writer(' ')
        __M_writer(str( year))
        __M_writer(': $0<h3>\n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


