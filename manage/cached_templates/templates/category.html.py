# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397071819.547057
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/category.html'
_template_uri = 'category.html'
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
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 33
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Categories</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/manage/edit_category__new/">Create New Category</a>\n</div>\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>Category Name</th>\n\t\t <th>Category Description</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 22
        for c in category:
            # SOURCE LINE 23
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 24
            __M_writer(str( c.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 25
            __M_writer(str( c.category_name))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 26
            __M_writer(str( c.category_description))
            __M_writer('</td>\n\t\t\t<td><a href="/manage/edit_category/')
            # SOURCE LINE 27
            __M_writer(str( c.id ))
            __M_writer('/">Edit</a>\n\t\t</tr>\n')
        # SOURCE LINE 30
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


