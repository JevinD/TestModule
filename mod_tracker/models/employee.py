from odoo import fields, models


class Contributors(models.Model):
    _inherit = "hr.employee"

    module_primary_ids = fields.One2many(
        "module.tracker", "prim_designer", string="Primary Designer", readonly=True,
    )
    module_contributor_ids = fields.Many2many(
        "module.tracker", "contributor", string="Contributed", readonly=True
    )
