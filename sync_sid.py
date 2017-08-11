#! /usr/bin/python
# -*- coding: utf-8 -*-
import re,argparse
import csv
import ast

def initiate_data():
    args = None
    parser = argparse.ArgumentParser(description='konversi SID a.k.a  SID converter to csv file\
    by Bambang Yuliarso me@bakulnet.com')
    parser.add_argument('-i', '--input', help='input .csv/ SID export source name filename')
    parser.add_argument('-s', '--source', help='input .csv/ datasource name filename')
    args = parser.parse_args()
    return args

def syncronize(args):
    file_input = args.input
    file_sumber = args.source
    def detectDelimiter(args):
        p = open(args, 'rb')
        header=p.readline()
        if header.find(";")!=-1:return ";"
        elif header.find("\t")!=-1:return "\t"
        elif header.find("|")!=-1:return "|"
        elif header.find(",")!=-1:return ","
        p.close()
    yy=detectDelimiter(file_sumber)
    form33=list_of_files[4].name
    zz = detectDelimiter(form33)
    csvdict_form33 =  csv.DictReader(open(form33,'rb'), delimiter=zz)
    csvdict_sumber = csv.DictReader(open(file_sumber,'rb'), delimiter=yy)

    master_data33=[]
    input = []
    for c in csvdict_form33:
        master_data33.append(c)

    for x in csvdict_sumber:
        input.append(x)


    xx=0
    kosong = ' '
    hasil = open('hasil.csv', 'w')
    s='|'
    for m in master_data33:
#     id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|jenis_fasilitas|id_fasilitas|sifat|no_rekening|no_akad_awal|tanggal_akad_awal|no_akad_akhir|tanggal_akad_akhir|tanggal_awal_kredit|tanggal_mulai|tanggal_jatuh_tempo|baru_perpanjangan|golongan_kredit|jenis_penggunaan|orientasi_penggunaan|sektor_ekonomi|dati2_lokasi_proyek|nilai_proyek|id_valuta|suku_bunga|sifat_suku_bunga|plafon_induk|plafon|baki_debet|original_currency|kelonggaran_tarik|discount|kolektibilitas|tanggal_macet|sebab_macet|keterangan_sebab_macet|tanggal_tunggakan|tunggakan_pokok|frekuensi_tunggakan_pokok|tunggakanbunga_intra|tunggakanbunga_ekstra|frekuensi_tunggakan_bunga|denda|cerukan|kondisi|tanggal_kondisi|agunan|ppap|kumulatif_realisasi|tanggal_restrukturisasi|restrukturisasi_ke|restrukturisasi_awal|kondisi_debitur|permasalahan_debitur|keterangan|create_date|create_user|update_date|status_kirim|versi|filler

        for n in input:
            if n['no_rekening'] == str(m['no_rekening'].split(' ')[0]):
#                 print m,'--master ',n,' --input'
                xx+=1
                #tambahkan parameter yang mau diubah
                m['no_rekening'] = n['no_rekening']
                #eof_tambahkan parameter yang mau diubah
#                 print 'ada',n['no_rekening'],n['ft_pokok'],'xx=',xx
                a1 = m['id_data']
                a2 = m['operation']
                a3 = m['id_lembaga']
                a4 = m['id_bank']
                a5 = m['id_kantor_cabang']
                a6 = m['bulan']
                a7 = m['tahun']
                a8 = m['jenis_fasilitas']
                a9 = m['id_fasilitas']
                a10 = m['sifat']
                a11	= str(n['no_rekening'].ljust(25,' '))
                a12 = m['no_akad_awal']
                a13 = m['tanggal_akad_awal']
                a14 = m['no_akad_akhir']
                a15 = m['tanggal_akad_akhir']
                a16 = m['tanggal_awal_kredit']
                a17 = m['tanggal_mulai']
                a18 = m['tanggal_jatuh_tempo']
                a19 = m['baru_perpanjangan']
                a20 = m['golongan_kredit']
                a21 = m['jenis_penggunaan']
                a22 = m['orientasi_penggunaan']
                a23 = m['sektor_ekonomi']
                a24 = m['dati2_lokasi_proyek']
                a25 = m['nilai_proyek']
                a26 = m['id_valuta']
                a27 = m['suku_bunga']
                a28 = m['sifat_suku_bunga']
                a29 = m['plafon_induk']
                a30 = m['plafon']
                a31 = m['baki_debet']
                a32 = m['original_currency']
                a33 = m['kelonggaran_tarik']
                a34 = m['discount']
                a35 = m['kolektibilitas']
                a36 = m['tanggal_macet']
                a37 = m['sebab_macet']
                a38 = m['keterangan_sebab_macet']
                a39 = m['tanggal_tunggakan']
                a40 = m['tunggakan_pokok']
                a41 = m['frekuensi_tunggakan_pokok']
                a42 = m['tunggakanbunga_intra']
                a43 = m['tunggakanbunga_ekstra']
                a44 = m['frekuensi_tunggakan_bunga']
                a45 = m['denda']
                a46 = m['cerukan']
                a47 = m['kondisi']
                a48 = m['tanggal_kondisi']
                a49 = m['agunan']
                a50 = m['ppap']
                a51 = m['kumulatif_realisasi']
                a52 = m['tanggal_restrukturisasi']
                a53 = m['restrukturisasi_ke']
                a54 = m['restrukturisasi_awal']
                a55 = str(m['kondisi_debitur']) or kosong.ljust(100,' ')
                a56 = str(m['permasalahan_debitur']) or kosong.ljust(100,' ')
                a57 = str(m['keterangan']) or kosong.ljust(100,' ')
                a58 = str(m['create_date']) or kosong.ljust(14,' ')
                a59 = str(m['create_user']) or 'Hikmah Prawira Perka'
                a60 = str(m['update_date']) or kosong.ljust(14,' ')
                a61 = str(m['status_kirim']) or kosong
                a62 = str(m['versi']) or kosong.ljust(8,' ')
                a63 = str(m['filler']) or kosong
                val= a1+s+a2+s+a3+s+a4+s+a5+s+a6+s+a7+s+a8+s+a9+s+a10+s+a11+s+a12+s+a13+s+a14+s+a15+s+a16+s+a17+s+a18+s+a19+s+a20+s+a21+s+a22+s+a23+s+a24+s+a25+s+a26+s+a27+s+a28+s+a29+s+a30+s+a31+s+a32+s+a33+s+a34+s+a35+s+a36+s+a37+s+a38+s+a39+s+a40+s+a41+s+a42+s+a43+s+a44+s+a45+s+a46+s+a47+s+a48+s+a49+s+a50+s+a51+s+a52+s+a53+s+a54+s+a55+s+a56+s+a57+s+a58+s+a59+s+a60+s+a61+s+a62+s+a63
                hasil.write(val)
                hasil.write('\n')
    print 'input---',len(input),' master_data33 ----',len(master_data33)

def baca_judul_tabel():
    enter = '\n'
    headerf1 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur|din|nama_debitur|nama_alias|status|keterangan_status|golongan_debitur|jenis_kelamin|no_ktp_no_akte_awal_pendirian|no_paspor|no_akte_akhir|tempat_lahir|tanggal_lahir_tanggal_akte_awal|tanggal_akte_akhir|npwp_debitur|alamat_debitur|dati2_debitur|kode_pos|kelurahan|kecamatan|kode_area|telepon|negara_domisili|nama_gadis_ibu_kandung_debitur|sandi_pekerjaan|tempat_bekerja|bidang_usaha|group_id|nama_group|hubungan_dgn_bank|melanggar_bmpk|melampaui_bmpk|rating_debitur|lembaga_rating|go_public|create_date|create_user|update_date|status_kirim|versi|filler'
    headerf2 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur|id_pengurus|nama_pengurus|jenis_kelamin|identitas_pengurus|npwp_pengurus|alamat_pengurus|dati2_pengurus|kelurahan|kecamatan|pangsa_pemilikan|id_jabatan|create_date|create_user|update_date|din|status_kirim|versi|filler'
    headerf31 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|jenis_fasilitas|id_fasilitas|jenis_penempatan|sandi_bank_penempatan|negara_domisili_bank|id_valuta|jangka_waktu_bulan|jangka_waktu_hari|kolektibilitas|suku_bunga|nilai_penempatan|original_currency|kondisi|tanggal_kondisi|agunan|ppap|keterangan|create_date|create_user|update_date|status_kirim|versi|filler'
    headerf33 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|jenis_fasilitas|id_fasilitas|sifat|no_rekening|no_akad_awal|tanggal_akad_awal|no_akad_akhir|tanggal_akad_akhir|tanggal_awal_kredit|tanggal_mulai|tanggal_jatuh_tempo|baru_perpanjangan|golongan_kredit|jenis_penggunaan|orientasi_penggunaan|sektor_ekonomi|dati2_lokasi_proyek|nilai_proyek|id_valuta|suku_bunga|sifat_suku_bunga|plafon_induk|plafon|baki_debet|original_currency|kelonggaran_tarik|discount|kolektibilitas|tanggal_macet|sebab_macet|keterangan_sebab_macet|tanggal_tunggakan|tunggakan_pokok|frekuensi_tunggakan_pokok|tunggakanbunga_intra|tunggakanbunga_ekstra|frekuensi_tunggakan_bunga|denda|cerukan|kondisi|tanggal_kondisi|agunan|ppap|kumulatif_realisasi|tanggal_restrukturisasi|restrukturisasi_ke|restrukturisasi_awal|kondisi_debitur|permasalahan_debitur|keterangan|create_date|create_user|update_date|status_kirim|versi|filler'
    headerf38 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|jenis_fasilitas|id_fasilitas|no_rekening|jenis_kredit_kelolaan|jenis_penggunaan|sektor_ekonomi|dati2_lokasi_proyek|nilai_proyek|tanggal_awal_kredit|tanggal_mulai|tanggal_jatuh_tempo|suku_bunga|id_valuta|jumlah|kolektibilitas|tanggal_tunggakan|tunggakan_pokok|tunggakan_bunga_intra|tunggakan_bunga_ekstra|tanggal_macet|sebab_macet|keterangan_sebab_macet|kondisi|tanggal_kondisi|keterangan|create_date|create_user|update_date|status_kirim|versi|filler'
    headerf41 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur|id_agunan|jenis_agunan|peringkat|jenis_pengikatan|pemilik_agunan|bukti_kepemilikan|dati2_lokasi_agunan|alamat_agunan|nilai_agunan|nilai_agunan_bank|nilai_agunan_penilai|penilai_independen|tanggal_penilaian|paripasu|asuransi|create_date_|create_user|update_date|din|status_kirim|versi|filler'
    headerf42 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur|id_fasilitas|id_penjamin|nama_penjamin|golongan_penjamin|bagian_dijamin|identitas_penjamin|npwp_penjamin|alamat_penjamin|prime_bank|create_date|create_user|update_date|din|status_kirim|versi|filler'
    headerf50 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|penempatan_pada_bank|surat_berharga|kredit_yang_diberikan|tagihan_lainnya|penyertaan|irrevocable_lc|garansi_yang_diberikan|penerusan_kredit|create_date|create_user|update_date|status_kirim|versi|filler'
    headerf60 = 'id_data|operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur|total_aktiva|aktiva_lancar|total_kewajiban|kewajiban_pada_bank|kewajiban_lancar|pinjaman_luar_negeri|modal|penjualan|pendapatan_operasional|biaya_operasional|pendapatan_non_operasional|biaya_non_operasional|laba_rugi_tahun_lalu|laba_rugi_tahun_berjalan|audited|create_date|create_user|update_date|din|status_kirim|versi|filler'
    headerf70 = 'operation|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|id_debitur_fasilitas|id_joint_account|jenis_fasilitas|id_debitur|id_fasilitas|create_date|create_user|update_date|din|no_rekening|status_kirim|tipe_account|versi|filler'
    form1.write(headerf1)
    form1.write(enter)
    form2.write(headerf2)
    form2.write(enter)
    form31.write(headerf31)
    form31.write(enter)
    form33.write(headerf33)
    form33.write(enter)
    form38.write(headerf38)
    form38.write(enter)
    form41.write(headerf41)
    form41.write(enter)
    form42.write(headerf42)
    form42.write(enter)
    form50.write(headerf50)
    form50.write(enter)
    form60.write(headerf60)
    form60.write(enter)
    form70.write(headerf70)
    form70.write(enter)

def hitung(args):
    baca_judul_tabel()
    sep='|'
    enter = '\n'
    try:
        for z in file_data:
            header_footer_data = re.findall('^\d.....',z)
            cocok_form1 = re.findall('^SID010',z)
            cocok_form2 = re.findall('^SID020',z)
            cocok_form31 = re.findall('^SID031',z)
            cocok_form33 = re.findall('^SID033',z)
            cocok_form38 = re.findall('^SID038',z)
            cocok_form41 = re.findall('^SID041',z)
            cocok_form42 = re.findall('^SID042',z)
            cocok_form50 = re.findall('^SID050',z)
            cocok_form60 = re.findall('^SID060',z)
            cocok_form70 = re.findall('^SID070',z)

#             if header_footer_data:
#                 if len(z) > 60 :
#                     headerf = 'jenis_data|id_data|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|waktu_create|nama_pengirim|versi_aplikasi|versi_referensi|versi_validasi|statusdata|total_debitur|total_pengurus|total_penempatan|total_surat_berharga|total_kredit|total_tagihan_lainnya|total_penyertaan|total_irrevocable_lc|total_garansi_diberikan|total_kredit_kelolaan|total_agunan|total_penjamin|total_kontrol_lbu|total_data_keuangan|total_relasi_debitur_fasilitas|total_record|nama_bank|alamat_bank|kode_area|no_telepon|status_kantor|status_bank|register|status_kirim|kode_kirim|sandi_terminal|filler'
#                     lines1 = z[0:13]+sep+z[13:19]+sep+z[19:22]+sep+z[22:28]+sep+z[28:31]+sep+z[31:33]+sep+z[33:37]+sep+z[37:51]+sep+z[51:81]+sep+z[81:85]+sep+z[85:89]+sep+z[89:93]+sep+z[93:97]+sep+z[97:104]+sep+z[104:111]+sep+z[111:118]+sep+z[118:125]+sep+z[125:132]+sep+z[132:139]+sep+z[139:146]+sep+z[146:153]+sep+z[153:160]+sep+z[160:167]+sep+z[167:174]+sep+z[174:181]+sep+z[181:188]+sep+z[188:195]+sep+z[195:202]+sep+z[202:214]+sep+z[214:264]+sep+z[264:314]+sep+z[314:318]+sep+z[318:327]+sep+z[327:328]+sep+z[328:330]+sep+z[330:367]+sep+z[367:368]+sep+z[368:369]+sep+z[369:371]+sep+z[371:372]
#                     head_er.write(headerf)
#                     head_er.write(enter)
#                     head_er.write(lines1)
#                 else:
#                     header_fff='jenis_data|id_data|id_lembaga|id_bank|id_kantor_cabang|bulan|tahun|total_record|filler'
#                     lines=z[0:13]+sep+z[13:19]+sep+z[19:22]+sep+z[22:28]+sep+z[28:31]+sep+z[31:33]+sep+z[33:37]+sep+z[37:49]+sep+z[49:50]
#                     foot_er.write(header_fff)
#                     foot_er.write(enter)
#                     foot_er.write(lines)

            if cocok_form1:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:68]+sep+z[68:88]+sep+z[88:188]+sep+z[188:238]+sep+z[238:242]+sep+z[242:292]+sep+z[292:295]+sep+z[295:296]+sep+z[296:326]+sep+z[326:356]+sep+z[356:386]+sep+z[386:436]+sep+z[436:444]+sep+z[444:452]+sep+z[452:472]+sep+z[472:572]+sep+z[572:576]+sep+z[576:581]+sep+z[581:631]+sep+z[631:681]+sep+z[681:685]+sep+z[685:693]+sep+z[693:696]+sep+z[696:746]+sep+z[746:749]+sep+z[749:799]+sep+z[799:804]+sep+z[804:810]+sep+z[810:830]+sep+z[830:834]+sep+z[834:835]+sep+z[835:836]+sep+z[836:841]+sep+z[841:891]+sep+z[891:892]+sep+z[892:906]+sep+z[906:926]+sep+z[926:940]+sep+z[940:941]+sep+z[941:949]+sep+z[949:950]
                form1.write(lines)
                form1.write(enter)

            if cocok_form2:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:68]+sep+z[68:100]+sep+z[100:200]+sep+z[200:201]+sep+z[201:231]+sep+z[231:251]+sep+z[251:351]+sep+z[351:355]+sep+z[355:405]+sep+z[405:455]+sep+z[455:460]+sep+z[460:462]+sep+z[462:476]+sep+z[476:496]+sep+z[496:510]+sep+z[510:530]+sep+z[530:531]+sep+z[531:539]+sep+z[539:540]
                form2.write(lines)
                form2.write(enter)

            if cocok_form31:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:29]+sep+z[29:61]+sep+z[61:63]+sep+z[63:66]+sep+z[66:69]+sep+z[69:72]+sep+z[72:75]+sep+z[75:77]+sep+z[77:78]+sep+z[78:83]+sep+z[83:98]+sep+z[98:113]+sep+z[113:115]+sep+z[115:123]+sep+z[123:138]+sep+z[138:153]+sep+z[153:253]+sep+z[253:267]+sep+z[267:287]+sep+z[287:301]+sep+z[301:302]+sep+z[302:310]+sep+z[310:311]
                form31.write(lines)
                form31.write(enter)

            if cocok_form33:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:29]+sep+z[29:81]+sep+z[81:83]+sep+z[83:108]+sep+z[108:133]+sep+z[133:141]+sep+z[141:166]+sep+z[166:174]+sep+z[174:182]+sep+z[182:190]+sep+z[190:198]+sep+z[198:200]+sep+z[200:202]+sep+z[202:204]+sep+z[204:205]+sep+z[205:210]+sep+z[210:214]+sep+z[214:229]+sep+z[229:232]+sep+z[232:237]+sep+z[237:238]+sep+z[238:253]+sep+z[253:268]+sep+z[268:283]+sep+z[283:298]+sep+z[298:313]+sep+z[313:328]+sep+z[328:329]+sep+z[329:337]+sep+z[337:339]+sep+z[339:439]+sep+z[439:447]+sep+z[447:462]+sep+z[462:465]+sep+z[465:480]+sep+z[480:495]+sep+z[495:498]+sep+z[498:513]+sep+z[513:528]+sep+z[528:530]+sep+z[530:538]+sep+z[538:553]+sep+z[553:568]+sep+z[568:583]+sep+z[583:591]+sep+z[591:593]+sep+z[593:601]+sep+z[601:701]+sep+z[701:801]+sep+z[801:901]+sep+z[901:915]+sep+z[915:935]+sep+z[935:949]+sep+z[949:950]+sep+z[950:958]+sep+z[958:959]
                form33.write(lines)
                form33.write(enter)

            if cocok_form38:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:29]+sep+z[29:81]+sep+z[81:106]+sep+z[106:108]+sep+z[108:110]+sep+z[110:115]+sep+z[115:119]+sep+z[119:134]+sep+z[134:142]+sep+z[142:150]+sep+z[150:158]+sep+z[158:163]+sep+z[163:166]+sep+z[166:181]+sep+z[181:182]+sep+z[182:190]+sep+z[190:205]+sep+z[205:220]+sep+z[220:235]+sep+z[235:243]+sep+z[243:245]+sep+z[245:345]+sep+z[345:347]+sep+z[347:355]+sep+z[355:455]+sep+z[455:469]+sep+z[469:489]+sep+z[489:503]+sep+z[503:504]+sep+z[504:512]+sep+z[512:513]
                form38.write(lines)
                form38.write(enter)

            if cocok_form41:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:68]+sep+z[68:100]+sep+z[100:102]+sep+z[102:106]+sep+z[106:108]+sep+z[108:158]+sep+z[158:208]+sep+z[208:212]+sep+z[212:312]+sep+z[312:327]+sep+z[327:342]+sep+z[342:357]+sep+z[357:407]+sep+z[407:415]+sep+z[415:420]+sep+z[420:421]+sep+z[421:435]+sep+z[435:455]+sep+z[455:469]+sep+z[469:489]+sep+z[489:490]+sep+z[490:498]+sep+z[498:499]
                form41.write(lines)
                form41.write(enter)

            if cocok_form42:
                lines= z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:68]+sep+z[68:120]+sep+z[120:149]+sep+z[149:199]+sep+z[199:202]+sep+z[202:207]+sep+z[207:232]+sep+z[232:252]+sep+z[252:352]+sep+z[352:353]+sep+z[353:367]+sep+z[367:387]+sep+z[387:401]+sep+z[401:421]+sep+z[421:422]+sep+z[422:430]+sep+z[430:431]
                form41.write(lines)
                form41.write(enter)

            if cocok_form50:
                lines = z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:43]+sep+z[43:61]+sep+z[61:79]+sep+z[79:97]+sep+z[97:115]+sep+z[115:133]+sep+z[133:151]+sep+z[151:169]+sep+z[169:183]+sep+z[183:203]+sep+z[203:217]+sep+z[217:218]+sep+z[218:226]+sep+z[226:227]
                form50.write(lines)
                form50.write(enter)

            if cocok_form60:
                lines=z[0:6]+sep+z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:68]+sep+z[68:83]+sep+z[83:98]+sep+z[98:113]+sep+z[113:128]+sep+z[128:143]+sep+z[143:144]+sep+z[144:159]+sep+z[159:174]+sep+z[174:189]+sep+z[189:204]+sep+z[204:219]+sep+z[219:234]+sep+z[234:249]+sep+z[249:264]+sep+z[264:265]+sep+z[265:279]+sep+z[279:299]+sep+z[299:313]+sep+z[313:333]+sep+z[333:334]+sep+z[334:342]+sep+z[342:343]

            if cocok_form70:
                lines= z[6:7]+sep+z[7:10]+sep+z[10:16]+sep+z[16:19]+sep+z[19:21]+sep+z[21:25]+sep+z[25:55]+sep+z[55:56]+sep+z[56:60]+sep+z[60:103]+sep+z[103:155]+sep+z[155:169]+sep+z[169:189]+sep+z[189:203]+sep+z[203:223]+sep+z[223:248]+sep+z[248:249]+sep+z[249:251]+sep+z[251:259]+sep+z[259:260]
                form70.write(lines)
                form70.write(enter)

#         form2.close()
#         form2.close()

    except ValueError as err:
        print(err.args)


if __name__ == "__main__":
    list_of_files = []
    mmm = initiate_data().input
    nnn = (open(mmm,'rb')).readline()[31:37] # cari bulan dan tahun laporan dalam isi file
    file_data = open(mmm,'rb')
    list_of_files.append(file_data)
#     head_er = open('header.sid', 'w')
#     foot_er = open('footer.sid', 'w')
    form1 = open(nnn+'-form1.csv', 'w')
    list_of_files.append(form1)
    form2 = open(nnn+'-form2.csv', 'w')
    list_of_files.append(form2)
    form31 = open(nnn+'-form31.csv', 'w')
    list_of_files.append(form31)
    form33 = open(nnn+'-form33.csv', 'w')
    list_of_files.append(form33)
    form38 = open(nnn+'-form38.csv', 'w')
    list_of_files.append(form38)
    form41 = open(nnn+'-form41.csv', 'w')
    list_of_files.append(form41)
    form42 = open(nnn+'-form42.csv', 'w')
    list_of_files.append(form42)
    form50 = open(nnn+'-form50.csv', 'w')
    list_of_files.append(form50)
    form60 = open(nnn+'-form60.csv', 'w')
    list_of_files.append(form60)
    form70 = open(nnn+'-form70.csv', 'w')
    list_of_files.append(form70)
    hitung(args=mmm)
    syncronize(args=initiate_data())
#     print 'list files----',list_of_files[4].name
#     print '-----',initiate_data()
    for daftar in list_of_files:
        daftar.close()
