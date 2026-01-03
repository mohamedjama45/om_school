from odoo import models,fields,api

class Class(models.Model):
    _name = 'school1.class'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Classes'


    name = fields.Char(string='Class Name', required='True')
