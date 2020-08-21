from odoo import fields, models, api, exceptions, _
from datetime import timedelta


class moduleTracker(models.Model):
    _name = "module.tracker"
    _description = "Keeps track of OSI public and private modules"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "mod_name"
    mod_name = fields.Char(
        string="Module Name", required=(True), track_visibility="always",
    )
    mod_description = fields.Text(string="Summary", track_visibility="always",)
    module_type = fields.Selection(
        [("public", "Public"), ("private", "Private")],
        string="Module Type",
        track_visibility="always",
    )
    repo_url = fields.Char(string="Github Repo Url", track_visibility="always",)
    rel_date = fields.Date(string="Release Date", track_visibility="always",)

    customer_id = fields.Many2one(
        "res.partner",
        ondelete="set null",
        string="Customer",
        track_visibility="always",
    )

    project_id = fields.Many2one(
        "project.project",
        ondelete="cascade",
        string="Project",
        track_visibility="always",
    )
    # possible create a configuration menu with the set numbers
    version_sup = fields.Char(string="Supported Versions", track_visibility="always",)
    prim_designer_id = fields.Many2one(
        "hr.employee",
        ondelete="cascade",
        string="Primary Designer",
        track_visibility="always",
    )
    prim_developer_id = fields.Many2one(
        "hr.employee",
        ondelete="cascade",
        string="Primary Developer",
        track_visibility="always",
    )
    contributor_ids = fields.Many2many(
        "hr.employee", string="Contributors", track_visibility="always",
    )
    dependencies = fields.Char(string="Dependencies", track_visibility="always",)
    special_circum = fields.Char(string="Special", track_visibility="always",)
    # config = fields.?

    # will need to be set in data file
    # returns the relationship not the name yet
    prim_category_id = fields.Many2one(
        "module.category", string="Primary Category", track_visibility="always",
    )
    # NOTE: DOES NOT TRACK THIS
    add_category_ids = fields.Many2many(
        "module.category", string="Categories", track_visibility="always",
    )


class Category(models.Model):
    _name = "module.category"
    _description = "stores category names for reduced repeating of module categories"

    name = fields.Char(string="Category Name", required=(True))

    module_category_ids = fields.One2many("module.tracker", "prim_category_id",)
