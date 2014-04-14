# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396999925.115424
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/comissions.html'
_template_uri = 'comissions.html'
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
        transactions = context.get('transactions', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        monthYear = context.get('monthYear', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 42
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        transactions = context.get('transactions', UNDEFINED)
        def content():
            return render_content(context)
        monthYear = context.get('monthYear', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Commissions for ')
        # SOURCE LINE 8
        __M_writer(str( monthYear))
        __M_writer(' </h1>\n\n<div class="row">\n  <div class="col-md-12">\n\t\t<table class="table table-striped">\n\t\t  <thead>\n\t\t\t\t<tr>\n\t\t\t\t <th>Employee ID</th>\n\t\t\t\t <th>Employee Username</th>\t\n\t\t\t\t <th>Customer ID</th>\n\t\t\t\t <th>Customer Username</th>\n\t\t\t\t <th>Transaction Amount</th>\n\t\t\t\t <th>Comission Amount</th>\n\t\t\t\t <th>Date</th>\n\t\t\t </tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n')
        # SOURCE LINE 25
        for t in transactions:
            # SOURCE LINE 26
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str( t.employee.id))
            __M_writer('</td>\n\t\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str( t.employee.username))
            __M_writer('</td>\t\n\t\t\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str( t.id))
            __M_writer('</td>\n\t\t\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(str( t.user.username))
            __M_writer('</td>\n\t\t\t\t\t<td>$')
            # SOURCE LINE 31
            __M_writer(str( t.amount))
            __M_writer('</td>\n\t\t\t\t\t<td>$')
            # SOURCE LINE 32
            __M_writer(str( t.comission_amount))
            __M_writer('\n\t\t\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(str( t.date))
            __M_writer('</td>\n\t\t\t\t</tr>\n')
        # SOURCE LINE 36
        __M_writer('\t\t\t</tbody>\n\t\t</table>\n  </div>\n</div>\n\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


