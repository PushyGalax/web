# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717171310.388175
_enable_loop = True
_template_filename = 'template/confirmation.html'
_template_uri = 'confirmation.html'
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
        nom = context.get('nom', UNDEFINED)
        concert = context.get('concert', UNDEFINED)
        prenom = context.get('prenom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Confirmation de Réservation</h2>\r\n    <ul>\r\n        <li><strong>Nom :</strong> ')
        __M_writer(str(nom))
        __M_writer('</li>\r\n        <li><strong>Prénom :</strong> ')
        __M_writer(str(prenom))
        __M_writer('</li>\r\n        <li><strong>Nom du Concert :</strong> ')
        __M_writer(str(concert))
        __M_writer('</li>\r\n    </ul>\r\n    <div>\r\n        <h3>Votre QR Code :</h3>\r\n        <img src="/static/assets/scan.png" alt="QR Code">\r\n    </div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/confirmation.html", "uri": "confirmation.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 6, "37": 6, "38": 7, "39": 7, "40": 8, "41": 8, "47": 41}}
__M_END_METADATA
"""
