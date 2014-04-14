# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397228117.046559
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
        brands = context.get('brands', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' %>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 63
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        brands = context.get('brands', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n<div class="row">\n  <div class="col-xs-12 col-md-12">&nbsp</div>\n</div>\n<div class="row">\n  <div class="col-md-12">\n    <div class="row">\n      <div class="col-md-9">\n      <img class="img-responsive" alt="Meyer Photography" src="/static/catalog/images/digitallife3.png"><br />\n      <div class="table-responsive">\n      <table class="table">\n        <tbody>\n          <tr>\n            <td><a href="/catalog/category/1/"><img class="img-responsive" alt="Professional Cameras" src="/static/catalog/images/cameras.png"></a><br /></td>\n            <td><a href="/catalog/rentable/"><img class="img-responsive" alt="Camera Rentals" src="/static/catalog/images/rentals.png"></a><br /></td>\n            <td><img class="img-responsive" alt="Meyer Photography" src="/static/catalog/images/certifiedrepair.png"><br /></td>\n          </tr>\n        </tbody>\n      </table>\n    </div>\n\n      </div>\n      <div class="col-md-3">\n        <div id="carousel" class="carousel slide" data-ride="carousel">\n          <ol class="carousel-indicators">\n            <li data-target="#carousel-example-captions" data-slide-to="1" class="active"></li>\n          </ol>\n          <div class="carousel-inner">\n            <div class="item active">\n              <img  alt="900x500" src="/static/base_app/images/mystufffinal.png">\n              <div class="carousel-caption">\n                <h6>My Stuff Products</h6>\n              </div>\n            </div>\n')
        # SOURCE LINE 39
        for p in products:
            # SOURCE LINE 40
            __M_writer('            <div class="item">\n              <img  alt="')
            # SOURCE LINE 41
            __M_writer(str( p.product_name))
            __M_writer('" src="/static/catalog/images/product/large/')
            __M_writer(str( p.sku))
            __M_writer('.jpg">\n              <div class="carousel-caption">\n                <h6>')
            # SOURCE LINE 43
            __M_writer(str( p.product_name))
            __M_writer('</h6>\n              </div>\n            </div>\n')
        # SOURCE LINE 47
        __M_writer('        </div>\n      </div>\n  </div>\n</div>\n<div class="row">\n  <div class="col-md-12">\n      <p class="lead" id="shopbybrand">&nbsp&nbspShop by Brand</p>\n      <ul class="list-inline">\n\n')
        # SOURCE LINE 56
        for b in brands:
            # SOURCE LINE 57
            __M_writer('        <li><a href="/catalog/brand/')
            __M_writer(str( b.id))
            __M_writer('/"><img class="img-thumbnail"src="/static/catalog/images/brand/')
            __M_writer(str( b.brand_name))
            __M_writer('.jpg" width="140" height="70"></li>\n')
        # SOURCE LINE 59
        __M_writer('       </ul>\n  </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


