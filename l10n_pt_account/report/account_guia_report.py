#-*- coding:utf-8 -*-
from openerp.report import report_sxw

import time


class account_guia(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_guia, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })
        
report_sxw.report_sxw(
    'report.account.guia',
    'account.guia',
    'report/account_guia.rml',
    parser=account_guia
)