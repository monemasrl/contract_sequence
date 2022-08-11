# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError



class ContractContract(models.Model):
    _inherit = 'contract.contract'

    code = fields.Char(
        string="Contract Number",
        required=True,
        default="/",
        readonly=True,
    )

    _sql_constraints = [
        ("contract_contract_unique_code", "UNIQUE (code)", _("The code must be unique!")),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """
            Create a new record for a model ContractContract
            @param values: provides a data for new record
    
            @return: returns a id of new record
        """
        for vals in vals_list:
            if vals.get("code", "/") == "/":
                vals["code"] = self.env["ir.sequence"].next_by_code("contract.contract")
        return super().create(vals_list)

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default["code"] = self.env["ir.sequence"].next_by_code("contract.contract")
        return super().copy(default)

    def name_get(self):
        result = super().name_get()
        new_result = []

        for contract in result:
            rec = self.browse(contract[0])
            name = "[{}] {}".format(rec.code, contract[1])
            new_result.append((rec.id, name))
        return new_result
