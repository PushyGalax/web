# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1716734849.8011854
_enable_loop = True
_template_filename = 'template/RechercheParCompositeur.html'
_template_uri = 'RechercheParCompositeur.html'
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
        composer = context.get('composer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Concerts pour le compositeur : ')
        __M_writer(str(composer))
        __M_writer('</h2>\r\n')
        if concerts:
            pass
            for concert in concerts:
                __M_writer('            <div class="concert-card" onclick="window.location.href=\'/concertDetails?id_=')
                __M_writer(str(concert[3]))
                __M_writer('\'">\r\n                <img src="/static/assets/')
                __M_writer(str(concert[0]))
                __M_writer('.png" alt="Image de ')
                __M_writer(str(concert[4]))
                __M_writer('" class="concert-image">\r\n                <div class="concert-details">\r\n                    <h4>')
                __M_writer(str(concert[0]))
                __M_writer('</h4>\r\n                    <p>')
                __M_writer(str(concert[1]))
                __M_writer('</p>\r\n                    <p>')
                __M_writer(str(concert[2]))
                __M_writer('</p>\r\n                </div>\r\n            </div>\r\n')
        else:
            __M_writer('        <p>Aucun concert trouvé pour ce compositeur.</p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/RechercheParCompositeur.html", "uri": "RechercheParCompositeur.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 4, "36": 4, "37": 5, "39": 6, "40": 7, "41": 7, "42": 7, "43": 8, "44": 8, "45": 8, "46": 8, "47": 10, "48": 10, "49": 11, "50": 11, "51": 12, "52": 12, "53": 16, "54": 17, "55": 19, "61": 55}}
__M_END_METADATA
"""
