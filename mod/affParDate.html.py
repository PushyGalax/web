# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717138238.4121575
_enable_loop = True
_template_filename = 'template/affParDate.html'
_template_uri = 'affParDate.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n<script>\r\n    function displayDate() {\r\n        var dropdown = document.getElementById("concertDate");\r\n        var output = document.getElementById("selecteddate");\r\n\r\n        var selecteddate = dropdown.value;\r\n        output.innerHTML = selecteddate;\r\n    }\r\n</script>\r\n\r\n<div class="container">\r\n    <h2>Choisissez une date de concert</h2>\r\n    <form action="Recherche_par_date" method="post">\r\n        <div class="form-group">\r\n            <label for="concertDate">Date de concert</label>\r\n            <input type="date" id="concertDate" name="concertDate" class="form-control" onchange="displayDate()" required>\r\n        </div>\r\n        <p>date sélectionné : <span id="selecteddate"></span></p>\r\n        <button type="submit" class="btn btn-primary">Valider</button>\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/affParDate.html", "uri": "affParDate.html", "source_encoding": "utf-8", "line_map": {"16": 3, "17": 4, "18": 5, "19": 6, "31": 0, "36": 1, "37": 5, "43": 37}}
__M_END_METADATA
"""
