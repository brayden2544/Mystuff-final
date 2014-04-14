# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396999922.370483
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/incomesheet.html'
_template_uri = 'incomesheet.html'
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
        SalesTaxPayable = context.get('SalesTaxPayable', UNDEFINED)
        ComissionsExpense = context.get('ComissionsExpense', UNDEFINED)
        revenue = context.get('revenue', UNDEFINED)
        year = context.get('year', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 43
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
        SalesTaxPayable = context.get('SalesTaxPayable', UNDEFINED)
        ComissionsExpense = context.get('ComissionsExpense', UNDEFINED)
        revenue = context.get('revenue', UNDEFINED)
        year = context.get('year', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Income Statement for ')
        # SOURCE LINE 8
        __M_writer(str( month))
        __M_writer(' ')
        __M_writer(str( year))
        __M_writer(' </h1>\n\n<div class="row">\n  <div class="col-md-10">\n\t\t<table class="table table-striped">\n\t\t  <thead>\n\t\t\t\t<tr>\n\t\t\t\t <th>Account</th>\n\t\t\t\t <th>Balance</th>\n\t\t\t\t <th>Month</th>\n\t\t\t </tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n\t\t\t\t<tr>\n\t\t\t\t\t<td>Revenue</td>\n\t\t\t\t\t<td>$')
        # SOURCE LINE 23
        __M_writer(str( revenue.balance))
        __M_writer('</td>\n\t\t\t\t\t<td>')
        # SOURCE LINE 24
        __M_writer(str( revenue.account_name))
        __M_writer('</td>\n\t\t\t\t</tr>\n\t\t\t\t<tr>\n\t\t\t\t\t<td>ComissionsExpense</td>\n\t\t\t\t\t<td>$')
        # SOURCE LINE 28
        __M_writer(str( ComissionsExpense.balance))
        __M_writer('</td>\n\t\t\t\t\t<td>')
        # SOURCE LINE 29
        __M_writer(str( ComissionsExpense.account_name))
        __M_writer('</td>\n\t\t\t\t</tr>\n\t\t\t\t<tr>\n\t\t\t\t\t<td>Sales Tax Payable</td>\n\t\t\t\t\t<td>$')
        # SOURCE LINE 33
        __M_writer(str( SalesTaxPayable.balance))
        __M_writer('</td>\n\t\t\t\t\t<td>')
        # SOURCE LINE 34
        __M_writer(str( SalesTaxPayable.account_name))
        __M_writer('</td>\n\t\t\t\t</tr>\n\t\t\t</tbody>\n\t\t</table>\n  </div>\n  <div class="col-md-2"></div>\n</div>\n\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


