# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397213555.938478
_enable_loop = True
_template_filename = 'C:\\app\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left']


# SOURCE LINE 5
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 7
        cart = request.session.get('cart', {}) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cart'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 8
        rental_cart = request.session.get('rental_cart', {}) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['rental_cart'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 9
        repair_cart = request.session.get('repair_cart', {}) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repair_cart'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 10
        user = request.user
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['user'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 11
        cart_items = len(cart) + len(rental_cart) + len(repair_cart)
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cart_items'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 12
        from manage import models as mmod 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mmod'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        # SOURCE LINE 13
        categories = mmod.Category.objects.all() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['categories'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>My Stuff</title>\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="/static/base_app/styles/bootstrap.css"/>\n    <script src="/static/base_app/scripts/bootstrap.js"></script>\n    <script src="/static/base_app/scripts/jquery.form.js"></script>\n    <script src="/static/base_app/scripts/jquery.loadmodal.js"></script>\n  \n')
        # SOURCE LINE 27
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\t\n  \n  </head>\n  <body>\n      <div id="top_container">\n        <div id="head_container">\n        <div id="header-left" class="col-md-1"></div>\n          <div id="header" class="col-md-7">\n            <img src="/static/base_app/images/mystuffbyu.png">\n          </div>\n          <div id="login" class="col-md-4">\n')
        # SOURCE LINE 39
        if request.user.is_authenticated():
            # SOURCE LINE 40
            if request.user.is_superuser:
                # SOURCE LINE 41
                __M_writer('                <a href="/manage/"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-cog"></span> Manage</button></a>\n')
            # SOURCE LINE 43
            if request.user.is_staff:
                # SOURCE LINE 44
                __M_writer('                <a href="/catalog/employee_checkout/"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-shopping-cart"></span> Employee Checkout</button></a><br />\n                <h5 class="pull-right">Welcome ')
                # SOURCE LINE 45
                __M_writer(str( user.username))
                __M_writer('</h5>\n')
            # SOURCE LINE 47
        else:
            # SOURCE LINE 48
            __M_writer('         <li><button id="login_button" class="btn btn-success"><span class="glyphicon glyphicon-lock"></span> Login</button></li>     \n\t\t\t  <h5 class="pull-right">Welcome Guest</h5>\n')
        # SOURCE LINE 51
        __M_writer('          </div>\n        </div>\n      </div>\n      <div id="nav_container">\n        <div id="navigation">\n            <div id="nav_right" class="col-md-12">\n              <nav id="navbar-example" class="navbar navbar-default navbar-static" role="navigation">\n                    <div class="container-fluid">\n  \n                      <div class="collapse navbar-collapse bs-example-js-navbar-collapse">\n                        <ul class="nav navbar-nav">\n                          <li>\n                              <a href="/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-home"></span> Home</a>\n                          </li>  \n                          <li class="dropdown">\n                            <a id="drop1" href="/catalog/categories/" role="button" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-tag"> Products <b class="caret"></b></a>\n                            <ul class="dropdown-menu" role="menu" aria-labelledby="drop1">\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/1/">Cameras</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/2/">Accessories</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/3/">Printers</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/category/4/">Storage</a></li>\n                            </ul>\n                          </li>\n                          <!--\n                          <li class="dropdown">\n                            <a href="#" id="drop2" role="button" class="dropdown-toggle" data-toggle="dropdown">Dropdown 2 <b class="caret"></b></a>\n                            <ul class="dropdown-menu" role="menu" aria-labelledby="drop2">\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Action</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Another action</a></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Something else here</a></li>\n                              <li role="presentation" class="divider"></li>\n                              <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Separated link</a></li>\n                            </ul>\n                          </li>\n                          -->\n                          <li>\n                              <a href="/catalog/rentable/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-time"></span> Rentable Products</a>\n                          </li>  \n                          <li>\n                              <a href="/catalog/cart/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-globe"></span> About Us</a>\n                          </li>\n                          <li>\n                              <a href="/catalog/cart/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-earphone"></span> Contact Us</a>\n                          </li>\n                        </ul>\n                        <ul class="nav navbar-nav navbar-right">\n\n                          <li id="fat-menu" class="dropdown">\n                            <a href="/catalog/cart/" id="drop3" role="button" class="btn btn-defult"><span class="glyphicon glyphicon-shopping-cart"></span> Cart &nbsp<span class="badge">')
        # SOURCE LINE 99
        __M_writer(str( cart_items))
        __M_writer('</span></a>\n                          </li>\n                        </ul>\n')
        # SOURCE LINE 102
        if request.user.is_authenticated():
            # SOURCE LINE 103
            __M_writer('                          <ul class="nav navbar-nav navbar-right">\n                            <li id="fat-menu" class="dropdown">\n                              <a href="/account/my_account/" id="drop3" role="button" class="btn btn-defult" data-toggle="dropdown"><span class="glyphicon glyphicon-user"></span> My Account <b class="caret"></b></a>\n                              <ul class="dropdown-menu" role="menu" aria-labelledby="drop3">\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/my_account/">View My Account</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_account/')
            # SOURCE LINE 108
            __M_writer(str( request.user.id))
            __M_writer('">Edit Account</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_password/">Change Password</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/catalog/view_repairs/">View Repair Status</a></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/edit_my_account__deactivate/">Delete Account</a></li>\n                                <li role="presentation" class="divider"></li>\n                                <li role="presentation"><a role="menuitem" tabindex="-1" href="/account/login__logout/">Log Out</a></li>\n                              </ul>\n                            </li>\n                          </ul>\n')
        # SOURCE LINE 118
        __M_writer('                      </div><!-- /.nav-collapse -->\n                    </div><!-- /.container-fluid -->\n                  </nav>\n            </div>\n        </div>\n      </div>\n      <div id="center_container" class="col-md-12">\n        <div id="main_container" class="col-md-12">\n          <div id="you_are_here" class="col-md-12"></div>\n          <div id="center">\n')
        # SOURCE LINE 129
        __M_writer('            <div class="col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        # SOURCE LINE 132
        __M_writer('\n            </div>\n')
        # SOURCE LINE 135
        __M_writer('            <div id="center_body" class="col-md-10">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 138
        __M_writer('\n            </div>\n')
        # SOURCE LINE 141
        __M_writer('          </div>\n        </div>\n      </div>\n\t  </div>\n  </div>\n      <div id="bottom_container" class="col-md-12">\n        <div id="footer_container" class="col-md-12">\n         <div class="row">\n            <div class="col-md-3"> <img class="pull-left" src="/static/base_app/images/mystuffmobilesmall2.png"></div>\n            <div class="col-md-3">\n                <h6><u>Categories</u></h6>\n                <ul class="list-unstyled">\n')
        # SOURCE LINE 153
        for c in categories: 
            # SOURCE LINE 154
            __M_writer('                    <li><h7><a href="/catalog/category/')
            __M_writer(str( c.id))
            __M_writer('">')
            __M_writer(str( c.category_name))
            __M_writer('</h7></li>\n')
        # SOURCE LINE 156
        __M_writer('                </ul>\n\n            </div>\n            <div class="col-md-3">\n                <h6><u>Information</u></h6>\n            </div>\n            <div class="col-md-3">\n                <h6>(801) 422-4222</h6>\n                <h6>Sales@Byuisys.com</h6><br />\n                <h6>Open Mon-Sat 9-5</h6>\n\n            </div>\n          </div>\n        </div>\n      </div>\n\n')
        # SOURCE LINE 173
        __M_writer('<script src="//static.getclicky.com/js" type="text/javascript"></script>\n<script type="text/javascript">try{ clicky.init(100726293); }catch(e){}</script>\n<noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/100726293ns.gif" /></p></noscript>\n\n')
        # SOURCE LINE 178
        __M_writer('\n    ')
        # SOURCE LINE 179
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 136
        __M_writer('\n                Site content goes here in sub-templates.\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 130
        __M_writer('\n                 \n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


