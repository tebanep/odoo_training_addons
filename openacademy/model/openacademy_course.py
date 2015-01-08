from openerp import models, fields, api


class Course(models.Model):
    '''
    This class creates a model for courses
    '''
    _name = 'openacademey.course'

    name = fields.Char(string='Title', required=True)
    description = fields.Tex(string='Description')
