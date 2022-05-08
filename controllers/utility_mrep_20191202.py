#level Transfer

#============================= 
def utility():
    task_id = 'rm_utility_manage'
    access_permission = check_role(task_id)
    if (access_permission == False):
        session.flash='Access is Denied !'
        redirect (URL('default','home'))
    
    response.title='Batch Process'
    c_id=session.cid
    
    #--------------------- 
    depot_transfer='NO'
    depot_settings_check=db((db.sm_settings.cid==c_id) & (db.sm_settings.s_key=='DEPOT_TRANSFER')).select(db.sm_settings.s_value,limitby=(0,1))
    for depot_settings_check in depot_settings_check :
        depot_transfer=depot_settings_check.s_value 
        
    #------------------ Show Last ID    
    showLastIDType=''
    showLastID=''
    
    #----------
    btn_show_lastID=request.vars.btn_show_lastID
    
    #---------------------
    if btn_show_lastID:
        showLastIDType=str(request.vars.showLastIDType).strip()
        if showLastIDType=='':
            response.title='Select Type'
        else:
            if showLastIDType=='DOCTOR':
                doctorRows=db(db.sm_doctor.cid==c_id).select(db.sm_doctor.doc_id,orderby=~db.sm_doctor.doc_id,limitby=(0,1))
                if doctorRows:
                    showLastID=doctorRows[0].doc_id
                    
            elif showLastIDType=='RETAILER':
                clientRows=db(db.sm_client.cid==c_id).select(db.sm_client.client_id,orderby=~db.sm_client.client_id,limitby=(0,1))
                if clientRows:
                    showLastID=clientRows[0].client_id
            
            elif showLastIDType=='REP':
                repRows=db((db.sm_rep.cid==c_id)&(db.sm_rep.user_type=='rep')).select(db.sm_rep.rep_id,orderby=~db.sm_rep.rep_id,limitby=(0,1))
                if repRows:
                    showLastID=repRows[0].rep_id
            
            elif showLastIDType=='SUPERVISOR':
                repRows=db((db.sm_rep.cid==c_id)&(db.sm_rep.user_type=='sup')).select(db.sm_rep.rep_id,orderby=~db.sm_rep.rep_id,limitby=(0,1))
                if repRows:
                    showLastID=repRows[0].rep_id
                    
    return dict(depot_transfer=depot_transfer,showLastIDType=showLastIDType,showLastID=showLastID,access_permission=access_permission)


def utility_settings():
    task_id = 'rm_utility_manage'
    access_permission = check_role(task_id)
    if (access_permission == False):
        session.flash='Access is Denied !'
        redirect (URL('default','home'))
    
    response.title='Utility'
    c_id=session.cid
    
    #--------------------- 
    depot_transfer='NO'
    depot_settings_check=db((db.sm_settings.cid==c_id) & (db.sm_settings.s_key=='DEPOT_TRANSFER')).select(db.sm_settings.s_value,limitby=(0,1))
    for depot_settings_check in depot_settings_check :
        depot_transfer=depot_settings_check.s_value 
        break
        
    #------------------ Show Last ID    
    showLastIDType=''
    showLastID=''
    
    #----------
    btn_show_lastID=request.vars.btn_show_lastID
    btn_item_batch_release=request.vars.btn_item_batch_release
    
    btn_update_block_qty=request.vars.btn_update_block_qty
    
    #---------------------
    if btn_show_lastID:
        showLastIDType=str(request.vars.showLastIDType).strip()
        if showLastIDType=='':
            response.title='Select Type'
        else:
            if showLastIDType=='DOCTOR':
                doctorRows=db(db.sm_doctor.cid==c_id).select(db.sm_doctor.doc_id,orderby=~db.sm_doctor.doc_id,limitby=(0,1))
                if doctorRows:
                    showLastID=doctorRows[0].doc_id
                    
            elif showLastIDType=='RETAILER':
                clientRows=db(db.sm_client.cid==c_id).select(db.sm_client.client_id,orderby=~db.sm_client.client_id,limitby=(0,1))
                if clientRows:
                    showLastID=clientRows[0].client_id
            
            elif showLastIDType=='REP':
                repRows=db((db.sm_rep.cid==c_id)&(db.sm_rep.user_type=='rep')).select(db.sm_rep.rep_id,orderby=~db.sm_rep.rep_id,limitby=(0,1))
                if repRows:
                    showLastID=repRows[0].rep_id
            
            elif showLastIDType=='SUPERVISOR':
                repRows=db((db.sm_rep.cid==c_id)&(db.sm_rep.user_type=='sup')).select(db.sm_rep.rep_id,orderby=~db.sm_rep.rep_id,limitby=(0,1))
                if repRows:
                    showLastID=repRows[0].rep_id
    
    elif btn_item_batch_release:
        depot_id=str(request.vars.release_depot_id).strip().upper().split('|')[0]
        store_id=str(request.vars.release_store_id).strip().upper().split('|')[0]
        item_id=str(request.vars.release_item_id).strip().upper().split('|')[0]
        
        if depot_id=='' or store_id=='' or item_id=='':
            response.flash='Required Branch ID, Store ID and Item ID'
        else:
            depotRows=db((db.sm_depot.cid==c_id)&(db.sm_depot.depot_id==depot_id)).select(db.sm_depot.depot_id,limitby=(0,1))
            if not depotRows:
                response.flash='Invalid Depot ID'            
            else:
                storeRows=db((db.sm_depot_store.cid==c_id)&(db.sm_depot_store.depot_id==depot_id)&(db.sm_depot_store.store_id==store_id)).select(db.sm_depot_store.store_id,limitby=(0,1))
                if not storeRows:
                    response.flash='Invalid Store ID of the Branch'            
                else:
                    itemRows=db((db.sm_item.cid==c_id)&(db.sm_item.item_id==item_id)).select(db.sm_item.item_id,limitby=(0,1))
                    if not itemRows:
                        response.flash='Invalid Item ID'            
                    else:
                        redirect (URL('item_release',vars=dict(depotId=depot_id,storeId=store_id,itemId=item_id)))
    
    elif btn_update_block_qty:
        depot_id=str(request.vars.block_depot_id).strip().upper().split('|')[0]
        store_id=str(request.vars.block_store_id).strip().upper().split('|')[0]
        item_id=str(request.vars.block_item_id).strip().upper().split('|')[0]
        batch_id=str(request.vars.block_batch_id)
        
        if depot_id=='' or store_id=='' or item_id=='' or batch_id=='':
            response.flash='Required Branch ID, Store ID and Item ID and Batch ID'
        else:
            depotRows=db((db.sm_depot.cid==c_id)&(db.sm_depot.depot_id==depot_id)).select(db.sm_depot.depot_id,limitby=(0,1))
            if not depotRows:
                response.flash='Invalid Depot ID'            
            else:
                storeRows=db((db.sm_depot_store.cid==c_id)&(db.sm_depot_store.depot_id==depot_id)&(db.sm_depot_store.store_id==store_id)).select(db.sm_depot_store.store_id,limitby=(0,1))
                if not storeRows:
                    response.flash='Invalid Store ID of the Branch'            
                else:
                    itemRows=db((db.sm_item.cid==c_id)&(db.sm_item.item_id==item_id)).select(db.sm_item.item_id,limitby=(0,1))
                    if not itemRows:
                        response.flash='Invalid Item ID'            
                    else:
                        itemBatchRows=db((db.sm_item_batch.cid==c_id)&(db.sm_item_batch.item_id==item_id)&(db.sm_item_batch.batch_id==batch_id)).select(db.sm_item_batch.batch_id,limitby=(0,1))
                        if not itemBatchRows:
                            response.flash='Invalid Batch ID'            
                        else:
                            invQty=0
                            invBonusQty=0
                            totalInvQty=0
                            stockBlockQty=0                
                            invRows=db((db.sm_invoice.cid==c_id)&(db.sm_invoice.depot_id==depot_id)&(db.sm_invoice.store_id==store_id)&(db.sm_invoice.item_id==item_id)&(db.sm_invoice.batch_id==batch_id)&(db.sm_invoice.status=='Submitted')).select(db.sm_invoice.quantity.sum(),db.sm_invoice.bonus_qty.sum(),groupby=db.sm_invoice.depot_id|db.sm_invoice.store_id|db.sm_invoice.item_id|db.sm_invoice.batch_id)
                            
                            for invRow in invRows:
                                invQty=invRow[db.sm_invoice.quantity.sum()]
                                invBonusQty=invRow[db.sm_invoice.bonus_qty.sum()]
                                totalInvQty=invQty+invBonusQty
                            
                            blockQtyRows=db((db.sm_depot_stock_balance.cid==c_id)&(db.sm_depot_stock_balance.depot_id==depot_id)&(db.sm_depot_stock_balance.store_id==store_id)&(db.sm_depot_stock_balance.item_id==item_id)&(db.sm_depot_stock_balance.batch_id==batch_id)).select(db.sm_depot_stock_balance.id,db.sm_depot_stock_balance.block_qty,limitby=(0,1))
                            if blockQtyRows:
                                stockBlockQty=blockQtyRows[0].block_qty
                            
                            if totalInvQty==0 and stockBlockQty>0:
                                blockQtyRows[0].update_record(block_qty=0)
                            else:
                                blockQtyRows[0].update_record(block_qty=totalInvQty)
                            
                            response.flash='Update successfully. Item ID:' +str(item_id)+',  Batch ID: ' +str(batch_id)   
                            
                        
    return dict(depot_transfer=depot_transfer,showLastIDType=showLastIDType,showLastID=showLastID,access_permission=access_permission)



    
def item_release():
    task_id = 'rm_utility_manage'
    access_permission = check_role(task_id)
    if (access_permission == False):
        session.flash='Access is Denied !'
        redirect (URL('default','home'))
        
    response.title='Item Release'
    cid=session.cid
    
    depotId=str(request.vars.depotId).strip().upper().split('|')[0]
    storeId=str(request.vars.storeId).strip().upper().split('|')[0]
    itemId=str(request.vars.itemId).strip().upper().split('|')[0]
    
    depotName=''
    storeName=''
    itemName=''
    depotRows=db((db.sm_depot.cid==cid)&(db.sm_depot.depot_id==depotId)).select(db.sm_depot.name,limitby=(0,1))
    if depotRows:
        depotName=depotRows[0].name
    storeRows=db((db.sm_depot_store.cid==cid)&(db.sm_depot_store.depot_id==depotId)&(db.sm_depot_store.store_id==storeId)).select(db.sm_depot_store.store_name,limitby=(0,1))
    if storeRows:
        storeName=storeRows[0].store_name
    itemRows=db((db.sm_item.cid==cid)&(db.sm_item.item_id==itemId)).select(db.sm_item.name,limitby=(0,1))
    if itemRows:
        itemName=itemRows[0].name
        
    #----------------
    btn_update=request.vars.btn_update
    if btn_update:
        check_update=request.vars.check_update
        batchId=request.vars.batchId
        
        try:
            rowid=int(request.vars.rowid)
        except:
            rowid=0
            
        if check_update!='YES':
            response.flash='Required Checked Confirmation'
        else:
            if rowid==0:
                response.flash='Invalid Request'
            else:
                invQty=0
                invBonusQty=0
                totalInvQty=0                
                invRows=db((db.sm_invoice.cid==cid)&(db.sm_invoice.depot_id==depotId)&(db.sm_invoice.store_id==storeId)&(db.sm_invoice.item_id==itemId)&(db.sm_invoice.batch_id==batchId)&(db.sm_invoice.status=='Submitted')).select(db.sm_invoice.quantity.sum(),db.sm_invoice.bonus_qty.sum(),groupby=db.sm_invoice.batch_id)
                
                for invRow in invRows:
                    invQty=invRow[db.sm_invoice.quantity.sum()]
                    invBonusQty=invRow[db.sm_invoice.bonus_qty.sum()]
                    totalInvQty=invQty+invBonusQty
                
                db((db.sm_depot_stock_balance.cid==cid)&(db.sm_depot_stock_balance.depot_id==depotId)&(db.sm_depot_stock_balance.store_id==storeId)&(db.sm_depot_stock_balance.item_id==itemId)&(db.sm_depot_stock_balance.batch_id==batchId)&(db.sm_depot_stock_balance.id==rowid)).update(block_qty=totalInvQty)
                
                response.flash='Released successfully. Batch ID: ' +str(batchId)     
                
    #----------------------
    qset=db()
    qset=qset(db.sm_depot_stock_balance.cid==cid)
    qset=qset(db.sm_depot_stock_balance.depot_id==depotId)
    qset=qset(db.sm_depot_stock_balance.store_id==storeId)
    qset=qset(db.sm_depot_stock_balance.item_id==itemId)
    
    records=qset.select(db.sm_depot_stock_balance.ALL,orderby=db.sm_depot_stock_balance.batch_id)
    
    return dict(records=records,depotId=depotId,storeId=storeId,itemId=itemId,depotName=depotName,storeName=storeName,itemName=itemName)


def level_transfer():
    #----------
    response.title='Level Transfer'
    
    #----------
    btn_transfer=request.vars.btn_transfer
    checkbox=request.vars.checkbox
    if btn_transfer and checkbox==None:
        session.flash='Please Confirm First'  
        
    if btn_transfer and checkbox!=None:
        level_id=str(request.vars.level_id).strip().upper()
        under_level_id=str(request.vars.under_level_id).strip().upper()
        
        if ((level_id != '') and (under_level_id != '')):
            level_check=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id==level_id)).select(db.sm_level.ALL,limitby=(0,1))
            under_level_check=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id==under_level_id)).select(db.sm_level.ALL,limitby=(0,1))
#             return under_level_check
            if (under_level_check):
                under_level_name=under_level_check[0].level_name
                
            if (level_check):
                level_name=level_check[0].level_name
                
            if (level_check and under_level_check):
                for level_check in level_check :
                    depth_level=level_check.depth
                    
                    level0_level=level_check.level0
                    level1_level=level_check.level1 
                    level2_level=level_check.level2 
                    level3_level=level_check.level3 
                    level4_level=level_check.level4  
                    level5_level=level_check.level5 
                    level6_level=level_check.level6 
                    level7_level=level_check.level7 
                    level8_level=level_check.level8
                    
                    level0_level_name=level_check.level0_name
                    level1_level_name=level_check.level1_name
                    level2_level_name=level_check.level2_name
                    level3_level_name=level_check.level3_name
                    level4_level_name=level_check.level4_name 
                    level5_level_name=level_check.level5_name
                    level6_level_name=level_check.level6_name
                    level7_level_name=level_check.level7_name
                    level8_level_name=level_check.level8_name 
                    break 
                    
                for under_level_check in under_level_check :
                    depth_under_level=under_level_check.depth
                    level0_under_level=under_level_check.level0
                    level1_under_level=under_level_check.level1 
                    level2_under_level=under_level_check.level2 
                    level3_under_level=under_level_check.level3 
                    level4_under_level=under_level_check.level4  
                    level5_under_level=under_level_check.level5 
                    level6_under_level=under_level_check.level6 
                    level7_under_level=under_level_check.level7 
                    level8_under_level=under_level_check.level8 
                    
                    level0_under_level_name=under_level_check.level0_name
                    level1_under_level_name=under_level_check.level1_name 
                    level2_under_level_name=under_level_check.level2_name 
                    level3_under_level_name=under_level_check.level3_name 
                    level4_under_level_name=under_level_check.level4_name  
                    level5_under_level_name=under_level_check.level5_name 
                    level6_under_level_name=under_level_check.level6_name 
                    level7_under_level_name=under_level_check.level7_name 
                    level8_under_level_name=under_level_check.level8_name
                    break
#                 return level2_under_level    
                if (int(depth_level)==int(depth_under_level)+1):
                    if (depth_level>0):
                        if (depth_level==1):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,parent_level_name=under_level_name,level0_name=level0_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level1==level_id) ).update(level0=level0_under_level,level0_name=level0_under_level_name)
                            
                        elif (depth_level==2):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level2==level_id) ).update(level0=level0_under_level,level1=level1_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name)
                            
                        elif (depth_level==3):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level3==level_id) ).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name)
                                
                        elif (depth_level==4):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level4 == level_id)).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name)
                            
                        elif (depth_level==5):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level5 == level_id)).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name)
                            
                        elif (depth_level==6):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level6 == level_id)).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name)   
                        
                        elif (depth_level==7):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level,level6=level6_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name,level6_name=level6_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level7 == level_id)).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level,level6=level6_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name,level6_name=level6_under_level_name)    
                        elif (depth_level==8):
                            parent_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level_id == level_id)).update(parent_level_id=under_level_id,level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level,level6=level6_under_level,level7=level7_under_level, parent_level_name=under_level_name,level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name,level6_name=level6_under_level_name,level7_name=level7_under_level_name)
                            child_update=db((db.sm_level.cid==session.cid) & (db.sm_level.level8 == level_id)).update(level0=level0_under_level,level1=level1_under_level,level2=level2_under_level,level3=level3_under_level,level4=level4_under_level,level5=level5_under_level,level6=level6_under_level,level7=level7_under_level, level0_name=level0_under_level_name,level1_name=level1_under_level_name,level2_name=level2_under_level_name,level3_name=level3_under_level_name,level4_name=level4_under_level_name,level5_name=level5_under_level_name,level6_name=level6_under_level_name,level7_name=level7_under_level_name)
                        
                        session.flash='Transfered Successfully'    
                    else:
                        session.flash='Please Check Level Properly'
                else:
                     session.flash='Please Check Level Properly'    
            else:
                session.flash='Please Check Level Properly'
        else:
            session.flash='Please Check Level Properly'          
    else:
        pass                
    
    redirect (URL('utility_mrep','utility_settings'))
    
def depot_transfer(): 
    
    #----------
    response.title='Depot Transfer'
    
    #----------
    btn_transfer_depot=request.vars.btn_transfer_depot
    checkbox=request.vars.checkbox
    if btn_transfer_depot and checkbox==None:
        session.flash='Please Confirm First' 
        redirect (URL('utility_mrep','utility')) 
#    return 'nadira'    
    if btn_transfer_depot and checkbox!=None:
#        return checkbox
        depot_id=str(request.vars.depot_id).strip().upper()
        transfer_with_depot_id=str(request.vars.transfer_with_depot_id).strip().upper()
#        return 'level_id'
        if ((depot_id != '') and (transfer_with_depot_id != '')):
            if (depot_id==transfer_with_depot_id):
                session.flash='Please choose differnt depot ID for Transfer' 
                redirect (URL('utility_mrep','utility')) 
            depot_id_check=db((db.sm_depot.cid==session.cid) & (db.sm_depot.depot_id==depot_id)).select(db.sm_depot.depot_category,limitby=(0,1))
            transfer_with_depot_id_check=db((db.sm_depot.cid==session.cid) & (db.sm_depot.depot_id==transfer_with_depot_id)).select(db.sm_depot.depot_category,limitby=(0,1))
#            return db._lastsql
            
            if (depot_id_check and transfer_with_depot_id_check):
                for depot_id_check in depot_id_check :
                    depot_id_check_catagory=depot_id_check.depot_category  
                    
                for transfer_with_depot_id_check in transfer_with_depot_id_check :
                    transfer_with_depot_id_check_catagory=transfer_with_depot_id_check.depot_category    
                
                if (depot_id_check_catagory == transfer_with_depot_id_check_catagory):  
                    # update client,rep,rep_area,level,depotsettings,--stockbalance    
                      client_update=db((db.sm_client.cid==session.cid) & (db.sm_client.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
                      rep_update=db((db.sm_rep.cid==session.cid) & (db.sm_rep.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
                      #rep_area_update=db((db.sm_rep_area.cid==session.cid) & (db.sm_rep_area.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
#                      return db._lastsql
                      
                      level_update=db((db.sm_level.cid==session.cid) & (db.sm_level.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
                      
                      # Update depot settings from and to
                      depot_settings_update=db((db.sm_depot_settings.cid==session.cid) & (db.sm_depot_settings.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
                      depot_settings_update=db((db.sm_depot_settings.cid==session.cid) & (db.sm_depot_settings.depot_id_from_to == depot_id)).update(depot_id_from_to=transfer_with_depot_id)
                      
                      # sm_depot_stock_balance
                      depot_settings_check=db((db.sm_settings.cid==session.cid) & (db.sm_settings.s_key=='STKTRANS_N_DPTTRANS')).select(db.sm_settings.s_value,limitby=(0,1))
                      depot_stock_transfer='NO'
                      for depot_settings_check in depot_settings_check :
                          depot_stock_transfer=depot_settings_check.s_value
                      if (depot_stock_transfer=='YES'):
                          depot_stock_balance_update=db((db.sm_depot_stock_balance.cid==session.cid) & (db.sm_depot_stock_balance.depot_id == depot_id)).update(depot_id=transfer_with_depot_id)
                      session.flash='Depot Transfered Successfully'    
                    
                else:
                     session.flash='Please Select Same Catagory Depot'    
            else:
                session.flash='Please Check Depot Properly'
        else:
            session.flash='Depot or Transfer Depot can not be blanked'          
    else:
        pass                
    
#    return 'nadira'
    redirect (URL('utility_mrep','utility'))    




#Not Used. using function at inbox
def sms_resubmit():
    import urllib
    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility'))
    
    c_id=session.cid
    
    search_date=SQLFORM(db.sm_search_date,
                  fields=['from_date']           
                  )
    
    smspath=''
    settRow=db((db.sm_settings.cid==c_id)&(db.sm_settings.s_key=='SMS_PATH')).select(db.sm_settings.s_value,limitby=(0,1))
    if not settRow:
        session.flash='Required settings'
        redirect(URL('utility'))
    else:
        smspath=str(settRow[0].s_value)
    
    #-------
    hostName=request.env.http_host
    appName=request.application
    baseUrl='http://'+str(hostName)+'/'+str(appName)+'/'+smspath
    #-----
    
    btn_resubmit=request.vars.btn_resubmit
    if btn_resubmit:        
        smsDate=request.vars.from_date
        returnflag='Yes'
        smsMobile=request.vars.smsMobile
        smsText=request.vars.smsText
        
        validDate=True
        try:
            smsdate= datetime.datetime.strptime(str(smsDate),'%Y-%m-%d %H:%M:%S')
        except:
            validDate=False
        
        if (smsDate=='' or smsMobile=='' or smsText==''):
            response.flash='Required Value'
        else:
            if validDate==False:
                response.flash='Invalid Date'
            else:
                validMobile=True
                try:
                    smsMobile= int(smsMobile)
                except:
                    validMobile=False
                
                if validMobile==False:
                    response.flash='Invalid Mobile'
                else:
                    mobileRow=db((db.sm_comp_mobile.cid==c_id)&(db.sm_comp_mobile.mobile_no==smsMobile)).select(db.sm_comp_mobile.mobile_no,limitby=(0,1))
                    if not mobileRow:
                        response.flash='Invalid Mobile'
                    else:                                    
                        urlPath=str(baseUrl) +'&smsdate='+str(smsdate)+'&returnflag='+str(returnflag)+ '&mob='+str(smsMobile)+'&cid='+str(c_id)+'&msg=.'+str(smsText)
                        
#                        return urlPath
                        
                        urlRes = urllib.urlopen(urlPath).read()                        
                        if urlRes!='':
                            response.flash=urlRes[5:]
                        else:
                            response.flash='Error in process'
                            
    return dict(search_date=search_date)

#http://127.0.0.1:8000/skf/utility_mrep/set_product_list
#http://c003.cloudapp.net/skf/utility_mrep/set_product_list
#=======================Set Product Liist

def set_product_list():
    
    cid = 'NOVIVO'
    #     Special rate==================
    itemBonusList = []
    itemBonusList_str = []
    itemBonusRows = db((db.sm_promo_product_bonus_products.cid == cid) & (db.sm_promo_product_bonus_products.status == 'ACTIVE') & (db.sm_promo_product_bonus_products.from_date <= current_date)  & (db.sm_promo_product_bonus_products.to_date >= current_date) ).select(db.sm_promo_product_bonus_products.product_id,db.sm_promo_product_bonus_products.product_name, db.sm_promo_product_bonus_products.note, orderby=db.sm_promo_product_bonus_products.product_name)
    for itemBonusRows in itemBonusRows:
        product_id = itemBonusRows.product_id       
        note= itemBonusRows.note
        itemBonusList.append(str(product_id))
        itemBonusList_str.append(note)
        
#     Special rate==================
    itemSpecialList = []
    itemSpecialList_str = []
    itemSpecialRows = db((db.sm_promo_special_rate.cid == cid) & (db.sm_promo_special_rate.status == 'ACTIVE')  & (db.sm_promo_special_rate.from_date <= current_date)  & (db.sm_promo_special_rate.to_date >= current_date) ).select(db.sm_promo_special_rate.product_id,db.sm_promo_special_rate.product_name, db.sm_promo_special_rate.special_rate_tp, db.sm_promo_special_rate.special_rate_vat, db.sm_promo_special_rate.min_qty, orderby=db.sm_promo_special_rate.product_name)
    for itemSpecialRows in itemSpecialRows:
        
        product_id = itemSpecialRows.product_id       
        special_rate_tp = itemSpecialRows.special_rate_tp
        special_rate_vat = itemSpecialRows.special_rate_vat
        min_qty = itemSpecialRows.min_qty
#         return min_qty
        total= float(special_rate_tp)+float(special_rate_vat)
#         return total
        itemSpecialList.append(str(product_id))
#         itemSpecialList_str.append('Special:Min '+str(min_qty)+' TP ' +str(special_rate_tp)+' Vat'+str(special_rate_vat)+'='+str(total))
        itemSpecialList_str.append('Special:Min '+str(min_qty)+' CPP ' +str(total))
         

#     Flat rate==================
    itemFlatList = []
    itemFlatList_str = []
    itemFlatRows = db((db.sm_promo_flat_rate.cid == cid)  & (db.sm_promo_flat_rate.status == 'ACTIVE') & (db.sm_promo_flat_rate.from_date <= current_date)  & (db.sm_promo_flat_rate.to_date >= current_date) ).select(db.sm_promo_flat_rate.product_id,db.sm_promo_flat_rate.product_name, db.sm_promo_flat_rate.min_qty, db.sm_promo_flat_rate.flat_rate,db.sm_promo_flat_rate.vat, orderby=db.sm_promo_flat_rate.product_name)
    for itemFlatRows in itemFlatRows:
        product_id = itemFlatRows.product_id
        product_name = itemFlatRows.product_name
        flat_rate = float(itemFlatRows.flat_rate)+float(itemFlatRows.vat)
        
        min_qty = itemFlatRows.min_qty      
        itemFlatList.append(str(product_id))
        itemFlatList_str.append('Flat:Min '+str(min_qty)+' Rate '+str(flat_rate))
    
    
    
    productStr = ''
    productRows = db((db.sm_item.cid == cid) & (db.sm_item.status == 'ACTIVE') & (db.sm_item.category_id != 'BONUS')).select(db.sm_item.item_id, db.sm_item.name, db.sm_item.price, db.sm_item.vat_amt, orderby=db.sm_item.name)
    
    for productRow in productRows:
        item_id = productRow.item_id       
        name = str(productRow.name).replace(".","").replace(",","")
        price_amt = productRow.price
        vat_amt=productRow.vat_amt
        price_get=float(price_amt)+float(vat_amt)
        price=round(price_get, 2)
        
#         recRow=''
        recRow_str=''
        
        
#         ===========Bonus Rate
        recRowBonus=''
        recRowBonus_str=''
        if [s for s in itemBonusList if item_id in s]:
            index_element = itemBonusList.index(item_id)           
            recRowBonus=itemBonusList[index_element]
            recRowBonus_str=itemBonusList_str[index_element]
            recRowBonus_str=str(recRowBonus_str)+'&nbsp;'
#             return recRowBonus_str
#         ===========Special Rate
        recRowSpecial=''
        recRowSpecial_str=''
        if [s for s in itemSpecialList if item_id in s]:
            index_element = itemSpecialList.index(item_id)           
            recRowSpecial=itemSpecialList[index_element]
            recRowSpecial_str=itemSpecialList_str[index_element]
            recRowSpecial_str=str(recRowSpecial_str)+'&nbsp;'
        
#             ============Flat Rate
        recRowFlat=''
        recRowFlat_str=''
        if [f for f in itemFlatList if item_id in f]:
            index_element = itemFlatList.index(item_id)                        
            recRowFlat=itemFlatList[index_element]
            recRowFlat_str=itemFlatList_str[index_element]
            recRowFlat_str=str(recRowFlat_str)+'&nbsp;'


#             ============Product Bonus
        
        recRowFlat=''
        recRowFlat_str=''
        if [f for f in itemFlatList if item_id in f]:
            index_element = itemFlatList.index(item_id)                        
            recRowFlat=itemFlatList[index_element]
            recRowFlat_str=itemFlatList_str[index_element]
            recRowFlat_str=str(recRowFlat_str)+'&nbsp;'
            
        recRow_str= recRowBonus_str+recRowSpecial_str+ recRowFlat_str     
        
        if productStr == '':
            productStr = str(item_id) + '<fd>' + str(name) + '<fd>' + str(price) + '<fd>' + str(recRow_str)+'<fd>'+str(vat_amt)
        else:
            productStr += '<rd>' + str(item_id) + '<fd>' + str(name) + '<fd>' + str(price) + '<fd>' + str(recRow_str)+'<fd>'+str(vat_amt)
     
#     return productStr
    item_update=db((db.sm_company_settings.cid==cid)).update(field1=productStr)
    
    if (item_update>0):
        session.flash='Successfully Prepared'        
    else:
        session.flash='Error in process'
        
    redirect (URL('utility_mrep','utility_settings'))
    
#------------- clean function call
#Only this function is used to clean data
def branch_data_clean_request():
    import urllib
    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility_settings'))
        
    c_id=session.cid
    
    btn_clean_branch_data=request.vars.btn_clean_branch_data
    if btn_clean_branch_data:
        clean_branch_id=request.vars.clean_branch_id
        clean_password=request.vars.clean_password
        clean_checkbox=request.vars.clean_checkbox
        
        if (clean_branch_id=='' or clean_password=='' or clean_checkbox!='Confirm'):
            session.flash='Required All Value accurately'
        else:
            depotCheck=db((db.sm_depot.cid==c_id) & (db.sm_depot.depot_id==clean_branch_id)).select(db.sm_depot.name,limitby=(0,1))
            if not depotCheck:
                session.flash='Invalid Branch ID'
            else:
                clean_branch_name=depotCheck[0].name
                #-----------------------
                if clean_password!='sdf23423dfdg343fdgfd':
                    session.flash='Invalid Password'
                else:
                    depotid=str(clean_branch_id)
                    
                    requisitionHead=db((db.sm_requisition_head.cid==c_id)&(db.sm_requisition_head.depot_id==depotid)).delete()
                    requisitionDetails=db((db.sm_requisition.cid==c_id)&(db.sm_requisition.depot_id==depotid)).delete()
                    
                    issueHead=db((db.sm_issue_head.cid==c_id)&(db.sm_issue_head.depot_id==depotid)).delete()
                    issueDetails=db((db.sm_issue.cid==c_id)&(db.sm_issue.depot_id==depotid)).delete()
                    
                    receiveHead=db((db.sm_receive_head.cid==c_id)&(db.sm_receive_head.depot_id==depotid)).delete()
                    receiveDetails=db((db.sm_receive.cid==c_id)&(db.sm_receive.depot_id==depotid)).delete()
                    
                    damageHead=db((db.sm_damage_head.cid==c_id)&(db.sm_damage_head.depot_id==depotid)).delete()
                    damageDetails=db((db.sm_damage.cid==c_id)&(db.sm_damage.depot_id==depotid)).delete()
                    
                    disputeHead=db((db.sm_transaction_dispute_head.cid==c_id)&(db.sm_transaction_dispute_head.depot_id==depotid)).delete()
                    disputeDetails=db((db.sm_transaction_dispute.cid==c_id)&(db.sm_transaction_dispute.depot_id==depotid)).delete()
                    
                    #--------------
                    orderHead=db((db.sm_order_head.cid==c_id)&(db.sm_order_head.depot_id==depotid)).update(status='Invoiced',flag_data='1',field2=1)
                    orderDetails=db((db.sm_order.cid==c_id)&(db.sm_order.depot_id==depotid)).update(status='Invoiced',flag_data='1',field2=1)
                    
                    invoiceHead=db((db.sm_invoice_head.cid==c_id)&(db.sm_invoice_head.depot_id==depotid)).delete()
                    invoiceDetails=db((db.sm_invoice.cid==c_id)&(db.sm_invoice.depot_id==depotid)).delete()
                    
                    returnHead=db((db.sm_return_head.cid==c_id)&(db.sm_return_head.depot_id==depotid)).delete()
                    returnDetails=db((db.sm_return.cid==c_id)&(db.sm_return.depot_id==depotid)).delete()
                    returnCancel=db((db.sm_return_cancel.cid==c_id)&(db.sm_return_cancel.depot_id==depotid)).delete() #new
                    
                    tpRulesTemp=db((db.sm_tp_rules_temp_process.cid==c_id)&(db.sm_tp_rules_temp_process.depot_id==depotid)).delete()
                    tpRulesManualTemp=db((db.sm_tp_rules_temp_process_manual.cid==c_id)&(db.sm_tp_rules_temp_process_manual.depot_id==depotid)).delete()
                    
                    payment=db((db.sm_payment_collection.cid==c_id)&(db.sm_payment_collection.depot_id==depotid)).delete()
                    
                    stock=db((db.sm_depot_stock_balance.cid==c_id)&(db.sm_depot_stock_balance.depot_id==depotid)).update(quantity=0,block_qty=0)
                    
                    rptTransaction=db((db.sm_rpt_transaction.cid==c_id)&(db.sm_rpt_transaction.depot_id==depotid)).delete() #new
                    
                    ledgerSql="delete FROM `sm_transaction` WHERE `reference` like('"+depotid+"%')"
                    db.executesql(ledgerSql)
                    
                    urlRes='Data clean: Requisition,Issue,Receive,Damage,Dispute,Invoice,Return,Payment,Ledger; Data update: Order and stock '
                    session.flash='Branch ID:'+str(depotid)+', Branch Name:'+str(clean_branch_name)+'. '+urlRes
                    
                    #-------------------------                    
    redirect(URL('utility_settings'))
    
#Only this function is used to clean customer
def branch_customer_clean_request():
    import urllib
    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility_settings'))
        
    c_id=session.cid
    
    btn_clean_branch_data=request.vars.btn_clean_branch_data
    if btn_clean_branch_data:
        clean_branch_id=request.vars.clean_branch_id
        clean_password=request.vars.clean_password
        clean_checkbox=request.vars.clean_checkbox
        
        if (clean_branch_id=='' or clean_password=='' or clean_checkbox!='Confirm'):
            session.flash='Required All Value accurately'
        else:
            depotCheck=db((db.sm_depot.cid==c_id) & (db.sm_depot.depot_id==clean_branch_id)).select(db.sm_depot.name,limitby=(0,1))
            if not depotCheck:
                session.flash='Invalid Branch ID'
            else:
                clean_branch_name=depotCheck[0].name
                #-----------------------
                if clean_password!='abc123cba321':
                    session.flash='Invalid Password'
                else:
                    depotid=str(clean_branch_id)
                    
                    customerData=db((db.sm_client.cid==c_id)&(db.sm_client.depot_id==depotid)).delete()
                    
                    urlRes='Data clean: Customer'
                    session.flash='Branch ID:'+str(depotid)+', Branch Name:'+str(clean_branch_name)+'. '+urlRes
                    
                    #-------------------------
                    
    redirect(URL('utility_settings'))

#------------- clean function call
def branch_data_clean_request_bak():
    import urllib
    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility_settings'))
    
    c_id=session.cid
    
    
    cleanpath='utility/clean_depot_data?'
    #-------
    hostName=request.env.http_host
    appName=request.application
    baseUrl='http://'+str(hostName)+'/'+str(appName)+'/'+cleanpath
    #-----
    
    btn_clean_branch_data=request.vars.btn_clean_branch_data
    if btn_clean_branch_data:
        clean_branch_id=request.vars.clean_branch_id
        clean_password=request.vars.clean_password
        clean_checkbox=request.vars.clean_checkbox
        
        if (clean_branch_id=='' or clean_password=='' or clean_checkbox!='YES'):
            session.flash='Required All Value'
        else:            
            depotCheck=db((db.sm_depot.cid==c_id) & (db.sm_depot.depot_id==clean_branch_id) & (db.sm_depot.depot_category=='DEPOT')).select(db.sm_depot.name,limitby=(0,1))
            if not depotCheck:
                session.flash='Invalid Branch ID'
            else:
                clean_branch_name=depotCheck[0].name
                
                urlPath=str(baseUrl) +'cid='+str(c_id)+'&depotid='+str(clean_branch_id)+'&password='+str(clean_password)
                
                urlRes = urllib.urlopen(urlPath).read()                        
                if urlRes!='':
                    session.flash='Branch ID:'+str(clean_branch_id)+', Branch Name:'+str(clean_branch_name)+'. '+urlRes
                else:
                    session.flash='Error in process'
    
    redirect(URL('utility_settings'))


#=======================Set Prescription Liist
def set_prescription_list():
    
    c_id = 'NOVIVO'


    productStr_A = ''
    recordstring_A="SELECT item_id,name FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'A%' ORDER BY `name` ASC"
    records_A=db.executesql(recordstring_A,as_dict = True)
    for records_A in records_A:
        item_id_A = records_A['item_id']
        name_A = str(records_A['name']).replace(".","").replace(",","")
        if productStr_A == '':
            productStr_A = str(item_id_A) + '<fd>' + str(name_A)
        else:
            productStr_A += '<rd>' + str(item_id_A) + '<fd>' + str(name_A)
    productStr_A='<ASTART>'+productStr_A+'<AEND>'

#     return productStr_A
    productStr_B = ''
    recordstring_B="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'B%' ORDER BY `name` ASC"
    records_B=db.executesql(recordstring_B,as_dict = True)
    for records_B in records_B:
        item_id_B = records_B['item_id']
        name_B = str(records_B['name']).replace(".","").replace(",","")
        if productStr_B == '':
            productStr_B = str(item_id_B) + '<fd>' + str(name_B)
        else:
            productStr_B += '<rd>' + str(item_id_B) + '<fd>' + str(name_B)
    productStr_B='<BSTART>'+productStr_B+'<BEND>'

    productStr_C = ''
    recordstring_C="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'C%' ORDER BY `name` ASC"
    records_C=db.executesql(recordstring_C,as_dict = True)
    for records_C in records_C:
        item_id_C = records_C['item_id']
        name_C = str(records_C['name']).replace(".","").replace(",","")
        if productStr_C == '':
            productStr_C = str(item_id_C) + '<fd>' + str(name_C)
        else:
            productStr_C += '<rd>' + str(item_id_C) + '<fd>' + str(name_C)
    productStr_C='<CSTART>'+productStr_C+'<CEND>'
#     return recordstring_C
    productStr_D = ''
    recordstring_D="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'D%' ORDER BY `name` ASC"
    records_D=db.executesql(recordstring_D,as_dict = True)
    for records_D in records_D:
        item_id_D = records_D['item_id']
        name_D = str(records_D['name']).replace(".","").replace(",","")
        if productStr_D == '':
            productStr_D = str(item_id_D) + '<fd>' + str(name_D)
        else:
            productStr_D += '<rd>' + str(item_id_D) + '<fd>' + str(name_D)
    productStr_D='<DSTART>'+productStr_D+'<DEND>'

    productStr_E = ''
    recordstring_E="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'E%' ORDER BY `name` ASC"
    records_E=db.executesql(recordstring_E,as_dict = True)
    for records_E in records_E:
        item_id_E = records_E['item_id']
        name_E = str(records_E['name']).replace(".","").replace(",","")
        if productStr_E == '':
            productStr_E = str(item_id_E) + '<fd>' + str(name_E)
        else:
            productStr_E += '<rd>' + str(item_id_E) + '<fd>' + str(name_E)
    productStr_E='<ESTART>'+productStr_E+'<EEND>'
#     return productStr_E
    productStr_F = ''
    recordstring_F="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'F%' ORDER BY `name` ASC"
    records_F=db.executesql(recordstring_F,as_dict = True)
    for records_F in records_F:
        item_id_F = records_F['item_id']
        name_F = str(records_F['name']).replace(".","").replace(",","")
        if productStr_F == '':
            productStr_F = str(item_id_F) + '<fd>' + str(name_F)
        else:
            productStr_F += '<rd>' + str(item_id_F) + '<fd>' + str(name_F)
    productStr_F='<FSTART>'+productStr_F+'<FEND>'

    productStr_G = ''
    recordstring_G="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'G%' ORDER BY `name` ASC"
    records_G=db.executesql(recordstring_G,as_dict = True)
    for records_G in records_G:
        item_id_G = records_G['item_id']
        name_G = str(records_G['name']).replace(".","").replace(",","")
        if productStr_G == '':
            productStr_G = str(item_id_G) + '<fd>' + str(name_G)
        else:
            productStr_G += '<rd>' + str(item_id_G) + '<fd>' + str(name_G)
    productStr_G='<GSTART>'+productStr_G+'<GEND>'

    productStr_H = ''
    recordstring_H="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'H%' ORDER BY `name` ASC"
    records_H=db.executesql(recordstring_H,as_dict = True)
    for records_H in records_H:
        item_id_H = records_H['item_id']
        name_H = str(records_H['name']).replace(".","").replace(",","")
        if productStr_H == '':
            productStr_H = str(item_id_H) + '<fd>' + str(name_H)
        else:
            productStr_H += '<rd>' + str(item_id_H) + '<fd>' + str(name_H)
    productStr_H='<HSTART>'+productStr_H+'<HEND>'
#     return productStr_H
    productStr_I = ''
    recordstring_I="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'I%' ORDER BY `name` ASC"
    records_I=db.executesql(recordstring_I,as_dict = True)
    for records_I in records_I:
        item_id_I = records_I['item_id']
        name_I = str(records_I['name']).replace(".","").replace(",","")
        if productStr_I == '':
            productStr_I = str(item_id_I) + '<fd>' + str(name_I)
        else:
            productStr_I += '<rd>' + str(item_id_I) + '<fd>' + str(name_I)
    productStr_I='<ISTART>'+productStr_I+'<IEND>'
#     return productStr_I
    productStr_J = ''
    recordstring_J="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'J%' ORDER BY `name` ASC"
#     return recordstring_J
    records_J=db.executesql(recordstring_J,as_dict = True)
#     return len(records_J)
    for records_J in records_J:
        item_id_J = str(records_J['item_id'] )

        name_J = str(records_J['name']).replace(".","").replace(",","")
#         return name_J
        if productStr_J == '':
            productStr_J = str(item_id_J) #+ '<fd>' + str(name_J)
        else:
            productStr_J += '<rd>' + str(item_id_J) + '<fd>' + str(name_J)
#     return productStr_J
    productStr_J='<JSTART>'+productStr_J+'<JEND>'
#     return productStr_J
    productStr_K = ''
    recordstring_K="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'K%' ORDER BY `name` ASC"
    records_K=db.executesql(recordstring_K,as_dict = True)
    for records_K in records_K:
        item_id_K = records_K['item_id']
        name_K = str(records_K['name']).replace(".","").replace(",","")
        if productStr_K == '':
            productStr_K = str(item_id_K) + '<fd>' + str(name_K)
        else:
            productStr_K += '<rd>' + str(item_id_K) + '<fd>' + str(name_K)
    productStr_K='<KSTART>'+productStr_K+'<KEND>'
#     return productStr_K
    productStr_L = ''
    recordstring_L="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'L%' ORDER BY `name` ASC"
    records_L=db.executesql(recordstring_L,as_dict = True)
    for records_L in records_L:
        item_id_L = records_L['item_id']
        name_L = str(records_L['name']).replace(".","").replace(",","")
        if productStr_L == '':
            productStr_L = str(item_id_L) + '<fd>' + str(name_L)
        else:
            productStr_L += '<rd>' + str(item_id_L) + '<fd>' + str(name_L)
    productStr_L='<LSTART>'+productStr_L+'<LEND>'
#     return productStr_L
    productStr_M = ''
    recordstring_M="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'M%' ORDER BY `name` ASC"
#     return recordstring_M
    records_M=db.executesql(recordstring_M,as_dict = True)
#     return len(records_M)
    for records_M in records_M:
        item_id_M = records_M['item_id']
        name_M = str(records_M['name']).replace(".","").replace(",","")
        if productStr_M == '':
            productStr_M = str(item_id_M) + '<fd>' + str(name_M)
        else:
            productStr_M += '<rd>' + str(item_id_M) + '<fd>' + str(name_M)
    productStr_M='<MSTART>'+productStr_M+'<MEND>'

    productStr_N = ''
    recordstring_N="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'N%' ORDER BY `name` ASC"
    records_N=db.executesql(recordstring_N,as_dict = True)
    for records_N in records_N:
        item_id_N = records_N['item_id']
        name_N = str(records_N['name']).replace(".","").replace(",","")
        if productStr_N == '':
            productStr_N = str(item_id_N) + '<fd>' + str(name_N)
        else:
            productStr_N += '<rd>' + str(item_id_N) + '<fd>' + str(name_N)
    productStr_N='<NSTART>'+productStr_N+'<NEND>'
#     return productStr_N
    productStr_O = ''
    recordstring_O="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'O%' ORDER BY `name` ASC"
    records_O=db.executesql(recordstring_O,as_dict = True)
    for records_O in records_O:
        item_id_O = records_O['item_id']
        name_O = str(records_O['name']).replace(".","").replace(",","")
        if productStr_O == '':
            productStr_O = str(item_id_O) + '<fd>' + str(name_O)
        else:
            productStr_O += '<rd>' + str(item_id_O) + '<fd>' + str(name_O)
    productStr_O='<OSTART>'+productStr_O+'<OEND>'
#     return productStr_O
    productStr_P = ''
    recordstring_P="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'P%' ORDER BY `name` ASC"
    records_P=db.executesql(recordstring_P,as_dict = True)
    for records_P in records_P:
        item_id_P = records_P['item_id']
        name_P = str(records_P['name']).replace(".","").replace(",","")
        if productStr_P == '':
            productStr_P = str(item_id_P) + '<fd>' + str(name_P)
        else:
            productStr_P += '<rd>' + str(item_id_P) + '<fd>' + str(name_P)
    productStr_P='<PSTART>'+productStr_P+'<PEND>'

    productStr_Q = ''
    recordstring_Q="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'Q%' ORDER BY `name` ASC"
    records_Q=db.executesql(recordstring_Q,as_dict = True)
    for records_Q in records_Q:
        item_id_Q = records_Q['item_id']
        name_Q = str(records_Q['name']).replace(".","").replace(",","")
        if productStr_Q == '':
            productStr_Q = str(item_id_Q) + '<fd>' + str(name_Q)
        else:
            productStr_Q += '<rd>' + str(item_id_Q) + '<fd>' + str(name_Q)
    productStr_Q='<QSTART>'+productStr_Q+'<QEND>'

    productStr_R = ''
    recordstring_R="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'R%' ORDER BY `name` ASC"
    records_R=db.executesql(recordstring_R,as_dict = True)
    for records_R in records_R:
        item_id_R = records_R['item_id']
        name_R = str(records_R['name']).replace(".","").replace(",","")
        if productStr_R == '':
            productStr_R = str(item_id_R) + '<fd>' + str(name_R)
        else:
            productStr_R += '<rd>' + str(item_id_R) + '<fd>' + str(name_R)
    productStr_R='<RSTART>'+productStr_R+'<REND>'

    productStr_S = ''
    recordstring_S="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'S%' ORDER BY `name` ASC"
    records_S=db.executesql(recordstring_S,as_dict = True)
    for records_S in records_S:
        item_id_S = records_S['item_id']
        name_S = str(records_S['name']).replace(".","").replace(",","")
        if productStr_S == '':
            productStr_S = str(item_id_S) + '<fd>' + str(name_S)
        else:
            productStr_S += '<rd>' + str(item_id_S) + '<fd>' + str(name_S)
    productStr_S='<SSTART>'+productStr_S+'<SEND>'

    productStr_T = ''
    recordstring_T="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'T%' ORDER BY `name` ASC"
    records_T=db.executesql(recordstring_T,as_dict = True)
    for records_T in records_T:
        item_id_T = records_T['item_id']
        name_T = str(records_T['name']).replace(".","").replace(",","")
        if productStr_T == '':
            productStr_T = str(item_id_T) + '<fd>' + str(name_T)
        else:
            productStr_T += '<rd>' + str(item_id_T) + '<fd>' + str(name_T)
    productStr_T='<TSTART>'+productStr_T+'<TEND>'

    productStr_U = ''
    recordstring_U="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'U%' ORDER BY `name` ASC"
    records_U=db.executesql(recordstring_U,as_dict = True)
    for records_U in records_U:
        item_id_U = records_U['item_id']
        name_U = str(records_U['name']).replace(".","").replace(",","")
        if productStr_U == '':
            productStr_U = str(item_id_U) + '<fd>' + str(name_U)
        else:
            productStr_U += '<rd>' + str(item_id_U) + '<fd>' + str(name_U)
    productStr_U='<USTART>'+productStr_U+'<UEND>'

    productStr_V = ''
    recordstring_V="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'V%' ORDER BY `name` ASC"
    records_V=db.executesql(recordstring_V,as_dict = True)
    for records_V in records_V:
        item_id_V = records_V['item_id']
        name_V = str(records_V['name']).replace(".","").replace(",","")
        if productStr_V == '':
            productStr_V = str(item_id_V) + '<fd>' + str(name_V)
        else:
            productStr_V += '<rd>' + str(item_id_V) + '<fd>' + str(name_V)
    productStr_V='<VSTART>'+productStr_V+'<VEND>'

    productStr_W = ''
    recordstring_W="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'W%' ORDER BY `name` ASC"
    records_W=db.executesql(recordstring_W,as_dict = True)
    for records_W in records_W:
        item_id_W = records_W['item_id']
        name_W = str(records_W['name']).replace(".","").replace(",","")
        if productStr_W == '':
            productStr_W = str(item_id_W) + '<fd>' + str(name_W)
        else:
            productStr_W += '<rd>' + str(item_id_W) + '<fd>' + str(name_W)
    productStr_W='<WSTART>'+productStr_W+'<WEND>'

    productStr_X = ''
    recordstring_X="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'X%' ORDER BY `name` ASC"
    records_X=db.executesql(recordstring_X,as_dict = True)
    for records_X in records_X:
        item_id_X = records_X['item_id']
        name_X = str(records_X['name']).replace(".","").replace(",","")
        if productStr_X == '':
            productStr_X = str(item_id_X) + '<fd>' + str(name_X)
        else:
            productStr_X += '<rd>' + str(item_id_X) + '<fd>' + str(name_X)
    productStr_X='<XSTART>'+productStr_X+'<XEND>'

    productStr_Y = ''
    recordstring_Y="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'Y%' ORDER BY `name` ASC"
    records_Y=db.executesql(recordstring_Y,as_dict = True)
    for records_Y in records_Y:
        item_id_Y = records_Y['item_id']
        name_Y = str(records_Y['name']).replace(".","").replace(",","")
        if productStr_Y == '':
            productStr_Y = str(item_id_Y) + '<fd>' + str(name_Y)
        else:
            productStr_Y += '<rd>' + str(item_id_Y) + '<fd>' + str(name_Y)
    productStr_Y='<YSTART>'+productStr_Y+'<YEND>'

    productStr_Z = ''
    recordstring_Z="SELECT * FROM `sm_item` WHERE cid = '"+ c_id +"' AND status = 'ACTIVE' AND `name` LIKE 'Z%' ORDER BY `name` ASC"
    records_Z=db.executesql(recordstring_Z,as_dict = True)
    for records_Z in records_Z:
        item_id_Z = records_Z['item_id']
        name_Z = str(records_Z['name']).replace(".","").replace(",","")
        if productStr_Z == '':
            productStr_Z = str(item_id_Z) + '<fd>' + str(name_Z)
        else:
            productStr_Z += '<rd>' + str(item_id_Z) + '<fd>' + str(name_Z)
    productStr_Z='<ZSTART>'+productStr_Z+'<ZEND>'



    productStr=productStr_A+productStr_B+productStr_C+productStr_D+productStr_E+productStr_F+productStr_G+productStr_H+productStr_I+productStr_J+productStr_K+productStr_L+productStr_M+productStr_N+productStr_O+productStr_P+productStr_Q+productStr_R+productStr_S+productStr_T+productStr_U+productStr_V+productStr_W+productStr_X+productStr_Y+productStr_Z
#
    # return productStr


#     productStr='sjdjhk'
           
    item_update=db((db.sm_company_settings.cid==c_id)).update(item_list_mobile=productStr)
    
    if (item_update>0):
        session.flash='Successfully Prepared'        
    else:
        session.flash='Error in process'
                 
    redirect (URL('utility_mrep','utility_settings'))
    
def change_promotional_status():
    import urllib
    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility_settings'))
        
    task_id='rm_campaign_manage'
    access_permission=check_role(task_id)
    if (access_permission==False):
        session.flash='Access is Denied !'
        redirect(URL('utility_settings'))
        
    c_id=session.cid
    
    btn_change_status_promo=request.vars.btn_change_status_promo
    if btn_change_status_promo:        
        #requisitionHead=db((db.sm_requisition_head.cid==c_id)&(db.sm_requisition_head.depot_id==depotid)).update()
        
        db((db.sm_promo_approved_rate.cid==c_id)&(db.sm_promo_approved_rate.to_date<current_date)&(db.sm_promo_approved_rate.status!='INACTIVE')).update(status='INACTIVE')
        db((db.sm_promo_product_bonus.cid==c_id)&(db.sm_promo_product_bonus.to_date<current_date)&(db.sm_promo_product_bonus.status!='INACTIVE')).update(status='INACTIVE')
        db((db.sm_promo_special_rate.cid==c_id)&(db.sm_promo_special_rate.to_date<current_date)&(db.sm_promo_special_rate.status!='INACTIVE')).update(status='INACTIVE')
        db((db.sm_promo_flat_rate.cid==c_id)&(db.sm_promo_flat_rate.to_date<current_date)&(db.sm_promo_flat_rate.status!='INACTIVE')).update(status='INACTIVE')
        db((db.sm_promo_regular_discount.cid==c_id)&(db.sm_promo_regular_discount.to_date<current_date)&(db.sm_promo_regular_discount.status!='INACTIVE')).update(status='INACTIVE')
        session.flash='Updated successfully. Approved Rate, Product Bonus, Special Rate, Flat Rate and Regular Discount.'
        
        #-------------------------                    
    redirect(URL('utility_settings'))

def change_item_expiary_date():    
    if (session.user_type!='Admin'):
        session.flash='Access is denied'
        redirect(URL('utility_settings'))
        
    task_id='rm_utility_manage'
    access_permission=check_role(task_id)
    if (access_permission==False):
        session.flash='Access is Denied !'
        redirect(URL('utility_settings'))
        
    c_id=session.cid
    
    btn_change_item_expiary=request.vars.btn_change_item_expiary
    if btn_change_item_expiary:       
        item_id=request.vars.change_item_id
        batch_id=request.vars.change_batch_id
        new_expiary_date=request.vars.change_new_expiary_date
        password=request.vars.change_password
        checkbox=request.vars.change_checkbox
        
        rows_check1=db((db.sm_item.cid==c_id) & (db.sm_item.item_id==item_id) & (db.sm_item.status=='ACTIVE')).select(db.sm_item.item_id,limitby=(0,1))
        if not rows_check1:
            session.flash='Invalid Item ID!'
        else:
            rows_check2=db((db.sm_item_batch.cid==c_id) & (db.sm_item_batch.item_id==item_id) & (db.sm_item_batch.batch_id==batch_id)).select(db.sm_item_batch.id,limitby=(0,1))
            if not rows_check2:
                session.flash='Invalid Item Batch ID!'
            else:
                dateFlag=True
                try:
                    new_expiary_date=datetime.datetime.strptime(str(new_expiary_date),'%Y-%m-%d').strftime('%Y-%m-%d')
                except:
                    dateFlag=False
                    session.flash='Invalid Expiary Date!'
                    
                if dateFlag==False:
                    pass
                else:
                    if password!='abc123cba321':
                        session.flash='Invalid Password!'
                    else:                        
                        if checkbox!='Confirm':
                            session.flash='Required valid confirmation!'
                        else:
                            rows_check2[0].update_record(expiary_date=new_expiary_date)
                            
                            db((db.sm_depot_stock_balance.cid==c_id)&(db.sm_depot_stock_balance.item_id==item_id)&(db.sm_depot_stock_balance.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            db((db.sm_issue.cid==c_id)&(db.sm_issue.item_id==item_id)&(db.sm_issue.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            db((db.sm_receive.cid==c_id)&(db.sm_receive.item_id==item_id)&(db.sm_receive.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            db((db.sm_damage.cid==c_id)&(db.sm_damage.item_id==item_id)&(db.sm_damage.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            
                            db((db.sm_transaction_dispute.cid==c_id)&(db.sm_transaction_dispute.item_id==item_id)&(db.sm_transaction_dispute.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            db((db.sm_depot_stock_tran_snapshot.cid==c_id)&(db.sm_depot_stock_tran_snapshot.item_id==item_id)&(db.sm_depot_stock_tran_snapshot.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                            db((db.temp_closing_stock.cid==c_id)&(db.temp_closing_stock.item_id==item_id)&(db.temp_closing_stock.batch_id==batch_id)).update(expiary_date=new_expiary_date)
                                                                                    
                            session.flash='Updated successfully in Item Batch, Stock Balance, Issue, Receive, Adjustment/Transfer, Transaction Dispute, Snapshot and Closing Stock'
    
    #-------------------------                    
    redirect(URL('utility_settings'))
    
    
    
