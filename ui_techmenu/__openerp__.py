# -*- coding: utf-8 -*-



######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

{
    "name" : "TAG Create Technical Menu",
    "version" : "1.8",
    "author" : "Ursa Information Systems",
    "category" : "Extra Tools",
    "summary": "Explode Technical Menu out from under Settings (Ursa)",
    'description':
        """
Overview
--------
Moves the Technical Menu out from under Settings so it becomes a top level choice

Developer Notes
---------------
* OpenERP Version:  8.0
* Ursa Dev Team: RC
* TAG Menu has Email staying under Admin

Contact
-------
* contact@ursainfosystems.com
        """,
    'maintainer': 'Ursa Information Systems',
    'website': 'http://www.ursainfosystems.com',
    'images': ['static/description/ui_techmenu.png'],
    "depends" : ["base"],
    "init_xml" : [],

    "demo_xml" : [],
    "data" : [
        'menu.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
