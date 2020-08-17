from odoo.tests.common import TransactionCase


class TestModelCourse(TransactionCase):
    def test_course_creation(self):
        responsible_id = self.env["res.users"].search([("login", "=", "beverly")])
        record = self.env["academy.course"].create(
            {
                "name": "cs999",
                "description": "last class",
                "responsible_id": responsible_id,
            }
        )
        self.assertEqual(record.name, "cs999")
