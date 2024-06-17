
from odoo import models, fields


class SatNominaTipoContrato(models.Model):
    _name = "sat.nomina.c_tipo_contrato"
    _description = "SAT Nómina Tipo Contrato"

    name = fields.Char('Description', required=True)
    code = fields.Char('Code', required=True)

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
