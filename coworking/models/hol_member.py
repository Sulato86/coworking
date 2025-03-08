from odoo import models, fields

class HolMember(models.Model):
    _name = 'coworking.hol_member'
    _description = 'Member Data'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Telepon')
    hol_membership_date = fields.Date(
        string='Join Date', 
        default=fields.Date.context_today
    )

    membership_plan_id = fields.Many2one(
        'coworking.hol_membership_plan', 
        string='Membership Plan'
    )
