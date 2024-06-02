# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717316998.3557746
_enable_loop = True
_template_filename = 'template/updateTable.html'
_template_uri = 'updateTable.html'
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
        field = context.get('field', UNDEFINED)
        entry = context.get('entry', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Mettre à jour les informations</h2>\r\n    <form action="/submitUpdate" method="post">\r\n        <input type="hidden" name="entry_id" value="')
        __M_writer(str(entry['id']))
        __M_writer('">\r\n')
        for key, value in entry.items():
            pass
            if field != 'id':
                __M_writer('                <div class="form-group">\r\n                    <label for="')
                __M_writer(str(field))
                __M_writer('">')
                __M_writer(str(field.capitalize()))
                __M_writer('</label>\r\n                    <input type="text" class="form-control" id="')
                __M_writer(str(field))
                __M_writer('" name="')
                __M_writer(str(field))
                __M_writer('" value="')
                __M_writer(str(value))
                __M_writer('" required>\r\n                </div>\r\n')
        __M_writer('        <button type="submit" class="btn btn-primary">Mettre à jour</button>\r\n    </form>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/updateTable.html", "uri": "updateTable.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 6, "36": 6, "37": 7, "39": 8, "40": 9, "41": 10, "42": 10, "43": 10, "44": 10, "45": 11, "46": 11, "47": 11, "48": 11, "49": 11, "50": 11, "51": 15, "57": 51}}
__M_END_METADATA
"""
