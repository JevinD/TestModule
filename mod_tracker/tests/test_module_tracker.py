from odoo.tests.common import TransactionCase, tagged
from odoo.modules.module import get_module_resource


@tagged("-at_install", "post_install")
class TestMtCases(TransactionCase):
    def setUp(self):
        super(TestMtCases, self).setUp()

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

    def test_Mt_Creation(self):
        self.assertEqual(self.module_track.mod_name, "name")
        self.assertEqual(self.module_track.mod_description, "description")
