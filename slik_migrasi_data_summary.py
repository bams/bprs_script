#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# copyrights: bambang yuliarso <me@bakulnet.com>                              #
# license : MIT license, please read @:                                       #
# https://en.wikipedia.org/wiki/MIT_License                                   #
#   data summary creator from several datas for ojk reporting                 #
#   requirements: python 2.7.x version (unix/linux/windows)                   #
#     Header : H                                                              #
#     Kode Jenis LJK : 0104 --> bprs                                          #
#     Kode LJK : 1939 --> bprs aau (lihat di referensi)                       #
#     Tahun : 2016 ->2016-2017                                                #
#     Bulan : 04 --> khusus data summary dari apr 2016 s.d apr.2017           #
#     Kode Segmen Jenis Fasilitas : F01 --> kredit                            #
#     Jumlah Baris Data File : rumus                                          #
#     contoh header data : H|0104|014|2017|04|S01|1                           #
#                                                                             #
###############################################################################

import csv
import subprocess
import collections
# import json

def get_filenames():
    output_f = subprocess.Popen(["ls", "."], stdout=subprocess.PIPE).communicate()[0]
    daftar = output_f.splitlines()
    ketemu=[]
    for x in daftar:
        if x.startswith('slik'):ketemu.append(x)
        else:continue
    return ketemu

def detectdelimiter(args):
    p = open(args, 'rb')
    header=p.readline()
    if header.find(";")!=-1:return ";"
    elif header.find("\t")!=-1:return "\t"
    elif header.find("|")!=-1:return "|"
    elif header.find(",")!=-1:return ","
    p.close()

def ambil_rekening(rekening):
    ketemu=get_filenames()
    filenya = open('collect_rekening.txt','w')
    for index,i in enumerate(ketemu,start=0):
        tanda = detectdelimiter(args=i)
        isi = csv.DictReader(open(i,'rb'),delimiter=tanda)
        for w in isi:
            data_rek = str(w['no_rekening']).replace('.','').replace('(','')
            id_rek = str(w['nasabah_id'])
            rekening.append((data_rek,id_rek))
    duplicate_items = [item for item, count in collections.Counter(rekening).items() if count > 1]
    non_duplicate_items = list(set(rekening) - set(duplicate_items))
    rekening = duplicate_items + non_duplicate_items
    filenya.write('rekening,cif'+'\n')
    for tulis in rekening: filenya.write(str(tulis)+'\n')
    filenya.close()

def buat_data_summary():
    #<Kode Jenis LJK>.<Kode LJK>.<Tahun>.<Bulan>.<Kode Segmen>.<Urutan>.txt
    tulis = open('0104.1939.2016.04.S01.1.txt', 'w')
    listf = get_filenames()
    m=n=o=jj=0
    #sesuaikan cifnya
    tanda1=detectdelimiter(args='cif_list.csv')
    data_cif = csv.DictReader(open('cif_list.csv','rb'), delimiter=tanda1)
    for t in data_cif:
        rek_cifs = t['no_rekening'].replace('.','').strip()
        xdatacif = {'no_rekening':rek_cifs, 'cif':t['cif']}
        cif.append(xdatacif)

    #daftar rekening
    kunci = csv.DictReader(open('collect_rekening.txt','rb'))
    for x in kunci:
        jj+=1
        rek_x = str(x['rekening'].split()[0]).replace('(','').replace("'","")
        for y in cif:
            dcif=''
            if y['no_rekening'] == rek_x:
                dcif = y['cif']
                data = {'flag':'D','no_rekening':rek_x,'cif':dcif,'kode_segmen':'F01',
                'k1':'','jt1':'','k2':'','jt2':'','k3':'','jt3':'','k4':'','jt4':'',
                'k5':'','jt5':'','k6':'','jt6':'','k7':'','jt7':'','k8':'','jt8':'',
                'k9':'','jt9':'','k10':'','jt10':'','k11':'','jt11':'','k12':'','jt12':''}
                data_summary.append(data)

    #penempatan kolek dan jumlah hari tunggakan
    for a in listf:
        m+=1
        d = detectdelimiter(args=a)
        a1 = csv.DictReader(open(a,'rb'), delimiter=d)
        var_j=''
        var_k=''
        for row in a1:
            o+=1
            rek = row['no_rekening'].replace('.','')
            for i in data_summary:
                var_k = 'k'+str(m)
                var_j = 'jt'+str(m)
                r_k = row['kolektibilitas']
                if r_k == 'L':r_k = '1'
                if r_k == 'KL':r_k = '3'
                if r_k == 'D':r_k = '4'
                if r_k == 'M':r_k = '5'
                r_jt = row['jml_hari_after_tagihan']
                if rek == i['no_rekening'] and r_k :
                    n+=1
                    i.update({var_k:r_k, var_j:r_jt})

    header = 'H|0104|1939|2017|04|S01|'+str(jj)
    tulis.write(header+'\n')
    s = '|'
    urutkan = sorted(data_summary, key=lambda data_summary: data_summary['no_rekening'])
    for index,p in enumerate(urutkan, start=0):
        hitung=0
        rek_l = str(p['no_rekening']).replace('(','').replace("'","")
#         cifdat =''
        for zx in p.iteritems():
            kunci =zx[0]
            if zx[1] == '':
                hitung +=1
                if hitung == (m*2):
                    del urutkan[index]
#                     print hitung
                    pass
                p.update({kunci:'0'})
        for j in cif:
            if rek_l == j['no_rekening']:cifdat = j['cif'].replace('.','')
        format_data = p['flag']+s+rek_l+s+cifdat+s+p['kode_segmen']+s+p['k1']+s+p['jt1']+s+p['k2']+s+p['jt2']+s+p['k3']+s+p['jt3']+s+p['k4']+s+p['jt4']+s+p['k5']+s+p['jt5']+s+p['k6']+s+p['jt6']+s+p['k7']+s+p['jt7']+s+p['k8']+s+p['jt8']+s+p['k9']+s+p['jt9']
#         if str(p).endswith('|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0'):
#
#             del p
#
        tulis.write(format_data+'\n')
    print 'jumlah bulan',m
    print 'jumlah kolom data',len(data_summary[0])
    tulis.close()

if __name__ == "__main__":
    data_summary= []
    rekening=[]
    cif = []
    ambil_rekening(rekening)
    buat_data_summary()
