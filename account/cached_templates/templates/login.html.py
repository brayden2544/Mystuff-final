# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397093033.541078
_enable_loop = True
_template_filename = 'C:\\app\\account\\templates/login.html'
_template_uri = 'login.html'
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
    return runtime._inherit_from(context, 'base_ajax_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 27
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n\t\t<form method="POST" action="/account/login/">\n\t\t\t<Login>\n\t\t\t<table>\n\t\t\t\t<tbody>\n\t\t\t    ')
        # SOURCE LINE 12
        __M_writer(str( form ))
        __M_writer('\n\t\t\t\t</tbody>\n\t\t\t</table>\n\t\t\t<a href="/account/forgot_password/">Forgot Password</a><br />\n\t\t\t</br>\n\t\t\t<input class="btn btn-success" type="submit" value="Login"/> &nbsp <a class="btn btn-default" href="/account/new_user_signup/">Create an account</a> &nbsp \n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


