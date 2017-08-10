#!/bin/bash
find ./ -type f -name "*.pyc" -print0 | xargs -0 /bin/rm -f;
find ./ -type f -name ".DS*" -print0 | xargs -0 /bin/rm -f;
#find ../ -type f -name "*.pyc" -print0 | xargs -0 /bin/rm -f;
#find ../ -type f -name ".DS*" -print0 | xargs -0 /bin/rm -f;
#daftar=(account account_accountant account_asset account_cancel account_chart account_voucher analytic base_setup board decimal_precision document edi knowledge mail process product resource)
# daftar=(coba saya)
# sumber=../openobject-addons
# tujuan=../open-ib
# for items in ${daftar[*]}
# do
#     if [ ! -d "$items" ]; then
#         mkdir $tujuan/$items
#         if  [ -d "$items" ]; then
#             echo "sudah ada"
#         fi
#     else
#         echo "sukses"
#        cp -R $sumber/$items $tujuan/$items
#     fi
#    cp -R $sumber/$items $tujuan/$items
#    cp -R ../openobject-addons/7.0/$items .
# done
#find ../openerp-web -type f -name "*.pyc" -print0 | xargs -0 /bin/rm -f;
