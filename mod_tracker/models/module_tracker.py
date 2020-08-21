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

    customer_id = fields.Many2one(
        "res.partner", ondelete="set null", string="Customer",
    )

    project_id = fields.Many2one(
        "project.project", ondelete="cascade", string="Project"
    )
    # possible create a configuration menu with the set numbers
    version_sup = fields.Char(string="Supported Versions")
    prim_designer = fields.Many2one(
        "hr.employee", ondelete="cascade", string="Primary Designer",
    )
    contributor_ids = fields.Many2many("hr.employee", string="Contributors")
    dependencies = fields.Char(string="Dependencies")
    special_circum = fields.Char(string="Special Circumstances")
    # config = fields.?

    # example accounting
    # will be set to the model created in configurations
    # will need to be set in data file
    # CHANGE THIS MODEL REF
    prim_category_id = fields.Many2one("module.category")
    # add_category = fields.One2many


class Category(models.Model):
    _name = "module.category"
    _description = "stores category names for reduced repeating of module categories"

    cat_name = fields.Char(string="Category Name", required=(True))

    module_category_ids = fields.One2many("module.tracker", "prim_category_id")
