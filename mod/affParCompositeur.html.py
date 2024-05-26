# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1716736867.3304482
_enable_loop = True
_template_filename = 'template/affParCompositeur.html'
_template_uri = 'affParCompositeur.html'
_source_encoding = 'utf-8'
_exports = []



import json


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
        compositeurs = context.get('compositeurs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n<script>\r\n    var compositeurs = ')
        __M_writer(str(json.dumps(compositeurs)))
        __M_writer(';\r\n\r\n    function displayComposer() {\r\n        var dropdown = document.getElementById("composerDropdown");\r\n        var output = document.getElementById("selectedComposer");\r\n\r\n        var selectedComposer = dropdown.options[dropdown.selectedIndex].text;\r\n        output.innerHTML = selectedComposer;\r\n    }\r\n</script>\r\n\r\n<div class="container">\r\n    <h2>Choisissez un compositeur</h2>\r\n    <form action="Recherche_par_compositeur" method="post">\r\n        <select id="composerDropdown" name="composer" class="form-control" onchange="displayComposer()">\r\n            <option value="">Sélectionnez un compositeur</option>\r\n')
        for composer in compositeurs:
            __M_writer('                <option value="')
            __M_writer(str(composer))
            __M_writer('">')
            __M_writer(str(composer))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n        <p>Compositeur sélectionné : <span id="selectedComposer"></span></p>\r\n        <button type="submit" class="btn btn-primary">Valider</button>\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/affParCompositeur.html", "uri": "affParCompositeur.html", "source_encoding": "utf-8", "line_map": {"16": 3, "17": 4, "18": 5, "19": 6, "31": 0, "37": 1, "38": 5, "39": 8, "40": 8, "41": 24, "42": 25, "43": 25, "44": 25, "45": 25, "46": 25, "47": 27, "53": 47}}
__M_END_METADATA
"""
