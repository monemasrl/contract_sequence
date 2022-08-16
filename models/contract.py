# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################
""" Contract Sequence Module """

from odoo import _, api, fields, models


class ContractContract(models.Model):
    """Extends the contract class with a new field 'number'"""

    _inherit = "contract.contract"

    number = fields.Char(
        string="Contract Number",
        required=True,
        default="/",
        readonly=True,
    )

    _sql_constraints = [
        (
            "contract_contract_unique_number",
            "UNIQUE (number)",
            _("The number must be unique!"),
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """
        Create a new record for a model ContractContract
        @param values: provides a data for new record
        @return: returns a id of new record
        """
        for vals in vals_list:
            if vals.get("number", "/") == "/":
                vals["number"] = self.env["ir.sequence"].next_by_code(
                    "contract.contract"
                )
        return super().create(vals_list)

    def copy(self, default=None):
        """Make a copy of the contract"""
        self.ensure_one()
        if default is None:
            default = {}
        default["number"] = self.env["ir.sequence"].next_by_code("contract.contract")
        return super().copy(default)

    def name_get(self):
        """Function used to get the name of the contract"""
        result = super().name_get()
        new_result = []

        for contract in result:
            rec = self.browse(contract[0])
            name = f"[{rec.number}] {contract[1]}"
            new_result.append((rec.id, name))
        return new_result
