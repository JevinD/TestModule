from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    module_id = fields.Many2one("module.tracker", string="Module", readonly=True)
