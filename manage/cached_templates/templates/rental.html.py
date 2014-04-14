# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397076093.47954
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/rental.html'
_template_uri = 'rental.html'
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
        rental = context.get('rental', UNDEFINED)
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
        

        # SOURCE LINE 36
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Current Rentals</h1>\n\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>Rental ID</th>\n\t\t <th>Product SKU</th>\n\t\t <th>Customer</th>\n\t\t <th>Date Out</th>\n\t\t <th>Return Date</th>\n\t\t <th>Options</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 23
        for r in rental:
            # SOURCE LINE 24
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 25
            __M_writer(str( r.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 26
            __M_writer(str( r.rental_item.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str( r.customer.username))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str( r.date_out))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str( r.expected_return))
            __M_writer('</td>\n\t\t\t<td><a href="/manage/rental_return/')
            # SOURCE LINE 30
            __M_writer(str( r.id))
            __M_writer('/">Return</a>\n\t\t</tr>\n')
        # SOURCE LINE 33
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


