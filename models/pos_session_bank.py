# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosSessionBank(models.Model):
	_inherit = "pos.session"

	bank_amount = fields.Monetary(
		compute="_compute_bank_journals",
		digits=0,
		string="Bank Transactions",
		help="Amount of bank journal transactions.",
		readonly=True)

	daily_billing = fields.Monetary(
		compute="_compute_bank_journals",
		digits=0,
		string="Dailly Billing",
		help="Sum of cash and bank transactions.",
		readonly=True)



	@api.depends('config_id', 'statement_ids')
	def _compute_bank_journals(self):
		for session in self:
			total_bank_amount = 0
			total_daily_amount = 0
			for journal in session.statement_ids:
				if journal.journal_type == 'bank':
					total_bank_amount += journal.total_entry_encoding
				total_daily_amount += journal.total_entry_encoding
			session.bank_amount = total_bank_amount
			session.daily_billing = total_daily_amount


