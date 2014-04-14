# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397145304.579715
_enable_loop = True
_template_filename = 'C:\\app\\account\\templates/my_account.html'
_template_uri = 'my_account.html'
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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 27
        __M_writer('  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> My Account</h1>\n\t\n<br>\n<div id="account_page">\n\t<div id="class="col-md-4"></div>\n\t<div id="class="col-md-1"></div>\n\t  <div id="account_info" class="col-md-6">\n\t\t\t\t<strong>Username: ')
        # SOURCE LINE 15
        __M_writer(str( user.username))
        __M_writer('</strong></br>\n\t\t\t\t<strong>First Name: ')
        # SOURCE LINE 16
        __M_writer(str( user.first_name))
        __M_writer('</strong></br>\n\t\t\t  <strong>Last Name: ')
        # SOURCE LINE 17
        __M_writer(str( user.last_name))
        __M_writer('</strong></br>\n\t\t\t\t<strong>Email: ')
        # SOURCE LINE 18
        __M_writer(str( user.email))
        __M_writer('</strong></br>\n\t\t\t\t<strong>Address: ')
        # SOURCE LINE 19
        __M_writer(str( user.address))
        __M_writer('</strong></br>\n\t\t\t\t<strong>City: ')
        # SOURCE LINE 20
        __M_writer(str( user.city))
        __M_writer('</strong></br>\n\t\t\t\t<strong>State: ')
        # SOURCE LINE 21
        __M_writer(str( user.state))
        __M_writer('</strong></br>\n\t\t\t\t<strong>ZIP: ')
        # SOURCE LINE 22
        __M_writer(str( user.zip_code))
        __M_writer('</strong></br>\n\t  </div>\n\t<div id="class="col-md-1"></div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


