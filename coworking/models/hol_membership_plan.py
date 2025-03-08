from odoo import models, fields

class HolMembershipPlan(models.Model):
    _name = 'coworking.hol_membership_plan'
    _description = 'Coworking Membership Plan'

    name = fields.Char(string='Plan Name', required=True)
    price = fields.Float(string='Price', required=True)
    duration = fields.Integer(string='Duration (Days)', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
