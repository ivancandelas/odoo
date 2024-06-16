
from odoo import models, fields


class SatCfdiRegimenFiscal(models.Model):
    _name = "sat.cfdi.c_regimen_fiscal"
    _description = "SAT CFDI Fiscal Regimen"

    name = fields.Char('Description', required=True)
    code = fields.Char('Code', required=True)
    natural = fields.Boolean(string="Apply to natural person")
    legal = fields.Boolean(string="Apply to legal person")
    date_start = fields.Date(string="Start date")
    date_end = fields.Date(string="End date")

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
