# Copyright (C) 2024 Iván Candelas
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Mexico SAT CFDI Catalogs',
    'version': '15.0.1.0.0',
    'description': 'Mexico SAT CFDI Catalogs',
    "summary": """
        This module provides the list of references to documents that
        the Mexican tax authority, Servicio de Administración Tributaria
        (SAT) requires to be signed/transferred.
    """,
    'author': 'Iván Candelas',
    'website': '',
    "license": "AGPL-3",
    "category": "Localization",
    "depends": ["base"],
    'data': [
        "security/ir.model.access.csv",
        "data/sat.cfdi.c_regimen_fiscal.csv",
        "views/menus.xml",
        "views/sat_cfdi_regimen_fiscal_view.xml"
    ],
    'application': False
}