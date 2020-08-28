from odoo import fields, models, api, exceptions, _
from datetime import timedelta


class ModuleTracker(models.Model):
    _name = "module.tracker"
    _description = "Keeps track of OSI public and private modules"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "mod_name"
    mod_name = fields.Char(
        string="Module Name", required=(True), track_visibility="always",
    )
    mod_description = fields.Text(
        string="Summary",
        track_visibility="always",
        help="located in the __manifest__.py file under summary",
    )
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
        domain="[('is_company','=','True'),('customer', '=', 'True')]",
    )

    project_id = fields.Many2one(
        "project.project",
        ondelete="cascade",
        string="Project",
        required=(True),
        track_visibility="always",
    )
    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    version_sup_ids = fields.Many2many(
        "module.version",
        string="Supported Versions",
        track_visibility="always",
        help="located in the __manifest__.py file",
    )
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
    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    contributor_ids = fields.Many2many(
        "hr.employee",
        string="Contributors",
        track_visibility="onchange",
        help="Additional Developers, Designers and Contributors can be listed here",
    )
    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    dependency_ids = fields.Many2many(
        "module.depend",
        string="Dependencies",
        track_visibility="onchange",
        help="located in the __manifest__.py file",
    )
    special_circum = fields.Char(string="Special Cases", track_visibility="always",)

    prim_category_id = fields.Many2one(
        "module.category", string="Primary Category", track_visibility="always",
    )
    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    add_category_ids = fields.Many2many(
        "module.category", string="Additional Categories", track_visibility="always",
    )

    @api.onchange("project_id")
    def _onchange_from_project(self):
        for rec in self:
            if rec.project_id:
                rec.customer_id = rec.project_id.partner_id

    @api.constrains("prim_category_id", "add_category_ids")
    def _check_prim_category_not_in_add_categories(self):
        for rec in self:
            if rec.prim_category_id and rec.prim_category_id in rec.add_category_ids:
                raise exceptions.ValidationError(
                    "Primary Category can not be used in additional categories"
                )

    @api.constrains("prim_developer_id", "contributor_ids")
    def _check_prim_developer_not_in_add_contributors(self):
        for rec in self:
            if rec.prim_developer_id and rec.prim_developer_id in rec.contributor_ids:
                raise exceptions.ValidationError(
                    "Primary Developer can not be used in additional contributors/developers"
                )

    @api.constrains("prim_designer_id", "contributor_ids")
    def _check_prim_designer_not_in_add_contributors(self):
        for rec in self:
            if rec.prim_designer_id and rec.prim_designer_id in rec.contributor_ids:
                raise exceptions.ValidationError(
                    "Primary Designer can not be used in additional contributors/developers"
                )


class Category(models.Model):
    _name = "module.category"
    _description = "stores category names for reduced repeating of module categories"

    name = fields.Char(string="Category Name", required=(True))

    module_category_ids = fields.One2many("module.tracker", "prim_category_id",)

    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The Category Name must be unique"),
    ]


class Dependency(models.Model):
    _name = "module.depend"
    _description = "stores Dependency names for reduced repeating of module categories"

    name = fields.Char(string="Dependency Name", required=(True))

    module_dependency_ids = fields.Many2many("module.tracker")

    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The Dependency Name must be unique"),
    ]


class SupportedVersion(models.Model):
    _name = "module.version"
    _description = "stores version numbers for no repeating of version numbers"

    name = fields.Float(string="Dependency version", required=(True))

    module_version_ids = fields.One2many("module.tracker", "version_sup_ids")

    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The Version must be unique"),
    ]

    @api.constrains("name")
    def _check_version_not_negative(self):
        for r in self:
            if r.name < 0:
                raise exceptions.ValidationError("version number can not be negative")
