# -*- coding: utf-8 -*-
from openerp import http

# class Mapledelivery(http.Controller):
#     @http.route('/mapledelivery/mapledelivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mapledelivery/mapledelivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mapledelivery.listing', {
#             'root': '/mapledelivery/mapledelivery',
#             'objects': http.request.env['mapledelivery.mapledelivery'].search([]),
#         })

#     @http.route('/mapledelivery/mapledelivery/objects/<model("mapledelivery.mapledelivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mapledelivery.object', {
#             'object': obj
#         })