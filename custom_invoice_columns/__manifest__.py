{
    'name': 'Custom Invoice Columns',
    'version': '1.0',
    'summary': 'Adds Previous, New, Actual readings and auto-quantity on invoices',
    'category': 'Accounting',
    'author': 'Your Name',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
        'report/invoice_report.xml',
    ],
    'installable': True,
    'application': False,
}
