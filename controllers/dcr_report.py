
#====================== Doctor Visit

from random import randint

#---------------------------- ADD
def index():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

    response.title = 'Doctor Visit Report'
    

    comRows = db((db.sm_settings.cid == session.cid) & (db. sm_settings.s_key == 'COM_NAME')).select(db.sm_settings.field1, limitby=(0, 1))
    if comRows:
        company_name=comRows[0].field1         
        session.company_name=company_name
        

    c_id = session.cid

    search_form =SQLFORM(db.sm_search_date)
    
    btn_dcrRegion=request.vars.btn_dcrRegion
    btn_dcrRegionD=request.vars.btn_dcrRegionD
    btn_dcrFm=request.vars.btn_dcrFm
    btn_dcrFmD=request.vars.btn_dcrFmD
    btn_dcrTeritory=request.vars.btn_dcrTeritory
    btn_dcrMso=request.vars.btn_dcrMso
    btn_dcrMsoD=request.vars.btn_dcrMsoD
    btn_dcrVisit=request.vars.btn_dcrVisit
    btn_dcrTeritoryD=request.vars.btn_dcrTeritoryD
    btn_dcrDoc=request.vars.btn_dcrDoc
    btn_dcrDocD=request.vars.btn_dcrDocD
    
    
    btn_dcrSummary=request.vars.btn_dcrSummary
    btn_dcrSummaryD=request.vars.btn_dcrSummaryD

    dcr_Summary_Rsm=request.vars.dcr_Summary_Rsm
    btn_dcrSummaryD_Rsm=request.vars.btn_dcrSummaryD_Rsm
    # return btn_dcrSummaryD_Rsm

    dcr_Summary_Am=request.vars.dcr_Summary_Am
    btn_dcrSummaryD_Am=request.vars.btn_dcrSummaryD_Am

    dcr_Summary_Mpo=request.vars.dcr_Summary_Mpo
    btn_dcrSummaryD_Mpo=request.vars.btn_dcrSummaryD_Mpo
    # return dcr_Summary_Am
    btn_dcrVSummary=request.vars.btn_dcrVSummary
    btn_dcrVSummaryD=request.vars.btn_dcrVSummaryD
    btn_dcrVSummarProduct=request.vars.btn_dcrVSummarProduct
    btn_dcrVSummarProductD=request.vars.btn_dcrVSummarProductD
    
    btn_prSummary=request.vars.btn_prSummary
    btn_prSummaryD=request.vars.btn_prSummaryD
    
    date_wise_visit_count=request.vars.date_wise_visit_count
    dcr_count_visit_count=request.vars.dcr_count_visit_count
    dcr_count_visit_count_fm=request.vars.dcr_count_visit_count_fm
    dcr_count_visit_count_fm_area_wise=request.vars.dcr_count_visit_count_fm_area_wise
    dcr_count_visit_count_fm_area_wise_d = request.vars.dcr_count_visit_count_fm_area_wise_d

    dcr_count_visit_count_d=request.vars.dcr_count_visit_count_d
    dcr_count_visit_count_fm_d=request.vars.dcr_count_visit_count_fm_d
    
    dcr_day_countDetails=request.vars.dcr_day_countDetails
    dcr_day_count=request.vars.dcr_day_count

    dcr_day_countDetails_MPO=request.vars.dcr_day_countDetails_MPO
    dcr_day_count_MPO=request.vars.dcr_day_count_MPO
    # return dcr_day_countDetails_MPO
    
    dcr_sum=request.vars.dcr_sum
    client_sum=request.vars.client_sum
    btn_fm_sum=request.vars.btn_fm_sum
    
    
    btn_dcrVSummarRep=request.vars.btn_dcrVSummarRep
    btn_dcrVSummarRepD=request.vars.btn_dcrVSummarRepD
    
    btn_dcrVSummarRep_date=request.vars.btn_dcrVSummarRep_date
    btn_dcrVSummarRepD_date=request.vars.btn_dcrVSummarRepD_date
    btn_activity_status_order_d=request.vars.btn_activity_status_order_d
    btn_activity_status_dcr_d = request.vars.btn_activity_status_dcr_d

    btn_associate_call_details=request.vars.btn_associate_call_details
    btn_associate_call_d=request.vars.btn_associate_call_d


    btn_associate_call_details_Zone=request.vars.btn_associate_call_details_Zone
    btn_associate_call_details_Reg=request.vars.btn_associate_call_details_Reg

    
    mpo_ranking=request.vars.mpo_ranking
    am_ranking=request.vars.am_ranking
    zm_ranking=request.vars.zm_ranking
    rsm_ranking=request.vars.rsm_ranking
    
    # return mpo_ranking
    if (btn_associate_call_details_Reg or btn_associate_call_details or btn_associate_call_details_Zone or btn_associate_call_d or btn_activity_status_order_d or btn_activity_status_dcr_d or btn_fm_sum or btn_dcrRegion or btn_dcrRegionD or btn_dcrFm or btn_dcrFmD or btn_dcrTeritory or btn_dcrMso or btn_dcrMsoD or btn_dcrVisit or btn_dcrTeritoryD or btn_dcrDoc or btn_dcrDocD or btn_dcrSummary or btn_dcrSummaryD or dcr_Summary_Rsm or btn_dcrSummaryD_Rsm or  dcr_Summary_Am or btn_dcrSummaryD_Am or dcr_Summary_Mpo or btn_dcrSummaryD_Mpo or btn_dcrVSummary or btn_dcrVSummaryD or btn_dcrVSummarProduct or btn_dcrVSummarProductD or btn_prSummary or btn_prSummaryD or date_wise_visit_count or dcr_count_visit_count_d or dcr_count_visit_count_fm_d or dcr_count_visit_count or dcr_count_visit_count_fm or dcr_count_visit_count_fm_area_wise or dcr_count_visit_count_fm_area_wise_d or dcr_day_countDetails or dcr_day_count or dcr_day_countDetails_MPO or dcr_day_count_MPO or btn_dcrVSummarRep or btn_dcrVSummarRepD or mpo_ranking or am_ranking or zm_ranking or rsm_ranking):
        date_from=request.vars.from_dt_3
        date_to=request.vars.to_dt_3
        
        depot=str(request.vars.sales_depot_id_SC)
        zm_SC=str(request.vars.zm_SC)
        rsm_SC=str(request.vars.rsm_SC)
        fm_SC=str(request.vars.fm_SC)
        # return fm_SC
        
        tr_SC=str(request.vars.tr_SC)
        mso=str(request.vars.mso_id_sales).replace(",","").replace("['","").replace("']","").replace("''","")
        doc_idname=str(request.vars.doc_id_sales).replace(",","").replace("['","").replace("']","").replace("''","")
        
        product=str(request.vars.product)
        brand=str(request.vars.brand)
        category=str(request.vars.category)
        
        if (len(mso) < 4):
            mso=''
            
            
        brand=brand
        category=category
        
        
        depot_id=depot
        depot_name=''
        
        
        dateFlag=True
        #           return 'asfsaf'
        try:
            from_dt2=datetime.datetime.strptime(str(date_from),'%Y-%m-%d')
        except:
            dateFlag=False
        
        
        if ((depot!='') & (depot.find('|') != -1)):             
            depot_id=depot.split('|')[0].upper().strip()
            depot_name=depot.split('|')[1].strip()
            
        else:
            depot_id=depot
            depot_name=''
        
        
        if ((product!='')) : 
            try:
                product_id=product.split('|')[0].upper().strip()
                product_name=product.split('|')[1].strip()
            except:
                product_id=product
                product_name='' 
        else:
            product_id=product
            product_name=''    
        

        if ((zm_SC!='')) : 
            try:
                zm_id=zm_SC.split('|')[0].upper().strip()
                zm_name=zm_SC.split('|')[1].strip()
            except:
                zm_id=zm_SC
        else:
            zm_id=zm_SC
            zm_name=''


        if ((rsm_SC!='')) : 
            try:
                rsm_id=rsm_SC.split('|')[0].upper().strip()
                rsm_name=rsm_SC.split('|')[1].strip()
            except:
                rsm_id=rsm_SC
        else:
            rsm_id=rsm_SC
            rsm_name=''
        


        if ((fm_SC!='') & (fm_SC.find('|') != -1)) : 
            fm_id=fm_SC.split('|')[0].upper().strip()
            fm_name=fm_SC.split('|')[1].strip()
            fmA_id=fm_SC.split('|')[2].strip()
            # return fm_area_id
        else:
            fm_id=fm_SC
            fm_name=''
            fmA_id=fm_SC
            # fmA_name=''
        


        if ((tr_SC!='') & (tr_SC.find('|') != -1)) : 
            tr_id=tr_SC.split('|')[0].upper().strip()
            tr_name=tr_SC.split('|')[1].strip()
        else:
            tr_id=tr_SC
            tr_name=''
        if ((mso!='') & (mso.find('|') != -1)) :  
            mso_id=mso.split('|')[0].upper().strip()
            mso_name=mso.split('|')[1].strip()
        else:
              mso_id=mso
              mso_name=''
        
        if ((doc_idname!='') & (doc_idname.find('|') != -1)) :  
            doc=doc_idname.split('|')[0].upper().strip()
            doc_name=doc_idname.split('|')[1].strip()
        else:
              doc=doc_idname
              doc_name=''
        
#         return mso_id
        dateDiff=0
        dateFlag=True
        try:
          from_dt2=datetime.datetime.strptime(str(date_from),'%Y-%m-%d')
          to_dt2=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 

          if from_dt2>to_dt2:
             dateFlag=False
        except:
            dateFlag=False
    
        if dateFlag==False:
            response.flash="Invalid Date Range"
        else:            
            dateDiff=(to_dt2-from_dt2).days
        if dateDiff>90 and not dcr_day_count:
            response.flash="Maximum 90 days allowed between Date Range"
            dateFlag=False
        if ((depot!='') & (depot.find('|') != -1)):             
                depot_id=depot.split('|')[0].upper().strip()
                depot_name=depot.split('|')[1].strip()
                user_depot_address=''
                if session.user_type!='Depot': 
                    depotRows = db((db.sm_depot.cid == session.cid) & (db.sm_depot.depot_id == depot_id)).select(db.sm_depot.name,db.sm_depot.depot_category,db.sm_depot.field1, limitby=(0, 1))
                    if depotRows:
                        user_depot_address=depotRows[0].field1         
                        session.user_depot_address=user_depot_address
        else:
             session.user_depot_address='' 
#         return    dateFlag  

        
        if dateFlag!=False:
            if btn_dcrRegion:
                redirect (URL('dcrRsm',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrRegionD:
                redirect (URL('dcrRsmD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrFm:
                redirect (URL('dcrFm',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrFmD:
                redirect (URL('dcrFmD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrTeritory:
                redirect (URL('dcrTeritory',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrMso:
                redirect (URL('dcrMso',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrMsoD:
                redirect (URL('dcrMsoD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrVisit:
                redirect (URL('dcrVisit',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrTeritoryD:
                redirect (URL('dcrTeritoryD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrDoc:
                redirect (URL('dcrDoc',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrDocD:
                redirect (URL('dcrDocD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            
            if btn_dcrSummary:
                redirect (URL('dcrSummaryZm',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,doc=doc,doc_name=doc_name)))           
            if btn_dcrSummaryD:
                redirect (URL('dcrSummaryD',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,doc=doc,doc_name=doc_name)))            
            
            if dcr_Summary_Rsm:
                redirect (URL('dcrSummaryRSM',vars=dict(date_from=date_from,date_to=date_to,rsm_id=rsm_id,rsm_name=rsm_name,doc=doc,doc_name=doc_name)))            
            if btn_dcrSummaryD_Rsm:
                redirect (URL('dcrSummaryRSM_D',vars=dict(date_from=date_from,date_to=date_to,rsm_id=rsm_id,rsm_name=rsm_name,doc=doc,doc_name=doc_name)))
           
            if dcr_Summary_Am:
                redirect (URL('dcrSummaryAM',vars=dict(date_from=date_from,date_to=date_to,fmA_id=fmA_id,doc=doc,doc_name=doc_name)))
            if btn_dcrSummaryD_Am:
                redirect (URL('dcrSummaryAM_D',vars=dict(date_from=date_from,date_to=date_to,fmA_id=fmA_id,doc=doc,doc_name=doc_name)))
           
            if dcr_Summary_Mpo:
                redirect (URL('dcrSummaryMPO',vars=dict(date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,tr_id=tr_id,tr_name=tr_name,doc=doc,doc_name=doc_name)))
           
            if btn_dcrSummaryD_Mpo:
                redirect (URL('dcrSummaryMPO_D',vars=dict(date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,tr_id=tr_id,tr_name=tr_name,doc=doc,doc_name=doc_name)))
           


            if btn_dcrVSummary:
                redirect (URL('dcrVSummary',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrVSummaryD:
                redirect (URL('dcrVSummaryD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrVSummarProduct:
                redirect (URL('dcrVSummaryProduct',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_dcrVSummarProductD:
                redirect (URL('dcrVSummaryProductD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_prSummary:
                redirect (URL('prSummary',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_prSummaryD:
                redirect (URL('prSummaryD',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            
            
            if dcr_day_countDetails:
                redirect (URL('dcr_day_count_details',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))            
            if dcr_day_count:
                redirect (URL('dcr_day_count',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            
            if dcr_day_countDetails_MPO:
                redirect (URL('dcr_day_count_details_MPO',vars=dict(date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))            
            if dcr_day_count_MPO:
                redirect (URL('dcr_day_count_MPO',vars=dict(date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            


            if date_wise_visit_count:
                redirect (URL('dcrSummaryDateWiseVisitCount',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count:
                redirect (URL('dcrCountVisitCount',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count_d:
                redirect (URL('dcrCountVisitCount_d',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count_fm:
                redirect(URL('dcrCountVisitCountFm',vars=dict(date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id,tr_name=tr_name, product_id=product_id, product_name=product_name, brand=brand,category=category, mso_id=mso_id, mso_name=mso_name, doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count_fm_d:
                redirect (URL('dcr_count_visit_count_fm_d',vars=dict(date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count_fm_area_wise:
                redirect(URL('dcrCountVisitCountFmAreaWise',vars=dict(date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id,tr_name=tr_name, product_id=product_id, product_name=product_name, brand=brand,category=category, mso_id=mso_id, mso_name=mso_name, doc=doc,doc_name=doc_name)))
            if dcr_count_visit_count_fm_area_wise_d:
                redirect(URL('dcrCountVisitCountFmAreaWiseD',vars=dict(date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id,tr_name=tr_name, product_id=product_id, product_name=product_name, brand=brand,category=category, mso_id=mso_id, mso_name=mso_name, doc=doc,doc_name=doc_name)))


            if btn_dcrVSummarRep:
                redirect (URL('ffreportData',vars=dict(date_from=date_from)))
            if btn_dcrVSummarRepD:
                redirect (URL('ffreportData_load',vars=dict(date_from=date_from)))
            if btn_activity_status_order_d:
                redirect (URL('activity_status_order_d',vars=dict(date_from=date_from,date_to=date_to)))
            if btn_activity_status_dcr_d:
                redirect (URL('activity_status_dcr_d',vars=dict(date_from=date_from,date_to=date_to)))
            
            if btn_associate_call_details:
                redirect (URL('associatedCallDetails',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))

            if btn_associate_call_d:
                redirect (URL('associatedCallD',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_associate_call_details_Zone:
                redirect (URL('associatedCallD_Zone',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if btn_associate_call_details_Reg:
                redirect (URL('associatedCallD_Region',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))


            if mpo_ranking:
                redirect (URL('sin_mpo_ranking',vars=dict(date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)))
            if am_ranking:
                redirect (URL('sin_fm_ranking',vars=dict(date_from=date_from,date_to=date_to,fm_id=fm_id,fm_name=fm_name,doc=doc,doc_name=doc_name)))
            if zm_ranking:
                redirect (URL('sin_zm_ranking',vars=dict(date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,doc=doc,doc_name=doc_name)))
            if rsm_ranking:
                redirect (URL('sin_rsm_ranking',vars=dict(date_from=date_from,date_to=date_to,rsm_id=rsm_id,rsm_name=rsm_name,doc=doc,doc_name=doc_name)))
                     

# Nazma

    if (btn_dcrVSummarRep_date or btn_dcrVSummarRepD_date):
        date_from=request.vars.from_dt_3
        date_to=request.vars.to_dt_3
        dateDiff=0
        dateFlag=True
        try:
          from_dt2=datetime.datetime.strptime(str(date_from),'%Y-%m-%d')
          to_dt2=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 

          if from_dt2>to_dt2:
             dateFlag=False
        except:
            dateFlag=False
    
        if dateFlag==False:
            response.flash="Invalid Date Range"
        else:            
            dateDiff=(to_dt2-from_dt2).days
        if dateDiff>31 and not dcr_day_count:
            response.flash="Maximum 31 days allowed between Date Range"
            dateFlag=False

        if dateFlag!=False:

            if btn_dcrVSummarRep_date:
                redirect (URL('total_ffreportData',vars=dict(date_from=date_from,date_to=date_to)))
            if btn_dcrVSummarRepD_date:
                redirect (URL('total_ffreportData_load',vars=dict(date_from=date_from,date_to=date_to)))
        

            
            
    if (btn_fm_sum or dcr_sum or client_sum ):
        yearGet=request.vars.yearGet
        monthGet=request.vars.monthGet                        
        tr_SC2= request.vars.tr_SC2
        txt_fm= request.vars.txt_fm
       
        
        
        if ((yearGet=='') or (monthGet=='')):
            response.flash="Please Select Year ,Month And Tr"
        else:
            if dcr_sum:
                if tr_SC2=='':
                    response.flash="Please Select Year ,Month And Tr"
                else:                    
                    redirect (URL('dcr_sum',vars=dict(yearGet=yearGet,monthGet=monthGet,tr_SC2=tr_SC2)))
            if client_sum:
                if tr_SC2=='':
                    response.flash="Please Select Year ,Month And Tr"
                else:
                    redirect (URL('client_sum',vars=dict(yearGet=yearGet,monthGet=monthGet,tr_SC2=tr_SC2)))
        
            if btn_fm_sum:
                if txt_fm=='':
                    response.flash="Required FM."
                else:
                    redirect (URL('dcr_sum_fm',vars=dict(yearGet=yearGet,monthGet=monthGet,txt_fm=txt_fm)))
            
            
#         flagRep=0
#         reportShow=''
#             recRep=db((db.sm_doc_visit_report.cid == cid) & (db.sm_doc_visit_report.y_month == year_month)  & (db.sm_doc_visit_report.tr==se_market_report)).select(db.sm_doc_visit_report.ALL, orderby=db.sm_doc_visit_report.tr)
           
#             
#             reportShow=reportShow+'<tr>'
#             reportShow=reportShow+'<td style="background-color:#FFC">'+str(recRep.doc)+'<td style="background-color:#FFC">'+str(recRep.doc_name)+'</td>'+'<td>'+str(d_1)+'</td>'+'<td>'+str(d_2)+'</td>'+'<td>'+str(d_3)+'</td>'+'<td>'+str(d_4)+'</td>'+'<td>'+str(d_5)+'</td>'+'<td>'+str(d_6)+'</td>'+'<td>'+str(d_7)+'</td>'+'<td>'+str(d_8)+'</td>'+'<td>'+str(d_9)+'</td>'+'<td>'+str(d_10)+'</td>'+'<td>'+str(d_11)+'</td>'+'<td>'+str(d_12)+'</td>'+'<td>'+str(d_13)+'</td>'+'<td>'+str(d_14)+'</td>'+'<td>'+str(d_15)+'</td>'+'<td>'+str(d_16)+'</td>'+'<td>'+str(d_17)+'</td>'+'<td>'+str(d_18)+'</td>'+'<td>'+str(d_19)+'</td>'+'<td>'+str(d_20)+'</td>'+'<td>'+str(d_21)+'</td>'+'<td>'+str(d_22)+'</td>'+'<td>'+str(d_23)+'</td>'+'<td>'+str(d_24)+'</td>'+'<td>'+str(d_25)+'</td>'+'<td>'+str(d_26)+'</td>'+'<td>'+str(d_27)+'</td>'+'<td>'+str(d_28)+'</td>'+'<td>'+str(d_29)+'</td>'+'<td>'+str(d_30)+'</td>'+'<td>'+str(d_31)+'</td>'+'<td style="background-color:#FFC">'+str(total)+'</td>'
#             reportShow=reportShow+'</tr>'
#     #             return total
#     #         reportShow=reportShow+'<tr>'
#     #         reportShow=reportShow+'<td>'+str(recRep.rsm_id)+'<td>'+str(recRep.rsm_name)+'</td>'+'<td>'+str(recRep.fm_id)+'<td>'+str(recRep.fm_name)+'</td>'+'<td>'+str(recRep.tr)+'<td>'+str(recRep.tr_name)+'</td>'+'<td>'+str(recRep.doc)+'<td>'+str(recRep.doc_name)+'</td>'+'<td>'+str(recRep.d_1)+'</td>'+'<td>'+str(recRep.d_2)+'</td>'+'<td>'+str(recRep.d_3)+'</td>'+'<td>'+str(recRep.d_4)+'</td>'+'<td>'+str(recRep.d_5)+'</td>'+'<td>'+str(recRep.d_6)+'</td>'+'<td>'+str(recRep.d_7)+'</td>'+'<td>'+str(recRep.d_8)+'</td>'+'<td>'+str(recRep.d_9)+'</td>'+'<td>'+str(recRep.d_10)+'</td>'+'<td>'+str(recRep.d_11)+'</td>'+'<td>'+str(recRep.d_12)+'</td>'+'<td>'+str(recRep.d_13)+'</td>'+'<td>'+str(recRep.d_14)+'</td>'+'<td>'+str(recRep.d_15)+'</td>'+'<td>'+str(recRep.d_16)+'</td>'+'<td>'+str(recRep.d_17)+'</td>'+'<td>'+str(recRep.d_18)+'</td>'+'<td>'+str(recRep.d_19)+'</td>'+'<td>'+str(recRep.d_20)+'</td>'+'<td>'+str(recRep.d_21)+'</td>'+'<td>'+str(recRep.d_22)+'</td>'+'<td>'+str(recRep.d_23)+'</td>'+'<td>'+str(recRep.d_24)+'</td>'+'<td>'+str(recRep.d_25)+'</td>'+'<td>'+str(recRep.d_26)+'</td>'+'<td>'+str(recRep.d_27)+'</td>'+'<td>'+str(recRep.d_28)+'</td>'+'<td>'+str(recRep.d_29)+'</td>'+'<td>'+str(recRep.d_30)+'</td>'+'<td>'+str(recRep.d_31)+'</td>'+'<td>'+str(total)+'</td>'
#     #         reportShow=reportShow+'</tr>'
#         
#         reportShow=reportShow+'</table>'   
                     
    return dict(search_form=search_form)




def associatedCallDetails():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   

    c_id = session.cid
    response.title='Associated Call Details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    
    # depot_id=str(request.vars.depot_id).strip()
    # depot_name=str(request.vars.depot_name).strip() 
    
    zm_id=str(request.vars.zm_id).strip()
    # return 
    zm_name=str(request.vars.zm_name).strip()

    rsm_id=str(request.vars.rsm_id).strip()
    # return rsm_id
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # return rsm_id

    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    # return mso_id
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
#    date_to_m=date_to_m + datetime.timedelta(days = 1) 

#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_associate_call.cid == c_id)
    qset = qset(db.sm_doctor_associate_call.visit_date >= date_from)
    qset = qset(db.sm_doctor_associate_call.visit_date <= date_to)
    
    # if (depot_id!=''):
    #     qset = qset(db.sm_doctor_associate_call.depot_id == depot_id)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level1_id == rsm_id)
    
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_associate_call.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_associate_call.level3_id == tr_id)

    if (mso_id!=''):
        qset = qset(db.sm_doctor_associate_call.visit_by_id == mso_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_associate_call.doc_id == doc)
   
    records = qset.select(db.sm_doctor_associate_call.ALL,orderby=~db.sm_doctor_associate_call.visit_date)
    # return records
    totalCount=qset.count()
    return dict(totalCount=totalCount,records=records,date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def associatedCallD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Associated Call Details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    
    # depot_id=str(request.vars.depot_id).strip()
    # depot_name=str(request.vars.depot_name).strip() 
    
    zm_id=str(request.vars.zm_id).strip()
    # return 
    zm_name=str(request.vars.zm_name).strip()

    rsm_id=str(request.vars.rsm_id).strip()
    # return rsm_id
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # return rsm_id

    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    # return mso_id
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
#    date_to_m=date_to_m + datetime.timedelta(days = 1) 

#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_associate_call.cid == c_id)
    qset = qset(db.sm_doctor_associate_call.am_flag == 1)
    qset = qset(db.sm_doctor_associate_call.visit_date >= date_from)
    qset = qset(db.sm_doctor_associate_call.visit_date <= date_to)
    
    # if (depot_id!=''):
    #     qset = qset(db.sm_doctor_associate_call.depot_id == depot_id)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level1_id == rsm_id)
    
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_associate_call.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_associate_call.level3_id == tr_id)

    if (mso_id!=''):
        qset = qset(db.sm_doctor_associate_call.visit_by_id == mso_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_associate_call.doc_id == doc)
    
    
    
   
    records = qset.select(db.sm_doctor_associate_call.ALL,orderby=~db.sm_doctor_associate_call.visit_date)
    # return db._lastsql
    totalCount=qset.count()
    # return records
    myString='DateRange,'+date_from+','+date_to+'\n\n'
    myString+='RSM,'+zm_id+'|'+zm_name+'\n'
    myString+='ZM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fmA_id+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
   # myString+='Product,'+product_id+'|'+product_name+'\n'
   # myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

    myString+= 'Total :'+','+str(totalCount) + '\n\n'     
    myString+='Date,Ref,Doc ID,Doc Name,Tr ID,Tr Name,Visit By ID, Visit By Name,AM ID,AM Name,ZM ID, ZM Name,RM ID,RM Name\n'
    
    
    for row in records:
        myString+=str(row.visit_date)+','+str(row.dcr_ref)+','+str(row.doc_id)+','+str(row.doc_name).replace(',',' ')+','+str(row.level3_id)+','+\
        str(row.level3_name)+','+str(row.visit_by_id)+','+str(row.visit_by_name)+','+str(row.level2_sup_id)+','+\
        str(row.level2_sup_name)+','+str(row.level1_sup_id)+','+str(row.level1_sup_name)+','+str(row.level0_sup_id)+','+\
        str(row.level0_sup_name)+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=associate_call_details.csv'   
    return str(myString)

# ===========================
def associatedCallD_Zone():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Associated Call Details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    
    # depot_id=str(request.vars.depot_id).strip()
    # depot_name=str(request.vars.depot_name).strip() 
    
    zm_id=str(request.vars.zm_id).strip()
    # return 
    zm_name=str(request.vars.zm_name).strip()

    rsm_id=str(request.vars.rsm_id).strip()
    # return rsm_id
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # return rsm_id

    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    # return mso_id
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
#    date_to_m=date_to_m + datetime.timedelta(days = 1) 

#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_associate_call.cid == c_id)
    qset = qset(db.sm_doctor_associate_call.level1_sup_id != '')

    qset = qset(db.sm_doctor_associate_call.visit_date >= date_from)
    qset = qset(db.sm_doctor_associate_call.visit_date <= date_to)
    
    # if (depot_id!=''):
    #     qset = qset(db.sm_doctor_associate_call.depot_id == depot_id)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level1_id == rsm_id)
    
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_associate_call.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_associate_call.level3_id == tr_id)

    if (mso_id!=''):
        qset = qset(db.sm_doctor_associate_call.visit_by_id == mso_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_associate_call.doc_id == doc)
    
    
    
   
    records = qset.select(db.sm_doctor_associate_call.ALL,db.sm_doctor_associate_call.id.count(),orderby=~db.sm_doctor_associate_call.visit_date, groupby= db.sm_doctor_associate_call.level0_id| db.sm_doctor_associate_call.level1_id| db.sm_doctor_associate_call.level1_sup_id| db.sm_doctor_associate_call.level1_sup_name )
    totalCount=qset.count()
    # return records
    myString='DateRange,'+date_from+','+date_to+'\n\n'
    myString+='RSM,'+zm_id+'|'+zm_name+'\n'
    myString+='ZM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fmA_id+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
   # myString+='Product,'+product_id+'|'+product_name+'\n'
   # myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

    myString+= 'Total :'+','+str(totalCount) + '\n\n'     
    myString+='RM ID,RM Name,ZM ID,Name,Count\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doctor_associate_call.level0_id]) +','+str(record[db.sm_doctor_associate_call.level0_name])+','+str(record[db.sm_doctor_associate_call.level1_sup_id]) +','+str(record[db.sm_doctor_associate_call.level1_sup_name])+','+str(record[db.sm_doctor_associate_call.id.count()])+'\n'
        
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=associate_call_details.csv'   
    return str(myString)


def associatedCallD_Region():
    # return 'Region'
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Associated Call Details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    
    # depot_id=str(request.vars.depot_id).strip()
    # depot_name=str(request.vars.depot_name).strip() 
    
    zm_id=str(request.vars.zm_id).strip()
    # return 
    zm_name=str(request.vars.zm_name).strip()

    rsm_id=str(request.vars.rsm_id).strip()
    # return rsm_id
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # return rsm_id

    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    # return mso_id
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
#    date_to_m=date_to_m + datetime.timedelta(days = 1) 

#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_associate_call.cid == c_id)
    qset = qset(db.sm_doctor_associate_call.level0_sup_id != '')

    qset = qset(db.sm_doctor_associate_call.visit_date >= date_from)
    qset = qset(db.sm_doctor_associate_call.visit_date <= date_to)
    
    # if (depot_id!=''):
    #     qset = qset(db.sm_doctor_associate_call.depot_id == depot_id)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_associate_call.level1_id == rsm_id)
    
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_associate_call.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_associate_call.level3_id == tr_id)

    if (mso_id!=''):
        qset = qset(db.sm_doctor_associate_call.visit_by_id == mso_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_associate_call.doc_id == doc)
    
    
    
   
    records = qset.select(db.sm_doctor_associate_call.ALL,db.sm_doctor_associate_call.id.count(),orderby=~db.sm_doctor_associate_call.visit_date, groupby=db.sm_doctor_associate_call.level0_sup_id| db.sm_doctor_associate_call.level0_sup_name)
    totalCount=qset.count()
    # return records
    myString='DateRange,'+date_from+','+date_to+'\n\n'
    myString+='RSM,'+zm_id+'|'+zm_name+'\n'
    myString+='ZM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fmA_id+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
   # myString+='Product,'+product_id+'|'+product_name+'\n'
   # myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

    myString+= 'Total :'+','+str(totalCount) + '\n\n'     
    myString+='RM ID,RM Name,Count\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doctor_associate_call.level0_sup_id]) +','+str(record[db.sm_doctor_associate_call.level0_sup_name])+','+str(record[db.sm_doctor_associate_call.id.count()])+'\n'
        
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=associate_call_details.csv'   
    return str(myString)
# ==========================

def dcr_sum_fm():
    cid=session.cid
    yearGet=request.vars.yearGet
    monthGet=request.vars.monthGet
    txt_fm=request.vars.txt_fm
    
    txt_fm_id=str(txt_fm).split('|')[0]
    fm_level_id=str(txt_fm).split('|')[2]
    
    year_month=str(yearGet)+'-'+str(monthGet)+'-01'
    
    qset=db()
    qset=qset(db.sm_doc_visit_report_fm.cid == cid)
    qset=qset(db.sm_doc_visit_report_fm.y_month == year_month)    
    qset=qset(db.sm_doc_visit_report_fm.fm_id == txt_fm_id)
    qset=qset(db.sm_doc_visit_report_fm.fm_level_id == fm_level_id)
    
    
    records=qset.select(db.sm_doc_visit_report_fm.ALL, orderby=db.sm_doc_visit_report_fm.doc)
    recordsSum=qset.select(db.sm_doc_visit_report_fm.id.count(),db.sm_doc_visit_report_fm.d_1.sum(),db.sm_doc_visit_report_fm.d_2.sum(),db.sm_doc_visit_report_fm.d_3.sum(),db.sm_doc_visit_report_fm.d_4.sum(),db.sm_doc_visit_report_fm.d_5.sum(),db.sm_doc_visit_report_fm.d_6.sum(),db.sm_doc_visit_report_fm.d_7.sum(),db.sm_doc_visit_report_fm.d_8.sum(),db.sm_doc_visit_report_fm.d_9.sum(),db.sm_doc_visit_report_fm.d_10.sum(),db.sm_doc_visit_report_fm.d_11.sum(),db.sm_doc_visit_report_fm.d_12.sum(),db.sm_doc_visit_report_fm.d_13.sum(),db.sm_doc_visit_report_fm.d_14.sum(),db.sm_doc_visit_report_fm.d_15.sum(),db.sm_doc_visit_report_fm.d_16.sum(),db.sm_doc_visit_report_fm.d_17.sum(),db.sm_doc_visit_report_fm.d_18.sum(),db.sm_doc_visit_report_fm.d_19.sum(),db.sm_doc_visit_report_fm.d_20.sum(),db.sm_doc_visit_report_fm.d_21.sum(),db.sm_doc_visit_report_fm.d_22.sum(),db.sm_doc_visit_report_fm.d_23.sum(),db.sm_doc_visit_report_fm.d_24.sum(),db.sm_doc_visit_report_fm.d_25.sum(),db.sm_doc_visit_report_fm.d_26.sum(),db.sm_doc_visit_report_fm.d_27.sum(),db.sm_doc_visit_report_fm.d_28.sum(),db.sm_doc_visit_report_fm.d_29.sum(),db.sm_doc_visit_report_fm.d_30.sum(),db.sm_doc_visit_report_fm.d_31.sum(), groupby=db.sm_doc_visit_report_fm.cid,limitby=(0,1))
    
    return dict(records=records,recordsSum=recordsSum,yearGet=yearGet,monthGet=monthGet,fm=txt_fm)




def dcr_sum():
    yearGet=request.vars.yearGet
    monthGet=request.vars.monthGet
    tr_SC2= request.vars.tr_SC2
    year_month=str(yearGet)+'-'+str(monthGet) 
    se_market_report=tr_SC2.split('|')[0]
    cid=session.cid
    rsm=''
    fm=''
    tr=''
    docTr=0
    recRepDoc=db((db.sm_doctor_area.cid == cid) & (db.sm_doctor_area.area_id == se_market_report)).select(db.sm_doctor_area.id.count(), limitby=(0,1))
    if recRepDoc:
        docTr=recRepDoc[0][db.sm_doctor_area.id.count()]
    
    
    recordDocStr="Select doc_id, doc_name FROM sm_doctor_area where doc_id NOT IN ( Select doc from sm_doc_visit_report where tr ='"+str(se_market_report)+"' and y_month='"+str(year_month)+"') and area_id='"+str(se_market_report)+"'"
    recordDoc=db.executesql(recordDocStr,as_dict = True)
    
    
#     db((db.sm_doctor_area.cid == cid) & (db.sm_doc_visit_report.cid == cid)  & (db.sm_doc_visit_report.doc!= db.sm_doctor_area.doc_id)  & (db.sm_doctor_area.area_id==se_market_report)& (db.sm_doc_visit_report.tr==se_market_report) & (db.sm_doc_visit_report.y_month == year_month)  ).select(db.sm_doctor_area.doc_id,db.sm_doctor_area.doc_name, orderby=db.sm_doctor_area.doc_name , groupby=db.sm_doctor_area.doc_id)
#     return db._lastsql
#     return recordDoc
#     return year_month
    records=db((db.sm_doc_visit_report.cid == cid) & (db.sm_doc_visit_report.y_month == year_month)  & (db.sm_doc_visit_report.tr==se_market_report)).select(db.sm_doc_visit_report.ALL, orderby=db.sm_doc_visit_report.tr)
#     return records
    for rec in records:
        rsm=str(rec.rsm_name)+' | '+str(rec.rsm_id)
        fm=str(rec.fm_name)+' | '+str(rec.fm_id)
        tr=str(rec.tr_name)+' | '+str(rec.tr)
    
    
    if monthGet=='01':monthGet='Jan'
    if monthGet=='02':monthGet='Feb'
    if monthGet=='03':monthGet='Mar'
    if monthGet=='04':monthGet='Apr'
    if monthGet=='05':monthGet='May'
    if monthGet=='06':monthGet='Jun'
    if monthGet=='07':monthGet='Jul'
    if monthGet=='08':monthGet='Aug'
    if monthGet=='09':monthGet='Sep'
    if monthGet=='10':monthGet='Oct'
    if monthGet=='11':monthGet='Nov'
    if monthGet=='12':monthGet='Dec'
    
    
    
    return dict(records=records,yearGet=yearGet,monthGet=monthGet,tr_SC2=tr_SC2,rsm=rsm,fm=fm,tr=tr,docTr=docTr,recordDoc=recordDoc)

def client_sum():
    yearGet=request.vars.yearGet
    monthGet=request.vars.monthGet
    tr_SC2= request.vars.tr_SC2
    year_month=str(yearGet)+'-'+str(monthGet) 
    se_market_report=tr_SC2.split('|')[0]
    cid=session.cid
#     cid='IBNSINA'
    rsm=''
    fm=''
    tr=''
    recRepDoc=db((db.sm_client.cid == cid) & (db.sm_client.area_id == se_market_report)).select(db.sm_client.id.count(), limitby=(0,1))
    docTr=0
    if recRepDoc:
        docTr=recRepDoc[0][db.sm_client.id.count()]
    records=db((db.sm_client_visit_report.cid == cid) & (db.sm_client_visit_report.y_month == year_month)  & (db.sm_client_visit_report.tr==se_market_report)).select(db.sm_client_visit_report.ALL, orderby=db.sm_client_visit_report.tr)
    for rec in records:
        rsm=str(rec.rsm_name)+' | '+str(rec.rsm_id)
        fm=str(rec.fm_name)+' | '+str(rec.fm_id)
        tr=str(rec.tr_name)+' | '+str(rec.tr)
    
    
    if monthGet=='01':monthGet='Jan'
    if monthGet=='02':monthGet='Feb'
    if monthGet=='03':monthGet='Mar'
    if monthGet=='04':monthGet='Apr'
    if monthGet=='05':monthGet='May'
    if monthGet=='06':monthGet='Jun'
    if monthGet=='07':monthGet='Jul'
    if monthGet=='08':monthGet='Aug'
    if monthGet=='09':monthGet='Sep'
    if monthGet=='10':monthGet='Oct'
    if monthGet=='11':monthGet='Nov'
    if monthGet=='12':monthGet='Dec'
    
    recordDocStr="Select client_id, name FROM sm_client where client_id NOT IN ( Select client_id from sm_client_visit_report where tr ='"+str(se_market_report)+"' and y_month='"+str(year_month)+"') and area_id='"+str(se_market_report)+"'"
    # return recordDocStr
    recordDoc=db.executesql(recordDocStr,as_dict = True)
    
    return dict(records=records,yearGet=yearGet,monthGet=monthGet,tr_SC2=tr_SC2,rsm=rsm,fm=fm,tr=tr,docTr=docTr,recordDoc=recordDoc)
    
#---------------------------- Reports
def dcrRsm():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='RSM Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.item_name,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrRsmD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='RSM Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
    
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.item_name,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.item_id)
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

        
    myString+='RSM  ,  ItemID   , ItemName  ,  A/B/C  ,  Sample Used (Qty)\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doc_visit_sample.level1_id])+','+str(record[db.sm_doc_visit_sample.item_id])+','+str(record[db.sm_doc_visit_sample.item_name])+','+str(record[db.sm_doc_visit_sample.item_cat])+','+str(record[(db.sm_doc_visit_sample.qty).sum()])+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=RSM_Summary.csv'   
    return str(myString)

def dcrFm():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Fm Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)   
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.item_name,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)
def dcrFmD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Fm Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)   
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.item_name,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.item_id)
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

        
    myString+='RSM  ,  FM  ,  ItemID   , ItemName  ,  A/B/C  ,  Sample Used (Qty)\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doc_visit_sample.level1_id])+','+str(record[db.sm_doc_visit_sample.level2_id])+','+str(record[db.sm_doc_visit_sample.item_id])+','+str(record[db.sm_doc_visit_sample.item_name])+','+str(record[db.sm_doc_visit_sample.item_cat])+','+str(record[(db.sm_doc_visit_sample.qty).sum()])+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=Fm_Summary.csv'   
    return str(myString) 
    
    
    
    
def dcrTeritory():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='TR Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)
    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrTeritoryD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='TR Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.item_id)
#     return records
    #REmove , from record.Cause , means new column in excel    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

        
    myString+='RSM  ,  FM  ,  TR   , TR Desc ,     ItemID   , ItemName  ,  A/B/C  ,  Sample Used (Qty)\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doc_visit_sample.level1_id])+','+str(record[db.sm_doc_visit_sample.level2_id])+','+str(record[db.sm_doc_visit_sample.route_id])+','+str(record[db.sm_doc_visit_sample.trDesc])+','+str(record[db.sm_doc_visit_sample.item_id])+','+str(record[db.sm_doc_visit_sample.item_name])+','+str(record[db.sm_doc_visit_sample.item_cat])+','+str(record[(db.sm_doc_visit_sample.qty).sum()])+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=TR_Summary.csv'   
    return str(myString) 


def dcrMso():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='MSO Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.rep_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.rep_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrMsoD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='MSO Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.rep_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.rep_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
        #REmove , from record.Cause , means new column in excel    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'

        
    myString+='RSM  ,  FM  ,  TR   , TR Desc ,   MSOID,MSOName , ItemID   , ItemName  ,  A/B/C  ,  Sample Used (Qty)\n'
    
    
    for record in records:
        myString+=str(record[db.sm_doc_visit_sample.level1_id])+','+str(record[db.sm_doc_visit_sample.level2_id])+','+str(record[db.sm_doc_visit_sample.route_id])+','+str(record[db.sm_doc_visit_sample.trDesc])+','+str(record[db.sm_doc_visit_sample.rep_id])+','+str(record[db.sm_doc_visit_sample.rep_name])+','+str(record[db.sm_doc_visit_sample.item_id])+','+str(record[db.sm_doc_visit_sample.item_name])+','+str(record[db.sm_doc_visit_sample.item_cat])+','+str(record[(db.sm_doc_visit_sample.qty).sum()])+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=MSO_Summary.csv'   
    return str(myString) 


def dcrDoc():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Doc Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.doc_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.doc_id|db.sm_doc_visit_sample.item_id)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrDocD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Doc Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    
    if (mso_id!=''):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL,(db.sm_doc_visit_sample.qty).sum(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.doc_id|db.sm_doc_visit_sample.item_name ,groupby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.doc_id|db.sm_doc_visit_sample.item_id)
    return records
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='RSM  ,  FM  ,  TR   , TR Desc ,   DocID,DocName , ItemID   , ItemName  ,  A/B/C  ,  Sample Used (Qty)\n'
        
        
    for record in records:
        myString+=str(record[db.sm_doc_visit_sample.level1_id])+','+str(record[db.sm_doc_visit_sample.level2_id])+','+str(record[db.sm_doc_visit_sample.route_id])+','+str(record[db.sm_doc_visit_sample.trDesc])+','+str(record[db.sm_doc_visit_sample.doc_id])+','+str(record[db.sm_doc_visit_sample.doc_name])+','+str(record[db.sm_doc_visit_sample.item_id])+','+str(record[db.sm_doc_visit_sample.item_name])+','+str(record[db.sm_doc_visit_sample.item_cat])+','+str(record[(db.sm_doc_visit_sample.qty).sum()])+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=Doc_Summary.csv'   
    return str(myString) 

def dcrVisit():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='NationalSummary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    # return fm_id
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    
    
    
   
    records = qset.select(db.sm_doc_visit_sample.ALL, orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.visit_sl|db.sm_doc_visit_sample.item_name)
#     return db._lastsql
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,doc=doc,doc_name=doc_name)
    
 #Jolly 
def dcrSummaryZm():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))


    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='Region Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()        
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

   
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 0)
    qset = qset(db.sm_doctor_visit.level0_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)
    
    
    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)
        qset = qset(db.sm_supervisor_level.level_id == zm_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id) 
    # return records
    
    return dict(records=records,date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrSummaryD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   
    c_id = session.cid
    response.title='Region Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
   
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()    
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 0)
    qset = qset(db.sm_doctor_visit.level0_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)
    
    
    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)
        qset = qset(db.sm_supervisor_level.level_id == zm_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_doctor_visit.id,db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id) 
   
   
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Region,'+zm_id+'|'+zm_name+'\n'    
    # myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    # myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Region,Submitted By ID,Submitted By Name,DCR Count\n'
    total=0
    for record in records:        
        myString+=str(record[db.sm_doctor_visit.level0_id])+','+str(record[db.sm_doctor_visit.rep_id])+','+str(record[db.sm_doctor_visit.rep_name])+','+str(record[db.sm_doctor_visit.id.count()])+'\n'
        total=total+int(record[db.sm_doctor_visit.id.count()])
    myString = myString+','+','+'Total :'+','+str(total) + '\n' 
             
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=ZM_DCR_Summary.csv'   
    return str(myString)



def dcrSummaryRSM():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title=' Zone Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to

    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()    
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 1)
    qset = qset(db.sm_doctor_visit.level1_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)


    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
        qset = qset(db.sm_supervisor_level.level_id == rsm_id)
   
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)
    
    
    return dict(records=records,date_from=date_from,date_to=date_to,rsm_id=rsm_id,rsm_name=rsm_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrSummaryRSM_D():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title=' Zone Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to

    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()    
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 1)
    qset = qset(db.sm_doctor_visit.level1_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)


    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
        qset = qset(db.sm_supervisor_level.level_id == rsm_id)
   
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)

   
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Zone,'+rsm_id+'|'+rsm_name+'\n'
    # myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Zone ,Submitted By ID,Submitted By Name , DCR Count\n'
        
    total=0
    for record in records:
        myString+=str(record[db.sm_doctor_visit.level1_id])+','+str(record[db.sm_doctor_visit.rep_id])+','+str(record[db.sm_doctor_visit.rep_name])+','+str(record[db.sm_doctor_visit.id.count()])+'\n'
        total=total+int(record[db.sm_doctor_visit.id.count()])
    myString = myString+','+','+'Total :'+','+str(total) + '\n' 
                  
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=RSM_WiseDCR_Summary.csv'   
    return str(myString)


def dcrSummaryAM():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title=' AM Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to    
    fmA_id=str(request.vars.fmA_id).strip()
    # return fmA_id
    # fm_name=str(request.vars.fm_name).strip()    
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 2)
    qset = qset(db.sm_doctor_visit.level2_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)    
   
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fmA_id)
        qset = qset(db.sm_supervisor_level.level_id == fmA_id)
   
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level2_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)

    
    return dict(records=records,date_from=date_from,date_to=date_to,fmA_id=fmA_id,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrSummaryAM_D():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title=' AM Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to    
    fmA_id=str(request.vars.fmA_id).strip()
    # return fmA_id
    # fm_name=str(request.vars.fm_name).strip()    
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == 2)
    qset = qset(db.sm_doctor_visit.level2_id == db.sm_supervisor_level.level_id)
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_supervisor_level.sup_id)    
   
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fmA_id)
        qset = qset(db.sm_supervisor_level.level_id == fmA_id)
   
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)

    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level2_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)
   
    
    myString='DateRange,'+date_from+','+date_to+'\n'    
    myString+='FM,'+fmA_id+'\n'   
    # myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Region,Zone,AM,Submitted By ID,Submitted By Name, DCR Count\n'
        
    total=0
    for record in records:        
        myString+=str(record[db.sm_doctor_visit.level0_id])+','+str(record[db.sm_doctor_visit.level1_id])+','+str(record[db.sm_doctor_visit.level2_id])+','+str(record[db.sm_doctor_visit.rep_id])+','+str(record[db.sm_doctor_visit.rep_name])+','+str(record[db.sm_doctor_visit.id.count()])+'\n'
        total=total+int(record[db.sm_doctor_visit.id.count()])
    myString = myString+','+',,,'+'Total :'+','+str(total) + '\n' 
    

    sql_str="""SELECT l.`level0`,l.`level0_name`, l.`level1`, l.`level1_name`,l.`level2`,l.`level2_name`,l.`level3`,l.`level3_name`, a.sup_id, a.sup_name
FROM sm_supervisor_level a, sm_level l 
WHERE l.cid = 'IBNSINA' AND a.cid='IBNSINA' AND   l.cid=a.cid  AND l.`level_id` = a.level_id  AND a.`level_depth_no`=2
AND a.sup_id 

NOT IN (

SELECT  `sm_doctor_visit`.`rep_id` FROM `sm_doctor_visit` 
WHERE (((`sm_doctor_visit`.`cid` = 'IBNSINA') AND (`sm_doctor_visit`.`visit_date` >= '"""+str(date_from)+"""')) 
AND (`sm_doctor_visit`.`visit_date` <= '"""+str(date_to)+"""')) 
GROUP BY `sm_doctor_visit`.`rep_id` 

);"""
    # return sql_str
    recordList_n = db.executesql(sql_str, as_dict=True)


    for i in range(len(recordList_n)):
        recordListStr = recordList_n[i]
        level0=str(recordListStr['level0'])
        level0_name=str(recordListStr['level0_name'])
        level1=str(recordListStr['level1'])
        level1_name=str(recordListStr['level1_name'])
        level2=str(recordListStr['level2'])
        level2_name=str(recordListStr['level2_name'])
        level3=str(recordListStr['level3'])
        level3_name=str(recordListStr['level3_name'])
        rep_id=str(recordListStr['sup_id'])
        rep_name    =str(recordListStr['sup_name'])

        myString+=str(level0)+','+str(level1)+','+str(level2)+','+str(rep_id)+','+str(rep_name)+',0\n'
        

    
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=AM_WiseDCR_Summary.csv'   
    return str(myString)

def dcrSummaryMPO():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='MPO Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    # qset = qset(db.sm_rep_area.cid == c_id)
    # qset = qset(db.sm_supervisor_level.level_depth_no == 3)
    # qset = qset(db.sm_doctor_visit.level3_id == db.sm_rep_area.area_id)
    # qset = qset(db.sm_doctor_visit.rep_id == db.sm_rep_area.rep_id) 

    
    if (mso_id!=''):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
        # qset = qset(db.sm_rep_area.rep_id == mso_id)
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.route_id == tr_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)
    # return db._lastsql
    return dict(records=records,date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,tr_id=tr_id,tr_name=tr_name,doc=doc,doc_name=doc_name)


def dcrSummaryMPO_D():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))
   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='MPO Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()

    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    # qset = qset(db.sm_rep_area.cid == c_id)
    # qset = qset(db.sm_supervisor_level.level_depth_no == 3)
    # qset = qset(db.sm_doctor_visit.level3_id == db.sm_rep_area.area_id)
    # qset = qset(db.sm_doctor_visit.rep_id != db.sm_rep_area.rep_id) 

    
    if (mso_id!=''):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
        # qset = qset(db.sm_rep_area.rep_id == mso_id)
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.route_id == tr_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)
   
    sql_str="""SELECT l.`level0`,l.`level0_name`, l.`level1`, l.`level1_name`,l.`level2`,l.`level2_name`,l.`level3`,l.`level3_name`, a.rep_id, a.rep_name
FROM sm_rep_area a, sm_level l 
WHERE l.cid = 'IBNSINA' AND a.cid='IBNSINA' AND  l.`is_leaf`=1 AND l.cid=a.cid  AND l.`level_id` = a.area_id  
AND a.rep_id 

NOT IN (

SELECT  `sm_doctor_visit`.`rep_id` FROM `sm_doctor_visit` 
WHERE (((`sm_doctor_visit`.`cid` = 'IBNSINA') AND (`sm_doctor_visit`.`visit_date` >= '"""+str(date_from)+"""')) 
AND (`sm_doctor_visit`.`visit_date` <= '"""+str(date_to)+"""')) 
GROUP BY `sm_doctor_visit`.`rep_id` 

);"""
    
    recordList_n = db.executesql(sql_str, as_dict=True)




    myString='DateRange,'+date_from+','+date_to+'\n'    
    myString+='MPO,'+mso_id+'|'+mso_name+'\n'    
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Region,Zone,AM,route,Submitted By ID,Submitted By Name, DCR Count\n'
        
    total=0
    for record in records:
        rep_search=str(record[db.sm_doctor_visit.rep_id])
        # repStr=repStr.replace(','+rep_search,'')
        myString+=str(record[db.sm_doctor_visit.level0_id])+','+str(record[db.sm_doctor_visit.level1_id])+','+str(record[db.sm_doctor_visit.level2_id])+','+str(record[db.sm_doctor_visit.route_id])+','+str(record[db.sm_doctor_visit.rep_id])+','+str(record[db.sm_doctor_visit.rep_name])+','+str(record[db.sm_doctor_visit.id.count()])+'\n'
        total=total+int(record[db.sm_doctor_visit.id.count()])
    myString = myString+',,,,,'+'Total :'+','+str(total) + '\n' 
    

    for i in range(len(recordList_n)):
        recordListStr = recordList_n[i]
        level0=str(recordListStr['level0'])
        level0_name=str(recordListStr['level0_name'])
        level1=str(recordListStr['level1'])
        level1_name=str(recordListStr['level1_name'])
        level2=str(recordListStr['level2'])
        level2_name=str(recordListStr['level2_name'])
        level3=str(recordListStr['level3'])
        level3_name=str(recordListStr['level3_name'])
        rep_id=str(recordListStr['rep_id'])
        rep_name    =str(recordListStr['rep_name'])

        myString+=str(level0)+','+str(level1)+','+str(level2)+','+str(level3)+','+str(rep_id)+','+str(rep_name)+',0\n'
        

    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=MPO_WiseDCR_Summary.csv'   
    return str(myString)


def sin_zm_ranking():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))


    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='Zone Wise Ranking'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()        
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
   
    # select sin rep
    # make list from rep area or supervisor level
    # select data from doctor_visit

    
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)


    qset = qset(db.sm_rep.cid == c_id)
    qset = qset(db.sm_rep.user_type == 'sup')
    qset = qset(db.sm_rep.note == 'SIN')


    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == '0')
    qset = qset(db.sm_doctor_visit.level0_id == db.sm_supervisor_level.level_id)



    
    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)
        qset = qset(db.sm_supervisor_level.level_id == zm_id)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id)
    # return records
    
    return dict (records=records,date_from=date_from,date_to=date_to,zm_id=zm_id,zm_name=zm_name,doc=doc,doc_name=doc_name)



def sin_rsm_ranking():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))


    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='Region Wise Ranking'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    rsm_id=str(request.vars.rsm_id).strip()
    # return rsm_id
    rsm_name=str(request.vars.rsm_name).strip()        
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
   
    # select sin rep
    # make list from rep area or supervisor level
    # select data from doctor_visit

    
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)


    qset = qset(db.sm_rep.cid == c_id)
    qset = qset(db.sm_rep.user_type == 'sup')
    qset = qset(db.sm_rep.note == 'SIN')


    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == '1')
    qset = qset(db.sm_doctor_visit.level1_id == db.sm_supervisor_level.level_id)



    
    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
        qset = qset(db.sm_supervisor_level.level_id == rsm_id)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id)
    # return records
    
    return dict (records=records,date_from=date_from,date_to=date_to,rsm_id=rsm_id,rsm_name=rsm_name,doc=doc,doc_name=doc_name)



def sin_fm_ranking():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))


    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='Area Wise Ranking'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    fm_id=str(request.vars.fm_id).strip()
    # return rsm_id
    fm_name=str(request.vars.fm_name).strip()        
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
   
    # select sin rep
    # make list from rep area or supervisor level
    # select data from doctor_visit

    
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)


    qset = qset(db.sm_rep.cid == c_id)
    qset = qset(db.sm_rep.user_type == 'sup')
    qset = qset(db.sm_rep.note == 'SIN')


    qset = qset(db.sm_supervisor_level.cid == c_id)
    qset = qset(db.sm_supervisor_level.level_depth_no == '2')
    qset = qset(db.sm_doctor_visit.level2_id == db.sm_supervisor_level.level_id)



    
    if (fm_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fm_id)
        qset = qset(db.sm_supervisor_level.level_id == fm_id)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id)
    # return records
    
    return dict (records=records,date_from=date_from,date_to=date_to,fm_id=fm_id,fm_name=fm_name,doc=doc,doc_name=doc_name)


def sin_mpo_ranking():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))


    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='MPO Wise Ranking'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
          
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
   
    # select sin rep
    # make list from rep area or supervisor level
    # select data from doctor_visit

    
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)


    qset = qset(db.sm_rep.cid == c_id)
    qset = qset(db.sm_rep.user_type == 'rep')
    qset = qset(db.sm_rep.note == 'SIN')


    qset = qset(db.sm_rep_area.cid == c_id)
    # qset = qset(db.sm_supervisor_level.level_depth_no == '2')
    qset = qset(db.sm_doctor_visit.rep_id == db.sm_rep_area.rep_id)



    
    if (mso_id!=''):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
        # qset = qset(db.sm_supervisor_level.level_id == mso_id)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)


    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(),db.sm_supervisor_level.level_depth_no, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id)
    # return records
    
    return dict (records=records,date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)


#Faisal
def dcrSummaryDateWiseVisitCount():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='DCR Summary Date wise '    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 

   
#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date < date_to_m)
    qset = qset(db.sm_level.cid == c_id)
    qset = qset(db.sm_doctor_visit.route_id == db.sm_level.level_id)
    qset = qset(db.sm_level.is_leaf == 1)

    
    if (depot_id!=''):
        qset = qset(db.sm_doctor_visit.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.route_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
   
    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_level.territory_des,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.visit_date,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.visit_date,groupby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.visit_date)

    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrCountVisitCountFmAreaWiseD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect(URL(c='default', f='home'))

    c_id = session.cid
    response.title = 'DCR Summary FM D'
    date_from = request.vars.date_from
    date_to = request.vars.date_to
    depot_id = str(request.vars.depot_id).strip()
    depot_name = str(request.vars.depot_name).strip()

    rsm_id = str(request.vars.rsm_id).strip()
    rsm_name = str(request.vars.rsm_name).strip()
    fm_id = str(request.vars.fm_id).strip()
    fm_name = str(request.vars.fm_name).strip()
    tr_id = str(request.vars.tr_id).strip()
    tr_name = str(request.vars.tr_name).strip()
    product_id = str(request.vars.product_id).strip()
    product_name = str(request.vars.product_name).strip()
    brand = str(request.vars.brand).strip()
    category = str(request.vars.category).strip()
    mso_id = str(request.vars.mso_id).strip()
    mso_name = str(request.vars.mso_name).strip()
    doc = str(request.vars.doc).strip()
    doc_name = str(request.vars.doc_name).strip()
    #     return mso_id

    condition = ''
    if (depot_id != ''):
        condition = condition + "AND a.depot_id = '" + str(depot_id) + "'"
    if (rsm_id != ''):
        condition = condition + "AND a.level1_id = '" + str(rsm_id) + "'"
    if (fm_id != ''):
        condition = condition + "AND a.level2_id = '" + str(fm_id) + "'"
    # if (tr_id != ''):
    #     condition = condition + "AND a.route_id = '" + str(tr_id) + "'"
    if (doc != ''):
        condition = condition + "AND a.doc_id = '" + str(doc) + "'"
    if (mso_id != ''):
        condition = condition + "AND a.rep_id = '" + str(mso_id) + "'"

    dateRecords = "SELECT a.level0_id as level0_id,a.level1_id as level1_id,a.level2_id as level2_id,a.rep_id as rep_id,a.rep_name as rep_name,count(distinct(a.visit_date)) as visit_date_count,count(a.id) as visit_count FROM sm_doctor_visit a,sm_supervisor_level b WHERE a.cid = '" + c_id + "' AND a.visit_date >= '" + date_from + "' AND  a.visit_date <= '" + date_to + "' AND a.cid=b.cid AND b.level_depth_no=2 AND a.rep_id=b.sup_id " + condition + " GROUP BY a.level1_id,a.level2_id,a.rep_id ORDER BY a.level1_id,a.level2_id,a.rep_id;"
    recordList = db.executesql(dateRecords, as_dict=True)

    myString = 'DateRange,' + date_from + ',' + date_to + '\n'
    myString += 'Depot/Branch,' + depot_id + '|' + depot_name + '\n'
    myString += 'RSM,' + rsm_id + '|' + rsm_name + '\n'
    myString += 'FM,' + fm_id + '|' + fm_name + '\n'
    myString += 'RT,' + tr_id + '|' + tr_name + '\n'
    myString += 'MSO,' + mso_id + '|' + mso_name + '\n'
    #     myString+='Product,'+product_id+'|'+product_name+'\n'
    #     myString+='Category,'+category+'\n'
    myString += 'Doctor,' + doc + '|' + doc_name + '\n\n'
    myString += 'RSM,Zone,FM,FM ID,FM Name,DCR Count,Visit Count \n'

    for i in range(len(recordList)):
        recordListStr = recordList[i]
        level0_id=str(recordListStr['level0_id'])
        level1_id=str(recordListStr['level1_id'])
        level2_id =str(recordListStr['level2_id'])
        rep_id = str(recordListStr['rep_id'])
        rep_name = str(recordListStr['rep_name'])
        visit_date_count = str(recordListStr['visit_date_count'])
        visit_count = str(recordListStr['visit_count'])

        myString += level0_id + ',' +level1_id + ',' + level2_id + ',' + rep_id + ',' + rep_name + ',' + visit_date_count + ',' + visit_count + '\n'

    # Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=DCR_Summary_FM.csv'
    return str(myString)
    #return dict(recordList=recordList, date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id, tr_name=tr_name,brand=brand, category=category, product_id=product_id, product_name=product_name, mso_id=mso_id,mso_name=mso_name, doc=doc, doc_name=doc_name)


def dcrCountVisitCountFmAreaWise():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect(URL(c='default', f='home'))

    c_id = session.cid
    response.title = 'DCR Summary FM'
    date_from = request.vars.date_from
    date_to = request.vars.date_to
    depot_id = str(request.vars.depot_id).strip()
    depot_name = str(request.vars.depot_name).strip()

    rsm_id = str(request.vars.rsm_id).strip()
    rsm_name = str(request.vars.rsm_name).strip()
    fm_id = str(request.vars.fm_id).strip()
    fm_name = str(request.vars.fm_name).strip()
    tr_id = str(request.vars.tr_id).strip()
    tr_name = str(request.vars.tr_name).strip()
    product_id = str(request.vars.product_id).strip()
    product_name = str(request.vars.product_name).strip()
    brand = str(request.vars.brand).strip()
    category = str(request.vars.category).strip()
    mso_id = str(request.vars.mso_id).strip()
    mso_name = str(request.vars.mso_name).strip()
    doc = str(request.vars.doc).strip()
    doc_name = str(request.vars.doc_name).strip()
    #     return mso_id

    condition = ''
    if (depot_id != ''):
        condition = condition + "AND a.depot_id = '" + str(depot_id) + "'"
    if (rsm_id != ''):
        condition = condition + "AND a.level1_id = '" + str(rsm_id) + "'"
    if (fm_id != ''):
        condition = condition + "AND a.level2_id = '" + str(fm_id) + "'"
    # if (tr_id != ''):
    #     condition = condition + "AND a.route_id = '" + str(tr_id) + "'"
    if (doc != ''):
        condition = condition + "AND a.doc_id = '" + str(doc) + "'"
    if (mso_id != ''):
        condition = condition + "AND a.rep_id = '" + str(mso_id) + "'"

    dateRecords = "SELECT a.level0_id as level0_id,a.level1_id as level1_id,a.level2_id as level2_id,a.rep_id as rep_id,a.rep_name as rep_name,count(distinct(a.visit_date)) as visit_date_count,count(a.id) as visit_count FROM sm_doctor_visit a,sm_supervisor_level b WHERE a.cid = '" + c_id + "' AND a.visit_date >= '" + date_from + "' AND  a.visit_date <= '" + date_to + "' AND a.cid=b.cid AND b.level_depth_no=2 AND a.rep_id=b.sup_id " + condition + " GROUP BY a.level1_id,a.level2_id,a.rep_id ORDER BY a.level1_id,a.level2_id,a.rep_id;"
    recordList = db.executesql(dateRecords, as_dict=True)

    return dict(recordList=recordList, date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id, tr_name=tr_name,brand=brand, category=category, product_id=product_id, product_name=product_name, mso_id=mso_id,mso_name=mso_name, doc=doc, doc_name=doc_name)



def dcrCountVisitCountFm():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect(URL(c='default', f='home'))

    c_id = session.cid
    response.title = 'DCR Summary FM'
    date_from = request.vars.date_from
    date_to = request.vars.date_to
    depot_id = str(request.vars.depot_id).strip()
    depot_name = str(request.vars.depot_name).strip()

    rsm_id = str(request.vars.rsm_id).strip()
    rsm_name = str(request.vars.rsm_name).strip()
    fm_id = str(request.vars.fm_id).strip()
    fm_name = str(request.vars.fm_name).strip()
    tr_id = str(request.vars.tr_id).strip()
    tr_name = str(request.vars.tr_name).strip()
    product_id = str(request.vars.product_id).strip()
    product_name = str(request.vars.product_name).strip()
    brand = str(request.vars.brand).strip()
    category = str(request.vars.category).strip()
    mso_id = str(request.vars.mso_id).strip()
    mso_name = str(request.vars.mso_name).strip()
    doc = str(request.vars.doc).strip()
    doc_name = str(request.vars.doc_name).strip()
    #     return mso_id

    condition = ''
    if (depot_id != ''):
        condition = condition + "AND a.depot_id = '" + str(depot_id) + "'"
    if (rsm_id != ''):
        condition = condition + "AND a.level1_id = '" + str(rsm_id) + "'"
    if (fm_id != ''):
        condition = condition + "AND a.level2_id = '" + str(fm_id) + "'"
    if (tr_id != ''):
        condition = condition + "AND a.route_id = '" + str(tr_id) + "'"
    if (doc != ''):
        condition = condition + "AND a.doc_id = '" + str(doc) + "'"
    if (mso_id != ''):
        condition = condition + "AND a.rep_id = '" + str(mso_id) + "'"

    dateRecords = "SELECT a.level0_id as level0_id,a.level1_id as level1_id,a.level2_id as level2_id,a.route_id as route_id,a.rep_id as rep_id,a.rep_name as rep_name,count(distinct(a.visit_date)) as visit_date_count,count(a.id) as visit_count FROM sm_doctor_visit a,sm_supervisor_level b WHERE a.cid = '" + c_id + "' AND a.visit_date >= '" + date_from + "' AND  a.visit_date <= '" + date_to + "' AND a.cid=b.cid AND b.level_depth_no=2 AND a.rep_id=b.sup_id " + condition + " GROUP BY a.level1_id,a.level2_id,a.route_id,a.rep_id ORDER BY a.level1_id,a.level2_id,a.route_id,a.rep_id;"
    recordList = db.executesql(dateRecords, as_dict=True)

    return dict(recordList=recordList, date_from=date_from, date_to=date_to, depot_id=depot_id, depot_name=depot_name,rsm_id=rsm_id, rsm_name=rsm_name, fm_id=fm_id, fm_name=fm_name, tr_id=tr_id, tr_name=tr_name,brand=brand, category=category, product_id=product_id, product_name=product_name, mso_id=mso_id,mso_name=mso_name, doc=doc, doc_name=doc_name)

def dcr_count_visit_count_fm_d():
    # return 'Nadira'
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect(URL(c='default', f='home'))

    c_id = session.cid
    response.title = 'DCR Summary FM'
    date_from = request.vars.date_from
    date_to = request.vars.date_to
    depot_id = str(request.vars.depot_id).strip()
    depot_name = str(request.vars.depot_name).strip()

    rsm_id = str(request.vars.rsm_id).strip()
    rsm_name = str(request.vars.rsm_name).strip()
    fm_id = str(request.vars.fm_id).strip()
    fm_name = str(request.vars.fm_name).strip()
    tr_id = str(request.vars.tr_id).strip()
    tr_name = str(request.vars.tr_name).strip()
    product_id = str(request.vars.product_id).strip()
    product_name = str(request.vars.product_name).strip()
    brand = str(request.vars.brand).strip()
    category = str(request.vars.category).strip()
    mso_id = str(request.vars.mso_id).strip()
    mso_name = str(request.vars.mso_name).strip()
    doc = str(request.vars.doc).strip()
    doc_name = str(request.vars.doc_name).strip()
    #     return mso_id

    condition = ''
    if (depot_id != ''):
        condition = condition + "AND a.depot_id = '" + str(depot_id) + "'"
    if (rsm_id != ''):
        condition = condition + "AND a.level1_id = '" + str(rsm_id) + "'"
    if (fm_id != ''):
        condition = condition + "AND a.level2_id = '" + str(fm_id) + "'"
    if (tr_id != ''):
        condition = condition + "AND a.route_id = '" + str(tr_id) + "'"
    if (doc != ''):
        condition = condition + "AND a.doc_id = '" + str(doc) + "'"
    if (mso_id != ''):
        condition = condition + "AND a.rep_id = '" + str(mso_id) + "'"

    dateRecords = "SELECT a.level0_id as level0_id,a.level1_id as level1_id,a.level2_id as level2_id,a.route_id as route_id,a.rep_id as rep_id,a.rep_name as rep_name,count(distinct(a.visit_date)) as visit_date_count,count(a.id) as visit_count FROM sm_doctor_visit a,sm_supervisor_level b WHERE a.cid = '" + c_id + "' AND a.visit_date >= '" + date_from + "' AND  a.visit_date <= '" + date_to + "' AND a.cid=b.cid AND b.level_depth_no=2 AND a.rep_id=b.sup_id " + condition + " GROUP BY a.level1_id,a.level2_id,a.route_id,a.rep_id ORDER BY a.level1_id,a.level2_id,a.route_id,a.rep_id;"
    recordList = db.executesql(dateRecords, as_dict=True)

    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Region  ,  Zone  ,  AM  ,  TR  ,  AM ID , AM Name  ,   DCR Count  , Visit Count\n'
    ShowSum1=0
    ShowSum=0
    for i in range(len(recordList)):
        recordListStr=recordList[i]
        level0_id=recordListStr['level0_id']
        level1_id=recordListStr['level1_id']
        level2_id=recordListStr['level2_id']
        route_id=recordListStr['route_id']
       
        rep_id=recordListStr['rep_id']
        rep_name=recordListStr['rep_name']
        visit_date=recordListStr['visit_date_count']
        ShowSum1=ShowSum1+int(recordListStr['visit_date_count'])
        show_id=recordListStr['visit_count']
        ShowSum=ShowSum+int(recordListStr['visit_count'])

        myString+=str(level0_id)+','+str(level1_id)+','+str(level2_id)+','+str(route_id)+','+str(rep_id)+','+str(rep_name)+','+str(visit_date)+','+str(show_id)+'\n'
    myString+=',,,,,Total,'+str(ShowSum1)+','+str(ShowSum)+'\n'
    


    sql_str="""SELECT l.`level0`,l.`level0_name`, l.`level1`, l.`level1_name`,l.`level2`,l.`level2_name`,l.`level3`,l.`level3_name`, a.sup_id, a.sup_name
FROM sm_supervisor_level a, sm_level l 
WHERE l.cid = 'IBNSINA' AND a.cid='IBNSINA' AND   l.cid=a.cid  AND l.`level_id` = a.level_id  AND a.`level_depth_no`=2
AND a.sup_id 

NOT IN (

SELECT  `sm_doctor_visit`.`rep_id` FROM `sm_doctor_visit` 
WHERE (((`sm_doctor_visit`.`cid` = 'IBNSINA') AND (`sm_doctor_visit`.`visit_date` >= '"""+str(date_from)+"""')) 
AND (`sm_doctor_visit`.`visit_date` <= '"""+str(date_to)+"""')) 
GROUP BY `sm_doctor_visit`.`rep_id` 

);"""
    # return sql_str
    recordList_n = db.executesql(sql_str, as_dict=True)
    
    for i in range(len(recordList_n)):
        recordListStr = recordList_n[i]
        level0=str(recordListStr['level0'])
        level0_name=str(recordListStr['level0_name'])
        level1=str(recordListStr['level1'])
        level1_name=str(recordListStr['level1_name'])
        level2=str(recordListStr['level2'])
        level2_name=str(recordListStr['level2_name'])
        level3=str(recordListStr['level3'])
        level3_name=str(recordListStr['level3_name'])
        rep_id=str(recordListStr['sup_id'])
        rep_name    =str(recordListStr['sup_name'])

        myString+=str(level0)+','+str(level1)+','+str(level2)+','+str(level3)+','+str(rep_id)+','+str(rep_name)+',0,0\n'



    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('DCR_Summary_AM.csv')
    response.headers['Content-disposition'] = 'attachment; filename=DCR_Summary_AM.csv'   
    return str(myString)
   

def dcrCountVisitCount():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='DCR Summary MPO'
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m = datetime.datetime.strptime(str(date_to), '%Y-%m-%d')
    date_to_m = str(date_to_m + datetime.timedelta(days=1))

    condition=''
    if (depot_id!=''):
        condition=condition+"AND depot_id = '"+str(depot_id)+"'"
    if (rsm_id!=''):
        condition=condition+"AND level1_id = '"+str(rsm_id)+"'"
    if (fm_id!=''):
        condition=condition+"AND level2_id = '"+str(fm_id)+"'"
    if (tr_id!=''):
        condition=condition+"AND route_id = '"+str(tr_id)+"'"
    if (doc!=''):            
        condition=condition+"AND doc_id = '"+str(doc)+"'"
    if (mso_id!=''):            
        condition=condition+"AND rep_id = '"+str(mso_id)+"'"
            
    
    dateRecords="SELECT sm_doctor_visit.level0_id as level0_id,sm_doctor_visit.level1_id as level1_id,sm_doctor_visit.level2_id as level2_id,sm_doctor_visit.route_id as route_id,sm_doctor_visit.level3_name as territory_des,sm_doctor_visit.rep_id as rep_id,sm_doctor_visit.rep_name as rep_name,count(distinct(sm_doctor_visit.visit_date)) as visit_date,count(sm_doctor_visit.id) as id FROM sm_doctor_visit WHERE ((sm_doctor_visit.cid = '"+c_id+"') AND (sm_doctor_visit.visit_date >= '"+date_from+"') AND  (sm_doctor_visit.visit_date < '"+date_to_m+"')  "+condition+") GROUP BY sm_doctor_visit.level1_id,sm_doctor_visit.level2_id,sm_doctor_visit.route_id,sm_doctor_visit.rep_id,sm_doctor_visit.rep_name ORDER BY sm_doctor_visit.level1_id,sm_doctor_visit.level2_id,sm_doctor_visit.route_id,sm_doctor_visit.rep_id,sm_doctor_visit.rep_name;"

    recordList=db.executesql(dateRecords,as_dict = True)     
    # return dateRecords

    return dict(recordList=recordList,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)

def dcrCountVisitCount_d():

    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='DCR Summary MPO'
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m = datetime.datetime.strptime(str(date_to), '%Y-%m-%d')
    date_to_m = str(date_to_m + datetime.timedelta(days=1))

    condition=''
    if (depot_id!=''):
        condition=condition+"AND depot_id = '"+str(depot_id)+"'"
    if (rsm_id!=''):
        condition=condition+"AND level1_id = '"+str(rsm_id)+"'"
    if (fm_id!=''):
        condition=condition+"AND level2_id = '"+str(fm_id)+"'"
    if (tr_id!=''):
        condition=condition+"AND route_id = '"+str(tr_id)+"'"
    if (doc!=''):            
        condition=condition+"AND doc_id = '"+str(doc)+"'"
    if (mso_id!=''):            
        condition=condition+"AND rep_id = '"+str(mso_id)+"'"
            
    
    dateRecords="SELECT sm_doctor_visit.level0_id as level0_id,sm_doctor_visit.level1_id as level1_id,sm_doctor_visit.level2_id as level2_id,sm_doctor_visit.route_id as route_id,sm_doctor_visit.level3_name as territory_des,sm_doctor_visit.rep_id as rep_id,sm_doctor_visit.rep_name as rep_name,count(distinct(sm_doctor_visit.visit_date)) as visit_date,count(sm_doctor_visit.id) as id FROM sm_doctor_visit WHERE ((sm_doctor_visit.cid = '"+c_id+"') AND (sm_doctor_visit.visit_date >= '"+date_from+"') AND  (sm_doctor_visit.visit_date < '"+date_to_m+"')  "+condition+") GROUP BY sm_doctor_visit.level1_id,sm_doctor_visit.level2_id,sm_doctor_visit.route_id,sm_doctor_visit.rep_id,sm_doctor_visit.rep_name ORDER BY sm_doctor_visit.level1_id,sm_doctor_visit.level2_id,sm_doctor_visit.route_id,sm_doctor_visit.rep_id,sm_doctor_visit.rep_name;"

    recordList=db.executesql(dateRecords,as_dict = True)     
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='Region  ,  Zone  ,  AM  ,  TR  ,  TR Desc  ,  MPO,MPO Name,DCR Count,Visit Count\n'
    ShowSum1=0
    ShowSum=0
    for i in range(len(recordList)):
        recordListStr=recordList[i]
        level0_id=recordListStr['level0_id']
        level1_id=recordListStr['level1_id']
        level2_id=recordListStr['level2_id']
        route_id=recordListStr['route_id']
        territory_des=recordListStr['territory_des']
        rep_id=recordListStr['rep_id']
        rep_name=recordListStr['rep_name']
        visit_date=recordListStr['visit_date']
        ShowSum1=ShowSum1+int(recordListStr['visit_date'])
        show_id=recordListStr['id']
        ShowSum=ShowSum+int(recordListStr['id'])

        myString+=str(level0_id)+','+str(level1_id)+','+str(level2_id)+','+str(route_id)+','+str(territory_des)+','+str(rep_id)+','+str(rep_name)+','+str(visit_date)+','+str(show_id)+'\n'
    myString+=',,,,,,Total,'+str(ShowSum1)+','+str(ShowSum)+'\n'  
    

    sql_str="""SELECT l.`level0`,l.`level0_name`, l.`level1`, l.`level1_name`,l.`level2`,l.`level2_name`,l.`level3`,l.`level3_name`, a.rep_id, a.rep_name
FROM sm_rep_area a, sm_level l 
WHERE l.cid = 'IBNSINA' AND a.cid='IBNSINA' AND  l.`is_leaf`=1 AND l.cid=a.cid  AND l.`level_id` = a.area_id  
AND a.rep_id 

NOT IN (

SELECT  `sm_doctor_visit`.`rep_id` FROM `sm_doctor_visit` 
WHERE (((`sm_doctor_visit`.`cid` = 'IBNSINA') AND (`sm_doctor_visit`.`visit_date` >= '"""+str(date_from)+"""')) 
AND (`sm_doctor_visit`.`visit_date` <= '"""+str(date_to)+"""')) 
GROUP BY `sm_doctor_visit`.`rep_id` 

);"""
    
    recordList_n = db.executesql(sql_str, as_dict=True)


    for i in range(len(recordList_n)):
        recordListStr = recordList_n[i]
        level0=str(recordListStr['level0'])
        level0_name=str(recordListStr['level0_name'])
        level1=str(recordListStr['level1'])
        level1_name=str(recordListStr['level1_name'])
        level2=str(recordListStr['level2'])
        level2_name=str(recordListStr['level2_name'])
        level3=str(recordListStr['level3'])
        level3_name=str(recordListStr['level3_name'])
        rep_id=str(recordListStr['rep_id'])
        rep_name    =str(recordListStr['rep_name'])

        myString+=str(level0)+','+str(level1)+','+str(level2)+','+str(level3)+','+str(level3_name)+','+str(rep_id)+','+str(rep_name)+',0,0\n'
        


    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('DCR_Summary.csv')
    response.headers['Content-disposition'] = 'attachment; filename=DCR_Summary.csv'   
    return str(myString)

def dcrVSummary():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='DCR'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(mso_id)<4) and (tr_id=='')):
        session.flash = 'Please select TR or MSO'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date < date_to_m)
    qset = qset(db.sm_level.cid == c_id)
    qset = qset(db.sm_level.level_id == db.sm_doctor_visit.route_id)
#     qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
#     qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)
    
    if (depot_id!=''):
        qset = qset(db.sm_doctor_visit.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.route_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_doctor_visit.item_id == product_id)
#     if (brand!=''):
#         qset = qset(db.sm_doctor_visit.item_brand == brand)
#     if (category!=''):
#         qset = qset(db.sm_doctor_visit.item_cat == category)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
    records = qset.select(db.sm_doctor_visit.id,db.sm_doctor_visit.visit_dtime,db.sm_doctor_visit.depot_id,db.sm_doctor_visit.note,db.sm_doctor_visit.doc_id,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_level.territory_des,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.giftnsample,groupby=db.sm_doctor_visit.depot_id|db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_level.territory_des|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.doc_id|db.sm_doctor_visit.doc_name|db.sm_doctor_visit.note|db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime|db.sm_doctor_visit.giftnsample, orderby= db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime)
    
#     records = qset.select(db.sm_doctor_visit.id,db.sm_doctor_visit.visit_dtime,db.sm_doctor_visit.depot_id,db.sm_doctor_visit.note,db.sm_doctor_visit.doc_id,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doc_visit_sample.trDesc,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.giftnsample,groupby=db.sm_doctor_visit.depot_id|db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doc_visit_sample.trDesc|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.doc_id|db.sm_doctor_visit.doc_name|db.sm_doctor_visit.note|db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime|db.sm_doctor_visit.giftnsample, orderby= db.sm_doctor_visit.depot_id|db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doc_visit_sample.trDesc|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.doc_id|db.sm_doctor_visit.doc_name|db.sm_doctor_visit.note|db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime|db.sm_doctor_visit.giftnsample)
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)


def dcrVSummaryProduct():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Doc Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(product_id)<1) and (product_id=='')):
        session.flash = 'Please select product'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_sample.cid == c_id)
    qset = qset(db.sm_doc_visit_sample.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_sample.visit_date < date_to_m)

    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_sample.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_sample.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_sample.route_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_sample.doc_id == doc)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_sample.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_sample.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_sample.item_cat == category)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doc_visit_sample.rep_id == mso_id)
    
    records = qset.select(db.sm_doc_visit_sample.level1_id,db.sm_doc_visit_sample.level2_id,db.sm_doc_visit_sample.route_id,db.sm_doc_visit_sample.rep_id,db.sm_doc_visit_sample.rep_name,db.sm_doc_visit_sample.level0_id,db.sm_doc_visit_sample.level0_name,db.sm_doc_visit_sample.id.count(), orderby= db.sm_doc_visit_sample.level1_id|db.sm_doc_visit_sample.level2_id|db.sm_doc_visit_sample.route_id|db.sm_doc_visit_sample.rep_id|db.sm_doc_visit_sample.rep_name ,groupby= db.sm_doc_visit_sample.rep_id)
#     return db._lastsql
#     records = qset.select(db.sm_doctor_visit.id,db.sm_doctor_visit.visit_dtime,db.sm_doctor_visit.depot_id,db.sm_doctor_visit.note,db.sm_doctor_visit.doc_id,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doc_visit_sample.trDesc,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.giftnsample,groupby=db.sm_doctor_visit.depot_id|db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doc_visit_sample.trDesc|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.doc_id|db.sm_doctor_visit.doc_name|db.sm_doctor_visit.note|db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime|db.sm_doctor_visit.giftnsample, orderby= db.sm_doctor_visit.depot_id|db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doc_visit_sample.trDesc|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name|db.sm_doctor_visit.doc_id|db.sm_doctor_visit.doc_name|db.sm_doctor_visit.note|db.sm_doctor_visit.id|db.sm_doctor_visit.visit_dtime|db.sm_doctor_visit.giftnsample)
#     return records
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)
def dcrVSummaryProductD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Doc Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(product_id)<1) and (product_id=='')):
        session.flash = 'Please select product'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doc_visit_prop.cid == c_id)
    qset = qset(db.sm_doc_visit_prop.visit_date >= date_from)
    qset = qset(db.sm_doc_visit_prop.visit_date < date_to_m)

    
    if (depot_id!=''):
        qset = qset(db.sm_doc_visit_prop.depot_id == depot_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doc_visit_prop.level1_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_doc_visit_prop.level2_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_doc_visit_prop.route_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_doc_visit_prop.doc_id == doc)
    if (product_id!=''):
        qset = qset(db.sm_doc_visit_prop.item_id == product_id)
    if (brand!=''):
        qset = qset(db.sm_doc_visit_prop.item_brand == brand)
    if (category!=''):
        qset = qset(db.sm_doc_visit_prop.item_cat == category)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doc_visit_prop.rep_id == mso_id)
    
    records = qset.select(db.sm_doc_visit_prop.level1_id,db.sm_doc_visit_prop.level2_id,db.sm_doc_visit_prop.route_id,db.sm_doc_visit_prop.rep_id,db.sm_doc_visit_prop.rep_name,db.sm_doc_visit_prop.id.count(), orderby= db.sm_doc_visit_prop.level1_id|db.sm_doc_visit_prop.level2_id|db.sm_doc_visit_prop.route_id|db.sm_doc_visit_prop.rep_id|db.sm_doc_visit_prop.rep_name ,groupby= db.sm_doc_visit_prop.rep_id)
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
    myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='RSM  ,  FM  ,  TR  ,  MSO  ,  MSO Name  ,  DCR Count\n'
        
    
    for record in records:
            myString+=str(record[db.sm_doc_visit_prop.level1_id])+','+str(record[db.sm_doc_visit_prop.level2_id])+','+str(record[db.sm_doc_visit_prop.route_id])+','+str(record[db.sm_doc_visit_prop.rep_id])+','+str(record[db.sm_doc_visit_prop.rep_name])+','+str(record[db.sm_doc_visit_prop.id.count()])+'\n'
             
        #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=DCR_Summary_Product.csv'   
    return str(myString)


def prSummary():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Prescription Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(rsm_id)<1) and (fm_id<1) and (tr_id<1) and (doc<1) and (product_id<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_prescription_head.cid == c_id)
    qset = qset(db.sm_prescription_head.submit_date >= date_from)
    qset = qset(db.sm_prescription_head.submit_date <= date_to)
#     qset = qset(db.sm_prescription_details.cid == c_id)
#     qset = qset(db.sm_prescription_details.sl == db.sm_prescription_head.sl)

    if (rsm_id!=''):
        qset = qset(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset = qset(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset = qset(db.sm_prescription_head.submit_by_id == mso_id)
    
    records = qset.select(db.sm_prescription_head.reg_id,db.sm_prescription_head.reg_name,db.sm_prescription_head.tl_id,db.sm_prescription_head.tl_name,db.sm_prescription_head.area_id,db.sm_prescription_head.area_name,db.sm_prescription_head.submit_by_id,db.sm_prescription_head.submit_by_name,db.sm_prescription_head.sl.count(), orderby=db.sm_prescription_head.sl,groupby= db.sm_prescription_head.submit_by_id)


# Self==============================  
    qset_self=db()
    qset_self = qset_self(db.sm_prescription_head.cid == c_id)
    qset_self = qset_self(db.sm_prescription_head.submit_date >= date_from)
    qset_self = qset_self(db.sm_prescription_head.submit_date < date_to)
    qset_self = qset_self(db.sm_prescription_details.cid == c_id)
    qset_self = qset_self(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_self = qset_self(db.sm_prescription_details.med_type == 'SELF')
   
    if (rsm_id!=''):
        qset_self = qset_self(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_self = qset_self(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_self = qset_self(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_self = qset_self(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_self = qset_self(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_self = qset_self.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    selfSbmittedByCountList=[]
    selfSbmittedByList=[]
    for records_self in records_self:
        selfSubId=records_self[db.sm_prescription_head.submit_by_id]
        selfSubCount=records_self[db.sm_prescription_details.sl.count()]
        selfSbmittedByList.append(selfSubId)
        selfSbmittedByCountList.append(selfSubCount)
        
        
        
    
    
    
# OTHER==============================  
    qset_other=db()
    qset_other = qset_other(db.sm_prescription_head.cid == c_id)
    qset_other = qset_other(db.sm_prescription_head.submit_date >= date_from)
    qset_other = qset_other(db.sm_prescription_head.submit_date < date_to)
    qset_other = qset_other(db.sm_prescription_details.cid == c_id)
    qset_other = qset_other(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_other = qset_other(db.sm_prescription_details.med_type == 'OTHER')
   
    if (rsm_id!=''):
        qset_other = qset_other(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_other = qset_other(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_other = qset_other(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_other = qset_other(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_other = qset_other(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_other = qset_other.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    otherSbmittedByCountList=[]
    otherSbmittedByList=[]
    for records_other in records_other:
        otherSubId=records_other[db.sm_prescription_head.submit_by_id]
        otherSubCount=records_other[db.sm_prescription_details.sl.count()]
        otherSbmittedByList.append(otherSubId)
        otherSbmittedByCountList.append(otherSubCount)
 
# Unknown==============================  
    qset_unknown=db()
    qset_unknown = qset_unknown(db.sm_prescription_head.cid == c_id)
    qset_unknown = qset_unknown(db.sm_prescription_head.submit_date >= date_from)
    qset_unknown = qset_unknown(db.sm_prescription_head.submit_date < date_to)
    qset_unknown = qset_unknown(db.sm_prescription_details.cid == c_id)
    qset_unknown = qset_unknown(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_unknown = qset_unknown(db.sm_prescription_details.medicine_id == '')
   
    if (rsm_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_unknown = qset_unknown(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_unknown = qset_unknown.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    unknownSbmittedByCountList=[]
    unknownSbmittedByList=[]
    for records_unknown in records_unknown:
        unknownSubId=records_unknown[db.sm_prescription_head.submit_by_id]
        unknownSubCount=records_unknown[db.sm_prescription_details.sl.count()]
        unknownSbmittedByList.append(unknownSubId)
        unknownSbmittedByCountList.append(unknownSubCount)
#     return qset_other
    
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name,selfSbmittedByList=selfSbmittedByList,selfSbmittedByCountList=selfSbmittedByCountList,otherSbmittedByList=otherSbmittedByList,otherSbmittedByCountList=otherSbmittedByCountList,unknownSbmittedByList=unknownSbmittedByList,unknownSbmittedByCountList=unknownSbmittedByCountList)


def prSummaryD():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='Prescription Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(rsm_id)<1) and (fm_id<1) and (tr_id<1) and (doc<1) and (product_id<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_prescription_head.cid == c_id)
    qset = qset(db.sm_prescription_head.submit_date >= date_from)
    qset = qset(db.sm_prescription_head.submit_date <= date_to)
#     qset = qset(db.sm_prescription_details.cid == c_id)
#     qset = qset(db.sm_prescription_details.sl == db.sm_prescription_head.sl)

    if (rsm_id!=''):
        qset = qset(db.sm_prescription_head.reg_id == reg_id)
    if (fm_id!=''):
        qset = qset(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset = qset(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_prescription_head.doctor_id == doc)
    if (product_id!=''):
        qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset = qset(db.sm_prescription_head.submit_by_id == mso_id)
    
    
    records = qset.select(db.sm_prescription_head.reg_id,db.sm_prescription_head.reg_name,db.sm_prescription_head.tl_id,db.sm_prescription_head.tl_name,db.sm_prescription_head.area_id,db.sm_prescription_head.area_name,db.sm_prescription_head.submit_by_id,db.sm_prescription_head.submit_by_name,db.sm_prescription_head.sl.count(), orderby=db.sm_prescription_head.sl,groupby= db.sm_prescription_head.submit_by_id)
    
    # Self==============================  
    qset_self=db()
    qset_self = qset_self(db.sm_prescription_head.cid == c_id)
    qset_self = qset_self(db.sm_prescription_head.submit_date >= date_from)
    qset_self = qset_self(db.sm_prescription_head.submit_date < date_to)
    qset_self = qset_self(db.sm_prescription_details.cid == c_id)
    qset_self = qset_self(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_self = qset_self(db.sm_prescription_details.med_type == 'SELF')
   
    if (rsm_id!=''):
        qset_self = qset_self(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_self = qset_self(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_self = qset_self(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_self = qset_self(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_self = qset_self(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_self = qset_self.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    selfSbmittedByCountList=[]
    selfSbmittedByList=[]
    for records_self in records_self:
        selfSubId=records_self[db.sm_prescription_head.submit_by_id]
        selfSubCount=records_self[db.sm_prescription_details.sl.count()]
        selfSbmittedByList.append(selfSubId)
        selfSbmittedByCountList.append(selfSubCount)
        
        
        
    
    
    
# OTHER==============================  
    qset_other=db()
    qset_other = qset_other(db.sm_prescription_head.cid == c_id)
    qset_other = qset_other(db.sm_prescription_head.submit_date >= date_from)
    qset_other = qset_other(db.sm_prescription_head.submit_date < date_to)
    qset_other = qset_other(db.sm_prescription_details.cid == c_id)
    qset_other = qset_other(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_other = qset_other(db.sm_prescription_details.med_type == 'OTHER')
   
    if (rsm_id!=''):
        qset_other = qset_other(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_other = qset_other(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_other = qset_other(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_other = qset_other(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_other = qset_other(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_other = qset_other.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    otherSbmittedByCountList=[]
    otherSbmittedByList=[]
    for records_other in records_other:
        otherSubId=records_other[db.sm_prescription_head.submit_by_id]
        otherSubCount=records_other[db.sm_prescription_details.sl.count()]
        otherSbmittedByList.append(otherSubId)
        otherSbmittedByCountList.append(otherSubCount)
 
# Unknown==============================  
    qset_unknown=db()
    qset_unknown = qset_unknown(db.sm_prescription_head.cid == c_id)
    qset_unknown = qset_unknown(db.sm_prescription_head.submit_date >= date_from)
    qset_unknown = qset_unknown(db.sm_prescription_head.submit_date < date_to)
    qset_unknown = qset_unknown(db.sm_prescription_details.cid == c_id)
    qset_unknown = qset_unknown(db.sm_prescription_details.sl == db.sm_prescription_head.sl)
    qset_unknown = qset_unknown(db.sm_prescription_details.medicine_id == '')
   
    if (rsm_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.reg_id == rsm_id)
    if (fm_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.tl_id == fm_id)
    if (tr_id!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.area_id == tr_id)
    if (doc!=''):
        qset_unknown = qset_unknown(db.sm_prescription_head.doctor_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_prescription_details.medicine_id == product_id)
    if (len(mso_id)>3):
        qset_unknown = qset_unknown(db.sm_prescription_head.submit_by_id == mso_id)
       
    records_unknown = qset_unknown.select(db.sm_prescription_head.submit_by_id,db.sm_prescription_details.sl.count(), orderby=db.sm_prescription_details.sl,groupby= db.sm_prescription_head.submit_by_id)
    unknownSbmittedByCountList=[]
    unknownSbmittedByList=[]
    for records_unknown in records_unknown:
        unknownSubId=records_unknown[db.sm_prescription_head.submit_by_id]
        unknownSubCount=records_unknown[db.sm_prescription_details.sl.count()]
        unknownSbmittedByList.append(unknownSubId)
        unknownSbmittedByCountList.append(unknownSubCount)
    
    
    myString='DateRange,'+date_from+','+date_to+'\n'
#     myString+='Depot/Branch,'+depot_id+'|'+depot_name+'\n'
    myString+='RSM,'+rsm_id+'|'+rsm_name+'\n'
    myString+='FM,'+fm_id+'|'+fm_name+'\n'
    myString+='RT,'+tr_id+'|'+tr_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Product,'+product_id+'|'+product_name+'\n'
#     myString+='Category,'+category+'\n'
    myString+='Doctor,'+doc+'|'+doc_name+'\n\n'
    myString+='RSM  ,  FM  ,  TR  ,  Submitted by ID  ,  Submitted by Name ,   Prescriptiom Count,OwnBrand,OtherBrand,Others\n'
    for record in records:
        selfCount=0
        otherCount=0
        unknownCount=0
        submit_by_id=record[db.sm_prescription_head.submit_by_id]
        if [s for s in selfSbmittedByList if submit_by_id in s]:
            index_element = selfSbmittedByList.index(submit_by_id)   
            selfCount=selfSbmittedByCountList[index_element]
        if [s for s in otherSbmittedByList if submit_by_id in s]:
            index_element = otherSbmittedByList.index(submit_by_id) 
            otherCount=otherSbmittedByCountList[index_element]
        if [s for s in unknownSbmittedByList if submit_by_id in s]:
            index_element = unknownSbmittedByList.index(submit_by_id)
            unknownCount=unknownSbmittedByCountList[index_element]
        myString+=str(record[db.sm_prescription_head.reg_id])+','+str(record[db.sm_prescription_head.tl_id])+','+str(record[db.sm_prescription_head.area_id])+','+str(record[db.sm_prescription_head.submit_by_id])+','+str(record[db.sm_prescription_head.sl.count()])+','+str(selfCount)+','+str(otherCount)+','+str(unknownCount)+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=Prescription_Summary.csv'   
    return str(myString)
# =====================================================



def dcr_day_count_details():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

    c_id = session.cid
    response.title='dcr_day_count_details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()
    # return zm_id
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # fm_name=str(request.vars.fm_name).strip()
    # return fm_id
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    
    product_id=str(request.vars.product_id).strip()
    # return product_id
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(rsm_id)<1) and (fmA_id<1) and (tr_id<1) and (doc<1) and (product_id<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)
#     qset = qset(db.sm_prescription_details.cid == c_id)
#     qset = qset(db.sm_prescription_details.sl == db.sm_prescription_head.sl)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.level3_id == tr_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)
   
    # if (product_id!=''):
    #     qset = qset(db.sm_prescription_details.medicine_id == product_id)
   
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
    
    records = qset.select(db.sm_doctor_visit.doc_id,db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level0_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level1_name,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.visit_date,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name, orderby=db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id,groupby= db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id)
    # return records
    totalCount=qset.count()
    
    return dict(totalCount=totalCount,records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fmA_id=fmA_id,tr_id=tr_id,tr_name=tr_name,product_id=product_id,product_name=product_name,brand=brand,category=category,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)


def dcr_day_count():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   

    c_id = session.cid
    response.title='dcr_day_count'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()

    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fmA_id=str(request.vars.fmA_id).strip()
    # fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((len(rsm_id)<1) and (fmA_id<1) and (tr_id<1) and (doc<1) and (product_id<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)
#     qset = qset(db.sm_prescription_details.cid == c_id)
#     qset = qset(db.sm_prescription_details.sl == db.sm_prescription_head.sl)

    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)

    if (rsm_id!=''):
        qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
    
    if (fmA_id!=''):
        qset = qset(db.sm_doctor_visit.level2_id == fmA_id)
    
    if (tr_id!=''):
        qset = qset(db.sm_doctor_visit.level3_id == tr_id)
    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
    
    records = qset.select(db.sm_doctor_visit.doc_id,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.visit_date,db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level0_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level1_name,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name, orderby=db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id,groupby= db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id)
    totalCount=qset.count()
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='ZM,'+zm_id+'|'+zm_name+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    myString+='Area,'+tr_id+'|'+tr_name+'\n'
    myString+='FM,'+fmA_id+'\n'
    myString+='Reg,'+rsm_id+'|'+rsm_name+'\n'
    myString+= 'Total :'+','+str(totalCount) + '\n\n' 
    myString+='doctorID  ,  doctorName ,RegionID,RegionName,ZoneID,ZoneName,AreaID, AreaName ,  Date  ,  Visit\n'
    for record in records:
        RegionID=str(record.level0_id)
        RegionName=str(record.level0_name)
        ZoneID=str(record.level1_id)
        ZoneName=str(record.level1_name)
        doctorID=str(record.doc_id)
        doctorName=str(record.doc_name)
        Date=str(record.visit_date)
        route_id=str(record.route_id)
        route_name=str(record.route_name)
        Visit='1'
        
        myString+=doctorID+','+doctorName+','+RegionID+','+RegionName+','+ZoneID+','+ZoneName+','+route_id+','+route_name+','+Date+','+Visit+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=dcr.csv'   
    return str(myString)


def dcr_day_count_details_MPO():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

    c_id = session.cid
    response.title='dcr_day_count_details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to    
   
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((doc<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)   
   
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
    
    records = qset.select(db.sm_doctor_visit.doc_id,db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level0_name,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level1_name,db.sm_doctor_visit.visit_date,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name, orderby=db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id,groupby= db.sm_doctor_visit.rep_id)    
    totalCount=qset.count()
    
    return dict(totalCount=totalCount,records=records,date_from=date_from,date_to=date_to,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)


def dcr_day_count_MPO():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

    c_id = session.cid
    response.title='dcr_day_count_details'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to    
   
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d') 
    date_to_m=date_to_m + datetime.timedelta(days = 1) 
    
#     return len(mso_id)
    if ((doc<1) and (mso_id<1)):
        session.flash = 'Please select RSM or FM or TR or product or submitted by'
        redirect (URL(c='dcr_report', f='index'))
   
    
#     return date_from
    qset=db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)

    
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)   
   
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    
    
    records = qset.select(db.sm_doctor_visit.doc_id,db.sm_doctor_visit.doc_name,db.sm_doctor_visit.visit_date,db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level0_name,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level1_name,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name, orderby=db.sm_doctor_visit.visit_date|db.sm_doctor_visit.doc_id,groupby= db.sm_doctor_visit.route_id)    
    totalCount=qset.count()
    
    myString='DateRange,'+date_from+','+date_to+'\n'
    myString+='MSO,'+mso_id+'|'+mso_name+'\n'
    # myString+='Area,'+tr_id+'|'+tr_name+'\n'
    # myString+='FM,'+fmA_id+'\n'
    # myString+='Reg,'+rsm_id+'|'+rsm_name+'\n'
    myString+= 'Total :'+','+str(totalCount) + '\n\n' 
    myString+='doctorID  ,  doctorName ,ZoneID, ZoneName ,RegionID, RegionName ,AreaID, AreaName ,  Date  ,  Visit\n'
    for record in records:
        ZoneID=str(record.level0_id)
        ZoneName=str(record.level0_name)
        RegionID=str(record.level1_id)
        RegionName=str(record.level1_name)
        doctorID=str(record.doc_id)
        doctorName=str(record.doc_name)
        Date=str(record.visit_date)
        route_id=str(record.route_id)
        route_name=str(record.route_name)
        Visit='1'
        
        myString+=doctorID+','+doctorName+','+ZoneID+','+ZoneName+','+RegionID+','+RegionName +','+route_id+','+route_name+','+Date+','+Visit+'\n'
         
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=MPO_dcr.csv'   
    return str(myString)



def ffreportData():
#     return 'dfdsf'
    cid=session.cid
 #   cid='IBNSINA'
#     cid=request.vars.c_id
    rpt_date=request.vars.date_from
   # return rpt_date
#    date_from=request.vars.date_from
    report_date = str(date_fixed.strftime('%d-%m-%Y'))
    report_time = str(date_fixed.strftime(' %I:%M:%S %p'))
    rep_asc_Str="""SELECT rpt_date_time ,rep_id,rep_name,level0_id,level0_name,level1_id,
                level1_name,level2_id,level2_name,level3_id,level3_name,order_count,first_order_time,dcr_count,first_visit_doc_id,first_visit_doc_name,
                first_visit_doc_date,rx_count,first_visit_rx_doc_id,first_visit_rx_doc_name,first_visit_rx_doc_date  from sm_ff_activity_status 
                where  cid ='"""+str(cid)+"""'  and  rpt_date ='"""+str(rpt_date)+"""' order by level0_name,level1_name,level2_name,level3_name asc"""
#     return rep_asc_Str
    ordrasc=db.executesql(rep_asc_Str,as_dict = True)
    
    
    recordCount="""SELECT count(sm_ff_activity_status.id) as totalVisit from sm_ff_activity_status 
                where  cid ='"""+str(cid)+"""'  and  rpt_date ='"""+str(rpt_date)+"""' 
                order by rep_id asc"""
#     return rep_asc_Str        
    ffCount=db.executesql(recordCount,as_dict = True)    

    recordCountShow=0
    if ffCount:
        for ffCount in ffCount:
            recordCountShow=ffCount['totalVisit']

    
    return dict(ordrasc=ordrasc,rpt_date=rpt_date,report_date=report_date,report_time=report_time,recordCountShow=recordCountShow)

def ffreportData_load():
 #   cid='IBNSINA'
    
    cid=session.cid
    rpt_date=request.vars.date_from

    rep_asc_Str="""SELECT rpt_date_time ,rep_id,rep_name,level0_id,level0_name,level1_id,
                level1_name,level2_id,level2_name,level3_id,level3_name,order_count,first_order_time,dcr_count,first_visit_doc_id,first_visit_doc_name,
                first_visit_doc_date,rx_count,first_visit_rx_doc_id,first_visit_rx_doc_name,first_visit_rx_doc_date  from sm_ff_activity_status 
                where  cid ='"""+str(cid)+"""'  and  rpt_date ='"""+str(rpt_date)+"""' order by level0_name,level1_name,level2_name,level3_name asc"""
#     return rep_asc_Str
    ordrasc=db.executesql(rep_asc_Str,as_dict = True)
#    myString='Date :'+str(date_fixed.strftime('%d-%m-%Y'))+'\n'
    myString='Date :'+str(rpt_date)+'\n'
#    myString=myString+'Time :'+str(date_fixed.strftime(' %I:%M:%S %p'))+'\n'
    myString=myString+'Zone Name,Zone Id,Region Name,Region Id,Area Name,Area Id,Territory Name,Territory Id,Representative Name,Representative Id,Order Count,Doctor Visit Count,\n'
    
    for ordrasc in ordrasc:
#        rpt_date_time=str(ordrasc['rpt_date_time'])
        rep_id=str(ordrasc['rep_id'])
        try:
            rep_name=str(ordrasc['rep_name'])
        except:
            rep_name=rep_id
        level0_id=str(ordrasc['level0_id'])
        level0_name=str(ordrasc['level0_name'])
        level1_id=str(ordrasc['level1_id'])
        level1_name=str(ordrasc['level1_name'])
        level2_id=str(ordrasc['level2_id'])
        level2_name=str(ordrasc['level2_name'])
        level3_id=str(ordrasc['level3_id'])
        level3_name=str(ordrasc['level3_name'])
        order_count=str(ordrasc['order_count'])
#         first_order_time=str(ordrasc['first_order_time'])
        dcr_count=str(ordrasc['dcr_count'])
#         first_visit_doc_id=str(ordrasc['first_visit_doc_id'])
#   
#         first_visit_doc_name=str(ordrasc['first_visit_doc_name'])
#         first_visit_doc_date=str(ordrasc['first_visit_doc_date'])
#         rx_count=str(ordrasc['rx_count'])
#         first_visit_rx_doc_id=str(ordrasc['first_visit_rx_doc_id'])
#         first_visit_rx_doc_name=str(ordrasc['first_visit_rx_doc_name'])
#         first_visit_rx_doc_date=str(ordrasc['first_visit_rx_doc_date'])
#          
#        myString=myString+str(level0_id)+','+str(level0_name)+','+str(level1_id)+','+str(level1_name)+','+str(level2_id)+','+str(level2_name)+','+str(level3_id)+','+str(level3_name)+','+str(rep_id)+','+str(rep_name)+','+str(order_count)+','+str(dcr_count)+'\n'

        myString=myString+str(level0_name)+','+str(level0_id)+','+str(level1_name)+','+str(level1_id)+','+str(level2_name)+','+str(level2_id)+','+str(level3_name)+','+str(level3_id)+','+str(rep_name)+','+str(rep_id)+','+str(order_count)+','+str(dcr_count)+'\n'
  
    
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=DailyVisitSmmary'+str(rpt_date)+'.csv'   
    return str(myString) 



#==========Nazma 2018/03/24

# http://127.0.0.1:8000/ibn_report/dcr_report/total_ffreportData?cid=IBNSINA&date_from=2018-03-05&date_to=2018-03-07

#count(sm_order_head.id) as totalVisit

def total_ffreportData():
    cid=session.cid
#    cid='IBNSINA'
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    report_date = str(date_fixed.strftime('%d-%m-%Y'))
    report_time = str(date_fixed.strftime(' %I:%M:%S %p'))
    rep_asc_Str="""SELECT rpt_date_time ,rep_id,rep_name,level0_id,level0_name,level1_id,
                level1_name,level2_id,level2_name,level3_id,level3_name,sum(order_count) as totalOrder,first_order_time,sum(dcr_count) as totalDcr,first_visit_doc_id,first_visit_doc_name,
                first_visit_doc_date,rx_count,first_visit_rx_doc_id,first_visit_rx_doc_name,first_visit_rx_doc_date  from sm_ff_activity_status 
                where  cid ='"""+str(cid)+"""'  and  rpt_date >='"""+str(date_from)+"""' and  rpt_date <='"""+str(date_to)+"""' group by rep_id  order by level0_name,level1_name,level2_name,level3_name  asc"""
#     return rep_asc_Str
    ordrasc=db.executesql(rep_asc_Str,as_dict = True)
    
#order    
#     record_order_Count="""SELECT sum(sm_ff_activity_status.order_count) as totalVisit from sm_ff_activity_status 
#                 where  cid ='"""+str(cid)+"""'  and  rpt_date >='"""+str(date_from)+"""' and  rpt_date <='"""+str(date_to)+"""' order by level0_name,level1_name,level2_name,level3_name asc"""
#     return rep_asc_Str        
#     ffCount_order=db.executesql(record_order_Count,as_dict = True)    
# 
# 
#     recordCountShow_order=0
#     if ffCount_order:
#         for ffCount_order in ffCount_order:
#             recordCountShow_order=ffCount_order['totalVisit']

#doctor
#     record_dcr_Count="""SELECT sum(sm_ff_activity_status.dcr_count) as totalVisit from sm_ff_activity_status 
#                 where  cid ='"""+str(cid)+"""'  and  rpt_date >='"""+str(date_from)+"""' and  rpt_date <='"""+str(date_to)+"""' order by level0_name,level1_name,level2_name,level3_name asc"""
# #     return rep_asc_Str        
#     ffCount_dcr=db.executesql(record_dcr_Count,as_dict = True)    
# 
#     recordCountShow_dcr=0
#     if ffCount_dcr:
#         for ffCount_dcr in ffCount_dcr:
#             recordCountShow_dcr=ffCount_dcr['totalVisit']

    recordCountShow_dcr=''
    recordCountShow_order=''
    return dict(ordrasc=ordrasc,date_from=date_from,date_to=date_to,report_date=report_date,report_time=report_time,recordCountShow_dcr=recordCountShow_dcr,recordCountShow_order=recordCountShow_order)

def total_ffreportData_load():
#     cid='IBNSINA'
    
    cid=session.cid
    date_from=request.vars.date_from
    date_to=request.vars.date_to

    rep_asc_Str="""SELECT rpt_date_time ,rep_id,rep_name,level0_id,level0_name,level1_id,
                level1_name,level2_id,level2_name,level3_id,level3_name,sum(order_count) as totalOrder,first_order_time,sum(dcr_count) as totalDcr,first_visit_doc_id,first_visit_doc_name,
                first_visit_doc_date,rx_count,first_visit_rx_doc_id,first_visit_rx_doc_name,first_visit_rx_doc_date  from sm_ff_activity_status 
                where  cid ='"""+str(cid)+"""'  and  rpt_date >='"""+str(date_from)+"""' and  rpt_date <='"""+str(date_to)+"""' group by rep_id  order by level0_name,level1_name,level2_name,level3_name  asc"""
#     return rep_asc_Str
    ordrasc=db.executesql(rep_asc_Str,as_dict = True)
    myString='From Date :'+str(date_from)+'\n'
    myString=myString+'To Date :'+str(date_to)+'\n\n'

    myString=myString+'Zone Name,Zone Id,Region Name,Region Id,Area Name,Area Id,Territory Name,Territory Id,Representative Name,Representative Id,Order Count,Doctor Visit Count,\n'
    
    for ordrasc in ordrasc:
#        rpt_date_time=str(ordrasc['rpt_date_time'])
        rep_id=str(ordrasc['rep_id'])
        try:
            rep_name=str(ordrasc['rep_name'])
        except:
            rep_name=rep_id
        level0_id=str(ordrasc['level0_id'])
        level0_name=str(ordrasc['level0_name'])
        level1_id=str(ordrasc['level1_id'])
        level1_name=str(ordrasc['level1_name'])
        level2_id=str(ordrasc['level2_id'])
        level2_name=str(ordrasc['level2_name'])
        level3_id=str(ordrasc['level3_id'])
        level3_name=str(ordrasc['level3_name'])
        order_count=str(ordrasc['totalOrder'])
        dcr_count=str(ordrasc['totalDcr'])

        myString=myString+str(level0_name)+','+str(level0_id)+','+str(level1_name)+','+str(level1_id)+','+str(level2_name)+','+str(level2_id)+','+str(level3_name)+','+str(level3_id)+','+str(rep_name)+','+str(rep_id)+','+str(order_count)+','+str(dcr_count)+'\n'
  
    
    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=VisitSmmary'+str(date_from)+'to'+str(date_to)+'.csv'   
    return str(myString)


def activity_status_order_d():
    cid = session.cid
    date_from = request.vars.date_from
    date_to = request.vars.date_to

    sin_list = []
    sinRep = "select rep_id from sm_rep where cid='" + cid + "' and note='SIN'"
    sinRep = db.executesql(sinRep, as_dict=True)
    for j in range(len(sinRep)):
        sinRepStr = sinRep[j]
        sin_list.append(sinRepStr['rep_id'])

    sup_list = []
    supervisor = "select sup_id from sm_supervisor_level where cid='" + cid + "'"
    supervisor = db.executesql(supervisor, as_dict=True)
    for i in range(len(supervisor)):
        superStr = supervisor[i]
        sup_list.append(superStr['sup_id'])

    clientRows = "select area_id,sum(1) as noOfClient  from sm_client where cid='" + cid + "' group by area_id"
    clientRows = db.executesql(clientRows, as_dict=True)


    sqlRep = 'SELECT a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level_id` as level_id,a.`level_name` as level_name,b.rep_id as rep_id,b.rep_name as rep_name,0 as ord_q,0 as ord_q_uniq FROM sm_level a,sm_rep_area b where a.cid ="' + cid + '" and a.depth=3 and a.level_id=b.area_id'
    #sqlSup = 'SELECT a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level3` as level_id,a.`level3_name` as level_name,b.sup_id as rep_id,b.sup_name as rep_name,0 as ord_q,"0" as ord_q_uniq FROM sm_level a,sm_supervisor_level b where a.cid ="' + cid + '" and a.depth=b.level_depth_no and a.level_id=b.level_id'
    orderRows = 'Select a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level_id` as level_id,a.`level_name` as level_name,b.rep_id as rep_id,b.rep_name as rep_name,sum(1) as ord_q,count(distinct(b.client_id)) as ord_q_uniq FROM sm_level a,sm_order_head b where a.cid ="' + cid + '" and b.order_date >="' + str(date_from) + '" and b.order_date <="' + str(date_to) + '" and a.depth=3 and a.level_id=b.area_id group by b.area_id,b.rep_id'
    records = "select level0,level0_name,level1,level1_name,level2,level2_name,level_id,level_name,rep_id,rep_name,sum(ord_q) as ord_q,sum(ord_q_uniq) as ord_q_uniq from (" + sqlRep + " union all " + orderRows + ") p group by level0,level1,level2,level_id,rep_id order by level0,level1,level2,level_id,rep_id;"
    records = db.executesql(records, as_dict=True)

    myString = 'From Date :' + str(date_from) + '\n'
    myString = myString + 'To Date :' + str(date_to) + '\n\n'

    myString = myString + 'Region ID,Region Name,Zone ID,Zone Name,Area ID,Area Name,Submitted By ID,Submitted By Name,Type,Team,Territory ID,Territory Name,Number Of Customer,Order Count,Visited Customer,\n' #,Number Of Doctor,Dcr Count,Visited Doctor

    for row in records:
        userType = ''
        division = ''
        level0 = str(row['level0'])
        level0_name = str(row['level0_name'])
        level1 = str(row['level1'])
        level1_name = str(row['level1_name'])
        level2 = str(row['level2'])
        level2_name = str(row['level2_name'])
        rep_id = str(row['rep_id'])
        rep_name = str(row['rep_name'])
        level3 = str(row['level_id'])
        level3_name = str(row['level_name'])

        ord_q = str(row['ord_q'])
        ord_q_uniq = str(row['ord_q_uniq'])

        if rep_id in sup_list:
            userType = 'Supervisor'
        else:
            userType = 'Representative'

        if rep_id in sin_list:
            division = 'Sinavison'
        else:
            division = 'General'

        noOfClient = 0
        for m in range(len(clientRows)):
            clientRow = clientRows[m]

            if clientRow['area_id'] == level3:
                noOfClient = str(clientRow['noOfClient'])
                break


        myString = myString + str(level0) + ',' + str(level0_name) + ',' + str(level1) + ',' + str(
            level1_name) + ',' + str(level2) + ',' + str(level2_name) + ',' + str(rep_id) + ',' + str(
            rep_name) + ',' + str(userType) + ',' + str(division) + ',' + str(level3) + ',' + str(
            level3_name) + ',' + str(noOfClient)+ ',' + str(ord_q) + ',' + str(
            ord_q_uniq) + '\n' # + ',' + str(noOfDoc)

    # Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=activity_status_order_download' + str(
        date_from) + 'to' + str(date_to) + '.csv'
    return str(myString)

def activity_status_dcr_d():
    cid = session.cid
    date_from = request.vars.date_from
    date_to = request.vars.date_to

    sin_list = []
    sinRep = "select rep_id from sm_rep where cid='" + cid + "' and note='SIN'"
    sinRep = db.executesql(sinRep, as_dict=True)
    for j in range(len(sinRep)):
        sinRepStr = sinRep[j]
        sin_list.append(sinRepStr['rep_id'])

    sup_list = []
    supervisor = "select sup_id from sm_supervisor_level where cid='" + cid + "'"
    supervisor = db.executesql(supervisor, as_dict=True)
    for i in range(len(supervisor)):
        superStr = supervisor[i]
        sup_list.append(superStr['sup_id'])

    docRows = "select area_id,sum(1) as noOfDoc from sm_doctor_area where cid='" + cid + "' group by area_id"
    docRows = db.executesql(docRows, as_dict=True)

    sqlRep = 'SELECT a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level_id` as level_id,a.`level_name` as level_name,b.rep_id as rep_id,b.rep_name as rep_name,0 as dcr_q,"0" as dcr_q_uniq FROM sm_level a,sm_rep_area b where a.cid ="' + cid + '" and a.depth=3 and a.level_id=b.area_id'
    dcrRows = 'Select a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level_id` as level_id,a.`level_name` as level_name,b.rep_id as rep_id,b.rep_name as rep_name,sum(1) as dcr_q,count(distinct(b.doc_id)) as dcr_q_uniq FROM sm_level a,sm_doctor_visit b where a.cid ="' + cid + '" and b.visit_date >="' + str(date_from) + '" and b.visit_date <="' + str(date_to) + '" and a.depth=3 and a.level_id=b.route_id group by b.route_id,b.rep_id'
    records = "select level0,level0_name,level1,level1_name,level2,level2_name,level_id,level_name,rep_id,rep_name,sum(dcr_q) as dcr_q,sum(dcr_q_uniq) as dcr_q_uniq  from (" + sqlRep + " union all " + dcrRows + ") p group by level0,level1,level2,level_id,rep_id order by level0,level1,level2,level_id,rep_id;"
    records = db.executesql(records, as_dict=True)

    myString = 'From Date :' + str(date_from) + '\n'
    myString = myString + 'To Date :' + str(date_to) + '\n\n'

    myString = myString + 'Region ID,Region Name,Zone ID,Zone Name,Area ID,Area Name,Submitted By ID,Submitted By Name,Type,Team,Territory ID,Territory Name,Number Of Doctor,Dcr Count,Visited Doctor,\n' #,Number Of Customer,Order Count,Visited Customer

    for row in records:
        userType = ''
        division = ''
        level0 = str(row['level0'])
        level0_name = str(row['level0_name'])
        level1 = str(row['level1'])
        level1_name = str(row['level1_name'])
        level2 = str(row['level2'])
        level2_name = str(row['level2_name'])
        rep_id = str(row['rep_id'])
        rep_name = str(row['rep_name'])
        level3 = str(row['level_id'])
        level3_name = str(row['level_name'])

        dcr_q = str(row['dcr_q'])
        dcr_q_uniq = str(row['dcr_q_uniq'])

        if rep_id in sup_list:
            userType = 'Supervisor'
        else:
            userType = 'Representative'

        if rep_id in sin_list:
            division = 'Sinavison'
        else:
            division = 'General'


        noOfDoc = 0
        for n in range(len(docRows)):
            docRow = docRows[n]

            if docRow['area_id'] == level3:
                noOfDoc = str(docRow['noOfDoc'])
                break


        myString = myString + str(level0) + ',' + str(level0_name) + ',' + str(level1) + ',' + str(
            level1_name) + ',' + str(level2) + ',' + str(level2_name) + ',' + str(rep_id) + ',' + str(
            rep_name) + ',' + str(userType) + ',' + str(division) + ',' + str(level3) + ',' + str(
            level3_name) + ',' + str(noOfDoc)+ ',' + str(dcr_q) + ',' + str(dcr_q_uniq) + '\n' #+ ',' + str(noOfClient)

    # Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=activity_status_dcr_download' + str(
        date_from) + 'to' + str(date_to) + '.csv'
    return str(myString)

def activity_status_d_b():
    cid = session.cid
    date_from = request.vars.date_from
    date_to = request.vars.date_to

    sup_list = []
    supervisor = "select sup_id from sm_supervisor_level where cid='" + cid + "'"
    supervisor = db.executesql(supervisor, as_dict=True)
    for i in range(len(supervisor)):
        superStr = supervisor[i]
        sup_list.append(superStr['sup_id'])

    sin_list = []
    rep = "select rep_id from sm_rep where cid='" + cid + "' and note='SIN'"
    rep = db.executesql(rep, as_dict=True)
    for j in range(len(rep)):
        repStr = rep[j]
        sin_list.append(repStr['rep_id'])

    clientRows = "select area_id as clArea,count(distinct(client_id)) as noOfClient from sm_client where cid='" + cid + "' group by area_id;"
    clientRows = db.executesql(clientRows, as_dict=True)

    docRows = "select area_id as docArea,count(distinct(doc_id)) as noOfDoc from sm_doctor_area where cid='" + cid + "' group by area_id;"
    docRows = db.executesql(docRows, as_dict=True)


    sql2='SELECT a.`level0` as level0,a.`level0_name` as level0_name,a.`level1` as level1,a.`level1_name` as level1_name,a.`level2` as level2,a.`level2_name` as level2_name,a.`level_id` as level_id,a.`level_name` as level_name,b.rep_id as rep_id,b.rep_name as rep_name, 0 as ord_q,0 as ord_q_uniq, 0 as dcr_q,0 as dcr_q_uniq FROM sm_level a,sm_rep_area b where a.cid ="'+ cid + '" and a.depth=3 and a.level_id=b.area_id'

    sql3='Select level0_id as level0,level0_name,level1_id as level1,level1_name,level2_id as level2,level2_name,area_id as level_id,area_name as level_name,rep_id,rep_name,1 as ord_q,client_id as ord_q_uniq,0 as dcr_q,0 as dcr_q_uniq FROM sm_order_head where cid ="'+ cid + '" and order_date >="' + str(date_from) + '" and order_date <="' + str(date_to) + '" '
    sql4='Select level0_id as level0,level0_name,level1_id as level1,level1_name,level2_id as level2,level2_name,route_id as level_id,level3_name as level_name,rep_id,rep_name,0 as ord_q,0 as ord_q_uniq,1 as dcr_q,doc_id as dcr_q_uniq FROM sm_doctor_visit where cid ="'+ cid + '" and visit_date >="' + str(date_from) + '" and visit_date <="' + str(date_to) + '"'

    records="select level0,level0_name,level1,level1_name,level2,level2_name,level_id,level_name,rep_id,rep_name,sum(ord_q) as ord_q,count(distinct(ord_q_uniq))-1 as ord_q_uniq, sum(dcr_q) as dcr_q,count(distinct(dcr_q_uniq))-1 as dcr_q_uniq from ("+sql2+" union all "+sql3+" union all "+sql4+") p group by level0,level1,level2,level_id,rep_id order by level0,level1,level2,level_id,rep_id;"
    records = db.executesql(records, as_dict=True)
    # rec_Str = "select `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level_id`,`level_name`, ff_count.* from(SELECT `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level_id`,`level_name` FROM `sm_level` where is_leaf=1 and depth=3 ) as area_struc ,(Select rep_id, rep_name, area_id, area_name, sum(ord_c) as ord_q, sum(ord_c_uniq) as ord_q_uniq, sum(dcr_c) as dcr_q,sum(dcr_c_uniq) as dcr_q_uniq from (SELECT rep_id,rep_name,area_id,area_name, 0 as ord_c,0 as ord_c_uniq, 0 as dcr_c,0 as dcr_c_uniq FROM ibnsina.sm_rep_area where cid ='IBNSINA' GROUP BY `rep_id`,area_id union Select rep_id, rep_name, area_id, area_name, count(id) as ord_c,count(distinct(client_id)) as ord_c_uniq, 0 as dcr_c,0 as dcr_c_uniq FROM ibnsina.sm_order_head where cid ='IBNSINA' and  order_date >='" + str(
    #     date_from) + "' and  order_date <='" + str(
    #     date_to) + "' group by rep_id,area_id union Select rep_id,rep_name,route_id,route_name, 0 as ord_c,0 as ord_c_uniq, count(id) as dcr_c,count(distinct(doc_id)) as dcr_c_uniq FROM ibnsina.sm_doctor_visit where cid ='IBNSINA' and visit_date >='" + str(
    #     date_from) + "' and  visit_date <='" + str(
    #     date_to) + "' group by rep_id,route_id ) as ord_dcr group by rep_id, area_id) as ff_count where ff_count.area_id=area_struc.level_id"

    #recStr = db.executesql(rec_Str, as_dict=True)
    #return rec_Str

    myString = 'From Date :' + str(date_from) + '\n'
    myString = myString + 'To Date :' + str(date_to) + '\n\n'

    myString = myString + 'Region ID,Region Name,Zone ID,Zone Name,Area ID,Area Name,Submitted By ID,Submitted By Name,Type,Sinavison,Territory ID,Territory Name,Number Of Customer,Number Of Doctor,Order Count,Visited Customer,Dcr Count,Visited Doctor,\n'

    for row in records:
        userType = ''
        division = ''
        level0 = str(row['level0'])
        level0_name = str(row['level0_name'])
        level1 = str(row['level1'])
        level1_name = str(row['level1_name'])
        level2 = str(row['level2'])
        level2_name = str(row['level2_name'])
        rep_id = str(row['rep_id'])
        rep_name = str(row['rep_name'])
        level3 = str(row['level_id'])
        level3_name = str(row['level_name'])
        ord_q = str(row['ord_q'])
        ord_q_uniq = str(row['ord_q_uniq'])
        dcr_q = str(row['dcr_q'])
        dcr_q_uniq = str(row['dcr_q_uniq'])

        noOfClient = 0
        for m in range(len(clientRows)):
            clientRow = clientRows[m]

            if clientRow['clArea'] == level3:
                noOfClient = str(clientRow['noOfClient'])

        noOfDoc = 0
        for n in range(len(docRows)):
            docRow = docRows[n]

            if docRow['docArea'] == level3:
                noOfDoc = str(docRow['noOfDoc'])

        if rep_id in sup_list:
            userType = 'Supervisor'
        else:
            userType = 'Representative'

        if rep_id in sin_list:
            division = 'Sinavison'
        else:
            division = 'General'

        myString = myString + str(level0) + ',' + str(level0_name) + ',' + str(level1) + ',' + str(
            level1_name) + ',' + str(level2) + ',' + str(level2_name) + ',' + str(rep_id) + ',' + str(
            rep_name) + ',' + str(userType) + ',' + str(division) + ',' + str(level3) + ',' + str(
            level3_name) + ',' + str(noOfClient) + ',' + str(noOfDoc) + ',' + str(ord_q) + ',' + str(
            ord_q_uniq) + ',' + str(dcr_q) + ',' + str(dcr_q_uniq) + '\n'

    # Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=Activity_Status_Download' + str(
        date_from) + 'to' + str(date_to) + '.csv'
    return str(myString)

def activity_status_d_190807():
    cid=session.cid
    date_from=request.vars.date_from
    date_to=request.vars.date_to

    sup_list=[]
    supervisor="select sup_id from sm_supervisor_level where cid='"+cid+"'"
    supervisor=db.executesql(supervisor,as_dict = True)
    for i in range(len(supervisor)):
        superStr=supervisor[i]
        sup_list.append(superStr['sup_id'])

    sin_list=[]
    rep="select rep_id from sm_rep where cid='"+cid+"' and note='SIN'"
    rep=db.executesql(rep,as_dict = True)
    for j in range(len(rep)):
        repStr=rep[j]
        sin_list.append(repStr['rep_id'])


    clientRows="select area_id as clArea,count(distinct(client_id)) as noOfClient from sm_client where cid='"+cid+"' group by area_id;"
    clientRows=db.executesql(clientRows,as_dict = True)

    docRows="select area_id as docArea,count(distinct(doc_id)) as noOfDoc from sm_doctor_area where cid='"+cid+"' group by area_id;"
    docRows=db.executesql(docRows,as_dict = True)



    rec_Str="select `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level_id`,`level_name`, ff_count.* from(SELECT `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level_id`,`level_name` FROM `sm_level` where is_leaf=1 and depth=3 ) as area_struc ,(Select rep_id, rep_name, area_id, area_name, sum(ord_c) as ord_q, sum(ord_c_uniq) as ord_q_uniq, sum(dcr_c) as dcr_q,sum(dcr_c_uniq) as dcr_q_uniq from (SELECT rep_id,rep_name,area_id,area_name, 0 as ord_c,0 as ord_c_uniq, 0 as dcr_c,0 as dcr_c_uniq FROM ibnsina.sm_rep_area where cid ='IBNSINA' GROUP BY `rep_id`,area_id union Select rep_id, rep_name, area_id, area_name, count(id) as ord_c,count(distinct(client_id)) as ord_c_uniq, 0 as dcr_c,0 as dcr_c_uniq FROM ibnsina.sm_order_head where cid ='IBNSINA' and  order_date >='"+str(date_from)+"' and  order_date <='"+str(date_to)+"' group by rep_id,area_id union Select rep_id,rep_name,route_id,route_name, 0 as ord_c,0 as ord_c_uniq, count(id) as dcr_c,count(distinct(doc_id)) as dcr_c_uniq FROM ibnsina.sm_doctor_visit where cid ='IBNSINA' and visit_date >='"+str(date_from)+"' and  visit_date <='"+str(date_to)+"' group by rep_id,route_id ) as ord_dcr group by rep_id, area_id) as ff_count where ff_count.area_id=area_struc.level_id"

    recStr=db.executesql(rec_Str,as_dict = True)

    myString='From Date :'+str(date_from)+'\n'
    myString=myString+'To Date :'+str(date_to)+'\n\n'

    myString=myString+'Zone ID,Zone Name,Region ID,Region Name,Area ID,Area Name,Submitted By ID,Submitted By Name,Type,Sinavison,Territory ID,Territory Name,Number Of Customer,Number Of Doctor,Order Count,Visited Customer,Dcr Count,Visited Doctor,\n'

    for row in recStr:
        userType=''
        division=''
        level0=str(row['level0'])
        level0_name=str(row['level0_name'])
        level1=str(row['level1'])
        level1_name=str(row['level1_name'])
        level2=str(row['level2'])
        level2_name=str(row['level2_name'])
        rep_id=str(row['rep_id'])
        rep_name=str(row['rep_name'])
        level3=str(row['level_id'])
        level3_name=str(row['level_name'])
        ord_q=str(row['ord_q'])
        ord_q_uniq=str(row['ord_q_uniq'])
        dcr_q=str(row['dcr_q'])
        dcr_q_uniq=str(row['dcr_q_uniq'])

        noOfClient=0
        for m in range(len(clientRows)):
            clientRow=clientRows[m]

            if clientRow['clArea']==level3:
                noOfClient=str(clientRow['noOfClient'])

        noOfDoc=0
        for n in range(len(docRows)):
            docRow=docRows[n]

            if docRow['docArea']==level3:
                noOfDoc=str(docRow['noOfDoc'])


        if rep_id in sup_list:
            userType='Supervisor'
        else:
            userType='Representative'

        if rep_id in sin_list:
            division='Sinavison'
        else:
            division='General'


        myString=myString+str(level0)+','+str(level0_name)+','+str(level1)+','+str(level1_name)+','+str(level2)+','+str(level2_name)+','+str(rep_id)+','+str(rep_name)+','+str(userType)+','+str(division)+','+str(level3)+','+str(level3_name)+','+str(noOfClient)+','+str(noOfDoc)+','+str(ord_q)+','+str(ord_q_uniq)+','+str(dcr_q)+','+str(dcr_q_uniq)+'\n'


    #Save as csv
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=Activity_Status_Download'+str(date_from)+'to'+str(date_to)+'.csv'
    return str(myString)



# def download():
#     cid=session.cid
#     date_from=request.vars.date_from
#     date_to=request.vars.date_to
#
#     sup_list=[]
#     supervisor=db(db.sm_supervisor_level.cid==cid).select(db.sm_supervisor_level.sup_id)
#
#     for i in supervisor:
#         sup_list.append(i.sup_id)
#
#     sin_list=[]
#     rep=db((db.sm_rep.cid==cid)&(db.sm_rep.note=='SIN')).select(db.sm_rep.rep_id)
#     for f in rep:
#         sin_list.append(f.rep_id)
#
#
#     rec_Str="select `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level3`,`level3_name`, ff_count.* from(SELECT `level0`, `level0_name`,`level1`,`level1_name`,`level2`,`level2_name`,`level3`,`level3_name` FROM `sm_level` where is_leaf=1) as area_struc ,(Select rep_id, rep_name, area_id, area_name, sum(ord_c) as ord_q, sum(dcr_c) as dcr_q from (SELECT rep_id,rep_name,area_id,area_name, 0 as ord_c, 0 as dcr_c FROM ibnsina.sm_rep_area where cid ='IBNSINA' GROUP BY `rep_id`,area_id union Select rep_id, rep_name, area_id, area_name, count(id) as ord_c, 0 as dcr_c FROM ibnsina.sm_order_head where cid ='IBNSINA' and  order_date >='"+str(date_from)+"' and  order_date <='"+str(date_to)+"' group by rep_id,area_id union Select rep_id,rep_name,route_id,route_name, 0 as ord_c, count(id) as dcr_c FROM ibnsina.sm_doctor_visit where cid ='IBNSINA' and visit_date >='"+str(date_from)+"' and  visit_date <='"+str(date_to)+"' group by rep_id,route_id ) as ord_dcr group by rep_id, area_id) as ff_count where ff_count.area_id=area_struc.level3"
#     recStr=db.executesql(rec_Str,as_dict = True)
#
#     myString='From Date :'+str(date_from)+'\n'
#     myString=myString+'To Date :'+str(date_to)+'\n\n'
#
#     myString=myString+'Zone ID,Zone Name,Region ID,Region Name,Area ID,Area Name,Submitted By ID,Submitted By Name,Type,Sinavison,Territory ID,Territory Name,Order Count,Dcr Count,\n'
#
#     for row in recStr:
#         userType=''
#         division=''
#         level0=str(row['level0'])
#         level0_name=str(row['level0_name'])
#         level1=str(row['level1'])
#         level1_name=str(row['level1_name'])
#         level2=str(row['level2'])
#         level2_name=str(row['level2_name'])
#         rep_id=str(row['rep_id'])
#         rep_name=str(row['rep_name'])
#         level3=str(row['level3'])
#         level3_name=str(row['level3_name'])
#         ord_q=str(row['ord_q'])
#         dcr_q=str(row['dcr_q'])
#
#         if rep_id in sup_list:
#             userType='Supervisor'
#         else:
#             userType='Representative'
#
#         if rep_id in sin_list:
#             division='Sinavison'
#         else:
#             division='General'
#
#
#         myString=myString+str(level0)+','+str(level0_name)+','+str(level1)+','+str(level1_name)+','+str(level2)+','+str(level2_name)+','+str(rep_id)+','+str(rep_name)+','+str(userType)+','+str(division)+','+str(level3)+','+str(level3_name)+','+str(ord_q)+','+str(dcr_q)+'\n'
#
#
#     #Save as csv
#     import gluon.contenttype
#     response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
#     response.headers['Content-disposition'] = 'attachment; filename=Activity_Status_Download'+str(date_from)+'to'+str(date_to)+'.csv'
#     return str(myString)


#SINRX report==========================
def dcrSummaryZm_sinrx():
    task_id = 'rm_doctor_visit_manage'
    task_id_view = 'rm_doctor_visit_view'
    access_permission = check_role(task_id)
    access_permission_view = check_role(task_id_view)
    if (access_permission == False) and (task_id_view == False):
        session.flash = 'Access is Denied !'
        redirect (URL(c='default', f='home'))

   
    # return 'T' 
    c_id = session.cid
    #c_id = 'IBNSINA'
    response.title='ZM Wise Visit Summary'    
    date_from=request.vars.date_from
    date_to=request.vars.date_to
    depot_id=str(request.vars.depot_id).strip()
    depot_name=str(request.vars.depot_name).strip()    
    
    zm_id=str(request.vars.zm_id).strip()
    zm_name=str(request.vars.zm_name).strip()
    
    rsm_id=str(request.vars.rsm_id).strip()
    rsm_name=str(request.vars.rsm_name).strip()
    fm_id=str(request.vars.fm_id).strip()
    fm_name=str(request.vars.fm_name).strip()
    tr_id=str(request.vars.tr_id).strip()
    tr_name=str(request.vars.tr_name).strip()
    product_id=str(request.vars.product_id).strip()
    product_name=str(request.vars.product_name).strip()
    brand=str(request.vars.brand).strip()
    category=str(request.vars.category).strip()
    mso_id=str(request.vars.mso_id).strip()
    mso_name=str(request.vars.mso_name).strip()
    doc=str(request.vars.doc).strip()
    doc_name=str(request.vars.doc_name).strip()
#     return mso_id
    #date_to_m=datetime.datetime.strptime(str(date_to),'%Y-%m-%d')
    #date_to_m=date_to_m + datetime.timedelta(days = 1)

   
   
    
#     return date_from
    qset = db()
    qset = qset(db.sm_doctor_visit.cid == c_id)
    qset = qset(db.sm_doctor_visit.visit_date >= date_from)
    qset = qset(db.sm_doctor_visit.visit_date <= date_to)
    qset = qset(db.sm_doctor_visit.field2 == 0)

    # qset = qset(db.sm_level.cid == c_id)
    # qset = qset(db.sm_level.is_leaf == 1)
    # qset = qset(db.sm_level.depth == 3)

    # qset = qset(db.sm_doctor_visit.route_id == db.sm_level.level_id)


    
    if (depot_id!=''):
        qset = qset(db.sm_doctor_visit.depot_id == depot_id)

    
    if (zm_id!=''):
        qset = qset(db.sm_doctor_visit.level0_id == zm_id)

    # if (rsm_id!=''):
    #     qset = qset(db.sm_doctor_visit.level1_id == rsm_id)
    # if (fm_id!=''):
    #     qset = qset(db.sm_doctor_visit.level2_id == fm_id)
    # if (tr_id!=''):
    #     qset = qset(db.sm_doctor_visit.route_id == tr_id)
    if (doc!=''):
        qset = qset(db.sm_doctor_visit.doc_id == doc)
#     if (product_id!=''):
#         qset = qset(db.sm_doctor_visit.item_id == product_id)
#     if (brand!=''):
#         qset = qset(db.sm_doctor_visit.item_brand == brand)
#     if (category!=''):
#         qset = qset(db.sm_doctor_visit.item_cat == category)
    
    if (len(mso_id)>3):
        qset = qset(db.sm_doctor_visit.rep_id == mso_id)
    # limitby=(0,50)
    records = qset.select(db.sm_doctor_visit.level0_id,db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_doctor_visit.route_name,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id.count(), orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level0_id)
    # return records
    # records = qset.select(db.sm_doctor_visit.level1_id,db.sm_doctor_visit.level2_id,db.sm_doctor_visit.route_id,db.sm_level.territory_des,db.sm_doctor_visit.rep_id,db.sm_doctor_visit.rep_name,db.sm_doctor_visit.id, orderby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name ,groupby= db.sm_doctor_visit.level1_id|db.sm_doctor_visit.level2_id|db.sm_doctor_visit.route_id|db.sm_doctor_visit.rep_id|db.sm_doctor_visit.rep_name)
    # return db._lastsql
    
    return dict(records=records,date_from=date_from,date_to=date_to,depot_id=depot_id,depot_name=depot_name,zm_id=zm_id,zm_name=zm_name,rsm_id=rsm_id,rsm_name=rsm_name,fm_id=fm_id,fm_name=fm_name,tr_id=tr_id,tr_name=tr_name,brand=brand,category=category,product_id=product_id,product_name=product_name,mso_id=mso_id,mso_name=mso_name,doc=doc,doc_name=doc_name)
