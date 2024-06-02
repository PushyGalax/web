# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717311265.5718646
_enable_loop = True
_template_filename = 'template/deleteTable.html'
_template_uri = 'deleteTable.html'
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
        headers = context.get('headers', UNDEFINED)
        table_content = context.get('table_content', UNDEFINED)
        table = context.get('table', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Données de la table : ')
        __M_writer(str(table))
        __M_writer('</h2>\r\n')
        if table_content:
            __M_writer('        <table class="table table-bordered">\r\n            <thead>\r\n                <tr>\r\n')
            for header in headers:
                __M_writer('                        <th>')
                __M_writer(str(header))
                __M_writer('</th>\r\n')
            __M_writer('                    <th>Actions</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
            for row in table_content:
                __M_writer('                    <tr>\r\n')
                for item in row:
                    __M_writer('                            <td>')
                    __M_writer(str(item))
                    __M_writer('</td>\r\n')
                __M_writer('                        <td>\r\n                            <form action="deleteEntry" method="post" style="display:inline;">\r\n                                <input type="hidden" name="table" value="')
                __M_writer(str(table))
                __M_writer('">\r\n                                <input type="hidden" name="id" value="')
                __M_writer(str(row[0]))
                __M_writer('">\r\n                                <button type="submit" class="btn btn-danger">Supprimer</button>\r\n                            </form>\r\n                        </td>\r\n                    </tr>\r\n')
            __M_writer('            </tbody>\r\n        </table>\r\n')
        else:
            __M_writer('        <p>Aucune donnée trouvée pour cette table.</p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/deleteTable.html", "uri": "deleteTable.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 4, "37": 4, "38": 5, "39": 6, "40": 9, "41": 10, "42": 10, "43": 10, "44": 12, "45": 16, "46": 17, "47": 18, "48": 19, "49": 19, "50": 19, "51": 21, "52": 23, "53": 23, "54": 24, "55": 24, "56": 30, "57": 32, "58": 33, "59": 35, "65": 59}}
__M_END_METADATA
"""
