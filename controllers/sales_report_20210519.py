from random import randint
import urllib2
import calendar
import urllib
import time


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
def deduct_months(sourcedate, months):
    month = sourcedate.month - 1 - months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def sales_report_detail():

    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()
    password = str(request.vars.password).strip()
    synccode = str(request.vars.synccode).strip()
    
    rep_id_report = str(request.vars.rep_id_report).strip().upper()
    se_item_report = str(request.vars.se_item_report).strip().upper()
    se_market_report = str(request.vars.se_market_report).strip().upper()


    date_from=current_date
    now = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    date_ton=now - datetime.timedelta(days = 7)
    date_to=str(date_ton).split(' ')[0]

    from_dt = str(request.vars.from_dt).strip().upper()
    to_date= str(request.vars.to_dt).strip().upper()


    btn_filter=request.vars.btn_filter
    btn_all=request.vars.btn_all
    reqPage=len(request.args)
    if btn_filter:
        session.btn_filter=btn_filter
        reqPage=0
    elif btn_all:
        session.btn_filter=None
        reqPage=0
        
    #--------paging
    if reqPage:
        page=int(request.args[0])
    else:
        page=0
    items_per_page=session.items_per_page
    search_form =SQLFORM(db.sm_search_date)
    
    user_type = str(request.vars.user_type).strip().upper()

    repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.sync_code == synccode) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.ALL, limitby=(0, 1))
    if not repRow:
       retStatus = 'FAILED<SYNCDATA>Invalid Authorization'
       return retStatus
    else:
        user_type = str(repRow[0].user_type).upper()

       # pass
    
    if (user_type == 'SUP'):
        level_rep = repRow[0].level_id
        depth = repRow[0].field2
        level = 'level' + str(depth)
    
    report_string=""
    
    report_str=""
    
    if (user_type=='REP'):

        dateFlag=''
        reqPage=len(request.args)
        dateFlag=True
        try:
            from_dt=datetime.datetime.strptime(str(from_dt),'%Y-%m-%d')
            to_dt=datetime.datetime.strptime(str(to_date),'%Y-%m-%d')
        except:
            dateFlag=False

        condition=""
        if (se_market_report!="ALL"):        
           condition="and sm_order.area_id='"+ str(se_market_report) +"' "


        records_ov=[]
        if session.btn_filter:
            if (from_dt!='' and to_date!=''):

                sql_str="SELECT SUM((sm_order.price) * (sm_order.quantity)) as totalprice, sm_order.area_id as area_id, sm_order.area_name as area_name,sm_order.delivery_date as delivery_date,(SELECT count(sm_order_head.sl) FROM sm_order_head WHERE sm_order_head.cid = '"+ str(cid)+"' AND sm_order_head.rep_id = '"+ str(rep_id) +"' AND sm_order_head.delivery_date = sm_order.delivery_date) as visit_count,(SELECT count(sm_order_head.sl) FROM sm_order_head WHERE sm_order_head.cid = '"+ str(cid)+"' AND sm_order_head.rep_id = '"+ str(rep_id) +"' AND sm_order_head.field1='ORDER' AND sm_order_head.delivery_date = sm_order.delivery_date) as order_count FROM sm_order  WHERE sm_order.cid = '"+ str(cid) +"' AND sm_order.rep_id = '"+ str(rep_id) +"' AND sm_order.delivery_date > '"+ str(from_dt).split(' ')[0] +"' AND sm_order.delivery_date <= '"+ str(to_date) +"' "+ condition + " GROUP BY area_id,delivery_date;"

                records_ov=db.executesql(sql_str,as_dict = True)
            else:
                pass
        else:
            sql_str="SELECT SUM((sm_order.price) * (sm_order.quantity)) as totalprice, sm_order.area_id as area_id, sm_order.area_name as area_name,sm_order.delivery_date as delivery_date,(SELECT count(sm_order_head.sl) FROM sm_order_head WHERE sm_order_head.cid = '"+ str(cid)+"' AND sm_order_head.rep_id = '"+ str(rep_id) +"' AND sm_order_head.delivery_date = sm_order.delivery_date) as visit_count,(SELECT count(sm_order_head.sl) FROM sm_order_head WHERE sm_order_head.cid = '"+ str(cid)+"' AND sm_order_head.rep_id = '"+ str(rep_id) +"' AND sm_order_head.field1='ORDER' AND sm_order_head.delivery_date = sm_order.delivery_date) as order_count FROM sm_order WHERE sm_order.cid = '"+ str(cid) +"' AND sm_order.rep_id = '"+ str(rep_id) +"' AND sm_order.delivery_date <= '"+ str(date_from) +"' AND sm_order.delivery_date > '"+ str(date_to) +"' "+ condition + " GROUP BY area_id,delivery_date;"
        
            records_ov=db.executesql(sql_str,as_dict = True)

            

    return dict(date_to=date_to,cid=cid,rep_id=rep_id,password=password,synccode=synccode,se_market_report=se_market_report,records_ov=records_ov,search_form=search_form)


def sales_report_area_wise():

    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()
    password = str(request.vars.password).strip()
    synccode = str(request.vars.synccode).strip()
    area_id = str(request.vars.area_id).strip()
    
    rep_id_report = str(request.vars.rep_id_report).strip().upper()
    se_item_report = str(request.vars.se_item_report).strip().upper()
    se_market_report = str(request.vars.se_market_report).strip().upper()
    
    dlvry_date=str(request.vars.dlvry_date).strip()
    
    user_type = str(request.vars.user_type).strip().upper()
    now = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    date_to=now + datetime.timedelta(days = 1)
    
    repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.sync_code == synccode) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.ALL, limitby=(0, 1))
    if not repRow:
       retStatus = 'FAILED<SYNCDATA>Invalid Authorization'
       return retStatus
    else:
        user_type = str(repRow[0].user_type).upper()

    
    if (user_type == 'SUP'):
        level_rep = repRow[0].level_id
        depth = repRow[0].field2
        level = 'level' + str(depth)
    
    report_string=""
    
    report_str=""
    
    if (user_type=='REP'):
        #    Sales Call====================
        qset=db()
        qset=qset((db.sm_order_head.cid == cid) & (db.sm_order_head.rep_id == rep_id))
        qset=qset(db.sm_order_head.delivery_date == dlvry_date)
        qset=qset(db.sm_order_head.area_id==area_id)
        records=qset.select(db.sm_order_head.sl.count())
        if records:
            sales_call=records[0][db.sm_order_head.sl.count()]
        
        report_string=str(sales_call)
        #  Order Count  
        qset_oc=db()
        qset_oc=qset_oc((db.sm_order_head.cid == cid) & (db.sm_order_head.rep_id == rep_id) & (db.sm_order_head.field1 == 'ORDER')) 
        qset_oc=qset_oc(db.sm_order_head.delivery_date == dlvry_date)
        qset_oc=qset_oc(db.sm_order_head.area_id==area_id)
        records_oc=qset_oc.select(db.sm_order_head.sl.count())
        # return db._lastsql
        if records_oc:
            order_count=records_oc[0][db.sm_order_head.sl.count()]
        
        
        condition=""
        if (se_market_report!="ALL"):        
           condition="and sm_order.area_id='"+ str(se_market_report) +"' "


        records_ov=[]
        sql_str="SELECT (sm_order.client_id) as client_id,(sm_order.client_name) as client_name,SUM((sm_order.price) * (sm_order.quantity)) as totalprice, sm_order.area_id as area_id, sm_order.vsl as vsl FROM sm_order WHERE sm_order.cid = '"+ str(cid) +"' AND sm_order.rep_id = '"+ str(rep_id) +"' AND sm_order.delivery_date = '"+ str(dlvry_date) +"'  GROUP BY area_id,delivery_date,vsl;"

        records_ov=db.executesql(sql_str,as_dict = True)

    return dict(date_to=date_to,cid=cid,rep_id=rep_id,password=password,synccode=synccode,records_ov=records_ov,area_id=area_id,dlvry_date=dlvry_date)



def sales_report_slWise():

    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()
    password = str(request.vars.password).strip()
    synccode = str(request.vars.synccode).strip()
    area_id = str(request.vars.area_id).strip()
    vsl = str(request.vars.vsl).strip()
    client_id = str(request.vars.client_id).strip().upper()

    dlvry_date=str(request.vars.dlvry_date).strip()
    
    user_type = str(request.vars.user_type).strip().upper()
    now = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    date_ton=now + datetime.timedelta(days = 1)
    date_to=str(date_ton).split(' ')[0]

        
    
    repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.sync_code == synccode) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.ALL, limitby=(0, 1))
    if not repRow:
       retStatus = 'FAILED<SYNCDATA>Invalid Authorization'
       return retStatus
    else:
        user_type = str(repRow[0].user_type).upper()

    
    if (user_type == 'SUP'):
        level_rep = repRow[0].level_id
#        level_id = repRow[0].level_id
        depth = repRow[0].field2
        level = 'level' + str(depth)
    
    report_string=""
    
    report_str=""
    
    if (user_type=='REP'):

        records_ov=[]
        sql_str="SELECT SUM(sm_order.quantity) as item_qty, sm_order.item_id as item_id,sm_order.item_name as item_name, sm_order.quantity as qty,((sm_order.price) * (sm_order.quantity)) as amnt, sm_order.vsl as vsl,sm_order.delivery_date as delivery_date,(SELECT SUM((sm_order.price) * (sm_order.quantity))  FROM sm_order  WHERE sm_order.cid = '"+ str(cid) +"' AND sm_order.rep_id = '"+ str(rep_id) +"' AND sm_order.delivery_date = '"+ str(dlvry_date) +"' AND sm_order.vsl= '"+ str(vsl) +"' AND sm_order.area_id='"+str(area_id)+"' AND sm_order.client_id='"+str(client_id)+"'  GROUP BY sm_order.area_id) as totalprice FROM sm_order WHERE sm_order.cid = '"+ str(cid) +"' AND sm_order.rep_id = '"+ str(rep_id) +"' AND sm_order.delivery_date = '"+ str(dlvry_date) +"' AND sm_order.vsl= '"+ str(vsl) +"' AND sm_order.area_id='"+str(area_id)+"' AND sm_order.client_id='"+str(client_id)+"'  GROUP BY sm_order.area_id,item_id;"

        records_ov=db.executesql(sql_str,as_dict = True)

    return dict(records_ov=records_ov,vsl=vsl,dlvry_date=dlvry_date,area_id=area_id,client_id=client_id)

