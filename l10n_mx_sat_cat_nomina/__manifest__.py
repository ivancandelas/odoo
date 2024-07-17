# Copyright (C) 2024 Iván Candelas
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Mexico SAT Nómina Catalogs',
    'version': '15.0.1.0.0',
    'description': 'Mexico SAT Nómina Catalogs',
    "summary": """
        This module provides the list of references to payroll related
        documents that the Mexican tax authority, Servicio de
        Administración Tributaria (SAT) requires to be signed/transferred.
    """,
    'author': 'Iván Candelas',
    'website': '',
    "license": "AGPL-3",
    "category": "Localization",
    "depends": ["base", "l10n_mx_sat_cat_cfdi"],
    'data': [
        "security/ir.model.access.csv",
        "data/sat.nomina.c_tipo_contrato.csv",
        "data/sat.nomina.c_tipo_nomina.csv",
        "data/sat.nomina.c_tipo_regimen.csv",
        "data/sat.nomina.c_tipo_jornada.csv",
        "data/sat.nomina.c_riesgo_puesto.csv",
        "data/sat.nomina.c_tipo_percepcion.csv",
        "data/sat.nomina.c_tipo_deduccion.csv",
        "data/sat.nomina.c_tipo_otro_pago.csv",
        "views/menus.xml",
        "views/sat_nomina_tipo_contrato_view.xml",
        "views/sat_nomina_tipo_nomina_view.xml",
        "views/sat_nomina_tipo_regimen_view.xml",
        "views/sat_nomina_tipo_jornada_view.xml",
        "views/sat_nomina_riesgo_puesto_view.xml",
        "views/sat_nomina_tipo_percepcion_view.xml",
        "views/sat_nomina_tipo_deduccion_view.xml",
        "views/sat_nomina_tipo_otro_pago_view.xml"
    ],
    'application': False
}
