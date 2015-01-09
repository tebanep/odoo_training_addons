# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Course(models.Model):
    '''
    This class creates a model for courses
    '''
    _name = 'openacademy.course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res_users',
                                     ondelete='set null',
                                     string="Responsible",
                                     index=True)
    sessions_ids = fields.One2many('openacademy.session', 'course_id')
