#! /usr/bin/python
# -*- coding: utf-8 -*-
import re,argparse
import csv
import ast
from datetime import datetime

def argumen():
    args = None
    parser = argparse.ArgumentParser(description='konversi SID a.k.a  SID converter from/to export SID file\
    by Bambang Yuliarso me@bakulnet.com')
    parser.add_argument('-i', '--input', help='input .csv/ SID export source name filename')
    parser.add_argument('-s', '--source', help='input .csv/ datasource name filename')
    parser.add_argument('-f', '--form', help='input .csv/ form report code')
    args = parser.parse_args()
    return args

def detectDelimiter():
    p = open(sumber, 'rb')
    header=p.readline()
    if header.find(";")!=-1:return ";"
    elif header.find("\t")!=-1:return "\t"
    elif header.find("|")!=-1:return "|"
    elif header.find(",")!=-1:return ","
    p.close()

def buatform33():
    form33 = open('form33.csv', 'w')
    with open(inputl, 'rb') as datanya:
        for index,z in enumerate(datanya, start=0):
            cocok_form33 = re.findall('^SID033',z)
            if index == 0:
                header_kolom = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|'+\
                    'tahun|jenis_fasilitas|id_fasilitas|sifat|no_rekening|no_akad_awal|tanggal_akad_awal|'+\
                    'no_akad_akhir|tanggal_akad_akhir|tanggal_awal_kredit|tanggal_mulai|tanggal_jatuh_tempo|'+\
                    'baru_perpanjangan|golongan_kredit|jenis_penggunaan|orientasi_penggunaan|sektor_ekonomi|'+\
                    'dati2_lokasi_proyek|nilai_proyek|id_valuta|suku_bunga|sifat_suku_bunga|plafon_induk|'+\
                    'plafon|baki_debet|original_currency|kelonggaran_tarik|discount|kolektibilitas|'+\
                    'tanggal_macet|sebab_macet|keterangan_sebab_macet|tanggal_tunggakan|tunggakan_pokok|'+\
                    'frekuensi_tunggakan_pokok|tunggakanbunga_intra|tunggakanbunga_ekstra|'+\
                    'frekuensi_tunggakan_bunga|denda|cerukan|kondisi|tanggal_kondisi|agunan|ppap|'+\
                    'kumulatif_realisasi|tanggal_restrukturisasi|restrukturisasi_ke|restrukturisasi_awal|'+\
                    'kondisi_debitur|permasalahan_debitur|keterangan|create_date|create_user|update_date|'+\
                    'status_kirim|versi|filler'
                header = z
                form33.write(header_kolom)
                form33.write(enter)
                pass
            elif cocok_form33:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+\
                    sep+z[19:21]+sep+z[21:25]+sep+z[25:29]+sep+z[29:81]+sep+z[81:83]+\
                    sep+z[83:108]+sep+z[108:133]+sep+z[133:141]+sep+z[141:166]+sep+\
                    z[166:174]+sep+z[174:182]+sep+z[182:190]+sep+z[190:198]+sep+z[198:200]+\
                    sep+z[200:202]+sep+z[202:204]+sep+z[204:205]+sep+z[205:210]+sep+\
                    z[210:214]+sep+z[214:229]+sep+z[229:232]+sep+z[232:237]+sep+z[237:238]+\
                    sep+z[238:253]+sep+z[253:268]+sep+z[268:283]+sep+z[283:298]+sep+z[298:313]+\
                    sep+z[313:328]+sep+z[328:329]+sep+z[329:337]+sep+z[337:339]+sep+z[339:439]+\
                    sep+z[439:447]+sep+z[447:462]+sep+z[462:465]+sep+z[465:480]+sep+z[480:495]+\
                    sep+z[495:498]+sep+z[498:513]+sep+z[513:528]+sep+z[528:530]+sep+z[530:538]+\
                    sep+z[538:553]+sep+z[553:568]+sep+z[568:583]+sep+z[583:591]+sep+z[591:593]+\
                    sep+z[593:601]+sep+z[601:701]+sep+z[701:801]+sep+z[801:901]+sep+z[901:915]+\
                    sep+z[915:935]+sep+z[935:949]+sep+z[949:950]+sep+z[950:958]+sep+z[958:959]
                form33.write(lines)
                form33.write(enter)
            else:
                footer = z
                exportform33.write(header+footer)
    form33.close()

def sinkron():
    for x in sumber_file: nominatif.append(x)
    if forml == '33':
        a = datetime.now()
        o=0
        n=0
        temp_33 = csv.DictReader(open('form33.csv', 'rb'), delimiter=detectDelimiter())
        for y in temp_33:
            o+=1
            for k in nominatif:
                if y['no_rekening'] == k['no_rekening'].ljust(25,' '):
                    y['no_rekening'] = k['no_rekening'].ljust(25,'x')
                    y['baki_debet'] = k['saldo_nominatif'].zfill(15)
                    y['tunggakan_pokok'] = k['tunggakan_pokok'].zfill(15)
                    if k['kolekt'] == 'L':
                        y['kolektibilitas'] ='1'
                    elif k['kolekt'] == 'KL':
                        y['kolektibilitas'] ='3'
                    elif k['kolekt'] == 'D':
                        y['kolektibilitas']='4'
                    elif k['kolekt'] == 'M':
                        y['kolektibilitas']= '5'
                    y['frekuensi_tunggakan_pokok'] = k['ft_pokok'].zfill(3)
                    y['tunggakanbunga_intra'] = k['ft_bunga'].zfill(15)
                    y['frekuensi_tunggakan_bunga'] = k['ft_bunga'].zfill(3)
                    y['agunan'] = k['agunan_nilai'].zfill(15)
                    n+=1
            line_data = y['id_data']+y['operation']+y['id_lembaga']+y['id_bank']+y['id_kantor_cabang']+\
                y['bulan']+y['tahun']+y['jenis_fasilitas']+y['id_fasilitas']+y['sifat']+y['no_rekening']+\
                y['no_akad_awal']+y['tanggal_akad_awal']+y['no_akad_akhir']+y['tanggal_akad_akhir']+\
                y['tanggal_awal_kredit']+y['tanggal_mulai']+y['tanggal_jatuh_tempo']+y['baru_perpanjangan']+\
                y['golongan_kredit']+y['jenis_penggunaan']+y['orientasi_penggunaan']+y['sektor_ekonomi']+\
                y['dati2_lokasi_proyek']+y['nilai_proyek']+y['id_valuta']+y['suku_bunga']+y['sifat_suku_bunga']+\
                y['plafon_induk']+y['plafon']+y['baki_debet']+y['original_currency']+y['kelonggaran_tarik']+\
                y['discount']+y['kolektibilitas']+y['tanggal_macet']+y['sebab_macet']+\
                y['keterangan_sebab_macet']+y['tanggal_tunggakan']+y['tunggakan_pokok']+\
                y['frekuensi_tunggakan_pokok']+y['tunggakanbunga_intra']+y['tunggakanbunga_ekstra']+\
                y['frekuensi_tunggakan_bunga']+y['denda']+y['cerukan']+y['kondisi']+y['tanggal_kondisi']+\
                y['agunan']+y['ppap']+y['kumulatif_realisasi']+y['tanggal_restrukturisasi']+\
                y['restrukturisasi_ke']+y['restrukturisasi_awal']+y['kondisi_debitur']+\
                y['permasalahan_debitur']+y['keterangan']+y['create_date']+y['create_user']+\
                y['update_date']+y['status_kirim']+y['versi']+y['filler']
            tulis.append(line_data)
            exportform33.write(line_data)
            exportform33.write(enter)

if __name__ == "__main__":
    try:
        inputl = argumen().input
        forml = argumen().form
        sumber = argumen().source
        nominatif = []
        sumber_file = csv.DictReader(open(sumber,'rb'), delimiter=detectDelimiter())
        enter = '\n'
        sep='|'
        daftar_tabel = [1,2,31,33,38,41,42,5,6,7]
        exportform33 = open('exportform33.txt', 'w')
        buatform33()
        tulis = []
        sinkron()
        exportform33.close()
    except ValueError as err:
        print(err.args)
"""
#######struktur form33#####
 'id_data	z[0:6]	6
operation	z[6:7]	1
id_lembaga	z[7:10]	3
id_bank	z[10:16]	6
id_kantor_cabang	z[16:19]	3
bulan	z[19:21]	2
tahun	z[21:25]	4
jenis_fasilitas	z[25:29]	4
id_fasilitas	z[29:81]	52
sifat	z[81:83]	2
no_rekening	z[83:108]	25
no_akad_awal	z[108:133]	25
tanggal_akad_awal	z[133:141]	8
no_akad_akhir	z[141:166]	25
tanggal_akad_akhir	z[166:174]	8
tanggal_awal_kredit	z[174:182]	8
tanggal_mulai	z[182:190]	8
tanggal_jatuh_tempo	z[190:198]	8
baru_perpanjangan	z[198:200]	2
golongan_kredit	z[200:202]	2
jenis_penggunaan	z[202:204]	2
orientasi_penggunaan	z[204:205]	1
sektor_ekonomi	z[205:210]	5
dati2_lokasi_proyek	z[210:214]	4
nilai_proyek	z[214:229]	15
id_valuta	z[229:232]	3
suku_bunga	z[232:237]	5
sifat_suku_bunga	z[237:238]	1
plafon_induk	z[238:253]	15
plafon	z[253:268]	15
baki_debet	z[268:283]	15
original_currency	z[283:298]	15
kelonggaran_tarik	z[298:313]	15
discount	z[313:328]	15
kolektibilitas	z[328:329]	1
tanggal_macet	z[329:337]	8
sebab_macet	z[337:339]	2
keterangan_sebab_macet	z[339:439]	100
tanggal_tunggakan	z[439:447]	8
tunggakan_pokok	z[447:462]	15
frekuensi_tunggakan_pokok	z[462:465]	3
tunggakanbunga_intra	z[465:480]	15
tunggakanbunga_ekstra	z[480:495]	15
frekuensi_tunggakan_bunga	z[495:498]	3
denda	z[498:513]	15
cerukan	z[513:528]	15
kondisi	z[528:530]	2
tanggal_kondisi	z[530:538]	8
agunan	z[538:553]	15
ppap	z[553:568]	15
kumulatif_realisasi	z[568:583]	15
tanggal_restrukturisasi	z[583:591]	8
restrukturisasi_ke	z[591:593]	2
restrukturisasi_awal	z[593:601]	8
kondisi_debitur	z[601:701]	100
permasalahan_debitur	z[701:801]	100
keterangan	z[801:901]	100
create_date	z[901:915]	14
create_user	z[915:935]	20
update_date	z[935:949]	14
status_kirim	z[949:950]	1
versi	z[950:958]	8
filler'	z[958:959]	1

"""

"""
{'saldo_nominatif': '10000000',
 'premi': '0',
 'no_rekening': 'QD.2017.00006',
 'tgl_angsuran': '22-Jun-17',
 'bi_gol_debitur': '2',
 'nilai_penjaminan': '0',
 'jenis_pinjaman': 'QRD',
 'kode_agunan': '5',
 'nilai_likuidasi': '10200000',
 'my_kode_group': '012876',
 'agunan_nilai': '34000000',
 'kewajiban_bunga': '0',
 'satuan_waktu_angsuran': 'B',
 'sisa_margin': '0',
 'ft_pokok': '1',
 'jmlbayarbunga': '0',
 'bi_suku_bunga': '0',
 'bi_agunan_nilai': '34000000',
 'tunggakan_pokok': '1000000',
 'kode_sumber_dana': '',
 'alamat': 'JL. GURITA VII/09  RT.02/ RW.12 UNGARAN',
 'rescheduling': '0',
 'denda_after_jt': '0',
 'provisi': '0',
 'agunan_ikatan_hukum': '4',
 'tgg_pokok': '1000000',
 'type_channeling': '0',
 'jml_hari_after_tagihan': '9',
 'tunggakan_bunga': '0',
 'nama_nasabah': 'WELLY KRISHNA',
 'flag_bunga': 'PLAFON',
 'freq_after_jth_tempo': '-2',
 'tunggakan_denda': '0',
 'deskripsi_asuransi': 'Di bawah tangan',
 'lain_lain': '0',
 'kolekt': '',
 'adm': '0',
 'notariel': '0',
 'bobot': '30',
 'tujuan_penggunaan': 'DANA TALANGAN',
 'bi_gol_penjamin': '110',
 'bi_sifat': '4',
 'kolektibilitas': 'L',
 'akad': '6',
 'type_pinjaman': '900',
 'agunan': 'MOBIL TOYOTA INNOVA 2005 H-8628-MC AN. WELLY KRISHNA',
 'nasabah_id': '11.00838',
 'bi_jenis_penggunaan': '70',
 'kode_group2': '876',
 'kode_group3': '901',
 'kode_group1': '012',
 'nilai_asuransi': '0',
 'tgl_jatuh_tempo': '22-Sep-17',
 'kode_group4': '03',
 'tgl_realisasi': '22-Jun-17',
 'sid_kode_agunan': '02',
 'denda_per_angsuran': '0',
 'ft_bunga': '0',
 'jml_pinjaman': '10000000',
 'kota': ' Semarang, Kab.',
 'sid_agunan_ikatan_hukum': '03',
 'agunan_jenis': '4',
 'bi_jangka_waktu': '3',
 'kota_id': '0901',
 'deskripsi_group1': 'DODI',
 'after_jth_tempo': '-53',
 'tgg_bunga': '0',
 'deskripsi_group2': 'PERORANAN NON PEGAWAI',
 'telpon': '085640510969',
 'type_abp': '1',
 'bi_sektor_ekonomi': '1019',
 'kode_asuransi': '1',
 'tgl_akhir_trans': '2017-06-22'}
"""
