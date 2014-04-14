# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396999919.761275
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/balancesheet.html'
_template_uri = 'balancesheet.html'
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
        cash = context.get('cash', UNDEFINED)
        inventory_balance = context.get('inventory_balance', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        PrepaidServiceLiability = context.get('PrepaidServiceLiability', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 34
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cash = context.get('cash', UNDEFINED)
        inventory_balance = context.get('inventory_balance', UNDEFINED)
        def content():
            return render_content(context)
        PrepaidServiceLiability = context.get('PrepaidServiceLiability', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> MyStuff Balance Sheet Summary</h1>\n\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>Account</th>\n\t\t <th>Balance</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n\t\t<tr>\n\t\t\t<td>Inventory</td>\n\t\t\t<td>$')
        # SOURCE LINE 21
        __M_writer(str( inventory_balance))
        __M_writer('</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>Cash</td>\n\t\t\t<td>$')
        # SOURCE LINE 25
        __M_writer(str( cash.balance))
        __M_writer('</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>Prepaid Services Liability</td>\n\t\t\t<td>$')
        # SOURCE LINE 29
        __M_writer(str( PrepaidServiceLiability.balance))
        __M_writer('</td>\n\t\t</tr>\n\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


