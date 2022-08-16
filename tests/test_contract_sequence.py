from odoo.tests import common, tagged


class TestContractSequenceBase(common.SingleTransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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
    @tagged("contract_sequence")
    def test_contract(self):
        self.contract.partner_id = self.partner.id
        self.assertIsNotNone(self.contract.number)

    @tagged("contract_sequence")
    def test_contract_copy(self):
        contract1 = self.contract.copy()

        self.assertIsNotNone(contract1.number)
        self.assertNotEqual(self.contract.number, contract1.number)

    @tagged("contract_sequence")
    def test_name_get(self):
        contract_name = self.contract.name_get()
        self.assertEquals(contract_name[0][1], "[{}] {}".format(self.contract.number, self.contract.name))