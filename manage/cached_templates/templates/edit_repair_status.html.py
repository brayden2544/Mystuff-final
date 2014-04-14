# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397070495.848816
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/edit_repair_status.html'
_template_uri = 'edit_repair_status.html'
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
        repair = context.get('repair', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        customer = context.get('customer', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        import datetime
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 24
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        repair = context.get('repair', UNDEFINED)
        def content():
            return render_content(context)
        customer = context.get('customer', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> Update Repair Status</h1>\n<h3>')
        # SOURCE LINE 9
        __M_writer(str( customer.first_name))
        __M_writer(' ')
        __M_writer(str( customer.last_name))
        __M_writer('</h3>\n<h4>Repair ID:')
        # SOURCE LINE 10
        __M_writer(str( repair.id))
        __M_writer('</h4>\n<h4>Date Checked In: ')
        # SOURCE LINE 11
        __M_writer(str( repair.date_in))
        __M_writer('</h4>\n<h4>Expected Return: ')
        # SOURCE LINE 12
        __M_writer(str( repair.expected_return))
        __M_writer('</h4><br />\n<div class="row" style="text-align:center">\n    <form method="POST">\n        <table>\n            <tbody>\n                ')
        # SOURCE LINE 17
        __M_writer(str( form))
        __M_writer('\n            </tbody>\n        </table>\n        <input class="btn btn-success" type="submit" value="Update Status" />\n    </form>\n</div>  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


