# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396981716.971617
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/stores.html'
_template_uri = 'stores.html'
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
        stores = context.get('stores', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        stores = context.get('stores', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> All Stores</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/manage/edit_stores__new/">Create New Store</a>\n</div>\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>Store Number</th>\n\t\t <th>Location</th>\n\t\t <th>Street</th>\n\t\t <th>City</th>\n\t\t <th>State</th>\n\t\t <th>Zip</th>\n\t\t <th>Phone</th>\n\t\t <th>Hours</th>\n\t\t <th>Actions</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 29
        for s in stores:
            # SOURCE LINE 30
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str( s.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(str( s.store_number))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(str( s.location_name))
            __M_writer('</td>\n\t\t  <td>')
            # SOURCE LINE 34
            __M_writer(str( s.street))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(str( s.city))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 36
            __M_writer(str( s.state))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(str( s.zip_code))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 38
            __M_writer(str( s.phone))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 39
            __M_writer(str( s.hours))
            __M_writer('</td>\n\t\t\t<td><a href="/manage/edit_stores/')
            # SOURCE LINE 40
            __M_writer(str( s.id ))
            __M_writer('/">Edit</a><a href="/manage/edit_stores__deactivate/')
            __M_writer(str( s.id ))
            __M_writer('/"> Delete</a></td>\t\t\n\t\t</tr>\n')
        # SOURCE LINE 43
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


