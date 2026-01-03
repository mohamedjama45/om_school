from odoo import fields,models,api
from datetime import date

class Admission(models.Model):
    _name = 'school.admission'


    name = fields.Char(string='Student Name', required=True,tracking=True)
    phone = fields.Char(string='Phone Number')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender',required=True)
    age = fields.Integer(string='Age', compute='_compute_age')


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            now = date.today()
            if rec.date_of_birth:
                rec.age = now.year - rec.date_of_birth.year
            else:
                rec.age = 1



































