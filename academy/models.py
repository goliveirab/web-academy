# -*- coding: utf-8 -*-
from openerp import models, fields


class academy(models.Model):
    _name = 'academy.academy'

    name = fields.Char()


class Courses(models.Model):
    _name = 'academy.courses'
    _inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id',
                                 string="Courses")
