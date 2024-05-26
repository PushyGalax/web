# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1716734947.8630364
_enable_loop = True
_template_filename = 'template/concertDetails.html'
_template_uri = 'concertDetails.html'
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
        concert_ = context.get('concert_', UNDEFINED)
        morc = context.get('morc', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Détails du concert : ')
        __M_writer(str(concert_[8]))
        __M_writer('</h2>\r\n    <img src="/static/assets/')
        __M_writer(str(concert_[6]))
        __M_writer('" alt="Image de ')
        __M_writer(str(concert_[8]))
        __M_writer('" class="img-fluid">\r\n    <ul>\r\n        <li><strong>Date :</strong> ')
        __M_writer(str(concert_[0]))
        __M_writer('</li>\r\n        <li><strong>Lieu :</strong> ')
        __M_writer(str(concert_[1]))
        __M_writer('</li>\r\n        <li><strong>Formation :</strong> ')
        __M_writer(str(concert_[2]))
        __M_writer("</li>\r\n        <li><strong>Chef d'orchestre :</strong> ")
        __M_writer(str(concert_[3]))
        __M_writer('</li>\r\n        <li><strong>Soliste :</strong> ')
        __M_writer(str(concert_[4]))
        __M_writer('</li>\r\n        <li><strong>Prix :</strong> ')
        __M_writer(str(concert_[5]))
        __M_writer('€</li>\r\n        <li><strong>Genre :</strong> ')
        __M_writer(str(concert_[6]))
        __M_writer('</li>\r\n        <li><strong>Durée :</strong> ')
        __M_writer(str(concert_[7]))
        __M_writer(' minutes</li>\r\n        <li><strong>Morceaux :</strong>\r\n            <ul>\r\n')
        for morceau in morc:
            __M_writer('                    <li>')
            __M_writer(str(morceau))
            __M_writer('</li>\r\n')
        __M_writer('            </ul>\r\n        </li>\r\n    </ul>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/concertDetails.html", "uri": "concertDetails.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 4, "36": 4, "37": 5, "38": 5, "39": 5, "40": 5, "41": 7, "42": 7, "43": 8, "44": 8, "45": 9, "46": 9, "47": 10, "48": 10, "49": 11, "50": 11, "51": 12, "52": 12, "53": 13, "54": 13, "55": 14, "56": 14, "57": 17, "58": 18, "59": 18, "60": 18, "61": 20, "67": 61}}
__M_END_METADATA
"""
