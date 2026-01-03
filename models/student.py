from odoo import models,fields,api

class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Student'
    _rec_name = 'student_id'

    student_id = fields.Many2one(
        'school.admission',
        string='Student Registered',
        ondelete='cascade'
    )
    class_id = fields.Many2one(
        'school1.class',
        string='Assigned to this Class',
        required = True,
        ondelete = 'cascade'
    )
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender', related='student_id.gender')
    active = fields.Boolean(string='Active', default=1)
    date = fields.Date(string='DateTime',default=fields.Datetime.now)











