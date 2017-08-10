#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# copyrights: bambang yuliarso <me@bakulnet.com>                              #
# license : MIT license, please read @:                                       #
# https://en.wikipedia.org/wiki/MIT_License                                   #
#   data creator from several datas for ojk reporting                         #
#   requirements: python 2.7.x version (unix/linux/windows)                   #
#                                                                             #
###############################################################################
import sys, csv, re, argparse
from dateutil.parser import *
import json
import datetime

def initiate_data():
    args = None
    parser = argparse.ArgumentParser(description='konversi lapbul a.k.a  lapbul converter from csv file\
    by Bambang Yuliarso me@bakulnet.com')
    parser.add_argument('-i', '--input', help='input .csv filename')
    parser.add_argument('-f', '--form', help='input form number report format')
    args = parser.parse_args()
    return args

def detectDelimiter(args):
    p = open(args, 'rb')
    header=p.readline()
    if header.find(";")!=-1:return ";"
    elif header.find("\t")!=-1:return "\t"
    elif header.find("|")!=-1:return "|"
    elif header.find(",")!=-1:return ","
    p.close()

def hitung_datanya(args):
    def bersih_bersih(args):
        replacements = {'+ACI-':'','+AF8-':'_', '+AC0-':'-', '+ACU-':'',"'":'','Februari':'Feb','Okt':'Oct','Des':'Dec','Mei':'May','Juni':'Jun','April':'Apr','Juli':'Jul','Agustus':'Aug'}
        with open(file_input) as infile, open(file_input.split('.')[0]+'-edited.csv', 'w') as outfile:
            for line in infile:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    if args.input:
        file_input = args.input
        bersih_bersih(args=file_input)
        yy = detectDelimiter(args=file_input)
        xx = str(file_input.split('.')[0])+'-edited.csv'
        csvdict = csv.DictReader(open(xx,'rb'), delimiter=yy) #inisialisasi ke dictionary
        name_tujuan = 'form'+str(args.form)+'.exp'
        tujuan = open(name_tujuan, 'w')

    def rekening(rek):
        rek = rek.replace('.','').ljust(15, ' ')
        return rek

    def ubah_tgl(tgl):     #konversi tanggal
        try:
            if tgl == '1900-01-01' or tgl == '0000-00-00':
                tgl = '19000101'
                return tgl
            else:
                th = parse(tgl).year
                bl = parse(tgl).month
                hari = parse(tgl).day
                tgl = str(th)+str(bl).zfill(2)+str(hari).zfill(2)
                return tgl
        except ValueError as err:
            print(err.args)

    def tingkat_imbalan(imbalan): # konversi tingkat imbalan
        try:
            if imbalan == '0' or None:
                imbalan = '0000'
                return str(imbalan)
            if len(imbalan) <= 2:
                satu = str(re.findall(r'([0-9]+)',imbalan)[0]).zfill(2)+'00' #digit sebelah kiri desimal
                imbalan = satu
                return str(imbalan)
            else:
                satu = str(re.findall(r'([0-9]+)',imbalan)[0]).zfill(2) #digit sebelah kiri desimal
                dua = str(re.findall(r'([0-9]+)',imbalan)[1]).zfill(2) or '00' #digit sebelah kanan desimal
                imbalan = satu+dua
                return str(imbalan)
        except ValueError as err:
            print(err.args)


    def hit_ppap(ppap,kolek,jenisagunan,nilaiagunan,saldo):
        pengurang=None
#         if jenisagunan:
        if jenisagunan == '0': pengurang=0.0 #not defined
        if jenisagunan == '1': pengurang=1.0 #1. Kas, tabungan dan deposito
        if jenisagunan == '2': pengurang=1.0 #2. Perhiasanemasdanlogammulia
        if jenisagunan == '3': pengurang=0.8 #3. Tanahdanbangunan
        if jenisagunan == '4': pengurang=0.5 #4. Kendaraanbermotor
        if jenisagunan == '5': pengurang=0.5 #5. Tanahdanbangunan,kendaraanbermotor
        if jenisagunan == '6': pengurang=0.0 #6. Kas,tabungandandeposito,kendaraanbermotor
        if jenisagunan == '7': pengurang=0.0 #7. Emas,logammulia,tanahdanbangunan
        if jenisagunan == '8': pengurang=0.0 #8. Emas,logammulia,kendaraanbermotor
        if jenisagunan == '9': pengurang=0.0 #9. Lainnya
        kap = float(saldo) - (float(nilaiagunan) * pengurang )
        if kolek == '1': saldo = str(int(round(0.05 * kap)))
        if kolek == '2': saldo = str(int(round(0.1 * kap)))
        if kolek == '3': saldo = str(int(round(0.5 * kap)))
        if kolek == '4': saldo = str(int(round(1 * kap)))
        return saldo

    def form3():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS03'
            a1  = str(x['sandi_bank_penempatan'].zfill(3))
            a2  = x['sandi_bank2'].ljust(9, ' ')
            a3  = x['nama_bank'].ljust(100, ' ')
            a4  = x['keterkaitan']
            a5  = x['jenis_penempatan']
            a6  = str(ubah_tgl(tgl=x['periode_mulai']))
            a7  = str(ubah_tgl(tgl=x['periode_tempo']))
            a8  = x['kolektibilitas']
            a9  = str(tingkat_imbalan(imbalan=x['tingkat_imbalan']))
            a10 = x['jumlah'].zfill(12)
            a11 = x['jenis_agunan']
            a12 = x['nilai_agunan'].rjust(12,'0')
#             a13 = x['ppap'].zfill(12)
            a13 = str(hit_ppap(x['ppap'],x['kolektibilitas'],x['jenis_agunan'],x['nilai_agunan'],x['jumlah'])).zfill(12)
            a14 = x['bagi_hasil_id']
            a15 = str(x['gol_penjamin'].zfill(3))
            a16 = str(tingkat_imbalan(imbalan=x['bag_dijamin']))
            a17 = str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form4():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS04'
            a1  = rekening(rek=x['nomor_rekening'])
            a2  = x['jumlah_rekening'].ljust(8,' ')
            a3  = x['jenis_penggunaan']
            a4  = x['keterkaitan']
            a5  = ubah_tgl(tgl=x['periode_mulai'])
            a6  = ubah_tgl(tgl=x['periode_tempo'])
            a7  = x['kolektibilitas']
            a8  = str(tingkat_imbalan(imbalan=x['tingkat_imbalan']))
            a9  = x['sektor_ekonomi_id']
            a10 = x['harga_jual'].zfill(12)
            a11x = x['saldo_harga_pokok']
            a11 = x['saldo_harga_pokok'].zfill(12)
            a12 = x['saldo_margin'].zfill(12)
#             a13 = x['saldo_piutang'].zfill(12)
            a13 = str(int(a11) + int(a12)).zfill(12)
            a14 = x['jenis_agunan']
            a15 = x['nilai_agunan'].rjust(12,'0')
            a16 = x['ppap'].zfill(12)
#            a16x = str(hit_ppap(x['ppap'],x['kolektibilitas'],x['jenis_agunan'],x['nilai_agunan'],x['saldo_harga_pokok']))
            a16 = str(hit_ppap(x['ppap'],x['kolektibilitas'],x['jenis_agunan'],x['nilai_agunan'],x['saldo_harga_pokok'])).zfill(12)
            a17 = x['bagi_hasil_id']
            a18 = x['gol_penjamin'].zfill(3)
            a19 = str(tingkat_imbalan(imbalan=x['bag_dijamin']))
            a20 = x['gol_nasabah']
            a21 = x['lokasi_usaha'].zfill(4)
            a22 = x['gol_piutang']
            a23 = x['tujuan_milik']
            a24 = x['pendapatan_diterima'].zfill(12)
            a25 = x['datarestrukturisasi']
            a26 = str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26
            print a,'---kolek',a7,'saldo pokok',a11x,'ppap :',x['ppap'],' hitung_ppap :',a16x,' rekening=',x['nomor_rekening']
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form7():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0  = 'BS07'
            a1  = rekening(rek=x['nomor_rekening'])
            a2  = x['jumlah_rekening'].ljust(8,' ')
            a3  = x['jenis_pembiayaan']
            a4  = x['jenis_penggunaan']
            a5  = x['keterkaitan']
            a6  = ubah_tgl(tgl=x['periode_mulai'])
            a7  = ubah_tgl(tgl=x['periode_tempo'])
            a8  = x['kolektibilitas']
            a9  = tingkat_imbalan(imbalan=x['tingkat_imbalan'])
            a10 = x['sektor_ekonomi_id']
            a11 = x['plafond'].rjust(12,'0')
            a12 = x['kelonggaran_tarik'].rjust(12,'0')
            a13 = x['saldo_pembiayaan'].rjust(12,'0')
            a14 = x['jenis_agunan']
            a15 = x['nilai_agunan'].rjust(12,'0')
            a16 = x['ppap'].rjust(12,'0')
            a17 = x['sifat']
            a18 = x['bagi_hasil_pemb_id']
            a19 = x['bg_hsl_sd_id']
            a20 = x['gol_penjamin']
            a21 = tingkat_imbalan(imbalan=x['bag_dijamin'])
            a22 = x['gol_nasabah'].zfill(5)
            a23 = x['lokasi_usaha'].zfill(4)
            a24 = x['gol_pembiayaan']
            a25 = x['datarestrukturisasi']
            a26 = str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form12():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS12'
            a1 = rekening(rek=x['nomor_rekening'])
            a2 = x['jumlah_rekening'].ljust(8,' ')
            a3 = x['hubungan']
            a4 = x['lokasi_nasabah'].zfill(4)
            a5 = tingkat_imbalan(imbalan=x['tingkat_imbalan'])
            a6 = x['jumlah'].zfill(12)
            a7 = x['gol_nasabah']
            a8 = str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form13():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS13'
            a1 = rekening(rek=x['nomor_rekening'])
            a2 = x['jumlah_rekening'].ljust(8,' ')
            a3 = x['hubungan']
            a4 = x['lokasi_nasabah'].zfill(4)
            a5 = tingkat_imbalan(imbalan=x['tingkat_imbalan'])
            a6 = x['jumlah'].zfill(12)
            a7 = x['bagi_hasil_sd']
            a8 = x['gol_nasabah']
            a9 = ubah_tgl(tgl=x['periode_mulai'])
            a10= ubah_tgl(tgl=x['periode_tempo'])
            a11= str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form14():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS14'
            a1 = rekening(rek=x['nomor_rekening'])
            a2 = x['jumlah_rekening'].ljust(8,' ')
            a3 = x['jenis_deposito']
            a4 = x['hubungan']
            a5 = x['lokasi_nasabah'].zfill(4)
            a6 = ubah_tgl(tgl=x['periode_mulai'])
            a7 = ubah_tgl(tgl=x['periode_tempo'])
            a8 = tingkat_imbalan(imbalan=x['tingkat_imbalan'])
            a9 = x['jumlah'].zfill(12)
            a10= x['bagi_hasil_sd']
            a11= x['gol_nasabah']
            a12= str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form15():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS15'
            a1 = x['sandi_bank_penempatan']
            a2 = x['sandi_bank2'].ljust(9,' ')
            a3 = x['nama_bank'].replace('.','').ljust(100,' ')
            a4 = x['hubungan']
            a5 = x['jenis_kewajiban']
            a6 = ubah_tgl(tgl=x['periode_mulai'])
            a7 = ubah_tgl(tgl=x['periode_tempo'])
            a8 = tingkat_imbalan(imbalan=x['tingkat_imbalan'])
            a9= x['bagi_hasil_sd']
            a10= x['jumlah'].zfill(12)
            a11= str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    def form20():
        a = 0
        for x in csvdict:   #baca dictionary
            a = a + 1
            a0 = 'BS20'
            a1  = rekening(rek=x['nomor_rekening'])
            a2  = x['jumlah_rekening'].ljust(8,' ')
            a3  = x['jenis_penggunaan']
            a4  = x['keterkaitan']
            a5  = ubah_tgl(tgl=x['periode_mulai'])
            a6  = ubah_tgl(tgl=x['periode_tempo'])
            a7  = x['kolektibilitas']
            a8  = x['sektor_ekonomi_id']
            a9  = x['bagi_hasil_id']
            a10 = x['gol_penjamin'].zfill(3)
            a11 = tingkat_imbalan(imbalan=x['bag_dijamin'])
            a12 = x['gol_nasabah']
            a13 = x['lokasi_multijasa'].zfill(4)
            a14 = x['gol_piutang']
            a15 = x['nilai_akad'].zfill(12)
            a16 = x['saldo_harga_pokok'].zfill(12)
            a17 = x['pend_trans_mj_tg'].zfill(12)
#             a18 = x['saldo_piutang'].zfill(12)
            a18 = str(int(a16) + int(a17)).zfill(12)
            a19 = x['jenis_agunan']
            a20 = x['nilai_agunan'].rjust(12,'0')
            a21 = x['ppap'].zfill(12)
            a22 = x['datarestrukturisasi']
            a23 = str(a).zfill(5) # sequence 5 digit
            lines = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23
            tujuan.write(lines) #tulis dictionary ke file
            tujuan.write('\n')

    try:
        if args.form == '3':form3()
        if args.form == '4':form4()
        if args.form == '7':form7()
        if args.form == '12':form12()
        if args.form == '13':form13()
        if args.form == '14':form14()
        if args.form == '15':form15()
        if args.form == '20':form20()

    except ValueError as err:
        print(err.args)

    tujuan.close()

if __name__ == "__main__":
    initiate_data()
    hitung_datanya(args=initiate_data())
