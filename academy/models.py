# -*- coding: utf-8 -*-

from openerp import models, fields, api


class academy(models.Model):
    _name = 'academy.academy'

    name = fields.Char()


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
