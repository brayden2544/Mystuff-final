# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396977096.969555
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left']


# SOURCE LINE 4

from manage import models as mmod
    

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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        # SOURCE LINE 27
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n    ')
        # SOURCE LINE 6
        __M_writer('\n    <div class="panel-group" id="accordion">\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion"><a href="/catalog/categories/">\n              <span class="glyphicon glyphicon-shopping-cart"></span> &nbsp Products\n            </a>\n          </h4>\n        </div>\n        <div id="collapseOne" class="panel-collapse collapse in">\n          <div class="panel-body">\n')
        # SOURCE LINE 18
        for value in mmod.Category.objects.all():
            # SOURCE LINE 19
            __M_writer('            <a href="/catalog/category/')
            __M_writer(str( value.id))
            __M_writer('/"><button type="button" class="btn btn-default btn-block">')
            __M_writer(str( value))
            __M_writer('</button></a>\n')
        # SOURCE LINE 21
        __M_writer('          </div>\n        </div>\n      </div></br>\n      \n            <button type="button" id="search_button" class="btn btn-primary btn-block"><span class="glyphicon glyphicon-search"></span> Product Search</button>\n      </div>   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


