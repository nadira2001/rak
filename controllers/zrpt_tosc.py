
import urllib2
import calendar

def sub_months(sourcedate, months):
    month = sourcedate.month - 1 - months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def get_region_list():

    resStr=''
    rows = db().select(db.sm_level.level1, db.sm_level.level1_name, groupby =db.sm_level.level1, orderby=db.sm_level.level1_name)
    # return db._lastsql
    for row in rows:
        level_name = str(row.level1_name).replace('|', ' ').replace(',', ' ')
        level_id = str(row.level1)

        if resStr == '':
            resStr = level_id + '|' + level_name
        else:
            resStr += ',' + level_id + '|' + level_name
    return resStr


def get_area_list():

    resStr=''
    rows = db().select(db.sm_level.level2, db.sm_level.level2_name, groupby =db.sm_level.level2, orderby=db.sm_level.level2_name)
    # return db._lastsql
    for row in rows:
        level_name = str(row.level2_name).replace('|', ' ').replace(',', ' ')
        level_id = str(row.level2)

        if resStr == '':
            resStr = level_id + '|' + level_name
        else:
            resStr += ',' + level_id + '|' + level_name
    return resStr



def get_iten_list():

    resStr=''
    cid = session.cid
    rows = db(db.sm_item.cid == cid).select(db.sm_item.item_id, db.sm_item.name, orderby=db.sm_item.name)
    for row in rows:
        item_id = str(row.item_id)
        name = str(row.name).replace('|', ' ').replace(',', ' ')

        if resStr == '':
            resStr = item_id + '|' + name
        else:
            resStr += ',' + item_id + '|' + name
    return resStr


def get_mpo_list():

    resStr=''
    rows = db().select(db.sm_level.level3, db.sm_level.level3_name, groupby =db.sm_level.level3, orderby=db.sm_level.level3_name)
    # return db._lastsql
    for row in rows:
        level_name = str(row.level3_name).replace('|', ' ').replace(',', ' ')
        level_id = str(row.level3)

        if resStr == '':
            resStr = level_id + '|' + level_name
        else:
            resStr += ',' + level_id + '|' + level_name
    return resStr

def analysis2():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.select_region_value
    session.posmArea = request.vars.select_area_value
    session.posmTownCode = request.vars.posmTown

    if session.posmregion == None:
        session.posmregion=''
    if session.posmArea == None:
        session.posmArea=''
    if session.posmTownCode == None:
        session.posmTownCode=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.posmregion != ''):
            usagesTownList = str(session.posmregion).split('|')
            if len(usagesTownList) > 1:
                session.posmregion = usagesTownList[0]
            else:
                session.posmregion = session.posmregion

        if (session.posmArea != ''):
            usagesTownList = str(session.posmArea).split('|')
            if len(usagesTownList) > 1:
                session.posmArea = usagesTownList[0]
            else:
                session.posmArea = session.posmArea

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion=''
        session.posmArea = ''
        session.posmTownCode = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''

    if session.btn_filter:
        if session.posmregion != '':
            condition += ' and  rm_code="' + session.posmregion + '"'

        if session.posmArea != '':
            condition += ' and  fm_code ="' + session.posmArea + '"'


    record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' " + str(condition) + " group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code LIMIT "+str(minimum)+","+str(maximum)+""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)


    record_row_2 = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' " + str(condition) + " group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"

    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_analysis2():
    records=''
    if session.posmTownCode == None or session.posmTownCode == '':
        session.posmTownCode = ''

    if session.posmArea == None or session.posmArea == '':
        session.posmArea = ''
    if session.posmregion == None or session.posmregion == '':
        session.posmregion = ''

    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    condition = ''
    if session.btn_filter:
        if session.posmregion != '':
            condition += ' and  rm_code="' + session.posmregion + '"'

        if session.posmArea != '':
            condition += ' and  fm_code ="' + session.posmArea + '"'


    record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' " + str(condition) + " group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    records =''
    myString = 'Target vs Order Sale and Collection MPI \n\n'

    myString += 'Region_ID,Region Name,Area_id,Area Name,MPO_Code,Territory,Target,Order,Sales,Collection\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area']
        mpo_code = recordListStr['mpo_code']
        terri_name = recordListStr['terri_name']
        target = round(float(recordListStr['target']), 2)
        s_order = round(float(recordListStr['s_order']), 2)
        sales = round(float(recordListStr['sales']), 2)
        collection = round(float(recordListStr['collection']), 2)


        myString += str(rm_code) + ',' + str(region)+ ',' + str(fm_code)+ ',' + str(fm_area)+ ',' + str(mpo_code) + ',' + str(terri_name) + ',' + str(target) + ',' + str(s_order) + ',' + str(sales) + ',' + str(collection) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_Target_vs_Order_Sale_and_Coll_MPI.csv'
    return str(myString)



def region_and_area_wise():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion2 = request.vars.posmregion
    session.posmArea2 = request.vars.posmArea
    session.posmTownCode2 = request.vars.posmTown

    if session.posmregion2 == None:
        session.posmregion2=''
    if session.posmArea2 == None:
        session.posmArea2=''
    if session.posmTownCode2 == None:
        session.posmTownCode2=''

    if btn_filter:
        session.btn_filter2 = btn_filter
        session.searchTypePOSM2 = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM2 = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter2 = None
        session.searchTypePOSM2 = None
        session.searchValuePOSM2 = None
        session.posmregion2=''
        session.posmArea2 = ''
        session.posmTownCode2 = ''

        reqPage = 0
    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    records = ''
    record_row = "SELECT rm_code,region,fm_code,fm_area, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' GROUP BY rm_code,region,fm_code,fm_area ORDER BY `fm_code`"

    record_rowSTR = db.executesql(record_row, as_dict=True)
    recCount = 0
    return dict(record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)

def download_region_and_area_wise():

    records=''
    if session.posmTownCode2 == None or session.posmTownCode2 == '':
        session.posmTownCode2 = ''

    if session.posmArea2 == None or session.posmArea2 == '':
        session.posmArea2 = ''
    if session.posmregion2 == None or session.posmregion2 == '':
        session.posmregion2 = ''

    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    records = ''
    record_row = "SELECT rm_code,region,fm_code,fm_area, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' GROUP BY rm_code,region,fm_code,fm_area ORDER BY `fm_code`"

    record_rowSTR = db.executesql(record_row, as_dict=True)
    myString = 'Target vs Order Sale and Collection AI\n\n'

    myString += 'Region_ID,Region Name,Area_ID,Area Name,Target,Order,Sales,Collection\n'

    targetTotal = 0
    s_orderTotal = 0
    salesTotal = 0
    collectionTotal = 0

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area']
        # mpo_code = recordListStr['mpo_code']
        # terri_name = recordListStr['terri_name']
        targetTotal = round(float(recordListStr['target']),2)
        s_orderTotal = round(float(recordListStr['s_order']),2)
        salesTotal = round(float(recordListStr['sales']),2)
        collectionTotal = round(float(recordListStr['collection']),2)

        myString +=  str(rm_code) + ',' +str(region) + ',' +str(fm_code)+ ',' +str(fm_area)+ ',' +str(targetTotal) + ',' + str(s_orderTotal)+ ',' + str(salesTotal) + ',' + str(collectionTotal) +'\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_Target_vs_Order_Sale_and_Coll_AI.csv'
    return str(myString)



def summary_allocation_data_RI_mobile():

    response.title = 'M-Reporting'
    region_wise = request.vars.region_wise
    areaValue = request.vars.areaValue
    if region_wise == None:
        region_wise = ''
    if areaValue == None:
        areaValue = ''

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.sum_all_product_regionRI_M = request.vars.sum_all_product_regionRI_M
    session.sum_all_product_codeRI_M = request.vars.sum_all_product_codeRI_M


    if session.sum_all_product_regionRI_M == None:
        session.sum_all_product_regionRI_M=''
    if session.sum_all_product_codeRI_M == None:
        session.sum_all_product_codeRI_M=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM23= str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM23 = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.sum_all_product_regionRI_M=''
        session.sum_all_product_codeRI_M = ''

        reqPage = 0

        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging

    qset = db()
    condition = ''
    record_row = ''


    records = ''
    recCount = 0

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''


    if session.btn_filter:

        if (session.sum_all_product_regionRI_M != ''):
            usagesTownList = str(session.sum_all_product_regionRI_M).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_regionRI_M = usagesTownList[0]
            else:
                session.sum_all_product_regionRI_M = session.sum_all_product_regionRI_M

        if (session.sum_all_product_codeRI_M != ''):
            usagesTownList = str(session.sum_all_product_codeRI_M).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_codeRI_M = usagesTownList[0]
            else:
                session.sum_all_product_codeRI_M = session.sum_all_product_codeRI_M

        if session.sum_all_product_regionRI_M != '':
            condition += ' and  rm_code="' + session.sum_all_product_regionRI_M + '"'
            condition1 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'
            condition2 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'
            condition3 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'

        if session.sum_all_product_codeRI_M != '':
            condition += ' and  PPM_CODE ="' + session.sum_all_product_codeRI_M + '"'
            condition1 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'
            condition2 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'
            condition3 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    # record_row = "SELECT rm_code,region, REP_ID, ITEM_ID, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,EMPNO AS REP_ID, PPM_CODE  AS ITEM_ID, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' "+condition+" GROUP BY rm_code,region,EMPNO, PPM_CODE UNION SELECT  level1_id  as rm_code,level1_name as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition1+" GROUP BY level1_id,level1_name, REP_ID, ITEM_ID UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition2+" GROUP BY level1_id,level1_name, REP_ID, item_id UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition3+" GROUP BY level1_id,level1_name,REP_ID, item_id) AS T GROUP BY rm_code,region,REP_ID, ITEM_ID LIMIT " + str(minimum) + "," + str(maximum) + ""
    record_row = "SELECT rm_code,region, REP_ID,rep_name ,ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' "+condition+" GROUP BY rm_code,region,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion, REP_ID,rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition1+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition2+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition3+" GROUP BY level1_id,level1_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def summary_allocation_data_RI_mobile_back():

    response.title = 'M-Reporting'
    region_wise = request.vars.region_wise
    areaValue = request.vars.areaValue
    if region_wise == None:
        region_wise = ''
    if areaValue == None:
        areaValue = ''

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.sum_all_product_regionRI_M = request.vars.sum_all_product_regionRI_M
    session.sum_all_product_codeRI_M = request.vars.sum_all_product_codeRI_M

    if session.posmregion23 == None:
        session.posmregion23=''
    if session.sum_all_product_codeRI_M == None:
        session.sum_all_product_codeRI_M=''
    if session.sum_all_product_regionRI_M == None:
        session.sum_all_product_regionRI_M=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM23= str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM23 = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM23 = None
        session.searchValuePOSM23 = None
        session.sum_all_product_codeRI=''
        session.sum_all_product_regionRI_M = ''
        session.sum_all_product_codeRI_M = ''

    qset = db()

    condition = ''
    record_row = ''

    records = ''
    recCount = 0

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:
        if session.sum_all_product_regionRI_M != '':
            condition += ' and  rm_code="' + session.sum_all_product_regionRI_M + '"'
            condition1 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'
            condition2 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'
            condition3 += ' and  level1_id="' + session.sum_all_product_regionRI_M + '"'

        if session.sum_all_product_codeRI_M != '':
            condition += ' and  PPM_CODE ="' + session.sum_all_product_codeRI_M + '"'
            condition1 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'
            condition2 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'
            condition3 += ' and  item_id ="' + session.sum_all_product_codeRI_M + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="'+ str(session.mobile_report_rep_id) +'")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    record_row = "SELECT region, REP_ID, ITEM_ID, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code as region,EMPNO AS REP_ID, PPM_CODE  AS ITEM_ID, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + "  GROUP BY rm_code,EMPNO, PPM_CODE UNION SELECT  level1_id as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id, REP_ID, ITEM_ID UNION SELECT level1_id as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + "  GROUP BY level1_id, REP_ID, item_id UNION SELECT level1_id as rigion, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,REP_ID, item_id) AS T GROUP BY region,REP_ID, ITEM_ID"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)


def summary_allocation_data_RI():

    response.title = 'M-Reporting'
    region_wise = request.vars.region_wise
    areaValue = request.vars.areaValue
    if region_wise == None:
        region_wise = ''
    if areaValue == None:
        areaValue = ''

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.sum_all_product_regionRI = request.vars.sum_all_product_regionRI
    session.sum_all_product_codeRI = request.vars.sum_all_product_codeRI


    if session.sum_all_product_regionRI == None:
        session.sum_all_product_regionRI=''
    if session.sum_all_product_codeRI == None:
        session.sum_all_product_codeRI=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM23= str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM23 = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.sum_all_product_codeRI=''
        session.sum_all_product_regionRI = ''



        reqPage = 0

        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging

    qset = db()
    condition = ''
    record_row = ''


    records = ''
    recCount = 0

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''


    if session.btn_filter:

        if (session.sum_all_product_regionRI != ''):
            usagesTownList = str(session.sum_all_product_regionRI).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_regionRI = usagesTownList[0]
            else:
                session.sum_all_product_regionRI = session.sum_all_product_regionRI

        if (session.sum_all_product_codeRI != ''):
            usagesTownList = str(session.sum_all_product_codeRI).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_codeRI = usagesTownList[0]
            else:
                session.sum_all_product_codeRI = session.sum_all_product_codeRI

        if session.sum_all_product_regionRI != '':
            condition += ' and  rm_code="' + session.sum_all_product_regionRI + '"'
            condition1 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'
            condition2 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'
            condition3 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'

        if session.sum_all_product_codeRI != '':
            condition += ' and  PPM_CODE ="' + session.sum_all_product_codeRI + '"'
            condition1 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'
            condition2 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'
            condition3 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'

    record_row = "SELECT rm_code,region, REP_ID,rep_name ,ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' "+condition+" GROUP BY rm_code,region,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion, REP_ID,rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition1+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition2+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition3+" GROUP BY level1_id,level1_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)

def download_summary_allocation_data_RI():

    if session.sum_all_product_regionRI == None:
        session.sum_all_product_regionRI = ''
    if session.sum_all_product_codeRI == None:
        session.sum_all_product_codeRI = ''

    condition = ''
    record_row = ''
    # if ((session.btn_filter) and (session.sum_all_product_regionRI != '')):
    #     condition = condition + "AND region ='" + session.sum_all_product_regionRI + "'"
    # if ((session.btn_filter) and (session.sum_all_product_codeRI != '')):
    #     condition = condition + "AND PPM_CODE ='" + session.sum_all_product_codeRI + "'"

    records = ''
    recCount = 0

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.sum_all_product_regionRI == '':
        session.flash = 'Required Region Filter'
        redirect(URL('zrpt_tosc', 'summary_allocation_data_RI'))

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:


        if (session.sum_all_product_regionRI != ''):
            usagesTownList = str(session.sum_all_product_regionRI).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_regionRI = usagesTownList[0]
            else:
                session.sum_all_product_regionRI = session.sum_all_product_regionRI

        if (session.sum_all_product_codeRI != ''):
            usagesTownList = str(session.sum_all_product_codeRI).split('|')
            if len(usagesTownList) > 1:
                session.sum_all_product_codeRI = usagesTownList[0]
            else:
                session.sum_all_product_codeRI = session.sum_all_product_codeRI

        if session.sum_all_product_regionRI != '':
            condition += ' and  rm_code="' + session.sum_all_product_regionRI + '"'
            condition1 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'
            condition2 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'
            condition3 += ' and  level1_id="' + session.sum_all_product_regionRI + '"'

        if session.sum_all_product_codeRI != '':
            condition += ' and  PPM_CODE ="' + session.sum_all_product_codeRI + '"'
            condition1 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'
            condition2 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'
            condition3 += ' and  item_id ="' + session.sum_all_product_codeRI + '"'

    record_row = "SELECT rm_code,region, REP_ID,rep_name ,ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' "+condition+" GROUP BY rm_code,region,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion, REP_ID,rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition1+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition2+" GROUP BY level1_id,level1_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' "+condition3+" GROUP BY level1_id,level1_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,REP_ID, rep_name, ITEM_ID,item_name"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    myString = 'Allocation and Usage RI \n\n'

    myString += 'Region ID,Region Name,REP ID,REP Name,ITEM_ID,ITEM Name,Allocation Qty,Usage QTY,Gift QTY,PPM QTY,Sample QTY\n'

    ISSUE_QNTY=0

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region'].replace(',','')
        REP_ID = recordListStr['REP_ID']
        rep_name = recordListStr['rep_name'].replace(',','')
        ITEM_ID = recordListStr['ITEM_ID']
        item_name = recordListStr['item_name'].replace(',','')
        allocation = recordListStr['allocation']

        gift = recordListStr['gift']
        ppm = recordListStr['ppm']
        sample = recordListStr['sample']
        Usage_qty =gift + ppm + sample
        myString +=  str(rm_code)+ ',' +str(region)+ ',' +str(REP_ID)+ ',' +str(rep_name)+ ',' +str(ITEM_ID)+ ',' +str(item_name)+ ',' +str(allocation) + ',' +str(Usage_qty)+ ',' +str(gift)+ ',' +str(ppm)+ ',' +str(sample)+'\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_allocation_Usage_RI.csv'
    return str(myString)

def region_wise():

    response.title = 'M-Reporting'
    region_wise = request.vars.region_wise
    areaValue = request.vars.areaValue
    if region_wise == None:
        region_wise = ''
    if areaValue == None:
        areaValue = ''

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion23 = request.vars.posmregion
    session.posmArea23 = request.vars.posmArea
    session.posmTownCode23 = request.vars.posmTown

    if session.posmregion23 == None:
        session.posmregion23=''
    if session.posmArea23 == None:
        session.posmArea23=''
    if session.posmTownCode23 == None:
        session.posmTownCode23=''

    if btn_filter:
        session.btn_filter23 = btn_filter
        session.searchTypePOSM23= str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM23 = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter23 = None
        session.searchTypePOSM23 = None
        session.searchValuePOSM23 = None
        session.posmregion23=''
        session.posmArea23 = ''
        session.posmTownCode23 = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    # --------end paging

    qset = db()

    records = ''
    recCount = 0

    record_row = "SELECT rm_code,region, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' GROUP BY rm_code,region ORDER BY `rm_code`"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)

def download_region_wise():

    records=''

    qset = db()

    record_row = "SELECT rm_code,region, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' GROUP BY rm_code,region ORDER BY `rm_code`"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    myString = 'Target vs Order Sale and Collection RI \n\n'

    myString += 'region_id,Region Name,Target,Order,Sales,Collection\n'
    targetTotal=0
    s_orderTotal=0
    salesTotal=0
    collectionTotal=0

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        # fm_code = recordListStr['fm_code']
        # fm_area = recordListStr['fm_area']
        # mpo_code = recordListStr['mpo_code']
        # terri_name = recordListStr['terri_name']
        targetTotal = round(float(recordListStr['target']),2)
        s_orderTotal = round(float(recordListStr['s_order']),2)
        salesTotal = round(float(recordListStr['sales']),2)
        collectionTotal = round(float(recordListStr['collection']),2)

        myString +=  str(rm_code) + ',' +str(region)+ ',' +str(targetTotal) + ',' + str(s_orderTotal)+ ',' + str(salesTotal) + ',' + str(collectionTotal) +'\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_Target_vs_Order_Sale and_Coll_RI.csv'
    return str(myString)



def analysis_report2():

    reqPage = len(request.args)

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    # -----
    db.sm_search_date.from_dt.requires = IS_DATE(format=T('%d-%m-%Y'))
    db.sm_search_date.to_dt.requires = IS_DATE(format=T('%d-%m-%Y'))
    search_form = SQLFORM(db.sm_search_date)

    # --------------------------------------patient
    btn_agency_report = request.vars.btn_agency_report
    posmCode = request.vars.posmCode
    cm_compliance = request.vars.cm_compliance
    exe_discrepancy = request.vars.exe_discrepancy
    exe_discrepancy_download = request.vars.exe_discrepancy_download

    townCode = request.vars.townCode

    posmCodeAgency = request.vars.posmCodeAgency
    agencyCode = request.vars.agencyCode
    territory_Name = request.vars.territory_Name
    townCode_Name = request.vars.townCode_Name
    # return townCode_Name
    # return agencyCode
    record2=''
    userCheck=''
    return dict(userCheck=userCheck, search_form=search_form, record2=record2, page=page)


def analysis():

    response.title = 'Analysis'

    c_id = session.cid

    # -----
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    Target_vs_Order_Sale_Coll_RI = request.vars.Target_vs_Order_Sale_Coll_RI
    Target_vs_Order_Sale_Coll_RI_D = request.vars.Target_vs_Order_Sale_Coll_RI_D

    Target_vs_Order_Sale_Coll_AI = request.vars.Target_vs_Order_Sale_Coll_AI
    Target_vs_Order_Sale_Coll_AI_D = request.vars.Target_vs_Order_Sale_Coll_AI_D

    Target_vs_Order_Sale_Coll_MPI = request.vars.Target_vs_Order_Sale_Coll_MPI
    Target_vs_Order_Sale_Coll_MPI_D = request.vars.Target_vs_Order_Sale_Coll_MPI_D

    product_wise_sales_qrt_RI = request.vars.product_wise_sales_qrt_RI
    product_wise_sales_qrt_AI = request.vars.product_wise_sales_qrt_AI

    product_wise_sales_qrt_MPI = request.vars.product_wise_sales_qrt_MPI
    KPI_Prod_Target_vs_Sale_RI = request.vars.KPI_Prod_Target_vs_Sale_RI

    KPI_Prod_Target_vs_Sale_AI = request.vars.KPI_Prod_Target_vs_Sale_AI

    KPI_Prod_Target_vs_Sale_MPI = request.vars.KPI_Prod_Target_vs_Sale_MPI
    customer_wise_monthly_sales = request.vars.customer_wise_monthly_sales
    market_wise_monthly_sales = request.vars.market_wise_monthly_sales

    summary_allocation_data_RI = request.vars.summary_allocation_data_RI

    summary_allocation_data_AI = request.vars.summary_allocation_data_AI
    summary_allocation_data_MPI = request.vars.summary_allocation_data_MPI

    if Target_vs_Order_Sale_Coll_RI:
        redirect(URL('region_wise'))
    elif summary_allocation_data_RI:
        redirect(URL('summary_allocation_data_RI'))

    elif summary_allocation_data_MPI:
        redirect(URL('summary_allocation_data_MPI'))

    elif summary_allocation_data_AI:
        redirect(URL('summary_allocation_data_AI'))

    elif Target_vs_Order_Sale_Coll_RI_D:
        redirect(URL('download_region_wise'))
    elif Target_vs_Order_Sale_Coll_AI:
        redirect(URL('region_and_area_wise'))

    elif Target_vs_Order_Sale_Coll_AI_D:
        redirect(URL('download_region_and_area_wise'))
    elif Target_vs_Order_Sale_Coll_MPI:
        redirect(URL('analysis2'))

    elif Target_vs_Order_Sale_Coll_MPI_D:
        redirect(URL('download_analysis2'))

    elif product_wise_sales_qrt_MPI:
        redirect(URL('product_wise_sales_qrt_MPI'))

    elif product_wise_sales_qrt_AI:
        redirect(URL('product_wise_sales_qrt_AI'))
    elif product_wise_sales_qrt_RI:
        redirect(URL('product_wise_sales_qrt_RI'))

    elif customer_wise_monthly_sales:
        redirect(URL('customer_wise_monthly_sales'))
    elif market_wise_monthly_sales:
        redirect(URL('market_wise_monthly_sales'))
    elif KPI_Prod_Target_vs_Sale_RI:
        redirect(URL('KPI_Prod_Target_vs_Sale_RI'))
    elif KPI_Prod_Target_vs_Sale_AI:
        redirect(URL('KPI_Prod_Target_vs_Sale_AI'))
    elif KPI_Prod_Target_vs_Sale_MPI:
        redirect(URL('KPI_Prod_Target_vs_Sale_MPI'))

    regionRows = ''#db().select(db.zrpt_tosc_1.region,groupby=db.zrpt_tosc_1.region,orderby=db.zrpt_tosc_1.region)
    areaRows = ''#db().select(db.zrpt_tosc_1.fm_area, groupby=db.zrpt_tosc_1.fm_area, orderby=db.zrpt_tosc_1.fm_area)

    return dict(areaRows=areaRows,regionRows=regionRows)


def product_wise_sales_qrt_RI_mobile():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.product_regionRI_mobile = request.vars.product_regionRI
    session.product_codeRI_mobile = request.vars.product_codeRI

    if session.product_regionRI_mobile == None:
        session.product_regionRI_mobile = ''
    if session.product_regionRI == None:
        session.product_regionRI = ''
    if session.product_codeRI_mobile == None:
        session.product_codeRI_mobile = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionRI_mobile != ''):
            usagesTownList = str(session.product_regionRI_mobile).split('|')
            if len(usagesTownList) > 1:
                session.product_regionRI_mobile = usagesTownList[0]
            else:
                session.product_regionRI_mobile = session.product_regionRI_mobile

        if (session.product_codeRI_mobile != ''):
            usagesTownList = str(session.product_codeRI_mobile).split('|')
            if len(usagesTownList) > 1:
                session.product_codeRI_mobile = usagesTownList[0]
            else:
                session.product_codeRI_mobile = session.product_codeRI_mobile


        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.product_regionRI_mobile = ''
        session.product_codeRI_mobile = ''

        reqPage = 0


    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    condition =''
    if ((session.btn_filter) and (session.product_codeRI_mobile != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI_mobile + "'"
    if ((session.btn_filter) and (session.product_regionRI_mobile != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI_mobile + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='"+session.cid+"' AND mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,P_CODE,P_DESC order by region LIMIT "+str(minimum)+","+str(maximum)+""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='" + session.cid + "' AND mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " "+condition_level+" GROUP BY rm_code,region,P_CODE,P_DESC order by region LIMIT "+str(minimum)+","+str(maximum)+""

    record_rowSTR = db.executesql(record_row, as_dict=True)


    if session.mobile_report_rep_type == 'REP':
        record_row_2 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='"+session.cid+"' AND mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,P_CODE,P_DESC order by P_CODE"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row_2 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='" + session.cid + "' AND mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " "+condition_level+" GROUP BY rm_code,region,P_CODE,P_DESC order by P_CODE"

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def product_wise_sales_qrt_RI():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.product_regionRI = request.vars.product_regionRI
    session.product_codeRI = request.vars.product_codeRI

    if session.posmregion == None:
        session.posmregion = ''
    if session.product_regionRI == None:
        session.product_regionRI = ''
    if session.product_codeRI == None:
        session.product_codeRI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionRI != ''):
            usagesTownList = str(session.product_regionRI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionRI = usagesTownList[0]
            else:
                session.product_regionRI = session.product_regionRI

        if (session.product_codeRI != ''):
            usagesTownList = str(session.product_codeRI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeRI = usagesTownList[0]
            else:
                session.product_codeRI = session.product_codeRI


        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.product_regionRI = ''
        session.product_codeRI = ''

        reqPage = 0


    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI + "'"
    if ((session.btn_filter) and (session.product_regionRI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='"+session.cid+"' AND  mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" GROUP BY rm_code,region,P_CODE,P_DESC order by region LIMIT "+str(minimum)+","+str(maximum)+""

    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_3 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='" + session.cid + "' AND  mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " GROUP BY rm_code,region,P_CODE,P_DESC order by region "

    record_rowSTR_2 = db.executesql(record_row_3, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_product_wise_sales_qrt_RI():
    records=''
    if session.product_codeRI == None or session.product_codeRI == '':
        session.product_codeRI = ''
    if session.product_regionRI == None or session.product_regionRI == '':
        session.product_regionRI = ''
    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI + "'"
    if ((session.btn_filter) and (session.product_regionRI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw` WHERE human_vet='" + session.cid + "' AND  mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " GROUP BY rm_code,region,P_CODE,P_DESC order by P_CODE"

    record_rowSTR = db.executesql(record_row, as_dict=True)
    records =''
    myString = 'Product wise sales qnty RI \n\n'

    myString += 'Region_ID,Region Name,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        P_CODE = recordListStr['P_CODE']
        P_DESK = recordListStr['P_DESC'].replace(',','')
        sales = round(float(recordListStr['sales']), 2)
        SQNTY = recordListStr['SQNTY']



        myString += str(rm_code) + ',' +str(region) + ',' +str(P_CODE) + ',' + str(P_DESK) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_product_wise_sales_qrt_RI.csv'
    return str(myString)


def product_wise_sales_qrt_AI_mobile():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown
    session.product_codeAI_mob = request.vars.product_codeAI

    session.product_areaAI_mob = request.vars.product_areaAI
    session.product_regionAI_mob = request.vars.product_regionAI

    if session.product_codeAI_mob == None:
        session.product_codeAI_mob = ''
    if session.product_areaAI_mob == None:
        session.product_areaAI_mob = ''

    if session.product_regionAI_mob == None:
        session.product_regionAI_mob = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_codeAI_mob != ''):
            usagesTownList = str(session.product_codeAI_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_codeAI_mob = usagesTownList[0]
            else:
                session.product_codeAI_mob = session.product_codeAI_mob

        if (session.product_areaAI_mob != ''):
            usagesTownList = str(session.product_areaAI_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_areaAI_mob = usagesTownList[0]
            else:
                session.product_areaAI_mob = session.product_areaAI_mob

        if (session.product_regionAI_mob != ''):
            usagesTownList = str(session.product_regionAI_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_regionAI_mob = usagesTownList[0]
            else:
                session.product_regionAI_mob = session.product_regionAI_mob

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_codeAI_mob = ''
        session.product_areaAI_mob = ''
        session.product_regionAI_mob = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI_mob + "'"
    if ((session.btn_filter) and (session.product_areaAI_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI_mob + "'"
    if ((session.btn_filter) and (session.product_codeAI_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI_mob + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""
    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(
                session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(
                session.mobile_report_rep_id) + "') "
        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' " + condition_level + " GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    if session.mobile_report_rep_type == 'REP':
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"
    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' " + condition_level + " GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"

    # return record_row
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_rowSTR_2=record_rowSTR_2, record_rowSTR=record_rowSTR, records=records, page=page,items_per_page=items_per_page, recCount=recCount, search_form=search_form)
# #-----------------------
#     condition = ''
#     record_row = ''
#     if ((session.btn_filter) and (session.product_regionAI_mob != '')):
#         # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
#         condition = condition + "AND region ='" + session.product_regionAI_mob + "'"
#     if ((session.btn_filter) and (session.product_areaAI_mob != '')):
#         # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
#         condition = condition + "AND fm_area ='" + session.product_areaAI_mob + "'"
#     if ((session.btn_filter) and (session.product_codeAI_mob != '')):
#         # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
#         condition = condition + "AND P_CODE ='" + session.product_codeAI_mob + "'"
#
#     current_date_strat = str(current_date)[:7] + '-' + '01'
#     # current_date_end = str(current_date)[:7] + '-' + '31'
#     last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
#     current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
#     if session.mobile_report_rep_type == 'REP':
#         record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND human_vet='"+session.cid+"' GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"
#     else:
#
#         condition_level =''
#         if session.level_depth_no ==2:
#             condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
#         elif session.level_depth_no ==1:
#             condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
#
#         record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " "+condition_level+" AND human_vet='" + session.cid + "' GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"
#     # return record_row
#     record_rowSTR = db.executesql(record_row, as_dict=True)
#     records=''
#     recCount=0
#     return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)


def product_wise_sales_qrt_AI():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown
    session.product_codeAI = request.vars.product_codeAI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.product_regionAI == None:
        session.product_regionAI = ''
    if session.product_areaAI == None:
        session.product_areaAI = ''

    if session.product_codeAI == None:
        session.product_codeAI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionAI != ''):
            usagesTownList = str(session.product_regionAI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionAI = usagesTownList[0]
            else:
                session.product_regionAI = session.product_regionAI

        if (session.product_areaAI != ''):
            usagesTownList = str(session.product_areaAI).split('|')
            if len(usagesTownList) > 1:
                session.product_areaAI = usagesTownList[0]
            else:
                session.product_areaAI = session.product_areaAI

        if (session.product_codeAI != ''):
            usagesTownList = str(session.product_codeAI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeAI = usagesTownList[0]
            else:
                session.product_codeAI = session.product_codeAI

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionAI = ''
        session.product_areaAI = ''
        session.product_codeAI = ''

        reqPage = 0


    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI + "'"
    if ((session.btn_filter) and (session.product_areaAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI + "'"
    if ((session.btn_filter) and (session.product_codeAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""

    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_5 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"

    record_rowSTR_2 = db.executesql(record_row_5, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_product_wise_sales_qrt_AI():
    records=''
    if session.product_codeAI == None or session.product_codeAI == '':
        session.product_codeAI = ''
    if session.product_areaAI == None or session.product_areaAI == '':
        session.product_areaAI = ''
    if session.product_codeAI == None or session.product_codeAI == '':
        session.product_codeAI = ''
    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI + "'"
    if ((session.btn_filter) and (session.product_areaAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI + "'"
    if ((session.btn_filter) and (session.product_codeAI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    # current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='vet' GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"

    record_rowSTR = db.executesql(record_row, as_dict=True)
    records = ''


    records =''
    myString = 'Product wise sales qnty AI \n\n'

    myString += 'Region_ID,Region Name,Area_ID,Area Name,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        P_CODE = recordListStr['P_CODE']
        P_DESK = recordListStr['P_DESC'].replace(',','')
        sales = round(float(recordListStr['sales']), 2)
        SQNTY = recordListStr['SQNTY']



        myString +=str(rm_code) + ',' +str(region)+ ',' +str(fm_code)+ ',' +str(fm_area) + ',' +str(P_CODE) + ',' + str(P_DESK) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_product_wise_sales_qrt_AI.csv'
    return str(myString)


def product_wise_sales_qrt_MPI_mobile():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR_mob = request.vars.product_regionR
    session.product_areaR_mob = request.vars.product_areaR
    session.product_mpoR_mob = request.vars.product_mpoR
    session.product_codeR_mob = request.vars.product_codeR
    if session.product_regionR_mob == None:
        session.product_regionR_mob = ''
    if session.product_areaR_mob == None:
        session.product_areaR_mob = ''
    if session.product_mpoR_mob == None:
        session.product_mpoR_mob = ''
    if session.product_codeR_mob == None:
        session.product_codeR_mob = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_codeR_mob != ''):
            usagesTownList = str(session.product_codeR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_codeR_mob = usagesTownList[0]
            else:
                session.product_codeR_mob = session.product_codeR_mob

        if (session.product_mpoR_mob != ''):
            usagesTownList = str(session.product_mpoR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_mpoR_mob = usagesTownList[0]
            else:
                session.product_mpoR_mob = session.product_mpoR_mob

        if (session.product_areaR_mob != ''):
            usagesTownList = str(session.product_areaR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_areaR_mob = usagesTownList[0]
            else:
                session.product_areaR_mob = session.product_areaR_mob


        if (session.product_regionR_mob != ''):
            usagesTownList = str(session.product_regionR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_regionR_mob = usagesTownList[0]
            else:
                session.product_regionR_mob = session.product_regionR_mob

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_regionR_mob = ''
        session.product_areaR_mob = ''
        session.product_mpoR_mob = ''
        session.product_codeR_mob = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_mob + "'"

    if ((session.btn_filter) and (session.product_regionR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR_mob + "'"

    if ((session.btn_filter) and (session.product_areaR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR_mob + "'"

    if ((session.btn_filter) and (session.product_mpoR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_mob + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "'  "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    record_rowSTR = db.executesql(record_row, as_dict=True)


    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "'  "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)




def product_wise_sales_qrt_MPI_mobile_sup():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR_mob = request.vars.product_regionR
    session.product_areaR_mob = request.vars.product_areaR
    session.product_mpoR_mob = request.vars.product_mpoR
    session.product_codeR_mob = request.vars.product_codeR
    if session.product_regionR_mob == None:
        session.product_regionR_mob = ''
    if session.product_areaR_mob == None:
        session.product_areaR_mob = ''
    if session.product_mpoR_mob == None:
        session.product_mpoR_mob = ''
    if session.product_codeR_mob == None:
        session.product_codeR_mob = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_codeR_mob != ''):
            usagesTownList = str(session.product_codeR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_codeR_mob = usagesTownList[0]
            else:
                session.product_codeR_mob = session.product_codeR_mob

        if (session.product_mpoR_mob != ''):
            usagesTownList = str(session.product_mpoR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_mpoR_mob = usagesTownList[0]
            else:
                session.product_mpoR_mob = session.product_mpoR_mob

        if (session.product_areaR_mob != ''):
            usagesTownList = str(session.product_areaR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_areaR_mob = usagesTownList[0]
            else:
                session.product_areaR_mob = session.product_areaR_mob


        if (session.product_regionR_mob != ''):
            usagesTownList = str(session.product_regionR_mob).split('|')
            if len(usagesTownList) > 1:
                session.product_regionR_mob = usagesTownList[0]
            else:
                session.product_regionR_mob = session.product_regionR_mob

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_regionR_mob = ''
        session.product_areaR_mob = ''
        session.product_mpoR_mob = ''
        session.product_codeR_mob = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_mob + "'"

    if ((session.btn_filter) and (session.product_regionR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR_mob + "'"

    if ((session.btn_filter) and (session.product_areaR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR_mob + "'"

    if ((session.btn_filter) and (session.product_mpoR_mob != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_mob + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "'  "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    record_rowSTR = db.executesql(record_row, as_dict=True)


    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "'  "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)

#------------------------
    #
    # response.title = 'M-Reporting'
    #
    # btn_filter = request.vars.btn_filter
    # btn_all = request.vars.btn_all
    #
    # search_form = SQLFORM(db.sm_search_date)
    # session.posmregion = request.vars.posmregion
    # session.posmArea = request.vars.posmArea
    # session.posmTownCode = request.vars.posmTown
    #
    # session.product_regionR_mob = request.vars.product_regionR
    # session.product_areaR_mob = request.vars.product_areaR
    # session.product_mpoR_mob = request.vars.product_mpoR
    # session.product_codeR_mob = request.vars.product_codeR
    # if session.product_regionR_mob == None:
    #     session.product_regionR_mob = ''
    # if session.product_areaR_mob == None:
    #     session.product_areaR_mob = ''
    # if session.product_mpoR_mob == None:
    #     session.product_mpoR_mob= ''
    # if session.product_codeR_mob == None:
    #     session.product_codeR_mob = ''
    #
    # if btn_filter:
    #     session.btn_filter = btn_filter
    #     session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
    #     session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()
    #
    # elif btn_all:
    #     session.btn_filter = None
    #     session.searchTypePOSM = None
    #     session.searchValuePOSM = None
    #     session.posmregion = ''
    #     session.posmArea = ''
    #     session.product_codeR_mob = ''
    #     session.product_regionR_mob = ''
    #     session.product_areaR_mob = ''
    #     session.product_mpoR_mob = ''
    #
    #
    # regionValue = request.vars.regionValue
    # areaValue = request.vars.areaValue
    #
    # qset = db()
    #
    # condition = ''
    # record_row = ''
    # if ((session.btn_filter) and (session.product_codeR_mob != '')):
    #     # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
    #     condition = condition + "AND P_CODE ='" + session.product_codeR_mob + "'"
    #
    # if ((session.btn_filter) and (session.product_regionR_mob != '')):
    #     # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
    #     condition = condition + "AND region ='" + session.product_regionR_mob + "'"
    #
    # if ((session.btn_filter) and (session.product_areaR_mob != '')):
    #     # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
    #     condition = condition + "AND fm_area ='" + session.product_areaR_mob + "'"
    #
    # if ((session.btn_filter) and (session.product_mpoR_mob != '')):
    #     # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
    #     condition = condition + "AND MPO_CODE ='" + session.product_mpoR_mob + "'"
    #
    # current_date_strat = str(current_date)[:7] + '-' + '01'
    # # current_date_end = str(current_date)[:7] + '-' + '31'
    # last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    # current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    # if session.mobile_report_rep_type == 'REP':
    #     record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
    # else:
    #
    #     condition_level =''
    #     if session.level_depth_no ==2:
    #         condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
    #     elif session.level_depth_no ==1:
    #         condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
    #
    #     record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
    #
    # record_rowSTR = db.executesql(record_row, as_dict=True)
    # records=''
    # recCount=0
    # return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)


def product_wise_sales_qrt_MPI():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR = request.vars.product_regionR
    session.product_areaR = request.vars.product_areaR
    session.product_mpoR = request.vars.product_mpoR
    session.product_codeR = request.vars.product_codeR
    if session.product_regionR == None:
        session.product_regionR = ''
    if session.product_areaR == None:
        session.product_areaR = ''
    if session.product_mpoR == None:
        session.product_mpoR = ''
    if session.product_codeR == None:
        session.product_codeR = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionR != ''):
            usagesTownList = str(session.product_regionR).split('|')
            if len(usagesTownList) > 1:
                session.product_regionR = usagesTownList[0]
            else:
                session.product_regionR = session.product_regionR

        if (session.product_areaR != ''):
            usagesTownList = str(session.product_areaR).split('|')
            if len(usagesTownList) > 1:
                session.product_areaR = usagesTownList[0]
            else:
                session.product_areaR = session.product_areaR

        if (session.product_mpoR != ''):
            usagesTownList = str(session.product_mpoR).split('|')
            if len(usagesTownList) > 1:
                session.product_mpoR = usagesTownList[0]
            else:
                session.product_mpoR = session.product_mpoR


        if (session.product_codeR != ''):
            usagesTownList = str(session.product_codeR).split('|')
            if len(usagesTownList) > 1:
                session.product_codeR = usagesTownList[0]
            else:
                session.product_codeR = session.product_codeR

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_codeR = ''
        session.product_regionR = ''
        session.product_areaR = ''
        session.product_mpoR = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR + "'"

    if ((session.btn_filter) and (session.product_regionR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR + "'"

    if ((session.btn_filter) and (session.product_areaR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR + "'"

    if ((session.btn_filter) and (session.product_mpoR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR + "'"
    # session.product_areaR.replace('[','').replace("'",'')
    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+" '"+ str(condition) +" AND human_vet='"+session.cid+"' GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + " '" + str(condition) + " AND human_vet='" + session.cid + "' GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_product_wise_sales_qrt_MPI():
    records=''
    if session.product_codeR == None or session.product_codeR == '':
        session.product_codeR = ''
    if session.product_regionR == None or session.product_regionR == '':
        session.product_regionR = ''
    if session.product_areaR == None or session.product_areaR == '':
        session.product_areaR = ''
    if session.product_mpoR == None or session.product_mpoR == '':
        session.product_codeR = ''
    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR + "'"

    if ((session.btn_filter) and (session.product_regionR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR + "'"

    if ((session.btn_filter) and (session.product_areaR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR + "'"

    if ((session.btn_filter) and (session.product_mpoR != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+" '"+ str(condition) +" AND human_vet='"+session.cid+"' GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    records =''
    myString = 'Product wise sales qnty MPI \n\n'

    myString += 'Region_id,Region Name,Area_ID,Area Name,MPO Code,Territory,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        MPO_CODE = recordListStr['MPO_CODE']
        territory_name = recordListStr['territory_name'].replace(',','')

        P_CODE = recordListStr['P_CODE']
        P_DESK = recordListStr['P_DESC'].replace(',','')
        sales = round(float(recordListStr['sales']), 2)
        SQNTY = recordListStr['SQNTY']



        myString += str(rm_code) + ',' + str(region) + ',' + str(fm_code)+ ',' + str(fm_area)+ ',' + str(MPO_CODE) + ',' + str(territory_name) + ',' + str(P_CODE) + ',' + str(P_DESK) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_product_wise_sales_qrt_MPI.csv'
    return str(myString)




def analysis_mobile():

    response.title = 'Analysis'

    c_id = session.cid

    Target_vs_Order_Sale_Coll_RI = request.vars.Target_vs_Order_Sale_Coll_RI
    Target_vs_Order_Sale_Coll_AI = request.vars.Target_vs_Order_Sale_Coll_AI
    Target_vs_Order_Sale_Coll_MPI = request.vars.Target_vs_Order_Sale_Coll_MPI

    Target_vs_Order_Sale_Coll_MPI_sup = request.vars.Target_vs_Order_Sale_Coll_MPI_sup
    product_wise_sales_qrt_RI_mobile = request.vars.product_wise_sales_qrt_RI_mobile
    product_wise_sales_qrt_AI_mobile = request.vars.product_wise_sales_qrt_AI_mobile
    product_wise_sales_qrt_MPI_mobile = request.vars.product_wise_sales_qrt_MPI_mobile
    product_wise_sales_qrt_MPI_mobile_sup = request.vars.product_wise_sales_qrt_MPI_mobile_sup
    customer_wise_monthly_sales_mobile = request.vars.customer_wise_monthly_sales_mobile
    market_wise_monthly_sales_mobile = request.vars.market_wise_monthly_sales_mobile

    kpi_product_Sales_RI = request.vars.kpi_product_Sales_RI
    kpi_product_Sales_AI = request.vars.kpi_product_Sales_AI
    kpi_product_Sales_MPI = request.vars.kpi_product_Sales_MPI

    summary_allocation_data_RI_mobile = request.vars.summary_allocation_data_RI_mobile

    summary_allocation_data_AI_mobile = request.vars.summary_allocation_data_AI_mobile
    summary_allocation_data_MPI_mobile = request.vars.summary_allocation_data_MPI_mobile
    if Target_vs_Order_Sale_Coll_RI:
        redirect(URL('region_wise_mobile'))

    elif summary_allocation_data_MPI_mobile:
        redirect(URL('summary_allocation_data_MPI_mobile'))

    elif summary_allocation_data_AI_mobile:
        redirect(URL('summary_allocation_data_AI_mobile'))
    elif summary_allocation_data_RI_mobile:
        redirect(URL('summary_allocation_data_RI_mobile'))

    elif kpi_product_Sales_RI:
        redirect(URL('KPI_Prod_Sale_RI_mobile'))

    elif kpi_product_Sales_AI:
        redirect(URL('KPI_Prod_Sale_AI_mobile'))

    elif kpi_product_Sales_MPI:
        redirect(URL('KPI_Prod_Sale_MPI_mobile'))

    elif Target_vs_Order_Sale_Coll_AI:
        redirect(URL('region_and_area_wise_mobile'))


    elif Target_vs_Order_Sale_Coll_MPI:
        redirect(URL('analysis2_mobile'))

    elif Target_vs_Order_Sale_Coll_MPI_sup:
        redirect(URL('analysis2_mobile_sup'))

    elif product_wise_sales_qrt_RI_mobile:
        redirect(URL('product_wise_sales_qrt_RI_mobile'))
    elif product_wise_sales_qrt_AI_mobile:
        redirect(URL('product_wise_sales_qrt_AI_mobile'))

    elif product_wise_sales_qrt_MPI_mobile:
        redirect(URL('product_wise_sales_qrt_MPI_mobile'))

    elif product_wise_sales_qrt_MPI_mobile_sup:
        redirect(URL('product_wise_sales_qrt_MPI_mobile_sup'))

    elif customer_wise_monthly_sales_mobile:
        redirect(URL('customer_wise_monthly_sales_mobile'))

    elif market_wise_monthly_sales_mobile:
        redirect(URL('market_wise_monthly_sales_mobile'))
    # return dict()

def mobile_user_check():
    session.cid = request.vars.cid
    session.mobile_report_rep_id = request.vars.rep_id
    session.mobile_report_rep_pass = request.vars.rep_pass
    user_check = ''
    user_check = db((db.sm_rep.cid == session.cid) &(db.sm_rep.rep_id == session.mobile_report_rep_id) & (db.sm_rep.password == session.mobile_report_rep_pass) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.user_type)

    session.mobile_report_rep_type = ''

    if user_check:
        session.mobile_report_rep_type = user_check[0].user_type.upper()
        redirect(URL('mobile_report'))
    else:
        return 'Invalid Authorization'
    return dict(user_type=user_type)

def mobile_report():

    user_type = ''
    session.level_depth_no = ''
    if session.mobile_report_rep_type=='SUP':

        check_level_depth_no = "SELECT level_depth_no FROM `sm_supervisor_level` WHERE sup_id='"+str(session.mobile_report_rep_id)+"'"
        record_rowSTR = db.executesql(check_level_depth_no, as_dict=True)

        for i in range(len(record_rowSTR)):
            record_rowSTRAS = record_rowSTR[i]
            session.level_depth_no = record_rowSTRAS['level_depth_no']

    return dict(user_type=user_type)

def region_wise_mobile():

    response.title = 'M-Reporting'
    region_wise = request.vars.region_wise
    areaValue = request.vars.areaValue
    if region_wise == None:
        region_wise = ''
    if areaValue == None:
        areaValue = ''

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.posmregion23 = request.vars.posmregion
    session.posmArea23 = request.vars.posmArea
    session.posmTownCode23 = request.vars.posmTown

    if session.posmregion23 == None:
        session.posmregion23=''
    if session.posmArea23 == None:
        session.posmArea23=''
    if session.posmTownCode23 == None:
        session.posmTownCode23=''

    if btn_filter:
        session.btn_filter23 = btn_filter
        session.searchTypePOSM23= str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM23 = str(request.vars.searchValuePOSM).strip()



    elif btn_all:
        session.btn_filter23 = None
        session.searchTypePOSM23 = None
        session.searchValuePOSM23 = None
        session.posmregion23=''
        session.posmArea23 = ''
        session.posmTownCode23 = ''


    # --------paging

    qset = db()
    records = ''
    recCount = 0
    if session.mobile_report_rep_type=='REP':
        # record_row = "SELECT rm_code,region,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region ORDER BY `region`"
        record_row = "SELECT rm_code,region, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region ORDER BY `rm_code`"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+"  GROUP BY rm_code,region ORDER BY `region`"

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)



def region_and_area_wise_mobile():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.posmregion2 = request.vars.posmregion
    session.posmArea2 = request.vars.posmArea
    session.posmTownCode2 = request.vars.posmTown

    if session.posmregion2 == None:
        session.posmregion2=''
    if session.posmArea2 == None:
        session.posmArea2=''
    if session.posmTownCode2 == None:
        session.posmTownCode2=''

    if btn_filter:
        session.btn_filter2 = btn_filter
        session.searchTypePOSM2 = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM2 = str(request.vars.searchValuePOSM).strip()



    elif btn_all:
        session.btn_filter2 = None
        session.searchTypePOSM2 = None
        session.searchValuePOSM2 = None
        session.posmregion2=''
        session.posmArea2 = ''
        session.posmTownCode2 = ''



    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    records = ''
    recCount = 0
    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,fm_code,fm_area, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,fm_code,fm_area ORDER BY `fm_code`"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        record_row = "SELECT rm_code,region,fm_code,fm_area, SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+" GROUP BY rm_code,region,fm_code,fm_area ORDER BY `fm_code`"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    return dict(record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records,recCount=recCount,search_form=search_form)



def analysis2_mobile():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.select_region_value
    session.posmArea = request.vars.select_area_value
    session.posmTownCode = request.vars.posmTown

    if session.posmregion == None:
        session.posmregion=''
    if session.posmArea == None:
        session.posmArea=''
    if session.posmTownCode == None:
        session.posmTownCode=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.posmregion != ''):
            usagesTownList = str(session.posmregion).split('|')
            if len(usagesTownList) > 1:
                session.posmregion = usagesTownList[0]
            else:
                session.posmregion = session.posmregion

        if (session.posmArea != ''):
            usagesTownList = str(session.posmArea).split('|')
            if len(usagesTownList) > 1:
                session.posmArea = usagesTownList[0]
            else:
                session.posmArea = session.posmArea

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion=''
        session.posmArea = ''
        session.posmTownCode = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0

    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''

    if session.btn_filter:
        if session.posmregion != '':
            condition += ' and  rm_code="' + session.posmregion + '"'

        if session.posmArea != '':
            condition += ' and  fm_code ="' + session.posmArea + '"'


    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+" group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " "+condition_level+" group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code LIMIT " + str(minimum) + "," + str(maximum) + ""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    #--------------------
    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+" group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " "+condition_level+" group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"

    record_row_2STR = db.executesql(record_row_2, as_dict=True)
    records = ''
    recCount = 0

    return dict(record_row_2STR=record_row_2STR, record_rowSTR=record_rowSTR, regionValue=regionValue, areaValue=areaValue,records=records, page=page, items_per_page=items_per_page, recCount=recCount, search_form=search_form)


def analysis2_mobile_sup():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.select_region_value
    session.posmArea = request.vars.select_area_value
    session.posmTownCode = request.vars.posmTown

    if session.posmregion == None:
        session.posmregion=''
    if session.posmArea == None:
        session.posmArea=''
    if session.posmTownCode == None:
        session.posmTownCode=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.posmregion != ''):
            usagesTownList = str(session.posmregion).split('|')
            if len(usagesTownList) > 1:
                session.posmregion = usagesTownList[0]
            else:
                session.posmregion = session.posmregion

        if (session.posmArea != ''):
            usagesTownList = str(session.posmArea).split('|')
            if len(usagesTownList) > 1:
                session.posmArea = usagesTownList[0]
            else:
                session.posmArea = session.posmArea

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion=''
        session.posmArea = ''
        session.posmTownCode = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0

    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''

    if session.btn_filter:
        if session.posmregion != '':
            condition += ' and  rm_code="' + session.posmregion + '"'

        if session.posmArea != '':
            condition += ' and  fm_code ="' + session.posmArea + '"'


    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+" group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " "+condition_level+" group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code LIMIT " + str(minimum) + "," + str(maximum) + ""
    record_rowSTR = db.executesql(record_row, as_dict=True)

    #--------------------
    if session.mobile_report_rep_type == 'REP':
        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='"+session.cid+"' AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " AND  mpo_code IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        # record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' "+condition_level+" group by rm_code,fm_code,mpo_code order by mpo_code "
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,mpo_code,terri_name,SUM(target) as target, SUM(s_order) as s_order, SUM(sales) as sales, SUM(collection) as collection FROM `zrpt_tosc_1` WHERE cid='" + session.cid + "' " + str(condition) + " "+condition_level+" group by rm_code,region,fm_code,fm_area,mpo_code,terri_name order by mpo_code"

    record_row_2STR = db.executesql(record_row_2, as_dict=True)
    records = ''
    recCount = 0

    return dict(record_row_2STR=record_row_2STR, record_rowSTR=record_rowSTR, regionValue=regionValue, areaValue=areaValue,records=records, page=page, items_per_page=items_per_page, recCount=recCount, search_form=search_form)

def customer_wise_monthly_sales():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionCUST = request.vars.posmregionCUST
    session.posmAreaCUST = request.vars.posmAreaCUST
    session.posmTownCUST = request.vars.posmTownCUST

    if session.posmregionCUST == None:
        session.posmregionCUST=''
    if session.posmAreaCUST == None:
        session.posmAreaCUST=''
    if session.posmTownCUST == None:
        session.posmTownCUST=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()
        if (session.posmregionCUST != ''):
            usagesTownList = str(session.posmregionCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmregionCUST = usagesTownList[0]
            else:
                session.posmregionCUST = session.posmregionCUST

        if (session.posmAreaCUST != ''):
            usagesTownList = str(session.posmAreaCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmAreaCUST = usagesTownList[0]
            else:
                session.posmAreaCUST = session.posmAreaCUST
        if (session.posmTownCUST != ''):
            usagesTownList = str(session.posmTownCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmTownCUST = usagesTownList[0]
            else:
                session.posmTownCUST = session.posmTownCUST


        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionCUST=''
        session.posmAreaCUST = ''
        session.posmTownCUST = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaCUST != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaCUST + "'"

    if ((session.btn_filter) and (session.posmregionCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionCUST + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionCUST + "'"


    if ((session.btn_filter) and (session.posmTownCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownCUST + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownCUST + "'"

    if condition=='':
        record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""
    else:
        record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""

    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = ''
    if condition == '':
        record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by cust_name"
    else:
        record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by cust_name"

    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_customer_wise_monthly_sales():
    records=''
    if session.posmregionCUST == None or session.posmregionCUST == '':
        session.posmregionCUST = ''

    if session.posmAreaCUST == None or session.posmAreaCUST == '':
        session.posmAreaCUST = ''
    if session.posmTownCUST == None or session.posmTownCUST == '':
        session.posmTownCUST = ''

    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaCUST != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaCUST + "'"

    if ((session.btn_filter) and (session.posmregionCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionCUST + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionCUST + "'"


    if ((session.btn_filter) and (session.posmTownCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownCUST + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownCUST + "'"

    if condition=='':
        record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by cust_name"
    else:
        record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by cust_name"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    records =''
    myString = 'Customer wise monthly sales Collection and Outstanding \n\n'

    myString += 'Region ID,Region Name,Area ID,Area Name,Territory ID,Territory Name,Customer Code,Customer Name,Sales,Collection,Outstanding\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        mpo_code = recordListStr['mpo_code']
        terri_name = recordListStr['terri_name'].replace(',','')
        cust_code = recordListStr['cust_code']
        cust_name = recordListStr['cust_name'].replace(',','')

        sale_value = round(float(recordListStr['sale_value']), 2)
        coll_value = round(float(recordListStr['coll_value']), 2)
        os_value = round(float(recordListStr['os_value']), 2)


        myString += str(rm_code) + ',' + str(region) + ',' + str(fm_code)+ ',' + str(fm_area)+ ',' + str(mpo_code) + ',' + str(terri_name) + ',' + str(cust_code)+ ',' + str(cust_name) + ',' + str(sale_value) + ',' + str(coll_value)+ ',' + str(os_value) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_Customer_wise_monthly_sales.csv'
    return str(myString)


def customer_wise_monthly_sales_mobile():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionCUST = request.vars.posmregionCUST
    session.posmAreaCUST = request.vars.posmAreaCUST
    session.posmTownCUST = request.vars.posmTownCUST

    if session.posmregionCUST == None:
        session.posmregionCUST=''
    if session.posmAreaCUST == None:
        session.posmAreaCUST=''
    if session.posmTownCUST == None:
        session.posmTownCUST=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()
        if (session.posmregionCUST != ''):
            usagesTownList = str(session.posmregionCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmregionCUST = usagesTownList[0]
            else:
                session.posmregionCUST = session.posmregionCUST

        if (session.posmAreaCUST != ''):
            usagesTownList = str(session.posmAreaCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmAreaCUST = usagesTownList[0]
            else:
                session.posmAreaCUST = session.posmAreaCUST
        if (session.posmTownCUST != ''):
            usagesTownList = str(session.posmTownCUST).split('|')
            if len(usagesTownList) > 1:
                session.posmTownCUST = usagesTownList[0]
            else:
                session.posmTownCUST = session.posmTownCUST


        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionCUST=''
        session.posmAreaCUST = ''
        session.posmTownCUST = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaCUST != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaCUST + "'"

    if ((session.btn_filter) and (session.posmregionCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionCUST + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionCUST + "'"


    if ((session.btn_filter) and (session.posmTownCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownCUST + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownCUST + "'"

    if session.mobile_report_rep_type == 'REP':
        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""
        else:
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""
    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' "+condition_level+" order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""
        else:
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND H_VET='"+session.cid+"' "+condition_level+" order by cust_name LIMIT "+str(minimum)+","+str(maximum)+""
    record_rowSTR = db.executesql(record_row, as_dict=True)

    if session.mobile_report_rep_type == 'REP':
        if condition == '':
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='" + session.cid + "' order by cust_name"
        else:
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='" + session.cid + "' order by cust_name "
    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        if condition == '':
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='" + session.cid + "' " + condition_level + " order by cust_name"
        else:
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND H_VET='" + session.cid + "' " + condition_level + " order by cust_name"
    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def customer_wise_monthly_sales_mobile_back():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionCUST = request.vars.posmregionCUST
    session.posmAreaCUST = request.vars.posmAreaCUST
    session.mpi_cust_M = request.vars.mpi_cust_M

    if session.posmregionCUST == None:
        session.posmregionCUST=''
    if session.posmAreaCUST == None:
        session.posmAreaCUST=''
    if session.mpi_cust_M == None:
        session.mpi_cust_M=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionCUST=''
        session.posmAreaCUST = ''
        session.mpi_cust_M = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    # minimum = page * items_per_page
    # maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaCUST != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_area ='" + session.posmAreaCUST + "'"

    if ((session.btn_filter) and (session.posmregionCUST!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "region ='" + session.posmregionCUST + "'"
        else:
            condition = condition + " AND region ='" + session.posmregionCUST + "'"


    if ((session.btn_filter) and (session.mpi_cust_M!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.mpi_cust_M + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.mpi_cust_M + "'"

    if session.mobile_report_rep_type == 'REP':
        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name"
        else:
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name"
    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' "+condition_level+" order by cust_name"
        else:
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND H_VET='"+session.cid+"' "+condition_level+" order by cust_name"



    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = ''
    if session.mobile_report_rep_type == 'REP':
        if condition == '':
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name"
        else:
            record_row_2 = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') AND H_VET='"+session.cid+"' order by cust_name"
    else:
        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' "+condition_level+" order by cust_name"
        else:
            record_row = "SELECT * FROM `navana_mpi_cust_wise_mon_sale_os_vw` WHERE " + str(condition) + "  AND H_VET='"+session.cid+"' "+condition_level+" order by cust_name"



    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def market_wise_monthly_sales():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionMKT = request.vars.posmregionMKT
    session.posmAreaMKT = request.vars.posmAreaMKT
    session.posmTownMKT = request.vars.posmTownMKT

    if session.posmregionMKT == None:
        session.posmregionMKT=''
    if session.posmAreaMKT == None:
        session.posmAreaMKT=''
    if session.posmTownMKT == None:
        session.posmTownMKT=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.posmTownMKT != ''):
            usagesTownList = str(session.posmTownMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmTownMKT = usagesTownList[0]
            else:
                session.posmTownMKT = session.posmTownMKT

        if (session.posmAreaMKT != ''):
            usagesTownList = str(session.posmAreaMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmAreaMKT = usagesTownList[0]
            else:
                session.posmAreaMKT = session.posmAreaMKT

        if (session.posmregionMKT != ''):
            usagesTownList = str(session.posmregionMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmregionMKT = usagesTownList[0]
            else:
                session.posmregionMKT = session.posmregionMKT



        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionMKT=''
        session.posmAreaMKT = ''
        session.posmTownMKT = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaMKT != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaMKT + "'"

    if ((session.btn_filter) and (session.posmregionMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionMKT + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionMKT + "'"


    if ((session.btn_filter) and (session.posmTownMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownMKT + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownMKT + "'"

    if condition=='':
        record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by mkt_desc LIMIT "+str(minimum)+","+str(maximum)+""
    else:
        record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by mkt_desc LIMIT "+str(minimum)+","+str(maximum)+""

    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = ''
    if condition == '':
        record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by mkt_desc"
    else:
        record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by mkt_desc"

    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def download_market_wise_monthly_sales():
    records=''
    if session.posmAreaMKT == None or session.posmAreaMKT == '':
        session.posmAreaMKT = ''

    if session.posmregionMKT == None or session.posmregionMKT == '':
        session.posmregionMKT = ''

    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaMKT != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaMKT + "'"

    if ((session.btn_filter) and (session.posmregionMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionMKT + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionMKT + "'"


    if ((session.btn_filter) and (session.posmTownMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownMKT + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownMKT + "'"

    if condition=='':
        record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' order by mkt_desc"
    else:
        record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' order by mkt_desc"

    record_rowSTR = db.executesql(record_row, as_dict=True)



    records =''
    myString = 'Market wise monthly sales Collection and Outstanding \n\n'

    myString += 'Region ID,Region,Area ID,Area Name,Territory ID,Territory Name,Market Code,Market Name,Sales,Collection,Outstanding\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        mpo_code = recordListStr['mpo_code']
        terri_name = recordListStr['terri_name'].replace(',','')
        mkt_code = recordListStr['mkt_code']
        mkt_desc = recordListStr['mkt_desc'].replace(',','')

        sale_value = round(float(recordListStr['sale_value']), 2)
        coll_value = round(float(recordListStr['coll_value']), 2)
        os_value = round(float(recordListStr['os_value']), 2)


        myString += str(rm_code) + ',' + str(region)+ ',' + str(fm_code)+ ',' + str(fm_area) + ',' + str(mpo_code) + ',' + str(terri_name) + ',' + str(mkt_code)+ ',' + str(mkt_desc) + ',' + str(sale_value) + ',' + str(coll_value)+ ',' + str(os_value) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_Market_wise_monthly_sales.csv'
    return str(myString)


def market_wise_monthly_sales_mobile():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionMKT = request.vars.posmregionMKT
    session.posmAreaMKT = request.vars.posmAreaMKT
    session.posmTownMKT = request.vars.posmTownMKT

    if session.posmregionMKT == None:
        session.posmregionMKT=''
    if session.posmAreaMKT == None:
        session.posmAreaMKT=''
    if session.posmTownMKT == None:
        session.posmTownMKT=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.posmTownMKT != ''):
            usagesTownList = str(session.posmTownMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmTownMKT = usagesTownList[0]
            else:
                session.posmTownMKT = session.posmTownMKT

        if (session.posmAreaMKT != ''):
            usagesTownList = str(session.posmAreaMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmAreaMKT = usagesTownList[0]
            else:
                session.posmAreaMKT = session.posmAreaMKT

        if (session.posmregionMKT != ''):
            usagesTownList = str(session.posmregionMKT).split('|')
            if len(usagesTownList) > 1:
                session.posmregionMKT = usagesTownList[0]
            else:
                session.posmregionMKT = session.posmregionMKT



        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionMKT=''
        session.posmAreaMKT = ''
        session.posmTownMKT = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaMKT != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_code ='" + session.posmAreaMKT + "'"

    if ((session.btn_filter) and (session.posmregionMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "rm_code ='" + session.posmregionMKT + "'"
        else:
            condition = condition + " AND rm_code ='" + session.posmregionMKT + "'"


    if ((session.btn_filter) and (session.posmTownMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.posmTownMKT + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.posmTownMKT + "'"



    if session.mobile_report_rep_type == 'REP':
        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' AND  MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc LIMIT " + str(minimum) + "," + str(maximum) + ""
        else:
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc LIMIT " + str(minimum) + "," + str(maximum) + ""
    else:
        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition == '':
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='" + session.cid + "' "+condition_level+" order by mkt_desc LIMIT " + str(minimum) + "," + str(maximum) + ""
        else:
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str( condition) + " AND H_VET='" + session.cid + "' "+condition_level+"  order by mkt_desc LIMIT " + str(minimum) + "," + str(maximum) + ""

    record_rowSTR = db.executesql(record_row, as_dict=True)



    if session.mobile_report_rep_type == 'REP':
        if condition=='':
            record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' AND  MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc"
        else:
            record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc"
    else:
        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition == '':
            record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='" + session.cid + "' "+condition_level+" order by mkt_desc "
        else:
            record_row_2 = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str( condition) + " AND H_VET='" + session.cid + "' "+condition_level+"  order by mkt_desc "

    record_row_2STR = db.executesql(record_row_2, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_row_2STR=record_row_2STR,record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)




def market_wise_monthly_sales_mobile_back():

    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregionMKT = request.vars.posmregionMKT
    session.posmAreaMKT = request.vars.posmAreaMKT
    session.mpi_code_market_M = request.vars.mpi_code_market_M

    if session.posmregionMKT == None:
        session.posmregionMKT=''
    if session.posmAreaMKT == None:
        session.posmAreaMKT=''
    if session.mpi_code_market_M == None:
        session.mpi_code_market_M=''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregionMKT=''
        session.posmAreaMKT = ''
        session.mpi_code_market_M = ''

        reqPage = 0



    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    # minimum = page * items_per_page
    # maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()


    condition =''
    record_row=''
    if ((session.btn_filter) and (session.posmAreaMKT != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "fm_area ='" + session.posmAreaMKT + "'"

    if ((session.btn_filter) and (session.posmregionMKT!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "region ='" + session.posmregionMKT + "'"
        else:
            condition = condition + " AND region ='" + session.posmregionMKT + "'"


    if ((session.btn_filter) and (session.mpi_code_market_M!='')):
        # qset=qset(db.zrpt_tosc_1.region==session.posmregion)
        if condition=='':
            condition = condition + "mpo_code ='" + session.mpi_code_market_M + "'"
        else:
            condition = condition + " AND mpo_code ='" + session.mpi_code_market_M + "'"


    if session.mobile_report_rep_type == 'REP':
        if condition=='':
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='"+session.cid+"' AND  MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc"
        else:
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str(condition) + " AND H_VET='"+session.cid+"' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  order by mkt_desc"
    else:
        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "


        if condition == '':
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE H_VET='" + session.cid + "' "+condition_level+" order by mkt_desc"
        else:
            record_row = "SELECT * FROM `navana_mpi_mkt_wise_mon_sale_os_vw` WHERE " + str( condition) + " AND H_VET='" + session.cid + "' "+condition_level+"  order by mkt_desc"

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    records = ''
    recCount = 0
    return dict(record_rowSTR=record_rowSTR,regionValue=regionValue,areaValue=areaValue,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def KPI_Prod_Sale_RI_mobile():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.product_regionRI_KPI = request.vars.product_regionRI_KPI
    session.product_codeRI_KPI = request.vars.product_codeRI_KPI

    if session.product_regionRI_KPI == None:
        session.product_regionRI_KPI = ''
    if session.product_regionRI == None:
        session.product_regionRI = ''
    if session.product_codeRI_KPI == None:
        session.product_codeRI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionRI_KPI != ''):
            usagesTownList = str(session.product_regionRI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionRI_KPI = usagesTownList[0]
            else:
                session.product_regionRI_KPI = session.product_regionRI_KPI

        if (session.product_codeRI_KPI != ''):
            usagesTownList = str(session.product_codeRI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeRI_KPI = usagesTownList[0]
            else:
                session.product_codeRI_KPI = session.product_codeRI_KPI

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionRI_KPI = ''
        session.product_regionRI = ''
        session.product_codeRI_KPI = ''

        reqPage = 0
    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI_KPI + "'"
    if ((session.btn_filter) and (session.product_regionRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'



    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,region,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    if session.mobile_report_rep_type == 'REP':
        record_row_2 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,P_CODE,P_DESC"

    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row_2 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') " + condition_level + " GROUP BY rm_code,region,P_CODE,P_DESC"
    # return record_row
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def KPI_Prod_Sale_RI_mobile_back():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.product_regionRI_KPI = request.vars.product_regionRI_KPI
    session.product_codeRI_KPI = request.vars.product_codeRI_KPI

    if session.product_regionRI_KPI == None:
        session.product_regionRI_KPI = ''
    if session.product_regionRI == None:
        session.product_regionRI = ''
    if session.product_codeRI_KPI == None:
        session.product_codeRI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()



    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionRI_KPI = ''
        session.product_regionRI = ''
        session.product_codeRI_KPI = ''


    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI_KPI + "'"
    if ((session.btn_filter) and (session.product_regionRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND region ='" + session.product_regionRI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,P_CODE,P_DESC"

    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,region,P_CODE,P_DESC"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)



def KPI_Prod_Target_vs_Sale_RI():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.product_regionRI_KPI = request.vars.product_regionRI_KPI
    session.product_codeRI_KPI = request.vars.product_codeRI_KPI

    if session.product_regionRI_KPI == None:
        session.product_regionRI_KPI = ''
    if session.product_regionRI == None:
        session.product_regionRI = ''
    if session.product_codeRI_KPI == None:
        session.product_codeRI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionRI_KPI != ''):
            usagesTownList = str(session.product_regionRI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionRI_KPI = usagesTownList[0]
            else:
                session.product_regionRI_KPI = session.product_regionRI_KPI

        if (session.product_codeRI_KPI != ''):
            usagesTownList = str(session.product_codeRI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeRI_KPI = usagesTownList[0]
            else:
                session.product_codeRI_KPI = session.product_codeRI_KPI

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionRI_KPI = ''
        session.product_regionRI = ''
        session.product_codeRI_KPI = ''

        reqPage = 0
    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue
    if regionValue == None:
        regionValue = ''
    if areaValue == None:
        areaValue = ''

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI_KPI + "'"
    if ((session.btn_filter) and (session.product_regionRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,P_CODE,P_DESC ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""
    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "')  GROUP BY rm_code,region,P_CODE,P_DESC"
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)




def download_KPI_Prod_Sale_RI():
    records=''
    if session.product_codeRI_KPI == None or session.product_codeRI_KPI == '':
        session.product_codeRI_KPI = ''

    if session.product_regionRI_KPI == None or session.product_regionRI_KPI == '':
        session.product_regionRI_KPI = ''



    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeRI_KPI + "'"
    if ((session.btn_filter) and (session.product_regionRI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionRI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    record_row = "SELECT rm_code,region,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "')  GROUP BY rm_code,region,P_CODE,P_DESC"

    record_rowSTR = db.executesql(record_row, as_dict=True)


    records =''
    myString = 'KPI Product Sale RI \n\n'

    myString += 'Region_ID,Region Name,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        P_CODE = recordListStr['P_CODE']
        P_DESC = recordListStr['P_DESC'].replace(',','')
        SQNTY = recordListStr['SQNTY']
        sales = round(float(recordListStr['sales']), 2)

        myString += str(rm_code) + ',' + str(region) + ',' + str(P_CODE)+ ',' + str(P_DESC) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_KPI_Prod_Sale_RI.csv'
    return str(myString)



def KPI_Prod_Sale_AI_mobile():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.product_regionAI_KPI = request.vars.product_regionAI_KPI
    session.product_areaAI_KPI = request.vars.product_areaAI_KPI
    session.posmTownCode = request.vars.posmTown
    session.product_codeAI_KPI = request.vars.product_codeAI_KPI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.product_regionAI_KPI == None:
        session.product_regionAI_KPI = ''
    if session.product_areaAI_KPI == None:
        session.product_areaAI_KPI = ''

    if session.product_codeAI_KPI == None:
        session.product_codeAI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionAI_KPI != ''):
            usagesTownList = str(session.product_regionAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionAI_KPI = usagesTownList[0]
            else:
                session.product_regionAI_KPI = session.product_regionAI_KPI

        if (session.product_areaAI_KPI != ''):
            usagesTownList = str(session.product_areaAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_areaAI_KPI = usagesTownList[0]
            else:
                session.product_areaAI_KPI = session.product_areaAI_KPI

        if (session.product_codeAI_KPI != ''):
            usagesTownList = str(session.product_codeAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeAI_KPI = usagesTownList[0]
            else:
                session.product_codeAI_KPI = session.product_codeAI_KPI
        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionAI_KPI = ''
        session.product_areaAI_KPI = ''
        session.product_codeAI_KPI = ''

        reqPage = 0
        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI_KPI + "'"
    if ((session.btn_filter) and (session.product_areaAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI_KPI + "'"
    if ((session.btn_filter) and (session.product_codeAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') " + condition_level + " GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    if session.mobile_report_rep_type == 'REP':
        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level = ''
        if session.level_depth_no == 2:
            condition_level += "AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no == 1:
            condition_level += "AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') " + condition_level + " GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC LIMIT " + str(minimum) + "," + str(maximum) + ""

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def KPI_Prod_Sale_AI_mobile_back():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.product_regionAI_KPI = request.vars.product_regionAI_KPI
    session.product_areaAI_KPI = request.vars.product_areaAI_KPI
    session.posmTownCode = request.vars.posmTown
    session.product_codeAI_KPI = request.vars.product_codeAI_KPI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.product_regionAI_KPI == None:
        session.product_regionAI_KPI = ''
    if session.product_areaAI_KPI == None:
        session.product_areaAI_KPI = ''

    if session.product_codeAI_KPI == None:
        session.product_codeAI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()



    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionAI_KPI = ''
        session.product_areaAI_KPI = ''
        session.product_codeAI_KPI = ''

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND region ='" + session.product_regionAI_KPI + "'"
    if ((session.btn_filter) and (session.product_areaAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_area ='" + session.product_areaAI_KPI + "'"
    if ((session.btn_filter) and (session.product_codeAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "')  GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"
    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+"  GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,P_CODE,P_DESC"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)


def KPI_Prod_Target_vs_Sale_AI():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.product_regionAI_KPI = request.vars.product_regionAI_KPI
    session.product_areaAI_KPI = request.vars.product_areaAI_KPI
    session.posmTownCode = request.vars.posmTown
    session.product_codeAI_KPI = request.vars.product_codeAI_KPI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.product_regionAI_KPI == None:
        session.product_regionAI_KPI = ''
    if session.product_areaAI_KPI == None:
        session.product_areaAI_KPI = ''

    if session.product_codeAI_KPI == None:
        session.product_codeAI_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        if (session.product_regionAI_KPI != ''):
            usagesTownList = str(session.product_regionAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionAI_KPI = usagesTownList[0]
            else:
                session.product_regionAI_KPI = session.product_regionAI_KPI

        if (session.product_areaAI_KPI != ''):
            usagesTownList = str(session.product_areaAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_areaAI_KPI = usagesTownList[0]
            else:
                session.product_areaAI_KPI = session.product_areaAI_KPI

        if (session.product_codeAI_KPI != ''):
            usagesTownList = str(session.product_codeAI_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeAI_KPI = usagesTownList[0]
            else:
                session.product_codeAI_KPI = session.product_codeAI_KPI
        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.product_regionAI_KPI = ''
        session.product_areaAI_KPI = ''
        session.product_codeAI_KPI = ''

        reqPage = 0
        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI_KPI + "'"
    if ((session.btn_filter) and (session.product_areaAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI_KPI + "'"
    if ((session.btn_filter) and (session.product_codeAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""
    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "')  GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC"
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def download_KPI_Prod_Sale_AI():
    records=''
    if session.product_regionAI_KPI == None or session.product_regionAI_KPI == '':
        session.product_regionAI_KPI = ''

    if session.product_areaAI_KPI == None or session.product_areaAI_KPI == '':
        session.product_areaAI_KPI = ''

    if session.product_codeAI_KPI == None or session.product_codeAI_KPI == '':
        session.product_codeAI_KPI = ''
    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_regionAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionAI_KPI + "'"
    if ((session.btn_filter) and (session.product_areaAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaAI_KPI + "'"
    if ((session.btn_filter) and (session.product_codeAI_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeAI_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,fm_code,fm_area,P_CODE,P_DESC"

    record_rowSTR = db.executesql(record_row, as_dict=True)


    records =''
    myString = 'KPI Product Sale AI \n\n'

    myString += 'Region_ID,Region Name,Area_ID,Area Name,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        P_CODE = recordListStr['P_CODE']
        P_DESC = recordListStr['P_DESC'].replace(',','')
        SQNTY = recordListStr['SQNTY']
        sales = round(float(recordListStr['sales']), 2)

        myString += str(rm_code)+ ',' + str(region) + ',' + str(fm_code)+ ',' + str(fm_area)+ ',' + str(P_CODE) + ',' + str(P_DESC) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_KPI_Prod_Sale_AI.csv'
    return str(myString)


def KPI_Prod_Sale_MPI_mobile():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR_KPI = request.vars.product_regionR_KPI
    session.product_areaR_KPI = request.vars.product_areaR_KPI
    session.product_mpoR_KPI = request.vars.product_mpoR_KPI
    session.product_codeR_KPI = request.vars.product_codeR_KPI
    if session.product_regionR_KPI == None:
        session.product_regionR_KPI = ''
    if session.product_areaR_KPI == None:
        session.product_areaR_KPI = ''
    if session.product_mpoR_KPI == None:
        session.product_mpoR_KPI = ''
    if session.product_codeR_KPI == None:
        session.product_codeR_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()
        if (session.product_regionR_KPI != ''):
            usagesTownList = str(session.product_regionR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionR_KPI = usagesTownList[0]
            else:
                session.product_regionR_KPI = session.product_regionR_KPI

        if (session.product_areaR_KPI != ''):
            usagesTownList = str(session.product_areaR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_areaR_KPI = usagesTownList[0]
            else:
                session.product_areaR_KPI = session.product_areaR_KPI
        if (session.product_mpoR_KPI != ''):
            usagesTownList = str(session.product_mpoR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_mpoR_KPI = usagesTownList[0]
            else:
                session.product_mpoR_KPI = session.product_mpoR_KPI

        if (session.product_codeR_KPI != ''):
            usagesTownList = str(session.product_codeR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeR_KPI = usagesTownList[0]
            else:
                session.product_codeR_KPI = session.product_codeR_KPI
        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_codeR_KPI = ''
        session.product_regionR_KPI = ''
        session.product_areaR_KPI = ''
        session.product_mpoR_KPI = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_KPI + "'"

    if ((session.btn_filter) and (session.product_regionR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR_KPI + "'"

    if ((session.btn_filter) and (session.product_areaR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR_KPI + "'"

    if ((session.btn_filter) and (session.product_mpoR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'


    if session.mobile_report_rep_type == 'REP':

        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC ORDER BY region LIMIT " + str(minimum) + "," + str(maximum) + ""

    record_rowSTR = db.executesql(record_row, as_dict=True)



    if session.mobile_report_rep_type == 'REP':

        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC"

    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row_2 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC"

    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)

def KPI_Prod_Sale_MPI_mobile_back():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR_KPI = request.vars.product_regionR_KPI
    session.product_areaR_KPI = request.vars.product_areaR_KPI
    session.product_mpoR_KPI = request.vars.product_mpoR_KPI
    session.product_codeR_KPI = request.vars.product_codeR_KPI
    if session.product_regionR_KPI == None:
        session.product_regionR_KPI = ''
    if session.product_areaR_KPI == None:
        session.product_areaR_KPI = ''
    if session.product_mpoR_KPI == None:
        session.product_mpoR_KPI = ''
    if session.product_codeR_KPI == None:
        session.product_codeR_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_codeR_KPI = ''
        session.product_regionR_KPI = ''
        session.product_areaR_KPI = ''
        session.product_mpoR_KPI = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    # minimum = page * items_per_page
    # maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_KPI + "'"

    if ((session.btn_filter) and (session.product_regionR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND region ='" + session.product_regionR_KPI + "'"

    if ((session.btn_filter) and (session.product_areaR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_area ='" + session.product_areaR_KPI + "'"

    if ((session.btn_filter) and (session.product_mpoR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    if session.mobile_report_rep_type == 'REP':
        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    if session.mobile_report_rep_type == 'REP':
        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"') AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id='" + str(session.mobile_report_rep_id) + "') GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"
    else:

        condition_level =''
        if session.level_depth_no ==2:
            condition_level +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
        elif session.level_depth_no ==1:
            condition_level +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        record_row_2 = "SELECT rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' " + str(condition) + " AND human_vet='" + session.cid + "' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='" + session.cid + "') "+condition_level+" GROUP BY rm_code,fm_code,fm_area,region,territory_name,MPO_CODE,P_CODE,P_DESC"

    # return record_row_2
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def KPI_Prod_Target_vs_Sale_MPI():
    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.product_regionR_KPI = request.vars.product_regionR_KPI
    session.product_areaR_KPI = request.vars.product_areaR_KPI
    session.product_mpoR_KPI = request.vars.product_mpoR_KPI
    session.product_codeR_KPI = request.vars.product_codeR_KPI
    if session.product_regionR_KPI == None:
        session.product_regionR_KPI = ''
    if session.product_areaR_KPI == None:
        session.product_areaR_KPI = ''
    if session.product_mpoR_KPI == None:
        session.product_mpoR_KPI = ''
    if session.product_codeR_KPI == None:
        session.product_codeR_KPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()
        if (session.product_regionR_KPI != ''):
            usagesTownList = str(session.product_regionR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_regionR_KPI = usagesTownList[0]
            else:
                session.product_regionR_KPI = session.product_regionR_KPI

        if (session.product_areaR_KPI != ''):
            usagesTownList = str(session.product_areaR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_areaR_KPI = usagesTownList[0]
            else:
                session.product_areaR_KPI = session.product_areaR_KPI
        if (session.product_mpoR_KPI != ''):
            usagesTownList = str(session.product_mpoR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_mpoR_KPI = usagesTownList[0]
            else:
                session.product_mpoR_KPI = session.product_mpoR_KPI

        if (session.product_codeR_KPI != ''):
            usagesTownList = str(session.product_codeR_KPI).split('|')
            if len(usagesTownList) > 1:
                session.product_codeR_KPI = usagesTownList[0]
            else:
                session.product_codeR_KPI = session.product_codeR_KPI
        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.product_codeR_KPI = ''
        session.product_regionR_KPI = ''
        session.product_areaR_KPI = ''
        session.product_mpoR_KPI = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_KPI + "'"

    if ((session.btn_filter) and (session.product_regionR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR_KPI + "'"

    if ((session.btn_filter) and (session.product_areaR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR_KPI + "'"

    if ((session.btn_filter) and (session.product_mpoR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)

    record_row_2 = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC"
    # return record_row
    record_rowSTR_2 = db.executesql(record_row_2, as_dict=True)

    records=''
    recCount=0
    return dict(record_rowSTR_2=record_rowSTR_2,record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def download_KPI_Prod_Sale_MPI():
    records=''
    if session.product_codeR_KPI == None or session.product_codeR_KPI == '':
        session.product_codeR_KPI = ''

    if session.product_regionR_KPI == None or session.product_regionR_KPI == '':
        session.product_regionR_KPI = ''

    if session.product_areaR_KPI == None or session.product_areaR_KPI == '':
        session.product_areaR_KPI = ''

    if session.product_mpoR_KPI == None or session.product_mpoR_KPI == '':
        session.product_mpoR_KPI = ''

    condition = ''
    record_row = ''
    if ((session.btn_filter) and (session.product_codeR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND P_CODE ='" + session.product_codeR_KPI + "'"

    if ((session.btn_filter) and (session.product_regionR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND rm_code ='" + session.product_regionR_KPI + "'"

    if ((session.btn_filter) and (session.product_areaR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND fm_code ='" + session.product_areaR_KPI + "'"

    if ((session.btn_filter) and (session.product_mpoR_KPI != '')):
        # qset = qset(db.zrpt_tosc_1.fm_area == session.posmArea)
        condition = condition + "AND MPO_CODE ='" + session.product_mpoR_KPI + "'"

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    record_row = "SELECT rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC,SUM(`SQNTY`) AS SQNTY,SUM((`SQNTY` * `TP_VAL`)) AS sales FROM `navana_mpi_prod_dt_wise_vw`WHERE mnyr>='"+current_date_strat+"' AND mnyr<'"+current_date_end+"' "+ str(condition) +" AND human_vet='"+session.cid+"' AND P_CODE IN (SELECT `P_CODE` FROM `navana_focused_product_list_vw` WHERE H_VET='"+session.cid+"')  GROUP BY rm_code,region,fm_code,fm_area,MPO_CODE,territory_name,P_CODE,P_DESC"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)


    records =''
    myString = 'KPI Product Sale MPI \n\n'

    myString += 'Region_ID,Region Name,Area_ID,Area Name,Territory ID,Territory,Product Code,Product Name,QTY,Sales\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]

        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        MPO_CODE = recordListStr['MPO_CODE']
        territory_name = recordListStr['territory_name'].replace(',','')
        P_CODE = recordListStr['P_CODE']
        P_DESC = recordListStr['P_DESC'].replace(',','')
        SQNTY = recordListStr['SQNTY']
        sales = round(float(recordListStr['sales']), 2)

        myString += str(rm_code)+ ',' + str(region) + ',' + str(fm_code)+ ',' + str(fm_area)+ ',' + str(MPO_CODE)+ ',' + str(territory_name)+ ',' + str(P_CODE) + ',' + str(P_DESC) + ',' + str(SQNTY) + ',' + str(sales) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_KPI_Prod_Sale_MPI.csv'
    return str(myString)




def summary_allocation_data_AI():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.region_allocation_data_AI = request.vars.region_allocation_data_AI
    session.area_allocation_data_AI = request.vars.area_allocation_data_AI
    session.ppm_allocation_data_AI = request.vars.ppm_allocation_data_AI
    session.product_codeAI_KPI = request.vars.product_codeAI_KPI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.region_allocation_data_AI == None:
        session.region_allocation_data_AI = ''
    if session.area_allocation_data_AI == None:
        session.area_allocation_data_AI = ''

    if session.ppm_allocation_data_AI == None:
        session.ppm_allocation_data_AI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.region_allocation_data_AI = ''
        session.area_allocation_data_AI = ''
        session.ppm_allocation_data_AI = ''

        reqPage = 0

        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''

    current_date_strat = str(current_date)[:7] + '-' + '01'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'



    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:

        if (session.ppm_allocation_data_AI != ''):
            usagesTownList = str(session.ppm_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_AI = usagesTownList[0]
            else:
                session.ppm_allocation_data_AI = session.ppm_allocation_data_AI

        if (session.area_allocation_data_AI != ''):
            usagesTownList = str(session.area_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_AI = usagesTownList[0]
            else:
                session.area_allocation_data_AI = session.area_allocation_data_AI

        if (session.region_allocation_data_AI != ''):
            usagesTownList = str(session.region_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_AI = usagesTownList[0]
            else:
                session.region_allocation_data_AI = session.region_allocation_data_AI

        if session.region_allocation_data_AI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_AI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_AI + '"'

        if session.area_allocation_data_AI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_AI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'

        if session.ppm_allocation_data_AI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_AI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'

    record_row = "SELECT rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code,region,fm_code,fm_area,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)





def summary_allocation_data_AI_mobile():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.region_allocation_data_AI = request.vars.region_allocation_data_AI
    session.area_allocation_data_AI = request.vars.area_allocation_data_AI
    session.ppm_allocation_data_AI = request.vars.ppm_allocation_data_AI
    session.product_codeAI_KPI = request.vars.product_codeAI_KPI

    session.product_regionAI = request.vars.product_regionAI
    session.product_areaAI = request.vars.product_areaAI

    if session.region_allocation_data_AI == None:
        session.region_allocation_data_AI = ''
    if session.area_allocation_data_AI == None:
        session.area_allocation_data_AI = ''

    if session.ppm_allocation_data_AI == None:
        session.ppm_allocation_data_AI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.region_allocation_data_AI = ''
        session.area_allocation_data_AI = ''
        session.ppm_allocation_data_AI = ''

        reqPage = 0

        # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1

    qset = db()

    condition = ''
    record_row = ''

    current_date_strat = str(current_date)[:7] + '-' + '01'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'



    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:

        if (session.ppm_allocation_data_AI != ''):
            usagesTownList = str(session.ppm_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_AI = usagesTownList[0]
            else:
                session.ppm_allocation_data_AI = session.ppm_allocation_data_AI

        if (session.area_allocation_data_AI != ''):
            usagesTownList = str(session.area_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_AI = usagesTownList[0]
            else:
                session.area_allocation_data_AI = session.area_allocation_data_AI

        if (session.region_allocation_data_AI != ''):
            usagesTownList = str(session.region_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_AI = usagesTownList[0]
            else:
                session.region_allocation_data_AI = session.region_allocation_data_AI

        if session.region_allocation_data_AI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_AI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_AI + '"'

        if session.area_allocation_data_AI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_AI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'

        if session.ppm_allocation_data_AI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_AI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    # record_row = "SELECT rm_code,region,fm_code,fm_area, REP_ID, ITEM_ID, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,EMPNO AS REP_ID, PPM_CODE  AS ITEM_ID, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code,region,fm_code,fm_area,EMPNO, PPM_CODE UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, ITEM_ID UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, item_id UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,REP_ID, item_id) AS T GROUP BY rm_code,region,fm_code,fm_area, REP_ID, ITEM_ID LIMIT "+str(minimum)+","+str(maximum)+""
    record_row = "SELECT rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code,region,fm_code,fm_area,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def summary_allocation_data_AI_mobile_back():
    response.title = 'M-Reporting'

    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all


    search_form = SQLFORM(db.sm_search_date)
    session.ppm_allocation_data_AI_M = request.vars.ppm_allocation_data_AI_M
    session.area_allocation_data_AI_M = request.vars.area_allocation_data_AI_M
    session.region_allocation_data_AI_M = request.vars.region_allocation_data_AI_M

    if session.region_allocation_data_AI_M == None:
        session.region_allocation_data_AI_M = ''
    if session.area_allocation_data_AI_M == None:
        session.area_allocation_data_AI_M = ''

    if session.ppm_allocation_data_AI_M == None:
        session.ppm_allocation_data_AI_M = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()



    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.ppm_allocation_data_AI_M = ''
        session.area_allocation_data_AI_M = ''
        session.region_allocation_data_AI_M = ''

    qset = db()

    condition = ''
    record_row = ''
    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'

    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'


    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:
        if session.region_allocation_data_AI_M != '':
            condition += ' and  rm_code="' + session.region_allocation_data_AI_M + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_AI_M + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_AI_M + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_AI_M + '"'

        if session.area_allocation_data_AI_M != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_AI_M + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_AI_M + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_AI_M + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_AI_M + '"'

        if session.ppm_allocation_data_AI_M != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_AI_M + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_AI_M + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_AI_M + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_AI_M + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    record_row = "SELECT region,area, REP_ID, ITEM_ID, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code as region,fm_code as area,EMPNO AS REP_ID, PPM_CODE  AS ITEM_ID, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code,fm_code,EMPNO, PPM_CODE UNION SELECT  level1_id as rigion,level2_id as area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + "  GROUP BY level1_id,level2_id, REP_ID, ITEM_ID UNION SELECT level1_id as rigion,level2_id as area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level2_id, REP_ID, item_id UNION SELECT level1_id as rigion,level2_id as area, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level2_id,REP_ID, item_id) AS T GROUP BY region,area,REP_ID, ITEM_ID"

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)
    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records,recCount=recCount,search_form=search_form)



def download_summary_allocation_data_AI():

    if session.region_allocation_data_AI == None:
        session.region_allocation_data_AI = ''
    if session.area_allocation_data_AI == None:
        session.area_allocation_data_AI = ''

    if session.ppm_allocation_data_AI == None:
        session.ppm_allocation_data_AI = ''

    qset = db()

    condition = ''
    record_row = ''

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.region_allocation_data_AI == '':
        session.flash = 'Required Region Filter'
        redirect(URL('zrpt_tosc', 'summary_allocation_data_AI'))

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:


        if (session.ppm_allocation_data_AI != ''):
            usagesTownList = str(session.ppm_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_AI = usagesTownList[0]
            else:
                session.ppm_allocation_data_AI = session.ppm_allocation_data_AI

        if (session.area_allocation_data_AI != ''):
            usagesTownList = str(session.area_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_AI = usagesTownList[0]
            else:
                session.area_allocation_data_AI = session.area_allocation_data_AI

        if (session.region_allocation_data_AI != ''):
            usagesTownList = str(session.region_allocation_data_AI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_AI = usagesTownList[0]
            else:
                session.region_allocation_data_AI = session.region_allocation_data_AI

        if session.region_allocation_data_AI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_AI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_AI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_AI + '"'

        if session.area_allocation_data_AI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_AI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_AI + '"'

        if session.ppm_allocation_data_AI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_AI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_AI + '"'

    record_row = "SELECT rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,EMPNO AS REP_ID,ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code,region,fm_code,fm_area,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area, REP_ID, rep_name, ITEM_ID,item_name"

    record_rowSTR = db.executesql(record_row, as_dict=True)


    records =''
    myString = 'Allocation and Usage AI \n\n'

    myString += 'Region ID,Region,Area ID,Area Name,REP ID,REP Name,ITEM_ID,ITEM Name,Allocation Qty,Usage QTY,Gift QTY,PPM QTY,Sample QTY\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        REP_ID = recordListStr['REP_ID']
        rep_name = recordListStr['rep_name'].replace(',','')
        ITEM_ID = recordListStr['ITEM_ID']
        item_name = recordListStr['item_name'].replace(',','')
        allocation = recordListStr['allocation']

        gift = recordListStr['gift']
        ppm = recordListStr['ppm']
        sample = recordListStr['sample']
        Usage_qty = gift + ppm + sample
        myString += str(rm_code) + ',' + str(region)+ ',' + str(fm_code)+ ',' + str(fm_area) + ',' + str(REP_ID)+ ',' + str(rep_name)+ ',' + str(ITEM_ID)+ ',' + str(item_name) + ',' + str(allocation) + ',' + str(Usage_qty) + ',' + str(gift) + ',' + str(ppm) + ',' + str(sample) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_allocation_Usage_AI.csv'
    return str(myString)


def summary_allocation_data_MPI():

    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.region_allocation_data_MPI = request.vars.region_allocation_data_MPI
    session.area_allocation_data_MPI = request.vars.area_allocation_data_MPI
    session.mpi_allocation_data_MPI = request.vars.mpi_allocation_data_MPI
    session.ppm_allocation_data_MPI = request.vars.ppm_allocation_data_MPI
    if session.region_allocation_data_MPI == None:
        session.region_allocation_data_MPI = ''
    if session.area_allocation_data_MPI == None:
        session.area_allocation_data_MPI = ''
    if session.mpi_allocation_data_MPI == None:
        session.mpi_allocation_data_MPI = ''
    if session.ppm_allocation_data_MPI == None:
        session.ppm_allocation_data_MPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.region_allocation_data_MPI = ''
        session.area_allocation_data_MPI = ''
        session.mpi_allocation_data_MPI = ''
        session.ppm_allocation_data_MPI = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:


        if (session.ppm_allocation_data_MPI != ''):
            usagesTownList = str(session.ppm_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_MPI = usagesTownList[0]
            else:
                session.ppm_allocation_data_MPI = session.ppm_allocation_data_MPI

        if (session.area_allocation_data_MPI != ''):
            usagesTownList = str(session.area_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_MPI = usagesTownList[0]
            else:
                session.area_allocation_data_MPI = session.area_allocation_data_MPI

        if (session.region_allocation_data_MPI != ''):
            usagesTownList = str(session.region_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_MPI = usagesTownList[0]
            else:
                session.region_allocation_data_MPI = session.region_allocation_data_MPI

        if session.region_allocation_data_MPI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_MPI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'

        if session.area_allocation_data_MPI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_MPI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'

        if session.ppm_allocation_data_MPI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_MPI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'

    record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME as territory,EMPNO AS REP_ID, ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)


    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)



def summary_allocation_data_MPI_mobile():

    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.region_allocation_data_MPI = request.vars.region_allocation_data_MPI
    session.area_allocation_data_MPI = request.vars.area_allocation_data_MPI
    session.mpi_allocation_data_MPI = request.vars.mpi_allocation_data_MPI
    session.ppm_allocation_data_MPI = request.vars.ppm_allocation_data_MPI
    if session.region_allocation_data_MPI == None:
        session.region_allocation_data_MPI = ''
    if session.area_allocation_data_MPI == None:
        session.area_allocation_data_MPI = ''
    if session.mpi_allocation_data_MPI == None:
        session.mpi_allocation_data_MPI = ''
    if session.ppm_allocation_data_MPI == None:
        session.ppm_allocation_data_MPI = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.region_allocation_data_MPI = ''
        session.area_allocation_data_MPI = ''
        session.mpi_allocation_data_MPI = ''
        session.ppm_allocation_data_MPI = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 20
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    minimum = page * items_per_page
    maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''
    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:


        if (session.ppm_allocation_data_MPI != ''):
            usagesTownList = str(session.ppm_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_MPI = usagesTownList[0]
            else:
                session.ppm_allocation_data_MPI = session.ppm_allocation_data_MPI

        if (session.area_allocation_data_MPI != ''):
            usagesTownList = str(session.area_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_MPI = usagesTownList[0]
            else:
                session.area_allocation_data_MPI = session.area_allocation_data_MPI

        if (session.region_allocation_data_MPI != ''):
            usagesTownList = str(session.region_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_MPI = usagesTownList[0]
            else:
                session.region_allocation_data_MPI = session.region_allocation_data_MPI

        if session.region_allocation_data_MPI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_MPI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'

        if session.area_allocation_data_MPI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_MPI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'

        if session.ppm_allocation_data_MPI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_MPI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME as territory,EMPNO AS REP_ID, ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name ORDER BY region LIMIT "+str(minimum)+","+str(maximum)+""

    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)


    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)




def summary_allocation_data_MPI_mobile_back():

    response.title = 'M-Reporting'
    reqPage = len(request.args)
    btn_filter = request.vars.btn_filter
    btn_all = request.vars.btn_all
    reqPage = len(request.args)

    search_form = SQLFORM(db.sm_search_date)
    session.posmregion = request.vars.posmregion
    session.posmArea = request.vars.posmArea
    session.posmTownCode = request.vars.posmTown

    session.region_allocation_data_MPI = request.vars.region_allocation_data_MPI
    session.area_allocation_data_MPI = request.vars.area_allocation_data_MPI
    session.mpi_allocation_data_MPI = request.vars.mpi_allocation_data_MPI
    session.ppm_allocation_data_MPI_M = request.vars.ppm_allocation_data_MPI_M
    if session.region_allocation_data_MPI == None:
        session.region_allocation_data_MPI = ''
    if session.area_allocation_data_MPI == None:
        session.area_allocation_data_MPI = ''
    if session.mpi_allocation_data_MPI == None:
        session.mpi_allocation_data_MPI = ''
    if session.ppm_allocation_data_MPI_M == None:
        session.ppm_allocation_data_MPI_M = ''

    if btn_filter:
        session.btn_filter = btn_filter
        session.searchTypePOSM = str(request.vars.searchTypePOSM).strip()
        session.searchValuePOSM = str(request.vars.searchValuePOSM).strip()

        reqPage = 0

    elif btn_all:
        session.btn_filter = None
        session.searchTypePOSM = None
        session.searchValuePOSM = None
        session.posmregion = ''
        session.posmArea = ''
        session.region_allocation_data_MPI = ''
        session.area_allocation_data_MPI = ''
        session.mpi_allocation_data_MPI = ''
        session.ppm_allocation_data_MPI_M = ''

        reqPage = 0

    # --------paging
    if reqPage:
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = session.items_per_page
    # limitby = (page * items_per_page, (page + 1) * items_per_page + 1)

    # minimum = page * items_per_page
    # maximum = (page + 1) * items_per_page + 1
    # --------end paging
    regionValue = request.vars.regionValue
    areaValue = request.vars.areaValue

    qset = db()

    condition = ''
    record_row = ''

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:
        if session.ppm_allocation_data_MPI_M != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_MPI_M + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_MPI_M + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_MPI_M + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_MPI_M + '"'

    if session.mobile_report_rep_type == 'REP':
        condition += ' AND MPO_CODE IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition1 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition2 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'
        condition3 += ' AND route_id IN (SELECT area_id FROM sm_rep_area WHERE rep_id="' + str(session.mobile_report_rep_id) + '")'

    if session.mobile_report_rep_type == 'SUP':
        if session.level_depth_no ==2:
            condition +="AND  fm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level2_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

        elif session.level_depth_no ==1:
            condition +="AND  rm_code IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition1 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition2 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "
            condition3 += "AND  level1_id IN (SELECT level_id FROM sm_supervisor_level WHERE sup_id='" + str(session.mobile_report_rep_id) + "') "

    record_row = "SELECT region,area,territory, REP_ID, ITEM_ID, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code as region,fm_code as area,MPO_CODE as territory,EMPNO AS REP_ID, PPM_CODE  AS ITEM_ID, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + "  GROUP BY rm_code,fm_code,MPO_CODE,EMPNO, PPM_CODE UNION SELECT  level1_id as rigion,level2_id as area,route_id as territory, REP_ID, ITEM_ID, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level2_id,route_id, REP_ID, ITEM_ID UNION SELECT level1_id as rigion,level2_id as area,route_id as territory, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + "  GROUP BY level1_id,level2_id,route_id, REP_ID, item_id UNION SELECT level1_id as rigion,level2_id as area,route_id as territory, REP_ID, ITEM_ID, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + " GROUP BY level1_id,level2_id,route_id,REP_ID, item_id) AS T GROUP BY region,area,territory,REP_ID, ITEM_ID"
    # return record_row
    record_rowSTR = db.executesql(record_row, as_dict=True)


    records=''
    recCount=0
    return dict(record_rowSTR=record_rowSTR,records=records, page=page, items_per_page=items_per_page,recCount=recCount,search_form=search_form)


def download_summary_allocation_data_MPI():

    if session.region_allocation_data_MPI == None:
        session.region_allocation_data_MPI = ''
    if session.area_allocation_data_MPI == None:
        session.area_allocation_data_MPI = ''
    if session.mpi_allocation_data_MPI == None:
        session.mpi_allocation_data_MPI = ''
    if session.ppm_allocation_data_AI == None:
        session.ppm_allocation_data_AI = ''

    qset = db()

    condition = ''
    record_row = ''

    current_date_strat = str(current_date)[:7] + '-' + '01'
    # current_date_end = str(current_date)[:7] + '-' + '31'
    last_mont_from_date2 = add_months(datetime.datetime.strptime(str(current_date), '%Y-%m-%d'), 1)
    current_date_end = str(last_mont_from_date2)[:7] + '-' + '01'
    if session.region_allocation_data_MPI == '':
        session.flash = 'Required Region Filter'
        redirect(URL('zrpt_tosc', 'summary_allocation_data_MPI'))

    condition = ''
    condition1 = ''
    condition2 = ''
    condition3 = ''

    if session.btn_filter:

        if (session.ppm_allocation_data_MPI != ''):
            usagesTownList = str(session.ppm_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.ppm_allocation_data_MPI = usagesTownList[0]
            else:
                session.ppm_allocation_data_MPI = session.ppm_allocation_data_MPI

        if (session.area_allocation_data_MPI != ''):
            usagesTownList = str(session.area_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.area_allocation_data_MPI = usagesTownList[0]
            else:
                session.area_allocation_data_MPI = session.area_allocation_data_MPI

        if (session.region_allocation_data_MPI != ''):
            usagesTownList = str(session.region_allocation_data_MPI).split('|')
            if len(usagesTownList) > 1:
                session.region_allocation_data_MPI = usagesTownList[0]
            else:
                session.region_allocation_data_MPI = session.region_allocation_data_MPI

        if session.region_allocation_data_MPI != '':
            condition += ' and  rm_code="' + session.region_allocation_data_MPI + '"'
            condition1 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition2 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'
            condition3 += ' and  level1_id="' + session.region_allocation_data_MPI + '"'

        if session.area_allocation_data_MPI != '':
            condition += ' and  fm_code ="' + session.area_allocation_data_MPI + '"'
            condition1 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition2 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'
            condition3 += ' and  level2_id ="' + session.area_allocation_data_MPI + '"'

        if session.ppm_allocation_data_MPI != '':
            condition += ' and  PPM_CODE ="' + session.ppm_allocation_data_MPI + '"'
            condition1 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition2 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'
            condition3 += ' and  item_id ="' + session.ppm_allocation_data_MPI + '"'

    record_row = "SELECT rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name, SUM(ALLO_QTY) as allocation, SUM(GIFT_QTY) as gift, SUM(PPM_QTY) as ppm, SUM(SAMPLE_QTY) as sample FROM (SELECT rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME as territory,EMPNO AS REP_ID, ENAME as rep_name, PPM_CODE  AS ITEM_ID,PPM_DESC as item_name, SUM(ISSUE_QNTY) AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `navana_sample_allow` WHERE mnyr>='" + current_date_strat + "' AND mnyr<'" + current_date_end + "' AND H_VET='" + session.cid + "' " + condition + " GROUP BY rm_code, region,fm_code, fm_area,MPO_CODE,TERRI_NAME,EMPNO,ENAME, PPM_CODE,PPM_DESC UNION SELECT  level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, SUM(item_qty) AS GIFT_QTY, 0 AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_gift` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition1 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, SUM(item_qty) AS PPM_QTY, 0 AS SAMPLE_QTY FROM `sm_doc_visit_ppm` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition2 + " GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name, REP_ID, rep_name, ITEM_ID,item_name UNION SELECT level1_id  as rm_code,level1_name as rigion,level2_id as fm_code,level2_name as fm_area,route_id as mpo_code,route_name as territory, REP_ID, rep_name, ITEM_ID,item_name, 0 AS ALLO_QTY, 0 AS GIFT_QTY, 0 AS PPM_QTY, SUM(qty) AS SAMPLE_QTY FROM `sm_doc_visit_sample` WHERE visit_date>='" + current_date_strat + "' AND visit_date<'" + current_date_end + "' AND cid='" + session.cid + "' " + condition3 + "  GROUP BY level1_id,level1_name,level2_id,level2_name,route_id,route_name,REP_ID, rep_name, ITEM_ID,item_name) AS T GROUP BY rm_code,region,fm_code,fm_area,mpo_code,territory, REP_ID, rep_name, ITEM_ID,item_name"

    record_rowSTR = db.executesql(record_row, as_dict=True)

    records =''
    myString = 'Allocation and Usage MPI \n\n'

    myString += 'Region ID,Region Name,Area ID,Area Name,Territory ID,Territory Name,REP ID,REP Name,ITEM_ID,ITEM Name,Allocation Qty,Usage QTY,Gift QTY,PPM QTY,Sample QTY\n'

    for i in range(len(record_rowSTR)):
        recordListStr = record_rowSTR[i]
        rm_code = recordListStr['rm_code']
        region = recordListStr['region']
        fm_code = recordListStr['fm_code']
        fm_area = recordListStr['fm_area'].replace(',','')
        mpo_code = recordListStr['mpo_code']
        territory = recordListStr['territory'].replace(',','')
        REP_ID = recordListStr['REP_ID']
        rep_name = recordListStr['rep_name'].replace(',','')
        ITEM_ID = recordListStr['ITEM_ID']
        item_name = recordListStr['item_name'].replace(',','')
        allocation = recordListStr['allocation']

        gift = recordListStr['gift']
        ppm = recordListStr['ppm']
        sample = recordListStr['sample']
        Usage_qty = gift + ppm + sample
        myString += str(rm_code) + ',' + str(region)+ ',' + str(fm_code)+ ',' + str(fm_area) + ',' + str(mpo_code) + ',' + str(territory) + ',' + str(REP_ID)+ ',' + str(rep_name) + ',' + str(ITEM_ID)+ ',' + str(item_name) + ',' + str(allocation) + ',' + str(Usage_qty) + ',' + str(gift) + ',' + str(ppm) + ',' + str(sample) + '\n'
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=download_allocation_Usage_MPI.csv'
    return str(myString)
