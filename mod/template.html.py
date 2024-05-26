# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1716730350.047905
_enable_loop = True
_template_filename = 'template/template.html'
_template_uri = 'template.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\r\n<html lang="fr">\r\n<head>\r\n    <meta charset="utf-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\r\n    <!-- Bootstrap CSS -->\r\n    <link rel="stylesheet" href="/static/css/bootstrap.min.css">\r\n    <!-- CSS Perso -->\r\n    <link rel="stylesheet" href="/static/css/style.css">\r\n    <title>tpWeb</title>\r\n</head>\r\n<body>\r\n    <!-- Optional JavaScript -->\r\n    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\r\n    <script src="/static/js/jquery-3.5.0.min.js"></script>\r\n    <script src="/static/js/bootstrap.min.js"></script>\r\n    <style>\r\n        .bansyso {\r\n            top: 1vh;\r\n            height: 10vw;\r\n            width: 100%;\r\n            background-image: url(\'/static/assets/bannière_symphonica.webp\');\r\n            background-repeat: no-repeat;\r\n            background-position: center center;\r\n        }\r\n        .concert-card {\r\n            display: flex;\r\n            align-items: center;\r\n            margin-bottom: 20px;\r\n            background: linear-gradient(to right, #f0f0f0 0%, #ffffff 100%);\r\n            padding: 10px;\r\n            border: 1px solid #ddd;\r\n            border-radius: 5px;\r\n            transition: box-shadow 0.3s;\r\n            cursor: pointer;\r\n        }\r\n        .concert-card:hover {\r\n            box-shadow: 0 4px 8px rgba(0,0,0,0.1);\r\n        }\r\n        .concert-image {\r\n            width: 150px;\r\n            height: 100px;\r\n            object-fit: cover;\r\n            margin-right: 20px;\r\n        }\r\n        .concert-details {\r\n            flex: 1;\r\n        }\r\n    </style>\r\n    <div class="container-fluid">\r\n        <div class="bansyso"></div>\r\n        <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n            <div class="collapse navbar-collapse" id="navbarNavDropdown">\r\n                <ul class="navbar-nav">\r\n                    <li class="nav-item active">\r\n                        <a class="nav-link" href="index">Accueil <span class="sr-only">(page courante)</span></a>\r\n                    </li>\r\n                    <li class="nav-item dropdown">\r\n                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                            Recherche\r\n                        </a>\r\n                        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n                            <a class="dropdown-item" href="affParMorceau">Par morceau</a>\r\n                            <a class="dropdown-item" href="affParGenre">Par genre</a>\r\n                            <a class="dropdown-item" href="affParDate">Par date</a>\r\n                            <a class="dropdown-item" href="affParCompositeur">Par compositeur</a>\r\n                        </div>\r\n                    </li>\r\n                    <li class="nav-item">\r\n                        <a class="nav-link" href="insertPage">Insertion</a>\r\n                    </li>\r\n                    <li class="nav-item">\r\n                        <a class="nav-link" href="adminPage">Admin</a>\r\n                    </li>\r\n                </ul>\r\n            </div>\r\n        </nav>\r\n        ')
        __M_writer(str(self.body()))
        __M_writer('\r\n    </div>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "template/template.html", "uri": "template.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 78, "24": 78, "30": 24}}
__M_END_METADATA
"""
