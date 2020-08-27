from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    module_customer_ids = fields.Many2many(
        "module.tracker", string="Customer", readonly=True
    )
