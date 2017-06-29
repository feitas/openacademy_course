# -*- coding: utf-8 -*-

from odoo import models, fields, api


# 课程
class Course(models.Model):
    _inherit = 'openacademy.course'
    # _name = 'openacademy.course'

    has_books = fields.Boolean(string="教科书",default=False)
    exam_type = fields.Selection([
        ('theory',"理论"),
        ('practice',"实践"),
        ('theory and practice',"理论+实践")
    ],string="考试类型")
