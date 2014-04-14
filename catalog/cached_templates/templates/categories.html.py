# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397006380.187607
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/categories.html'
_template_uri = 'categories.html'
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
        categories = context.get('categories', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 30
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        categories = context.get('categories', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n<h1> Product Categories</h1>\n<br>\n<div id="category_page">\n\t<TABLE BORDER="0" cellpadding="0" CELLSPACING="0">\n\t\t\t\n\t\t  <thead>\n\t\t\t\t<tr>\n')
        # SOURCE LINE 14
        for category in categories:
            # SOURCE LINE 15
            __M_writer('\t\t\t\t <th><a href="/catalog/category/')
            __M_writer(str( category.id))
            __M_writer('"><h3>')
            __M_writer(str( category.category_name))
            __M_writer('</h3></a></th>\n')
        # SOURCE LINE 17
        __M_writer('\t\t\t </tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n\t\t\t<TR>\n')
        # SOURCE LINE 21
        for category in categories:
            # SOURCE LINE 22
            __M_writer('\t\t\t\t<TD WIDTH="200" HEIGHT="200" BACKGROUND="/static/catalog/images/category/')
            __M_writer(str( category.category_name))
            __M_writer('.jpg"> </TD>\n')
        # SOURCE LINE 24
        __M_writer('\t\t\t</TR>\n\t\t\n\t\t\t\n\t\t</TABLE>\n\t\t\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


