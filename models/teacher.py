from odoo import models,fields,api

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    phone = fields.Char(string='Phone Number')
    class_id = fields.Many2one(
           'school1.class',
          required = True,
        ondelete = 'cascade'
    )





