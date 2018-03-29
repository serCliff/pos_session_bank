# -*- coding: utf-8 -*-
{
    'name': "Pos Session Bank Transactions",

    'summary': """
        Allow to know the correct daily billing""",

    'description': """
        This module make a count of your bank journals transactions and total daily billing and show it better

        When we go to close the session, not appear the daily billing
        https://github.com/serCliff/pos_session_bank/blob/10.0/img/when_close.png

        When the session will be closed will appear the bank transactions and total billing
        https://github.com/serCliff/pos_session_bank/blob/10.0/img/closed.png


        STILL MISSING
        
        - Without seccurity groups

        git: https://github.com/serCliff/pos_session_bank
    """,


    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    'category': 'point_of_sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_session_views.xml',
    ],
}