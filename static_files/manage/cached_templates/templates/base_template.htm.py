# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396975206.645881
_enable_loop = True
_template_filename = 'C:\\app\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content']


# SOURCE LINE 5
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>My Stuff | Austen Smack</title>\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="/static/base_app/styles/bootstrap.css"/>\n    <script src="/static/base_app/scripts/bootstrap.js"></script>\n    <script src="/static/base_app/scripts/jquery.form.js"></script>\n    <script src="/static/base_app/scripts/jquery.loadmodal.js"></script>\n  \n')
        # SOURCE LINE 19
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n      <div id="top_container">\n        <div id="head_container">\n        <div id="header-left" class="col-md-1"></div>\n          <div id="header" class="col-md-7">\n            <img src="/static/base_app/images/mystufffinal.png">\n          </div>\n          <div id="login" class="col-md-4">\n')
        # SOURCE LINE 30
        if request.user.is_authenticated():
            # SOURCE LINE 31
            if request.user.is_superuser:
                # SOURCE LINE 32
                __M_writer('                <a href="/manage/"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-cog"></span> Manage</button></a>\n')
            # SOURCE LINE 34
            if request.user.is_staff:
                # SOURCE LINE 35
                __M_writer('                <a href="/catalog/employee_checkout/"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-shopping-cart"></span> Employee Checkout</button></a>\n')
            # SOURCE LINE 37
            __M_writer('              <a href="/account/login__logout/"><button type="button" class="btn btn-danger">Logout</button></a>\n')
            # SOURCE LINE 38
        else:
            # SOURCE LINE 39
            __M_writer('              <button id="login_button" class="btn btn-success"><span class="glyphicon glyphicon-lock"></span> Login</button>\n')
        # SOURCE LINE 41
        __M_writer('          </div>\n        </div>\n      </div>\n      <div id="nav_container">\n        <div id="navigation">\n            <div id="nav_right" class="col-md-12">\n              <nav id="navbar-example" class="navbar navbar-default navbar-static" role="navigation">\n                    <div class="container-fluid">\n                      <div class="navbar-header">\n                        <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".bs-example-js-navbar-collapse">\n                          <span class="sr-only">Toggle navigation</span>\n                          <span class="icon-bar"></span>\n                          <span class="icon-bar"></span>\n                          <span class="icon-bar"></span>\n                        </button>\n                        <a class="btn btn-default" href="/catalog/"><span class="glyphicon glyphicon-home"></a>\n                      </div>\n                      <div class="collapse navbar-collapse bs-example-js-navbar-collapse">\n                        <ul class="nav navbar-nav">\n                          <li class="dropdown">\n                            <a id="drop1" href="/catalog/categories/" role="button" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-tag"> Products <b class="caret"></b></a>\n                            <ul class="dropdown-menu" role="menu" aria-labelledby="drop1">\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/1/">Cameras</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/2/">Accessories</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/3/">Printers</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/4/">Storage</a></li>\n                            </ul>\n                          </li>\n                          <!--\n                          <li class="dropdown">\n                            <a href="#" id="drop2" role="button" class="dropdown-toggle" data-toggle="dropdown">Dropdown 2 <b class="caret"></b></a>\n                            <ul class="dropdown-menu" role="menu" aria-labelledby="drop2">\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Action</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Another action</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Something else here</a></li>\n                              <li role="presentation" class="divider"></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Separated link</a></li>\n                            </ul>\n                          </li>\n                          -->\n                        </ul>\n                        \n                        \n                        <ul class="nav navbar-nav navbar-right">\n                          <li id="fat-menu" class="dropdown">\n                            <a href="/catalog/cart/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-shopping-cart"></span> Cart</a>\n                          </li>\n                        </ul>\n')
        # SOURCE LINE 89
        if request.user.is_authenticated():
            # SOURCE LINE 90
            __M_writer('                          <ul class="nav navbar-nav navbar-right">\n                            <li id="fat-menu" class="dropdown">\n                              <a href="/account/my_account/" id="drop3" role="button" class="btn btn-defult" data-toggle="dropdown"><span class="glyphicon glyphicon-user"></span> My Account <b class="caret"></b></a>\n                              <ul class="dropdown-menu" role="menu" aria-labelledby="drop3">\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/my_account/">View Account</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_account/')
            # SOURCE LINE 95
            __M_writer(str( request.user.id))
            __M_writer('">Edit Account</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_password/">Change Password</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/view_repairs/">View Repair Status</a></li>\n                                <li role="presentation" class="divider"></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_account__deactivate/">Delete Account</a></li>\n                              </ul>\n                            </li>\n                          </ul>\n')
        # SOURCE LINE 104
        __M_writer('                      </div><!-- /.nav-collapse -->\n                    </div><!-- /.container-fluid -->\n                  </nav>\n            </div>\n        </div>\n      </div>\n      <div id="center_container" class="col-md-12">\n        <div id="main_container" class="col-md-12">\n          <div id="you_are_here" class="col-md-12"></div>\n          <div id="center">\n')
        # SOURCE LINE 115
        __M_writer('            <div class="col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        # SOURCE LINE 118
        __M_writer('\n            </div>\n')
        # SOURCE LINE 121
        __M_writer('            <div id="center_body" class="col-md-10">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 124
        __M_writer('\n            </div>\n')
        # SOURCE LINE 127
        __M_writer('          </div>\n        </div>\n      </div>\n      <div id="bottom_container" class="col-md-12">\n        <div id="footer_container" class="col-md-12">\n        </div>\n      </div>\n')
        # SOURCE LINE 135
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 116
        __M_writer('\n                 \n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 122
        __M_writer('\n                Site content goes here in sub-templates.\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


