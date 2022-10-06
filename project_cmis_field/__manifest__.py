# Copyright 2022 rmorant
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project CMIS Folder",
    "summary": "Adds",
    "version": "14.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Alpha", #Alfa|Beta|Production/Stable|Mature",
    "category": "Uncategorized",
    "website": "https://github.com/OCA/project", #or "https://github.com/OCA/project/tree/14.0/project_cmis_field",
    "author": "Rafa Morant (ALBA Software), Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    #"maintainers": ["your-github-login"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        # https://github.com/acsone/alfodoo/tree/14.0
        "cmis_field",
    ],
    "data": [
        "views/project_view.xml",
    ],
}
