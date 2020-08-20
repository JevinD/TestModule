from odoo import fields, models, api, exceptions, _
from datetime import timedelta


class moduleTracker(models.Model):
    _name = "module.tracker"
    _description = "Keeps track of OSI public and private modules"

    mod_name = fields.Char(string="Module Name", required=(True))
    mod_description = fields.Text(string="Summary")
    module_type = fields.Selection(
        [("public", "Public"), ("private", "Private")], string="Module Type",
    )
    repo_url = fields.Char(string="Github Repo Url")
    rel_date = fields.Date(string="Release Date")
    customer = fields.Many2many("res.partner", ondelete="set null", string="Customer",)
    # used for attaching projects to a module
    # how do I auto fill this or display a selection
    project_ids = fields.One2many(
        "project.project", "subtask_project_id", ondelete="cascade", string="Project"
    )
    # version_sup = fields.many2many()
    prim_designer = fields.Many2one(
        "hr.employee", ondelete="cascade", string="Primary Designer",
    )
    contributor = fields.Many2many("hr.employee", string="Contributors & Developers")
    dependencies = fields.Many2many("ir.module.module")
    # special_circum = fields.?
    # config = fields.?

    # example accounting
    # prim_category = fields.Many2one("ir.module.module")
    # add_category = fields.One2many
