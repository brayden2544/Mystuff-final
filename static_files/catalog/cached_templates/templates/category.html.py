# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396977111.826546
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/category.html'
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
        products = context.get('products', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 31
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n<div class="row">\n  <a class="btn btn-default" href="/catalog/categories/"><span class="glyphicon glyphicon-chevron-left"></span> Back To Categories</a>\n</div>\n<h1> ')
        # SOURCE LINE 9
        __M_writer(str( category.category_name))
        __M_writer('</h1>\n<p>___________________________________________________________________________________________________________________________</p>\n<div id="category_list_page">\n')
        # SOURCE LINE 12
        for product in products:
            # SOURCE LINE 13
            __M_writer('\t\t<div class="row">\n\t\t  <div class="col-md-2">\n\t\t\t\t<a href="/catalog/product/')
            # SOURCE LINE 15
            __M_writer(str( product.sku))
            __M_writer('/"><img src="/static/catalog/images/product/thumb/')
            __M_writer(str( product.sku))
            __M_writer('-thumb.jpg" alt="')
            __M_writer(str( category.category_name))
            __M_writer('" class="img-thumbnail"></a>\n\t\t\t</div>\n\t\t  <div class="col-md-8">\n\t\t\t\t<a href="/catalog/product/')
            # SOURCE LINE 18
            __M_writer(str( product.sku))
            __M_writer('"><h3>')
            __M_writer(str( product.product_name))
            __M_writer('</h3></a></br>\n\t\t\t\t<strong>SKU: ')
            # SOURCE LINE 19
            __M_writer(str( product.sku))
            __M_writer(' </br> Brand: ')
            __M_writer(str( product.brand))
            __M_writer('</strong>\n\t\t\t</div>\n\t\t  <div class="col-md-2">\n\t\t\t\t<h3>$')
            # SOURCE LINE 22
            __M_writer(str( product.price))
            __M_writer('</h3>\n\t\t  \t<a class="btn btn-primary" href="/catalog/product/')
            # SOURCE LINE 23
            __M_writer(str( product.sku))
            __M_writer('">View Product Details</a>\n\t\t\t\t<a class="btn btn-success" href="/catalog/product__add_to_cart/')
            # SOURCE LINE 24
            __M_writer(str( product.id))
            __M_writer('"><span class="glyphicon glyphicon-shopping-cart"></span> Add to Cart</a>\n\t\t\t\t\n\t\t  </div>\n\t\t</div>\n\t\t<p>___________________________________________________________________________________________________________________________</p>\n')
        # SOURCE LINE 30
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


