# Copyright 2024 ALBA Software S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import models, fields


class ProjectTimeType(models.Model):
    _inherit = "project.time.type"

    #employee_ids = fields.Many2many(
    #    string="Employee Filter",
    #    comodel_name="hr.employee",
    #    relation="project_time_type_employee_rel",
    #    column1="time_type_id",
    #    column2="employee_id",
    #)

    user_ids = fields.Many2many(
        string="User Filter",
        comodel_name="res.users",
        relation="project_time_type_user_rel",
        column1="time_type_id",
        column2="user_id",
    )


