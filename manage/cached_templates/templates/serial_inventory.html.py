# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397187336.445038
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/serial_inventory.html'
_template_uri = 'serial_inventory.html'
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
        

        # SOURCE LINE 52
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
        __M_writer('\n\n\n<h1> All Inventory</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/manage/edit_serial_inventory__new/">Add New Serial Inventory</a>\n</div>\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>SKU</th>\n\t\t <th>Availability</th>\n\t\t <th>Catagory</th>\n\t\t <th>Brand</th>\n\t\t <th>Description</th>\n\t\t <th>Price</th>\n\t\t <th>Serial</th>\n\t\t <th>Store Location</th>\n\t\t <th>Shelf Location</th>\n\t\t <th>Date Purchased</th>\n\t\t <th>Comission Rate</th>\n\t\t <th>Actions</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 32
        for i in inventory:
            # SOURCE LINE 33
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(str( i.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(str( i.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 36
            __M_writer(str( i.availability))
            __M_writer('</td>\n\t\t  <td>')
            # SOURCE LINE 37
            __M_writer(str( i.category))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 38
            __M_writer(str( i.brand))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 39
            __M_writer(str( i.description))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 40
            __M_writer(str( i.price))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 41
            __M_writer(str( i.serial))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 42
            __M_writer(str( i.store_location))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 43
            __M_writer(str( i.shelf_location))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 44
            __M_writer(str( i.date_purchased))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 45
            __M_writer(str( i.comission_rate))
            __M_writer('</td>\n\t\t  <td><a href="/manage/edit_serial_inventory/')
            # SOURCE LINE 46
            __M_writer(str( i.id))
            __M_writer('/">Edit</a><a href="/manage/edit_serial_inventory__deactivate/')
            __M_writer(str( i.id))
            __M_writer('/"> Delete</a></td> \n\t\t</tr>\n')
        # SOURCE LINE 49
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


