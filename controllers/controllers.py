# -*- coding: utf-8 -*-
from odoo import http

# class PosSessionBank(http.Controller):
#     @http.route('/pos_session_bank/pos_session_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_session_bank/pos_session_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_session_bank.listing', {
#             'root': '/pos_session_bank/pos_session_bank',
#             'objects': http.request.env['pos_session_bank.pos_session_bank'].search([]),
#         })

#     @http.route('/pos_session_bank/pos_session_bank/objects/<model("pos_session_bank.pos_session_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_session_bank.object', {
#             'object': obj
#         })