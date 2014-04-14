# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396981721.284447
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/inventory.html'
_template_uri = 'inventory.html'
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
        inventory = context.get('inventory', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 44
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        inventory = context.get('inventory', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Current Inventory</h1>\n\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>SKU</th>\n\t\t <th>Availability</th>\n\t\t <th>Stock Count</th>\n\t\t <th>Catagory</th>\n\t\t <th>Brand</th>\n\t\t <th>Price</th>\n\t\t <th>Actions</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 25
        for i in inventory:
            # SOURCE LINE 26
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str( i.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str( i.sku))
            __M_writer('</td>\n')
            # SOURCE LINE 29
            if i.availability == 1:
                # SOURCE LINE 30
                __M_writer('\t\t\t\t<td>In Stock</td>\n')
                # SOURCE LINE 31
            else:
                # SOURCE LINE 32
                __M_writer('\t\t\t\t<td>Out Of Stock</td>\n')
            # SOURCE LINE 34
            __M_writer('\t\t\t<td>')
            __M_writer(str( i.product_count))
            __M_writer('\n\t\t  <td>')
            # SOURCE LINE 35
            __M_writer(str( i.category))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 36
            __M_writer(str( i.brand))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(str( i.price))
            __M_writer('</td>\n\t\t  <td><a href="/manage/add_inventory/')
            # SOURCE LINE 38
            __M_writer(str( i.sku))
            __M_writer('/">Add Inventory</a></td> \n\t\t</tr>\n')
        # SOURCE LINE 41
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


