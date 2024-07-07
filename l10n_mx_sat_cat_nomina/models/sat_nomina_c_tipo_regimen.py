
from odoo import models, fields


class SatNominaTipoRegimen(models.Model):
    _name = "sat.nomina.c_tipo_regimen"
    _description = "SAT Nómina Tipo Regimen"

    name = fields.Char('Regime Type', required=True)
    code = fields.Char('Code', required=True)
    date_start = fields.Date(string="Start date")
    date_end = fields.Date(string="End date")

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
