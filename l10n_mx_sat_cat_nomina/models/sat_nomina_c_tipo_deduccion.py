
from odoo import models, fields


class SatNominaTipoDeduccion(models.Model):
    _name = "sat.nomina.c_tipo_deduccion"
    _description = "SAT Nómina Tipo Deducción"

    name = fields.Char('Deduction Type', required=True)
    code = fields.Char('Code', required=True)
    date_start = fields.Date(string="Start date")
    date_end = fields.Date(string="End date")

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
