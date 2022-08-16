"""Test for contract sequence"""
from odoo.tests import common, tagged


class TestContractSequenceBase(common.SingleTransactionCase):
    """Base class used by TestContractSequence"""

    @classmethod
    def setUpClass(cls):
        """setUp Class"""
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
    """Test suite for contract_sequence"""

    @tagged("contract_sequence")
    def test_contract(self):
        """Test contract.number is not None"""
        self.contract.partner_id = self.partner.id
        self.assertIsNotNone(self.contract.number)

    @tagged("contract_sequence")
    def test_contract_copy(self):
        """Test copy of a contract"""
        contract1 = self.contract.copy()

        self.assertIsNotNone(contract1.number)
        self.assertNotEqual(self.contract.number, contract1.number)

    @tagged("contract_sequence")
    def test_name_get(self):
        """Test name get"""
        contract_name = self.contract.name_get()
        self.assertEqual(
            contract_name[0][1], f"[{self.contract.number}] {self.contract.name}"
        )
