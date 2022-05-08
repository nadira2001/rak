
#============================= Test dynamic path
def dmpath():
    import urllib2
    cid = str(request.vars.CID).strip().upper()
    url = 'http://im-gp.com/dmpath/index.php?CID=' + cid + '&HTTPPASS=e99business321cba'

    result = ''
    try:
        result = urllib2.urlopen(url)
    except:
        result = 'Invalid Request'
    return result


#     cid = str(request.vars.CID).strip().upper()
#     if (cid='BIOPHARMA'):
#         return '<start>http://127.0.0.1:8000/mrepbiopharma/syncmobile/<fd>http://127.0.0.1:8000/mrepbiopharma/static/<fd>http://127.0.0.1:8000/mrepbiopharma/syncmobile/<end>'
    #     return '<start>http://e2.businesssolutionapps.com/mrepbiopharma/syncmobile/<fd>http://e2.businesssolutionapps.com/mrepbiopharma/static/<fd>http://e2.businesssolutionapps.com/mrepbiopharma/syncmobile/<end>'



#============================= get dynamic path

def get_path():
    CID=request.vars.CID
    HTTPPASS=request.vars.HTTPPASS
    if HTTPPASS!='e99business321cba':
        return 'FAILED'
    else:
        if CID=='MACROCABLE':
            # Return: <start>sync<fd>imageShow<fd>imageSubmit<end>
             
            #return '<start>http://127.0.0.1:8000/macrocable/syncmobile/<fd>http://127.0.0.1:8000/macrocable/static/<fd>http://127.0.0.1:8000/macrocable/syncmobile/<end>'
            return '<start>http://e2.businesssolutionapps.com/mrepmacrocable/syncmobile/<fd>http://e2.businesssolutionapps.com/mrepmacrocable/static/<fd>http://e2.businesssolutionapps.com/mrepmacrocable/syncmobile/<end>'

        elif CID=='TKG':
            return '<start>http://w05.yeapps.com/tkg/syncmobile_417_new/<fd>http://107.167.187.177/tkg_image/<fd>http://107.167.187.177/tkg_image/syncmobile_417_new/<fd>http://w05.yeapps.com/tkg/syncmobile_417_new/<end>'
#             return '<start>http://w02.yeapps.com/tkg/syncmobile_417_new/<fd>http://w02.yeapps.com/tkg/static/<fd>http://w02.yeapps.com/tkg/syncmobile_417_new/<fd>http://w02.yeapps.com/tkg/syncmobile_417_new/<end>'
        elif CID=='SRBIL':
            return '<start>http://w05.yeapps.com/srbil/syncmobile_417_new/<fd>http://107.167.187.177/tkg_image/<fd>http://107.167.187.177/tkg_image/syncmobile_417_new/<fd>http://w05.yeapps.com/srbil/syncmobile_417_new/<fd>http://w05.yeapps.com/srbil/tour_web/<fd>http://w05.yeapps.com/srbil/tour_web_members/<fd>http://w05.yeapps.com/srbil/track_mobile/<end>'
#             return '<start>http://w05.yeapps.com/srbil/syncmobile_417_new/<fd>http://107.167.187.177/tkg_image/<fd>http://107.167.187.177/tkg_image/syncmobile_417_new/<fd>http://w05.yeapps.com/srbil/syncmobile_417_new/<end>'
        elif CID=='SKF':
            return '<start>http://w04.yeapps.com/skf/syncmobile_rx_171128/<fd>http://w04.yeapps.com/skf/<fd>http://i002.yeapps.com/image_hub/skf_image/skf_image/<fd>http://w04.yeapps.com/skf/syncmobile_rx_171128/<end>'
 

        elif CID=='ACME':
            return '<start>http://a007.yeapps.com/acme/syncmobile_417_new/<fd>http://a007.yeapps.com/acme/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription_acme/<fd>http://a007.yeapps.com/acme/syncmobile_417_new/<end>'
#             return '<start>http://w02.yeapps.com/acme/syncmobile_417_new/<fd>http://a007.yeapps.com/acme/static/<fd>http://a007.yeapps.com/acme/syncmobile_417_new/<fd>http://a007.yeapps.com/acme/syncmobile_417_new/<end>'

        elif CID=='DEMO':
            
            return '<start>http://w02.yeapps.com/demo/syncmobile_417_new/<fd>http://w02.yeapps.com/demo/static/<fd>http://w02.yeapps.com/demo/syncmobile_417_new/<fd>http://w02.yeapps.com/demo/syncmobile_417_new/<end>'
#             return '<start>http://c003.cloudapp.net/demo/syncmobile_417_new/<fd>http://c003.cloudapp.net/demo/static/<fd>http://c003.cloudapp.net/demo/syncmobile_417_new/<fd>http://c003.cloudapp.net/demo/syncmobile_417_new/<end>'
        elif CID=='IBNSINA':
            return '<start>http://w05.yeapps.com/ipi/syncmobile_rx_171128/<fd>http://w05.yeapps.com/ipi/<fd>http://e3.businesssolutionapps.com/image_hub/ibnsina_image/ibnsina_image/<fd>http://w05.yeapps.com/ipi/syncmobile_rx_171128/<end>'
#             return '<start>http://w05.yeapps.com/ipi/syncmobile_rx_171128/<fd>http://w05.yeapps.com/ipi/<fd>http://i001.yeapps.com/image_hub/ibnsina_image/ibnsina_image/<fd>http://w05.yeapps.com/ipi/syncmobile_rx_171128/<end>'
#             return '<start>http://e2.businesssolutionapps.com/ipi/syncmobile_rx_171128/<fd>http://e2.businesssolutionapps.com/ipi/<fd>http://i001.yeapps.com/image_hub/ibnsina_image/ibnsina_image/<fd>http://e2.businesssolutionapps.com/ipi/syncmobile_rx_171128/<end>'
            # return '<start>http://a007.yeapps.com/ipi/syncmobile_rx_171128/<fd>http://a007.yeapps.com/ipi/<fd>http://i001.yeapps.com/image_hub/ibnsina_image/ibnsina_image/<fd>http://a007.yeapps.com/ipi/syncmobile_rx_171128/<end>'
#             return '<start>http://e2.businesssolutionapps.com/ipi/syncmobile_rx_171128/<fd>http://e2.businesssolutionapps.com/ipi/<fd>http://i001.yeapps.com/image_hub/ibnsina_image/ibnsina_image/<fd>http://e2.businesssolutionapps.com/ipi/syncmobile_rx_171128/<end>'
       
        elif CID=='IPINMD':
#             return '<start>http://w05.yeapps.com/ipinmd/syncmobile_417_new/<fd>http://c003.cloudapp.net/ibnsina/static/<fd>http://w05.yeapps.com/ipinmd/syncmobile_417_new/<fd>http://w05.yeapps.com/ipinmd/syncmobile_417_new/<end>'
            return '<start>http://w02.yeapps.com/ipinmd/syncmobile_417_new/<fd>http://c003.cloudapp.net/ibnsina/static/<fd>http://w02.yeapps.com/ipinmd/syncmobile_417_new/<fd>http://w02.yeapps.com/ipinmd/syncmobile_417_new/<end>'

        elif CID=='GPL':
            return '<start>http://w02air.azurewebsites.net/gpl/syncmobile_417_new/<fd>http://w02air.azurewebsites.net/gpl/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription/<fd>http://w02air.azurewebsites.net/gpl/syncmobile_417_new/<end>'
#             return '<start>http://a006.yeapps.com/gpl/syncmobile_417_new/<fd>http://a006.yeapps.com/gpl/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription/<fd>http://a006.yeapps.com/gpl/syncmobile_417_new/<end>'
#             return '<start>http://eapps001.cloudapp.net/mrepglob/syncmobile_order_to_delivery_gh/<fd>http://e2.businesssolutionapps.com/mrepskf/static/<fd>http://e2.businesssolutionapps.com/mrepskf/syncmobile_ofline_ppm_report_test_live_20150502/<end>'
        elif CID=='LABAID':
            return '<start>http://w05.yeapps.com/labaid/syncmobile_417_new/<fd>http://w05.yeapps.com/labaid/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription_labaid/<fd>http://w05.yeapps.com/labaid/syncmobile_417_new/<end>'
#             return '<start>http://w02.yeapps.com/labaid/syncmobile_417_new/<fd>http://w02.yeapps.com/labaid/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription_labaid/<fd>http://w02.yeapps.com/labaid/syncmobile_417_new/<end>'
        
        elif CID=='SKFAHD':
            return '<start>http://w03.yeapps.com/skfah/syncmobile_rx_171128/<fd>http://w03.yeapps.com/skfah/<fd>http://i001.yeapps.com/image_hub/skf_image/skfahd_image/<fd>http://w03.yeapps.com/skfah/syncmobile_rx_171128/<end>'
#             return '<start>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<fd>http://w02.yeapps.com/skfah/<fd>http://i001.yeapps.com/image_hub/skf_image/skf_image/<fd>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<end>'

        elif CID=='SERVIER':
            return '<start>http://w03.yeapps.com/servier/syncmobile_rx_171128/<fd>http://w03.yeapps.com/servier/<fd>http://i001.yeapps.com/image_hub/skf_image/skfahd_image/<fd>http://w03.yeapps.com/servier/syncmobile_rx_171128/<end>'
#             return '<start>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<fd>http://w02.yeapps.com/skfah/<fd>http://i001.yeapps.com/image_hub/skf_image/skf_image/<fd>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<end>'

        elif CID=='NOVO':
            return '<start>http://w03.yeapps.com/novo/syncmobile_rx_171128/<fd>http://w03.yeapps.com/novo/<fd>http://i001.yeapps.com/image_hub/skf_image/skfahd_image/<fd>http://w03.yeapps.com/novo/syncmobile_rx_171128/<end>'
#             return '<start>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<fd>http://w02.yeapps.com/skfah/<fd>http://i001.yeapps.com/image_hub/skf_image/skf_image/<fd>http://w02.yeapps.com/skfah/syncmobile_rx_171128/<end>'

        else:
            return '<start>http://w05.yeapps.com/mrep03/syncmobile_417_new/<fd>http://107.167.187.177/tkg_image/<fd>http://107.167.187.177/tkg_image/syncmobile_417_new/<fd>http://w05.yeapps.com/mrep03/syncmobile_417_new/<fd>http://w05.yeapps.com/mrep03/tour_web/<fd>http://w05.yeapps.com/mrep03/tour_web_members/<fd>http://w05.yeapps.com/mrep03/track_mobile/<end>'

#             return '<start>http://w05.yeapps.com/mrep02/syncmobile_417_new/<fd>http://107.167.187.177/tkg_image/<fd>http://107.167.187.177/tkg_image/syncmobile_417_new/<fd>http://w05.yeapps.com/mrep02/syncmobile_417_new/<end>'
#             return 'FAILED'








