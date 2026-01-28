{
    "name": "College ERP",
    "version": "18.0.1.1.0",
    "summary": "Comprehensive ERP solution for colleges and schools",
    "description": """
College ERP is a complete education management system designed for
colleges and schools. It helps manage students, teachers, courses,
classes, attendance, exams, and academic operations efficiently
within a single platform.
""",
    "author": "Sadiq Abishov",
    "maintainer": "Arther Technologies – Professional Business Solutions",
    "website": "https://www.arter.az",
    "category": "Education",
    "license": "LGPL-3",
    "images": ["static/description/icon.png"],
    "depends": [
        "base"
    ],
    "data": [
        # "security/ir.model.access.csv",
        # "views/menu.xml",
        # "views/student_view.xml",
        # "views/teacher_view.xml",
    ],
    "demo": [
        # "demo/demo.xml"
    ],
    "assets": {
        # "web.assets_backend": [
        #     "college_erp/static/src/css/style.css",
        #     "college_erp/static/src/js/script.js",
        # ],
    },
    "sequence": 1,
    "application": True,
    "installable": True,
    "auto_install": False
}
