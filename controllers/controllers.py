# -*- coding: utf-8 -*-
from odoo import http

# class OpenacademyCourse(http.Controller):
#     @http.route('/openacademy_course/openacademy_course/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_course/openacademy_course/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_course.listing', {
#             'root': '/openacademy_course/openacademy_course',
#             'objects': http.request.env['openacademy_course.openacademy_course'].search([]),
#         })

#     @http.route('/openacademy_course/openacademy_course/objects/<model("openacademy_course.openacademy_course"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_course.object', {
#             'object': obj
#         })