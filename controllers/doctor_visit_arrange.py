# http://127.0.0.1:8000/skf/doctor_visit_arrange/doctor_visit_arrange
#====================== Doctor Visit

from random import randint


#---------------------------- ADD
def doctor_visit_arrange():
    c_id='NAVANA'

    qset=db()
    qset=qset(db.sm_doctor_visit.cid==c_id)
    qset=qset(db.sm_doctor_visit.field2==0)
    qset=qset(db.sm_doctor_visit.giftnsample!='')



    limitby=(0,100)
    records=qset.select(db.sm_doctor_visit.ALL,orderby=db.sm_doctor_visit.id,limitby=limitby)
    # return records
    idList=[]
    showList=''
    sampinsDict={}
    sampinsList=[]
    propinsDict={}
    propinsList=[]
    giftinsDict={}
    giftinsList=[]
    ppminsDict={}
    ppminsList=[]
    for record in records:
        cid =record.cid
        rep_id =record.rep_id
        rep_name=record.rep_name
        doc_id=record.doc_id
        doc_name=record.doc_name
        route_id=record.route_id
        route_name=record.route_name
        depot_id=record.depot_id
        depot_name=''#record.depot_name
        level2_id=record.level2_id
        level2_name=record.level2_name
        level1_id=record.level1_id
        level1_name=record.level1_name
        level0_id=record.level0_id
        level0_name=record.level0_name
        visited_flag=''# record.visited_flag
        visit_sl=record.id
        visit_date=record.visit_date
        status=''
        idList.append(visit_sl) 
        showList=showList+','+str(visit_sl)
        # return record.giftnsample
        if record.giftnsample!='' : 
            dataList=str(record.giftnsample).split('rdsep')
            # return len(dataList)
            if len(dataList)==4:
                propList=str(dataList[0]).split('fdsep')
                giftList=str(dataList[1]).split('fdsep')
                sampleList=str(dataList[2]).split('fdsep')
                ppmList=str(dataList[3]).split('fdsep') 
                
                if str(dataList[0])!='' and len(propList)>0:
                    for m in range(len(propList)):
                        propDataList=str(propList[m]).split(',')
                        if len(propDataList)==2:
                            propitemID=propDataList[0]
                            propitemName=propDataList[1]
                            propinsDict={'cid':c_id,'rep_id':rep_id,'rep_name':rep_name,'doc_id':doc_id,'doc_name':doc_name,'route_id':route_id,'route_name':route_name,'depot_id':depot_id,'depot_name':depot_name,'level2_id':level2_id,'level2_name':level2_name,'level1_id':level1_id,'level1_name':level1_name,'level0_id':level0_id,'level0_name':level0_name, 'visited_flag':visited_flag,'visit_sl':visit_sl,'visit_date':visit_date,'item_id':propitemID,'item_name':propitemName}
                            propinsList.append(propinsDict) 
#                 return 'ghgjg'          
#                 Sample==============
                # return len(sampleList)
                if str(dataList[2])!='' and len(sampleList)>0:
                    for p in range(len(sampleList)):
                        sampitemID=''
                        sampitemName=''
                        sampitemQty=''
                        sampleDataList=str(sampleList[p]).split(',')
                        # return Len(sampleDataList)
                        if len(sampleDataList)==3:
                            sampitemID=sampleDataList[0]
                            sampitemName=sampleDataList[1]
                            sampitemQty=sampleDataList[2]
                            sampinsDict={'cid':c_id,'rep_id':rep_id,'rep_name':rep_name,'doc_id':doc_id,'doc_name':doc_name,'route_id':route_id,'route_name':route_name,'depot_id':depot_id,'depot_name':depot_name,'level2_id':level2_id,'level2_name':level2_name,'level1_id':level1_id,'level1_name':level1_name,'level0_id':level0_id,'level0_name':level0_name, 'visited_flag':visited_flag,'visit_sl':visit_sl,'visit_date':visit_date,'item_id':sampitemID,'item_name':sampitemName,'qty':sampitemQty}
                            sampinsList.append(sampinsDict)  

                if str(dataList[1])!='' and len(giftList)>0:
                    giftitemID=''
                    giftitemName=''
                    for n in range(len(giftList)):
                        giftDataList=str(giftList[n]).split(',')
                        if len(giftDataList)==3:
                            giftitemID=giftDataList[0]
                            giftitemName=giftDataList[1]
                            giftitemQty=giftDataList[2]
                             
 
                            giftinsDict={'cid':c_id,'rep_id':rep_id,'rep_name':rep_name,'doc_id':doc_id,'doc_name':doc_name,'route_id':route_id,'route_name':route_name,'depot_id':depot_id,'depot_name':depot_name,'level2_id':level2_id,'level2_name':level2_name,'level1_id':level1_id,'level1_name':level1_name,'level0_id':level0_id,'level0_name':level0_name, 'visited_flag':visited_flag,'visit_sl':visit_sl,'visit_date':visit_date,'item_id':giftitemID,'item_name':giftitemName,'item_qty':giftitemQty}
                            giftinsList.append(giftinsDict)  
#                             
# #                 ppm==============
                # return dataList[3]
                if str(dataList[3])!='' and len(ppmList)>0:
                    ppmitemID=''
                    ppmitemName=''
                    # return len(ppmList)
                    for q in range(len(ppmList)):
                        ppmDataList=str(ppmList[q]).split(',')
                        # return len(ppmDataList)
                        if len(ppmDataList)==3:
                            ppmitemID=ppmDataList[0]
                            ppmitemName=ppmDataList[1]
                              
                            ppminsDict={'cid':c_id,'rep_id':rep_id,'rep_name':rep_name,'doc_id':doc_id,'doc_name':doc_name,'route_id':route_id,'route_name':route_name,'depot_id':depot_id,'depot_name':depot_name,'level2_id':level2_id,'level2_name':level2_name,'level1_id':level1_id,'level1_name':level1_name,'level0_id':level0_id,'level0_name':level0_name, 'visited_flag':visited_flag,'visit_sl':visit_sl,'visit_date':visit_date,'item_id':ppmitemID,'item_name':ppmitemName}
                            ppminsList.append(ppminsDict)  
                            
    # return len(ppminsList)
    if records:
        if len(propinsList) > 0:
            inProp=db.sm_doc_visit_prop.bulk_insert(propinsList) 
            records_retS="update sm_doc_visit_prop, sm_item  set  sm_doc_visit_prop.item_brand=sm_item.manufacturer,sm_doc_visit_prop.item_cat=sm_item.category_id  WHERE sm_doc_visit_prop.cid = sm_item.cid AND sm_doc_visit_prop.item_id = sm_item.item_id  AND     sm_doc_visit_prop.item_brand='';"
            records_ret=db.executesql(records_retS)

        if len(sampinsList) >0:
            inSample=db.sm_doc_visit_sample.bulk_insert(sampinsList) 
            records_retS="update sm_doc_visit_sample, sm_item  set  sm_doc_visit_sample.item_brand=sm_item.manufacturer,sm_doc_visit_sample.item_cat=sm_item.category_id  WHERE sm_doc_visit_sample.cid = sm_item.cid AND sm_doc_visit_sample.item_id = sm_item.item_id  AND     sm_doc_visit_sample.item_brand='';"
            records_ret=db.executesql(records_retS)
            records_retS="update sm_doc_visit_sample, sm_level  set  sm_doc_visit_sample.trDesc=sm_level.territory_des WHERE sm_doc_visit_sample.cid = sm_level.cid AND sm_doc_visit_sample.route_id = sm_level.level_id  AND     sm_level.is_leaf=1 AND     sm_doc_visit_sample.trDesc='';"
            records_ret=db.executesql(records_retS)

        if len(giftinsList) > 0:
            inGift=db.sm_doc_visit_gift.bulk_insert(giftinsList) 

        planRecords=db((db.sm_doctor_visit.cid==c_id)& (db.sm_doctor_visit.id.belongs(idList)) ).update(field2=1)
        
        
        
         
        return 'SUCCESS'                    
    
# http://127.0.0.1:8000/skf/doctor_visit_arrange/doctor_visit_arrange_SP_tr 
# a002.businesssolutionapps.com/skf/doctor_visit_arrange/doctor_visit_arrange_SP_tr 
def doctor_visit_arrange_SP_tr():     
    c_id='NAVANA'

    records_S="update sm_doctor_visit, sm_level  set  sm_doctor_visit.special_territory_code=sm_level.special_territory_code  WHERE sm_doctor_visit.cid='"+c_id +"' and sm_doctor_visit.special_territory_code='' and sm_doctor_visit.field1=1 & sm_level.cid='"+c_id+"' and  sm_level.is_leaf=1 and sm_level.special_territory_code!='' and sm_level.level_id=sm_doctor_visit.route_id;"
#     return records_S
    records=db.executesql(records_S)
    records_S1="update sm_doctor_visit, sm_level  set  sm_doctor_visit.special_fm_code=sm_level.level2,sm_doctor_visit.special_rsm_code=sm_level.level1,sm_doctor_visit.field1=2  WHERE sm_doctor_visit.cid='"+c_id +"' and sm_doctor_visit.special_territory_code!='' and sm_doctor_visit.field1=1 & sm_level.cid='"+c_id+"' and  sm_level.is_leaf=1 and sm_level.level_id=sm_doctor_visit.special_territory_code;"
#     return records_S1
    recordsS1=db.executesql(records_S)

    return "SUCCESS"






# ==============================PPM=================================        
def doctor_visit_arrangePPM():
    c_id='NAVANA'
    
    qset=db()
    qset=qset(db.sm_doctor_visit.cid==c_id)
    qset=qset(db.sm_doctor_visit.field2==1)
    qset=qset(db.sm_doctor_visit.giftnsample!='')



    limitby=(0,100)
    records=qset.select(db.sm_doctor_visit.ALL,orderby=db.sm_doctor_visit.id,limitby=limitby)
#     return records
    idList=[]
    showList=''
    sampinsDict={}
    sampinsList=[]
    propinsDict={}
    propinsList=[]
    giftinsDict={}
    giftinsList=[]
    ppminsDict={}
    ppminsList=[]
#     return records
    for record in records:
        cid =record.cid
        rep_id =record.rep_id
        rep_name=record.rep_name
        doc_id=record.doc_id
        doc_name=record.doc_name
        route_id=record.route_id
        route_name=record.route_name
        depot_id=record.depot_id
        depot_name=''#record.depot_name
        level2_id=record.level2_id
        level2_name=record.level2_name
        level1_id=record.level1_id
        level1_name=record.level1_name
        level0_id=record.level0_id
        level0_name=record.level0_name
        visited_flag=''# record.visited_flag
        visit_sl=record.id
        visit_date=record.visit_date
        status=''
        idList.append(visit_sl) 
        showList=showList+','+str(visit_sl)
        if record.giftnsample!='' : 
            dataList=str(record.giftnsample).split('rdsep')
            if len(dataList)==4:
                propList=str(dataList[0]).split('fdsep')
                giftList=str(dataList[1]).split('fdsep')
                sampleList=str(dataList[2]).split('fdsep')
                ppmList=str(dataList[3]).split('fdsep')
                        
# #                 ppm==============
                
                if str(dataList[3])!='' and len(ppmList)>0:
                    ppmitemID=''
                    ppmitemName=''
                    # return range(len(ppmList))
                    for q in range(len(ppmList)):
                        ppmDataList=str(ppmList[q]).split(',')
                        if len(ppmDataList)==3:
                            ppmitemID=ppmDataList[0]
                            ppmitemName=ppmDataList[1]
                            ppmitemQty=ppmDataList[2]

                            records_ins="insert into sm_doc_visit_ppm (cid,rep_id,rep_name,doc_id,doc_name,route_id,route_name,depot_id,depot_name,level2_id,level2_name,level1_id,level1_name,level0_id,level0_name, visited_flag,visit_sl,visit_date,item_id,item_name,item_qty)  values ('"+str(c_id)+"','"+str(rep_id)+"','"+str(rep_name)+"','"+str(doc_id)+"','"+str(doc_name)+"','"+str(route_id)+"','"+str(route_name)+"','"+str(depot_id)+"','"+str(depot_name)+"','"+str(level2_id)+"','"+str(level2_name)+"','"+str(level1_id)+"','"+str(level1_name)+"','"+str(level0_id)+"','"+str(level0_name)+"','"+str(visited_flag)+"','"+str(visit_sl)+"','"+str(visit_date)+"','"+str(ppmitemID)+"','"+str(ppmitemName)+"','"+str(ppmitemQty)+"')";
                            # return records_ins
                            records=db.executesql(records_ins)  
                            
            
        planRecords=db((db.sm_doctor_visit.cid==c_id)& (db.sm_doctor_visit.id.belongs(idList)) ).update(field2=2)
        
        
        
         
        return 'SUCCESS'           