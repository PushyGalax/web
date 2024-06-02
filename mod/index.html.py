# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717314151.5972352
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
        concerts = context.get('concerts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<div class="container mt-5">\r\n  <h2 class="mb-4">Prochains Concerts</h2>\r\n')
        for concert in concerts:
            __M_writer('    <div class="concert-card">\r\n        <img src="/static/assets/concert1.jpg" alt="Concert" class="concert-image">\r\n        <div class="concert-details">\r\n            <h5>')
            __M_writer(str(concert[0]))
            __M_writer('</h5>\r\n            <p>Date : ')
            __M_writer(str(concert[1]))
            __M_writer('</p>\r\n            <p>Lieu : ')
            __M_writer(str(concert[2]))
            __M_writer('</p>\r\n        </div>\r\n    </div>\r\n')
        __M_writer('</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 2, "35": 7, "36": 8, "37": 11, "38": 11, "39": 12, "40": 12, "41": 13, "42": 13, "43": 17, "49": 43}}
__M_END_METADATA
"""
