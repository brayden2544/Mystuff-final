# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397209237.345789
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/receipt.html'
_template_uri = 'receipt.html'
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
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        description = context.get('description', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 18
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context)
        description = context.get('description', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n<div class="row" style="text-align:center">\n    <h4>Purchase Confirmed</h4>\n\n    <h2>Your purchase has been submitted successfully!</h2>\n    <h3>We have sent a copy of this reciept to your email</h3><br />\n\t\t\n</div>\n\t\t<u><h2>Please print this reciept for your records</h2></u>\n\t\t<h4>Confirmation ID: ')
        # SOURCE LINE 13
        __M_writer(str( id))
        __M_writer('</h4>\n\t\t<h4>Purchase Amount: $')
        # SOURCE LINE 14
        __M_writer(str( amount))
        __M_writer('</h4>\n\t\t<h4>Purchase Description ')
        # SOURCE LINE 15
        __M_writer(str( description))
        __M_writer('</h4>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


