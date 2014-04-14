# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397093711.959581
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/overdue_rental.html'
_template_uri = 'overdue_rental.html'
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
        ninety = context.get('ninety', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        sixty = context.get('sixty', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        import datetime
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 84
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ninety = context.get('ninety', UNDEFINED)
        def content():
            return render_content(context)
        sixty = context.get('sixty', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Overdue Rentals Report</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/manage/email_overdue_rentals/">Email All Overdue Rentals</a>\n</div>\n\t\n<h2>Rentals 30 Days Overdue</h2>\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>Rental ID</th>\n\t\t <th>Product SKU</th>\n\t\t <th>Customer</th>\n\t\t <th>Date Out</th>\n\t\t <th>Return Date</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 25
        for t in thirty:
            # SOURCE LINE 26
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str( t.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str( t.rental_item.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str( t.customer.username))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(str( t.date_out))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str( t.expected_return))
            __M_writer('</td>\n\t\t</tr>\n')
        # SOURCE LINE 34
        __M_writer('</table>\n\n<h2>Rentals 60 Days Overdue</h2>\t\n<table class="table table-striped">\t\n\t  <thead>\n\t\t\t<tr>\n\t\t\t <th>Rental ID</th>\n\t\t\t <th>Product SKU</th>\n\t\t\t <th>Customer</th>\n\t\t\t <th>Date Out</th>\n\t\t\t <th>Return Date</th>\n\t\t </tr>\n\t\t</thead>\n\t\t<tbody>\n')
        # SOURCE LINE 48
        for s in sixty:
            # SOURCE LINE 49
            __M_writer('\t\t\t\n\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 51
            __M_writer(str( s.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 52
            __M_writer(str( s.rental_item.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 53
            __M_writer(str( s.customer.username))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 54
            __M_writer(str( s.date_out))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 55
            __M_writer(str( s.expected_return))
            __M_writer('</td>\n\t\t</tr>\n')
        # SOURCE LINE 58
        __M_writer('</table>\n\n<h2>Rentals 90 Days Overdue</h2>\n<table class="table table-striped">\t\t\n\t  <thead>\n\t\t\t<tr>\n\t\t\t <th>Rental ID</th>\n\t\t\t <th>Product SKU</th>\n\t\t\t <th>Customer</th>\n\t\t\t <th>Date Out</th>\n\t\t\t <th>Return Date</th>\n\t\t </tr>\n\t\t</thead>\n\t\t<tbody>\n')
        # SOURCE LINE 72
        for n in ninety:
            # SOURCE LINE 73
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 74
            __M_writer(str( n.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 75
            __M_writer(str( n.rental_item.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 76
            __M_writer(str( n.customer.username))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 77
            __M_writer(str( n.date_out))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 78
            __M_writer(str( n.expected_return))
            __M_writer('</td>\n\t\t</tr>\n')
        # SOURCE LINE 81
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


