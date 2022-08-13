from odoo import exceptions
from odoo.tests import common,tagged


class TestContractSequenceBase(common.SingleTransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        admin_user = cls.env.ref('base.user_admin')
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "partner test contract",
                "email": "demo@demo.com",
            }
        )

        cls.contract = cls.env["contract.contract"].create(
            {
                "name": "Test Contract",
                "partner_id": cls.partner.id,
                "line_recurrence": True,
            }
        )


class TestContractSequence(TestContractSequenceBase):
    @tagged('contract_sequence')
    def test_contract(self):
        partner = self.partner.copy()
        self.contract.partner_id = self.partner.id

        self.assertEqual(self.contract.partner_id, self.partner)

    @tagged('contract_sequence')
    def test_contract_copy(self):
        contract1 = self.contract.copy()

        self.assertIsNotNone(contract1.number)
        self.assertNotEqual(self.contract.number, contract1.number)