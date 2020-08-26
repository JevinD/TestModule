from odoo import fields, models


class Contributors(models.Model):
    _inherit = "hr.employee"

    module_primary_ids = fields.One2many(
        "module.tracker", "prim_designer_id", string="Primary Designer", readonly=True,
    )
    module_primary_dev_ids = fields.One2many(
        "module.tracker",
        "prim_developer_id",
        string="Primary Developer",
        readonly=True,
    )
    module_contributor_ids = fields.Many2many(
        "module.tracker", string="Contributed", readonly=True
    )
