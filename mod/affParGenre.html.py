# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717082318.2220147
_enable_loop = True
_template_filename = 'template/affParGenre.html'
_template_uri = 'affParGenre.html'
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
        genres = context.get('genres', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n<script>\r\n    var genres = ')
        __M_writer(str(json.dumps(genres)))
        __M_writer(';\r\n\r\n    function displayGenre() {\r\n        var dropdown = document.getElementById("genreDropdown");\r\n        var output = document.getElementById("selectedGenre");\r\n\r\n        var selectedGenre = dropdown.options[dropdown.selectedIndex].text;\r\n        output.innerHTML = selectedGenre;\r\n    }\r\n</script>\r\n\r\n<div class="container">\r\n    <h2>Choisissez un genre</h2>\r\n    <form action="Recherche_par_genre" method="post">\r\n        <select id="genreDropdown" name="genre" class="form-control" onchange="displayGenre()">\r\n            <option value="">Sélectionnez un genre</option>\r\n')
        for genre in genres:
            __M_writer('                <option value="')
            __M_writer(str(genre))
            __M_writer('">')
            __M_writer(str(genre))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n        <p>Genre sélectionné : <span id="selectedGenre"></span></p>\r\n        <button type="submit" class="btn btn-primary">Valider</button>\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/affParGenre.html", "uri": "affParGenre.html", "source_encoding": "utf-8", "line_map": {"16": 3, "17": 4, "18": 5, "19": 6, "31": 0, "37": 1, "38": 5, "39": 8, "40": 8, "41": 24, "42": 25, "43": 25, "44": 25, "45": 25, "46": 25, "47": 27, "53": 47}}
__M_END_METADATA
"""
