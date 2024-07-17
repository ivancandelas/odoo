
from odoo import models, fields


class SatNominaTipoNomina(models.Model):
    _name = "sat.nomina.c_tipo_nomina"
    _description = "SAT Nómina Tipo Nómina"

    name = fields.Char('Payroll Type', required=True)
    code = fields.Char('Code', required=True)

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
