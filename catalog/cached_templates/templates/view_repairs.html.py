# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397072469.722762
_enable_loop = True
_template_filename = 'C:\\app\\catalog\\templates/view_repairs.html'
_template_uri = 'view_repairs.html'
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
        repairs = context.get('repairs', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        

        # SOURCE LINE 44
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        repairs = context.get('repairs', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> My Current Repairs</h1>\n\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>Repair ID</th>\n\t\t <th>Repair Item</th>\n\t\t <th>Status</th>\n\t\t <th>Issue</th>\n\t\t <th>Damage Report</th>\n\t\t <th>Expected Return</th>\n\t\t <th>Repair Fees</th>\n\t\t <th>Pay Now</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 25
        for r in repairs:
            # SOURCE LINE 26
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str( r.id))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str( r.repair_item))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str( r.status.status))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(str( r.issue))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str( r.damage_report))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(str( r.expected_return))
            __M_writer('</td>\n\t\t\t<td>$')
            # SOURCE LINE 33
            __M_writer(str( r.repair_fees))
            __M_writer('</td>\n')
            # SOURCE LINE 34
            if r.paid_for == False:
                # SOURCE LINE 35
                __M_writer('\t\t\t\t<td><a class="btn btn-primary" href="/catalog/view_repairs__add_to_cart/')
                __M_writer(str( r.id))
                __M_writer('/"><span class="glyphicon glyphicon-shopping-cart"></span> Pay Now!</a></td>\n')
                # SOURCE LINE 36
            else:
                # SOURCE LINE 37
                __M_writer('\t\t\t\t<td>Already Paid</td>\n')
            # SOURCE LINE 39
            __M_writer('\t\t</tr>\n')
        # SOURCE LINE 41
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


