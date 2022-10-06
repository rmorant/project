# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.addons.cmis_field import fields as cmis_fields

class ModelName(models.Model):
    _inherit = "project.project"

    cmis_folder = cmis_fields.CmisFolder(
        backend_name="localhost"
    )