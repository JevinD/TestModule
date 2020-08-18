from odoo import fields, models, api, exceptions, _


class academyCourse(models.Model):
    _name = "academy.course"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Academy courses"

    name = fields.Char(string="Course")
    description = fields.Text(string="description")

    responsible_id = fields.Many2one(
        "res.partner",
        ondelete="set null",
        string="Responsible",
        index=True,
        domain=[
            "|",
            ("instructor", "=", True),
            ("category_id.name", "ilike", "Teacher"),
        ],
    )
    session_ids = fields.One2many("academy.session", "course_id", string="Sessions")
    _sql_constraints = [
        (
            "name_description_check",
            "CHECK(name != description)",
            "The title of the course should not be the description",
        ),
        ("name_unique", "UNIQUE(name)", "The course title must be unique"),
    ]

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [("name", "=like", u"Copy of {}%".format(self.name))]
        )
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default["name"] = new_name
        return super(academyCourse, self).copy(default)
