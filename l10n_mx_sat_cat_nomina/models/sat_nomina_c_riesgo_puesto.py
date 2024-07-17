
from odoo import models, fields


class SatNominaRiesgoPuesto(models.Model):
    _name = "sat.nomina.c_riesgo_puesto"
    _description = "SAT Nómina Riesgo Puesto"

    name = fields.Char('Position Risk', required=True)
    code = fields.Char('Code', required=True)
    date_start = fields.Date(string="Start date")
    date_end = fields.Date(string="End date")

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
