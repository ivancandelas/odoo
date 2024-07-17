
from odoo import models, fields


class SatNominaTipoOtroPago(models.Model):
    _name = "sat.nomina.c_tipo_otro_pago"
    _description = "SAT Nómina Tipo Otro Pago"

    name = fields.Char('Other Payment Type', required=True)
    code = fields.Char('Code', required=True)
    date_start = fields.Date(string="Start date")
    date_end = fields.Date(string="End date")

    _sql_constraints = [
        ('type_code_unique',
         'unique(code)',
         'The code should be unique')
    ]
