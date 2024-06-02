# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717172280.1893494
_enable_loop = True
_template_filename = 'template/showrese.html'
_template_uri = 'showrese.html'
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
        rese = context.get('rese', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n')
        if rese:
            pass
            for re in rese:
                __M_writer('            <div class="concert-card">\r\n                <img src="/static/assets/scan.png" alt="Validation billet" class="concert-image">\r\n                <div class="concert-details">\r\n                    <h4>')
                __M_writer(str(re[2]))
                __M_writer('</h4>\r\n                    <p>')
                __M_writer(str(re[0]))
                __M_writer('</p>\r\n                    <p>')
                __M_writer(str(re[1]))
                __M_writer('</p>\r\n                </div>\r\n            </div>\r\n')
        else:
            __M_writer('        <p>pas de reservation</p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/showrese.html", "uri": "showrese.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 4, "36": 5, "37": 6, "38": 9, "39": 9, "40": 10, "41": 10, "42": 11, "43": 11, "44": 15, "45": 16, "46": 18, "52": 46}}
__M_END_METADATA
"""
