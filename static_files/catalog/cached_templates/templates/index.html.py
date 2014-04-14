# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396977096.95685
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/index.html'
_template_uri = 'index.html'
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
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 37
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n      <ol class="carousel-indicators">\n        <li data-target="#carousel-example-captions" data-slide-to="0" class="active"></li>\n')
        # SOURCE LINE 10
        for p in products:
            # SOURCE LINE 11
            __M_writer('\t\t\t\t\t<li data-target="#carousel-example-captions" data-slide-to="')
            __M_writer(str( p.id))
            __M_writer('" class=""></li>\n')
        # SOURCE LINE 13
        __M_writer('      </ol>\n      <div class="carousel-inner">\n        <div class="item active">\n          <img  alt="900x500" src="/static/base_app/images/mystufffinal.png">\n          <div class="carousel-caption">\n            <h2>My Stuff Products</h2>\n          </div>\n        </div>\n')
        # SOURCE LINE 21
        for p in products:
            # SOURCE LINE 22
            __M_writer('        <div class="item">\n          <img  alt="')
            # SOURCE LINE 23
            __M_writer(str( p.product_name))
            __M_writer('" src="/static/catalog/images/product/large/')
            __M_writer(str( p.sku))
            __M_writer('.jpg">\n          <div class="carousel-caption">\n            <h2>')
            # SOURCE LINE 25
            __M_writer(str( p.product_name))
            __M_writer('</h2>\n          </div>\n        </div>\n')
        # SOURCE LINE 29
        __M_writer('    </div>\n    <a class="left carousel-control" href="#carousel-example-captions" data-slide="prev">\n      <span class="glyphicon glyphicon-chevron-left"></span>\n    </a>\n    <a class="right carousel-control" href="#carousel-example-captions" data-slide="next">\n      <span class="glyphicon glyphicon-chevron-right"></span>\n    </a>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


