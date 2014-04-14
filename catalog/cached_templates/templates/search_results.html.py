# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397231807.053626
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/search_results.html'
_template_uri = 'search_results.html'
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
        search = context.get('search', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 39
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        search = context.get('search', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n<div class="row">\n  <a class="btn btn-default" href="/catalog/search/"><span class="glyphicon glyphicon-chevron-left"></span> Back To Search</a>\n</div>\n<h1> Search Results for ')
        # SOURCE LINE 10
        __M_writer(str( search))
        __M_writer('</h1>\n<p>___________________________________________________________________________________________________________________________</p>\n<div id="category_list_page">\n')
        # SOURCE LINE 13
        if products.count() > 0:
            # SOURCE LINE 14
            for p in products:
                # SOURCE LINE 15
                __M_writer('\t\t\t<div class="row">\n\t\t\t  <div class="col-md-2">\n\t\t\t\t\t<a href="/catalog/product/')
                # SOURCE LINE 17
                __M_writer(str( p.sku))
                __M_writer('/"><img src="/static/catalog/images/product/thumb/')
                __M_writer(str( p.sku))
                __M_writer('-thumb.jpg" alt="" class="img-thumbnail"></a>\n\t\t\t\t</div>\n\t\t\t  <div class="col-md-8">\n\t\t\t\t\t<a href="/catalog/product/')
                # SOURCE LINE 20
                __M_writer(str( p.sku))
                __M_writer('"><h3>')
                __M_writer(str( p.product_name))
                __M_writer('</h3></a></br>\n\t\t\t\t\t<strong>SKU: ')
                # SOURCE LINE 21
                __M_writer(str( p.sku))
                __M_writer(' </br> Brand: ')
                __M_writer(str( p.brand))
                __M_writer('</strong>\n\t\t\t\t</div>\n\t\t\t  <div class="col-md-2">\n\t\t\t\t\t<h3>$')
                # SOURCE LINE 24
                __M_writer(str( p.price))
                __M_writer('</h3>\n\t\t\t  \t<a class="btn btn-primary" href="/catalog/product/')
                # SOURCE LINE 25
                __M_writer(str( p.sku))
                __M_writer('">View Product Details</a>\n\t\t\t\t\t<a class="btn btn-success" href="/manage/Setup_Default_Store/"><span class="glyphicon glyphicon-shopping-cart"></span> Add to Cart</a>\n\t\t\t\t\n\t\t\t  </div>\n\t\t\t</div>\n\t\t\t<p>___________________________________________________________________________________________________________________________</p>\n')
            # SOURCE LINE 32
        else:
            # SOURCE LINE 33
            __M_writer('\t\t<h2>Sorry there were no results matching your search.</h2>\n')
        # SOURCE LINE 35
        __M_writer('</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


