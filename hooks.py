# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    """
    With this pre-init-hook we want to avoid error when creating the UNIQUE
    number constraint when the module is installed and before the
    post-init-hook is launched.
    """
    cr.execute("ALTER TABLE contract_contract ADD COLUMN number character varying;")
    cr.execute("UPDATE contract_contract SET number = id;")


def post_init_hook(cr, registry):
    """
    This post-init-hook will update all existing contract assigning them the
    corresponding sequence number.
    """
    env = api.Environment(cr, SUPERUSER_ID, dict())
    contract_obj = env["contract.contract"]
    sequence_obj = env["ir.sequence"]
    contracts = contract_obj.search([], order="id")
    for contract_id in contracts.ids:
        cr.execute(
            "UPDATE contract_contract SET number = %s WHERE id = %s;",
            (
                sequence_obj.next_by_code("contract.contract"),
                contract_id,
            ),
        )
