# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1716621075.2887964
_enable_loop = True
_template_filename = 'template/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


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
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<h1>WIP</h1>\r\n\r\n<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">\r\n    <ol class="carousel-indicators">\r\n      <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>\r\n      <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>\r\n      <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>\r\n    </ol>\r\n    <div class="carousel-inner">\r\n')
        for i in range(3):
            __M_writer('        <div class="carousel-item active">\r\n          <img class="d-block" src="/static/assets/bannière_symphonica.webp">\r\n        </div>\r\n')
        __M_writer('    </div>\r\n    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">\r\n      <span class="carousel-control-prev-icon" aria-hidden="true"></span>\r\n      <span class="sr-only">Previous</span>\r\n    </a>\r\n    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">\r\n      <span class="carousel-control-next-icon" aria-hidden="true"></span>\r\n      <span class="sr-only">Next</span>\r\n    </a>\r\n  </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 2, "35": 14, "36": 15, "37": 19, "43": 37}}
__M_END_METADATA
"""
