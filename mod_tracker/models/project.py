from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    module_id = fields.One2many(
        "module.tracker", "project_ids", string="Module", readonly=True
    )
