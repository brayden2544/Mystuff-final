# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396975206.588267
_enable_loop = True
_template_filename = 'C:\\app\\manage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left']


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
        

        # SOURCE LINE 164
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
        __M_writer('\n    <div class="panel-group" id="accordion">\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\n              <span class="glyphicon glyphicon-th-list"></span> &nbsp Stores \n            </a>\n          </h4>\n        </div>\n        <div id="collapseOne" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/stores/"><button type="button" class="btn btn-default btn-block">View All Stores</button></a>\n    \t\t\t\t<a href="/manage/edit_stores__new/"><button type="button" class="btn btn-default btn-block">Create New Store</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\n              <span class="glyphicon glyphicon-tags"></span> &nbsp Categories\n            </a>\n          </h4>\n        </div>\n        <div id="collapseTwo" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/category/"><button type="button" class="btn btn-default btn-block">View All Categories</button></a>\n    \t\t\t\t<a href="/manage/edit_category__new/"><button type="button" class="btn btn-default btn-block">Add New Category</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\n              <span class="glyphicon glyphicon-certificate"></span> &nbsp Brands\n            </a>\n          </h4>\n        </div>\n        <div id="collapseThree" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/brand/"><button type="button" class="btn btn-default btn-block">View All Brands</button></a>\n    \t\t\t\t<a href="/manage/edit_brand__new/"><button type="button" class="btn btn-default btn-block">Add New Brand</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\n              <span class="glyphicon glyphicon-tag"></span> &nbsp Products\n            </a>\n          </h4>\n        </div>\n        <div id="collapseFour" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/catalog_items/"><button type="button" class="btn btn-default btn-block">View All Catalog Items</button></a>\n    \t\t\t\t<a href="/manage/edit_catalog_items__new/"><button type="button" class="btn btn-default btn-block">Add New Catalog Item</button></a>\n    \t\t\t\t<a href="/manage/serial_inventory/"><button type="button" class="btn btn-default btn-block">View Serial Inventory</button></a>\n    \t\t\t\t<a href="/manage/edit_serial_inventory__new/"><button type="button" class="btn btn-default btn-block">Add Serial Item</button></a>\n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseFive">\n              <span class="glyphicon glyphicon-list-alt"></span> &nbsp Inventory \n            </a>\n          </h4>\n        </div>\n          <div id="collapseFive" class="panel-collapse collapse">\n            <div class="panel-body">\n              <a href="/manage/inventory/"><button type="button" class="btn btn-default btn-block">View Inventory</button></a>\n      \t\t\t\t<a href="/manage/add_inventory/"><button type="button" class="btn btn-default btn-block">Add Inventory by SKU</button></a>\n            </div>\n          </div>\n       </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseSix">\n              <span class="glyphicon glyphicon-time"></span> &nbsp Rentals \n            </a>\n          </h4>\n        </div>\n          <div id="collapseSix" class="panel-collapse collapse">\n            <div class="panel-body">\n              <a href="/manage/rental/"><button type="button" class="btn btn-default btn-block">Current Rentals</button></a>\n      \t\t\t\t<a href="/manage/overdue_rental/"><button type="button" class="btn btn-default btn-block">Overdue Rentals</button></a>\n            </div>\n          </div>\n       </div>\n       <div class="panel panel-default">\n         <div class="panel-heading">\n           <h4 class="panel-title">\n             <a data-toggle="collapse" data-parent="#accordion" href="#collapseSeven">\n               <span class="glyphicon glyphicon-wrench"></span> &nbsp Repairs\n             </a>\n           </h4>\n         </div>\n           <div id="collapseSeven" class="panel-collapse collapse">\n             <div class="panel-body">\n               <a href="/manage/create_repair/"><button type="button" class="btn btn-default btn-block">Check In New Repair</button></a>\n               <a href="/manage/repairs/"><button type="button" class="btn btn-default btn-block">View Current Repairs</button></a>\n       \t\t\t\t <a href="/manage/rental/"><button type="button" class="btn btn-default btn-block">Change Repair Status</button></a>\n               <a href="/manage/"><button type="button" class="btn btn-default btn-block">Test</button></a>\n             </div>\n           </div>\n        </div>\n        <div class="panel panel-default">\n          <div class="panel-heading">\n            <h4 class="panel-title">\n              <a data-toggle="collapse" data-parent="#accordion" href="#collapseEight">\n                <span class="glyphicon glyphicon-user"></span> &nbsp Users \n              </a>\n            </h4>\n          </div>\n        <div id="collapseEight" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/account/users/"><button type="button" class="btn btn-default btn-block">View All Users</button></a>\n            <a href="/account/edit_user__new/"><button type="button" class="btn btn-default btn-block">Create New User</button></a>\n            <a href="/account/new_employee_signup/"><button type="button" class="btn btn-default btn-block">Create New Employee</button></a>\n            <a href="/account/users__staff/"><button type="button" class="btn btn-default btn-block">View All Employees</button></a>  \n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseNine">\n              <span class="glyphicon glyphicon-book"></span> &nbsp Accounting \n            </a>\n          </h4>\n        </div>\n        <div id="collapseNine" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/balancesheet/"><button type="button" class="btn btn-default btn-block"> Balance Sheet</button></a>\n            <a href="/manage/incomesheet/"><button type="button" class="btn btn-default btn-block"> Income Statement</button></a>\n            <a href="/manage/comissions/"><button type="button" class="btn btn-default btn-block"> Comissions Report</button></a>\n            <a href="/manage/transactions/"><button type="button" class="btn btn-default btn-block"> Monthly Transactions</button></a>\n            <a href="/manage/employee_transactions/"><button type="button" class="btn btn-default btn-block"> Employee Transactions</button></a>  \n          </div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapseTen">\n              <span class="glyphicon glyphicon-off"></span> &nbsp Administration \n            </a>\n          </h4>\n        </div>\n        <div id="collapseTen" class="panel-collapse collapse">\n          <div class="panel-body">\n            <a href="/manage/administration/"><button type="button" class="btn btn-default btn-block">Administration Options</button></a>\n          </div>\n        </div>\n      </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


