# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397181785.742404
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/product.html'
_template_uri = 'product.html'
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
        product = context.get('product', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 95
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n<div class="row">\n  <a class="btn btn-default" href="/catalog/category/')
        # SOURCE LINE 8
        __M_writer(str( product.category.id))
        __M_writer('/"><span class="glyphicon glyphicon-chevron-left"></span> Back To ')
        __M_writer(str( product.category.category_name))
        __M_writer('</a>\n</div>\n<h2> ')
        # SOURCE LINE 10
        __M_writer(str( product.product_name))
        __M_writer('</h2>\n<div id="product_info">\n\t<div class="row">\n\t  <div class="col-md-4">\n\t  \t<img class="img-thumbnail" src="/static/catalog/images/product/large/')
        # SOURCE LINE 14
        __M_writer(str( product.sku))
        __M_writer('.jpg"><br />\n\n\n\t  </div>\n\t  <div class="col-md-5">\n\t\t\t<strong>SKU: ')
        # SOURCE LINE 19
        __M_writer(str( product.sku))
        __M_writer('&nbsp|&nbspBrand: ')
        __M_writer(str( product.brand))
        __M_writer('</strong><br><br>\n\t\t\t<p>')
        # SOURCE LINE 20
        __M_writer(str( product.description))
        __M_writer('<br><p>\n\n\t\t\t\n\t  </div>\n\t\t<div class="col-md-3">\n\t\t\t<h3 class="text-danger">Our Price: $')
        # SOURCE LINE 25
        __M_writer(str( product.price))
        __M_writer('</h3><br>\n\t\t\t<a class="btn btn-success" href="/catalog/product__add_to_cart/')
        # SOURCE LINE 26
        __M_writer(str( product.id))
        __M_writer('/"><span class="glyphicon glyphicon-shopping-cart"></span> Add to Cart</a><br />\n')
        # SOURCE LINE 27
        if product.rentable == True:
            # SOURCE LINE 28
            __M_writer('\t\t\t\t\t<br />\n')
        # SOURCE LINE 30
        __M_writer('\t\t\t\t\t\t\n\t\t</div>\n\t</div>\n\t<div id="Product Options">\n\t\t<div class="row">\n\t\t\t<div class="col-md-4">\n\t\t\t\t<br /><br />\n\t\t\t\t<center><img class="img-thumbnail"src="/static/catalog/images/brand/')
        # SOURCE LINE 37
        __M_writer(str( product.brand))
        __M_writer('.jpg"></center>\n\t\t\t</div>\n\t\t\t<div class="col-md-5">\n')
        # SOURCE LINE 40
        if product.rentable == True:
            # SOURCE LINE 41
            __M_writer('\t\t\t\t<h3> You can also rent this item!</h3>\n\t\t\t\t<table class="table table-striped">\n\t\t\t\t      <thead>\n\t\t\t\t        <tr>\n\t\t\t\t          <th>Rental Option</th>\n\t\t\t\t          <th>Length</th>\n\t\t\t\t          <th>Cost</th>\n\t\t\t\t          <th>Rent Now!</th>\n\t\t\t\t        </tr>\n\t\t\t\t      </thead>\n\t\t\t\t      <tbody>\n\t\t\t\t        <tr>\n\t\t\t\t          <td>1</td>\n\t\t\t\t          <td>5 Days</td>\n\t\t\t\t          <td>$')
            # SOURCE LINE 55
            __M_writer(str( 5 * product.daily_rent_rate))
            __M_writer('</td>\n\t\t\t\t          <td><a class="btn btn-primary" href="/catalog/product__add_rental_to_cart/')
            # SOURCE LINE 56
            __M_writer(str( product.id))
            __M_writer('/5/"><span class="glyphicon glyphicon-shopping-cart"></span> Rent Now!</a></td>\n\t\t\t\t        </tr>\n\t\t\t\t        <tr>\n\t\t\t\t          <td>2</td>\n\t\t\t\t          <td>10 Days</td>\n\t\t\t\t          <td>$')
            # SOURCE LINE 61
            __M_writer(str( 10 * product.daily_rent_rate))
            __M_writer('</td>\n\t\t\t\t          <td><a class="btn btn-primary" href="/catalog/product__add_rental_to_cart/')
            # SOURCE LINE 62
            __M_writer(str( product.id))
            __M_writer('/10/"><span class="glyphicon glyphicon-shopping-cart"></span> Rent Now!</a></td>\n\t\t\t\t        </tr>\n\t\t\t\t        <tr>\n\t\t\t\t          <td>3</td>\n\t\t\t\t          <td>15 Days</td>\n\t\t\t\t          <td>$')
            # SOURCE LINE 67
            __M_writer(str( 15 * product.daily_rent_rate))
            __M_writer('</td>\n\t\t\t\t          <td><a class="btn btn-primary" href="/catalog/product__add_rental_to_cart/')
            # SOURCE LINE 68
            __M_writer(str( product.id))
            __M_writer('/15/"><span class="glyphicon glyphicon-shopping-cart"></span> Rent Now!</a></td>\n\t\t\t\t        </tr>\n\t\t\t\t      </tbody>\n\t\t\t\t    </table>\n')
        # SOURCE LINE 73
        __M_writer('\t\t\t</div>\n\t\t\t<div class="col-md-3"></div>\n\t\t</div>\n\n\t</div>\n\t\n\t<div class="row">\n\t\t<p>___________________________________________________________________________________________________________________________</p>\n\t  <div class="col-md-12"><h3>More ')
        # SOURCE LINE 81
        __M_writer(str( product.category.category_name))
        __M_writer(' in this Category</h3></div>\n\t</div>\n</div>\n\n\n\n')
        # SOURCE LINE 87
        for p in products:
            # SOURCE LINE 88
            if p != product:
                # SOURCE LINE 89
                __M_writer('\t<a href="/catalog/product/')
                __M_writer(str( p.sku))
                __M_writer('/"><img class="img-thumbnail" src="/static/catalog/images/product/thumb/')
                __M_writer(str( p.sku))
                __M_writer('-thumb.jpg"></a>\n')
        # SOURCE LINE 92
        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


