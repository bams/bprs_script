#! /usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import erppeek
import socket
import urllib2
import re
import base64
import sys
import csv
import xml.etree.ElementTree as ET
import geetree

if socket.gethostname()=='bams.local':
	host = 'localhost'
	port = '8069'
	dbname = '**'
	admin_pw = '*'
else:
	host = 'hostku.odoo.com'
	port = '8102'
	dbname = '***'
	admin_pw = '*'

client = erppeek.Client('http://%s:%s' % (host, port))
client.login('admin', admin_pw, dbname)

def get_date(date):
	new_date = None
	if date:
		dd,mm,yy = date.split("-")
		century = int(yy)<17 and "20" or "19"
		date = "%s-%s-%s%s" % (dd,mm,century,yy)
		new_date = datetime.strptime(date, '%d-%b-%Y').strftime('%Y-%m-%d')
	return new_date

def get_partners():
	partner_ids = client.model('res.partner').search([('cif','!=',False)])
	partners = client.model('res.partner').read(partner_ids,["cif"])
	return dict([(x['cif'],x['id']) for x in partners])

def get_bank_accounts():
	bank_account_ids = client.model('res.partner.bank').search([])
	bank_accounts = client.model('res.partner.bank').read(bank_account_ids,["acc_number"])
	return dict([(x['acc_number'],x['id']) for x in bank_accounts])

def get_bank_relation_code():
	rec_ids = client.model('bank.relation.code').search([])
	recs = client.model('bank.relation.code').read(rec_ids,["code"])
	return dict([(x['code'],x['id']) for x in recs])

def get_account_types():
	account_type_ids = client.model('bank.account.type').search([])
	account_types = client.model('bank.account.type').read(account_type_ids,["code"])
	return dict([(x['code'],x['id']) for x in account_types])

def get_account_products():
	account_product_ids = client.model('account.product').search([])
	account_products = client.model('account.product').read(account_product_ids,["code"])
	return dict([(x['code'],x['id']) for x in account_products])

def cek_data_deposito():
	tree = ET.parse("product_agunan_dan_master_trans/deposito.xml")
	root = tree.getroot()
	n=0
	for child in root:
		for dep in child:
			print dep.tag.lower()+","

def main():
	tree = ET.parse("product_agunan_dan_master_trans/deposito.xml")
	root = tree.getroot()

	bank_accounts = get_bank_accounts()
	partners = get_partners()
	account_types = get_account_types()
	account_products = get_account_products()
	relations = get_bank_relation_code()

	account_holders = []
	for index, child in enumerate(root,start=0):
		print "index:",index
		data = dict([('z_'+rec.tag.lower(),rec.text) for rec in child])
		product_id = account_products[data['z_jenis_deposito']]
		if data['z_tgl_registrasi']=='00/00/00':
			data['z_tgl_registrasi'] = '01/01/2000'
		vals = {
			'acc_number': data['z_no_rekening'],
			'partner_id': partners[data['z_nasabah_id']],
			'product_id': product_id,
			'bank_id': 2,
			'company_id': 1,
			'bank_relation_id':relations['9900'],
			'account_type_id': 8, # Deposito
			'reg_date': datetime.strptime(data['z_tgl_registrasi'], '%m/%d/%Y').strftime('%Y-%m-%d'),
			'state':'active',
		}
		if vals['acc_number'] in bank_accounts:
			client.model('res.partner.bank').write([bank_accounts[vals['acc_number']]],vals)
		else:
			new_bank_account_id = client.model('res.partner.bank').create(vals)
			bank_accounts.update({
				vals['acc_number']:new_bank_account_id,
			})

main()
