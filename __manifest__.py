
# -*- coding: utf-8 -*-
###############################################################################
#
#    jeffery CHEN fan<jeffery9@gmail.com>
#
#    Copyright (c) All rights reserved:
#        (c) 2017  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#    
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    "name": "Contract Sequence",
    "summary": "Contract Sequence Module Project",
    "version": "14.0.1.0.1",

    "description": """
Contract Sequence Module Project.
==============================================


    """,

    "author": "Monema S.r.l.",
    "maintainer": "Andrea Bettarini",
    "contributors": [
        "Andrea Bettarini <bettarini@monema.it>"
    ],
    "website": "https://monema.it",
    "license": "Other OSI approved licence",
    "category": "Sales",

    "depends": [
        "sale",
        "contract"
    ],
    "data": [
        "data/contract_sequence.xml",
        "views/contract.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
