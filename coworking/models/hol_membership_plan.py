from odoo import models, fields

class HolMembershipPlan(models.Model):
    _name = 'coworking.hol_membership_plan'
    _description = 'Coworking Membership Plan'

    name = fields.Char(string='Plan Name', required=True)
    price = fields.Float(string='Price', required=True)
    duration = fields.Integer(string='Duration (Days)', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    line_ids = fields.One2many('coworking.hol_membership_plan.line', 'hol_membership_plan_id', string='Service')


class HolMembershipPlanLine(models.Model):
    _name = 'coworking.hol_membership_plan.line'

    service_type_id = fields.Many2one('coworking.service_type', string='Service Type')
    get_service_type = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
        ('on_request', 'On Request'),
    ], string='Get Service Type ?')
    description = fields.Text('Description')
    hol_membership_plan_id = fields.Many2one('coworking.hol_membership_plan', string='Membership Plan')


class HolMembershipServiceType(models.Model):
    _name = 'coworking.service_type'

    name = fields.Char(string='Service Type')