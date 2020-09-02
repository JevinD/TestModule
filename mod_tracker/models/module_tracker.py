from odoo import fields, models, api, exceptions, _
from datetime import timedelta
from odoo.modules.module import get_module_resource


class ModuleTracker(models.Model):
    _name = "module.tracker"
    _description = "Keeps track of OSI public and private modules"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    image = fields.Binary(
        "Photo",
        attachment=True,
        help="This field holds the image of the icon, limited to 1024x1024px.",
    )

    name = fields.Char(
        string="Module Name", required=(True), track_visibility="always",
    )

    active = fields.Boolean(string="Active?", default=True, track_visibility="always",)

    mod_summary = fields.Text(string="Summary", track_visibility="always",)

    prim_category_id = fields.Many2one(
        "module.category", string="Primary Category", track_visibility="always",
    )
    module_type = fields.Selection(
        [("public", "Public"), ("private", "Private")],
        string="Module Type",
        track_visibility="always",
    )

    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The Module Name must be unique")
    ]

    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    add_category_ids = fields.Many2many(
        "module.category", string="Additional Categories", track_visibility="always",
    )

    # NOTE: OE_CHATTER DOES NOT TRACK THIS
    version_ids = fields.One2many(
        "module.tracker.version",
        "name_id",
        string="Module Versions",
        track_visibility="always",
        help="located in the __manifest__.py file",
    )

    mod_description = fields.Text(
        string="Description",
        track_visibility="always",
        help="located in the __manifest__.py file under description",
    )
    notes = fields.Text(string="Notes")
    special_circum = fields.Char(string="Special Cases", track_visibility="always",)

    @api.constrains("prim_category_id", "add_category_ids")
    def _check_prim_category_not_in_add_categories(self):
        for rec in self:
            if rec.prim_category_id and rec.prim_category_id in rec.add_category_ids:
                raise exceptions.ValidationError(
                    "Primary Category can not be used in additional categories"
                )


class Category(models.Model):
    _name = "module.category"
    _description = "stores category names for reduced repeating of module categories"

    name = fields.Char(string="Category Name", required=(True))

    module_category_ids = fields.Many2many("module.tracker",)

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


class ModuleVersion(models.Model):
    _name = "module.tracker.version"
    _description = "stores versions of modules"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "rel_date desc"

    name_id = fields.Many2one(
        "module.tracker", string="Module Name", track_visibility="always",
    )
    version = fields.Char(string="Version", required=(True), track_visibility="always",)
    active = fields.Boolean(string="Active?", default=True, track_visibility="always",)
    repo_url = fields.Char(string="Github Repo Url", track_visibility="always",)
    stage = fields.Selection(
        [
            ("development", "Development"),
            ("review", "Review"),
            ("published", "Published"),
        ],
        string="Status",
        track_visibility="always",
    )
    rel_date = fields.Date(string="Release Date", track_visibility="always",)
    comment = fields.Text(string="Comment", track_visibility="always",)

    # NOTE: OE_CHATTER DOES NOT TRACK THIS!
    project_ids = fields.Many2many(
        "project.project",
        ondelete="cascade",
        string="Project",
        track_visibility="always",
    )
    prim_designer_id = fields.Many2one(
        "res.partner",
        ondelete="cascade",
        string="Primary Designer",
        track_visibility="always",
    )

    prim_developer_id = fields.Many2one(
        "res.partner",
        ondelete="cascade",
        string="Primary Developer",
        track_visibility="always",
    )

    # NOTE: OE_CHATTER DOES NOT TRACK THIS!
    contributor_ids = fields.Many2many(
        "res.partner",
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
