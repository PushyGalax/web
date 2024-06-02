# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717310412.7404287
_enable_loop = True
_template_filename = 'template/insertIntoTable.html'
_template_uri = 'insertIntoTable.html'
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
        table = context.get('table', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n    <h2>Insertion dans la table : ')
        __M_writer(str(table))
        __M_writer('</h2>\r\n    <form action="insertEntry" method="post">\r\n')
        for header in headers:
            pass
            if not header["is_primary_key"]:
                __M_writer('                <div class="form-group">\r\n                    <label for="')
                __M_writer(str(header['name']))
                __M_writer('">')
                __M_writer(str(header['name']))
                __M_writer('</label>\r\n')
                if header["is_foreign_key"]:
                    __M_writer('                        <select class="form-control" id="')
                    __M_writer(str(header['name']))
                    __M_writer('" name="')
                    __M_writer(str(header['name']))
                    __M_writer('" required>\r\n')
                    for option in header["options"]:
                        __M_writer('                                <option value="')
                        __M_writer(str(option['value']))
                        __M_writer('">')
                        __M_writer(str(option['display']))
                        __M_writer('</option>\r\n')
                    __M_writer('                        </select>\r\n')
                else:
                    pass
                    if header["name"] == "date_composition":
                        __M_writer('                            <input type="text" class="form-control" id="')
                        __M_writer(str(header['name']))
                        __M_writer('" name="')
                        __M_writer(str(header['name']))
                        __M_writer('" size="4" placeholder="0000" pattern="[0-9]{4}" required>\r\n')
                    else:
                        pass
                        if header["name"] == "formation":
                            __M_writer('                                <select class="form-control" id="')
                            __M_writer(str(header['name']))
                            __M_writer('" name="')
                            __M_writer(str(header['name']))
                            __M_writer('" required>\r\n')
                            for elem in ['orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','traditionnelle','électro','spéciale']:
                                __M_writer('                                        <option value="')
                                __M_writer(str(elem))
                                __M_writer('">')
                                __M_writer(str(elem))
                                __M_writer('</option>\r\n')
                            __M_writer('                                </select>\r\n')
                        else:
                            pass
                            if header["name"] == "genre_concert":
                                __M_writer('                                <select class="form-control" id="')
                                __M_writer(str(header['name']))
                                __M_writer('" name="')
                                __M_writer(str(header['name']))
                                __M_writer('" required>\r\n')
                                for elem in ['symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','traditionnelle','spéciale']:
                                    __M_writer('                                        <option value="')
                                    __M_writer(str(elem))
                                    __M_writer('">')
                                    __M_writer(str(elem))
                                    __M_writer('</option>\r\n')
                                __M_writer('                                </select>\r\n')
                            else:
                                pass
                                if header["name"] == "genre":
                                    __M_writer('                                    <select class="form-control" id="')
                                    __M_writer(str(header['name']))
                                    __M_writer('" name="')
                                    __M_writer(str(header['name']))
                                    __M_writer('" required>\r\n')
                                    for elem in ['concerto','composition','symphonie','duo','trio','sonate','quatuor','soliste','rock','électro','traditionnelle','spéciale']:
                                        __M_writer('                                            <option value="')
                                        __M_writer(str(elem))
                                        __M_writer('">')
                                        __M_writer(str(elem))
                                        __M_writer('</option>\r\n')
                                    __M_writer('                                    </select>\r\n')
                                else:
                                    pass
                                    if "date" in header["name"]:
                                        __M_writer('                                            <input type="date" id="')
                                        __M_writer(str(header['name']))
                                        __M_writer('" name="')
                                        __M_writer(str(header['name']))
                                        __M_writer('" class="form-control"required>\r\n')
                                    else:
                                        __M_writer('                                            <input type="text" class="form-control" id="')
                                        __M_writer(str(header['name']))
                                        __M_writer('" name="')
                                        __M_writer(str(header['name']))
                                        __M_writer('" required>\r\n')
                __M_writer('                </div>\r\n')
        __M_writer('        <input type="hidden" name="table" value="')
        __M_writer(str(table))
        __M_writer('">\r\n        <button type="submit" class="btn btn-primary">Insérer</button>\r\n    </form>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/insertIntoTable.html", "uri": "insertIntoTable.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 4, "36": 4, "37": 6, "39": 7, "40": 8, "41": 9, "42": 9, "43": 9, "44": 9, "45": 10, "46": 11, "47": 11, "48": 11, "49": 11, "50": 11, "51": 12, "52": 13, "53": 13, "54": 13, "55": 13, "56": 13, "57": 15, "58": 16, "60": 17, "61": 18, "62": 18, "63": 18, "64": 18, "65": 18, "66": 19, "68": 20, "69": 21, "70": 21, "71": 21, "72": 21, "73": 21, "74": 22, "75": 23, "76": 23, "77": 23, "78": 23, "79": 23, "80": 25, "81": 26, "83": 27, "84": 28, "85": 28, "86": 28, "87": 28, "88": 28, "89": 29, "90": 30, "91": 30, "92": 30, "93": 30, "94": 30, "95": 32, "96": 33, "98": 34, "99": 35, "100": 35, "101": 35, "102": 35, "103": 35, "104": 36, "105": 37, "106": 37, "107": 37, "108": 37, "109": 37, "110": 39, "111": 40, "113": 41, "114": 42, "115": 42, "116": 42, "117": 42, "118": 42, "119": 43, "120": 44, "121": 44, "122": 44, "123": 44, "124": 44, "125": 51, "126": 54, "127": 54, "128": 54, "134": 128}}
__M_END_METADATA
"""
