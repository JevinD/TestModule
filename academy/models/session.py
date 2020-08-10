from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = "academy.session"
    _description = "Academy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(
        digits=(1, 0), help="Duration in days", string="Length in Days"
    )
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one(
        "res.partner",
        string="Instructor",
        domain=[
            "|",
            ("instructor", "=", True),
            ("category_id.name", "ilike", "Teacher"),
        ],
    )
    course_id = fields.Many2one(
        "academy.course", ondelete="cascade", string="Course", required=True
    )
    attendee_ids = fields.Many2many("school.student", string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")

    @api.depends("seats", "attendee_ids")
    def _taken_seats(self):
        for r in self:
            if not r.seats:

                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange("seats", "attendee_ids")
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                "warning": {
                    "title": "Incorrect 'seats' value",
                    "message": "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                "warning": {
                    "title": "Too many attendees",
                    "message": "Increase seats or remove excess attendees",
                },
            }


class academyCourse(models.Model):
    _name = "academy.course"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Academy courses"

    name = fields.Char(string="Course")
    description = fields.Text(string="description")

    responsible_id = fields.Many2one(
        "res.users", ondelete="set null", string="Responsible", index=True
    )
    session_ids = fields.One2many("academy.session", "course_id", string="Sessions")

    @api.constrains("instructor_id", "attendee_ids")
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError(
                    "A session's instructor can't be an attendee"
                )
