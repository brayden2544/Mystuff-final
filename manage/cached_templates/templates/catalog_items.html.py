# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397182915.232056
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/catalog_items.html'
_template_uri = 'catalog_items.html'
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
        item = context.get('item', UNDEFINED)
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
        def content():
            return render_content(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> All Catalog Items</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/manage/edit_catalog_items__new/">Add Catalog Item</a>\n</div>\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>SKU</th>\n\t\t <th>Availability</th>\n\t\t <th>Catagory</th>\n\t\t <th>Brand</th>\n\t\t <th>Description</th>\n\t\t <th>Price</th>\n\t\t <th>Actions</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 27
        for c in item:
            # SOURCE LINE 28
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str( c.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(str( c.sku))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str( c.availability))
            __M_writer('</td>\n\t\t  <td>')
            # SOURCE LINE 32
            __M_writer(str( c.category))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(str( c.brand))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(str( c.description))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(str( c.price))
            __M_writer('</td>\n\t\t  <td><a href="/manage/edit_catalog_items/')
            # SOURCE LINE 36
            __M_writer(str( c.id))
            __M_writer('/">Edit</a><a href="/manage/edit_catalog_items__deactivate/')
            __M_writer(str( c.id))
            __M_writer('/"> Delete</a></td> \n\t\t</tr>\n')
        # SOURCE LINE 39
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


