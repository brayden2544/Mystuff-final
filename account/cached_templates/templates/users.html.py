# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397091724.197071
_enable_loop = True
_template_filename = 'C:\\app\\account\\templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer('\n    <div class="panel-group" id="accordion">\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\n              <span class="glyphicon glyphicon-shopping-cart"></span> &nbsp Stores \n            </a>\n          </h4>\n        </div>\n        <div id="collapseOne" class="panel-collapse collapse in">\n          <div class="panel-body">\n            <a href="/manage/stores/"><button type="button" class="btn btn-default btn-block">View All Stores</button></a>\n    \t\t\t\t<a href="/manage/edit_stores__new/"><button type="button" class="btn btn-default btn-block">Create New Store</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\n              <span class="glyphicon glyphicon-tags"></span> &nbsp Products\n            </a>\n          </h4>\n        </div>\n        <div id="collapseTwo" class="panel-collapse collapse in">\n          <div class="panel-body">\n            <a href="/manage/catalog_items/"><button type="button" class="btn btn-default btn-block">View All Catalog Items</button></a>\n    \t\t\t\t<a href="/manage/catalog_items__new/"><button type="button" class="btn btn-default btn-block">Add New Catalog Item</button></a>\n    \t\t\t\t<a href="/manage/physical_inventory/"><button type="button" class="btn btn-default btn-block">View Current Inventory</button></a>\n    \t\t\t\t<a href="/manage/physical_inventory__new/"><button type="button" class="btn btn-default btn-block">Add New Inventory</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\n              <span class="glyphicon glyphicon-user"></span> &nbsp Users \n            </a>\n          </h4>\n        </div>\n        <div id="collapseThree" class="panel-collapse collapse in">\n          <div class="panel-body">\n            <a href="/account/users/"><button type="button" class="btn btn-default btn-block">View All Users</button></a> \n          </div>\n        </div>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        users = context.get('users', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n\n<h1> ')
        # SOURCE LINE 8
        __M_writer(str( title))
        __M_writer('</h1>\n<div class="pull-right">\n\t<a class="btn btn-success" href="/account/edit_user__new/">Create New User</a>\n</div>\t\n\n<table class="table table-striped">\n  <thead>\n\t\t<tr>\n\t\t <th>ID</th>\n\t\t <th>Username</th>\n\t\t <th>First Name</th>\n\t\t <th>Last Name</th>\n\t\t <th>Email</th>\n\t\t <th>Address</th>\n\t\t <th>City</th>\n\t\t <th>State</th>\n\t\t <th>Zip</th>\n\t\t <th>Actions</th>\n\t </tr>\n\t</thead>\n\t<tbody>\n')
        # SOURCE LINE 29
        for u in users:
            # SOURCE LINE 30
            __M_writer('\t\t<tr>\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str( u.id))
            __M_writer('</td> \n\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(str( u.username))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(str( u.first_name))
            __M_writer('</td>\n\t\t  <td>')
            # SOURCE LINE 34
            __M_writer(str( u.last_name))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(str( u.email))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 36
            __M_writer(str( u.address))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(str( u.city))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 38
            __M_writer(str( u.state))
            __M_writer('</td>\n\t\t\t<td>')
            # SOURCE LINE 39
            __M_writer(str( u.zip_code))
            __M_writer('</td>\n\t\t\t<td><a href="/account/edit_user/')
            # SOURCE LINE 40
            __M_writer(str( u.id ))
            __M_writer('/">Edit</a><a href="/account/edit_user__deactivate/')
            __M_writer(str( u.id ))
            __M_writer('/"> Delete</a></td>\n\t\t</tr>\n')
        # SOURCE LINE 43
        __M_writer('\t</tbody>\n</table>\t  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


