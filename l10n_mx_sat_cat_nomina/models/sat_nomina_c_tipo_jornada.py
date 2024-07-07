
from odoo import models, fields


class SatNominaTipoJornada(models.Model):
    _name = "sat.nomina.c_tipo_jornada"
    _description = "SAT Nómina Tipo Jornada"

    name = fields.Char('Shift Type', required=True)
    code = fields.Char('Code', required=True)

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
