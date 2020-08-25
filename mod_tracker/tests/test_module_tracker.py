from odoo.tests.common import TransactionCase, tagged


class TestMtCases(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestMtCases, self).setUp(*args, **kwargs)

        self.module_tracker = self.env["module.tracker"].create(
            {
                "mod_name": "name",
                "mod_description": "description",
                "module_type": "public",
                "repo_url": "https://github.com/",
                "rel_date": "2020-08-10",
                "customer_id": self.env.ref("base.main_company").id,
                "project_id": self.env.ref("project.project_project_1").id,
            }
        )

    def test_mt_creation(self):
        self.assertEqual(self.module_tracker.mod_name, "name")
