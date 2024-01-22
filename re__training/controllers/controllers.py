# -*- coding: utf-8 -*-
# from odoo import http


# class ReTraining(http.Controller):
#     @http.route('/re__training/re__training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/re__training/re__training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('re__training.listing', {
#             'root': '/re__training/re__training',
#             'objects': http.request.env['re__training.re__training'].search([]),
#         })

#     @http.route('/re__training/re__training/objects/<model("re__training.re__training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('re__training.object', {
#             'object': obj
#         })

