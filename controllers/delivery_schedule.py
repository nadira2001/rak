def delivery_schedule():    
	cid=session.cid	
	year=str(request.vars.year).strip()
	month=str(request.vars.month).strip()	
	branch_name=str(request.vars.del_depot).strip()
	# return branch_name
	
	btn_set=request.vars.btn_set 	
	session.year=year
	session.month=month
	session.branch_name=branch_name

	branch_code=''
	depot_id=''
	chkbCode=db((db.sm_depot.cid==cid) & (db.sm_depot.name==branch_name)).select(db.sm_depot.depot_id,limitby=(0,1))        	    
	# return chkbCode
	if chkbCode:
		depot_id=chkbCode[0].depot_id
	session.branch_code=depot_id
		
	if year=='' or month=='':               
		response.flash='Valid Year-Month required'
	else:
		first_date=year+'-'+month+'-01'
    
	
	if  year!='' and month!='' and btn_set=='Set Schedule':		
		chkIDRows=db((db.delivery_schedule_format.cid==cid) & (db.delivery_schedule_format.year==year) & (db.delivery_schedule_format.month==month)& (db.delivery_schedule_format.branch_name==branch_name)).select(db.delivery_schedule_format.year,db.delivery_schedule_format.month,limitby=(0,1))        	    
		# return chkIDRows
		
		if not chkIDRows:
			session.flash='Added Successfully' 					
			redirect(URL(c='delivery_schedule',f='delivery_schedule_add',vars=dict(year=year,month=month,branch_name=branch_name)))    			
		else:			
			session.flash='Already Added' 
			records=db((db.delivery_schedule_format.cid==cid) & (db.delivery_schedule_format.year==year) & (db.delivery_schedule_format.month==month) & (db.delivery_schedule_format.branch_name==branch_name)).select(db.delivery_schedule_format.ALL,orderby=db.delivery_schedule_format.id)						
			# return records
			redirect(URL(c='delivery_schedule',f='delivery_schedule_add',vars=dict(year=year,month=month,branch_name=branch_name)))		
	
	depotRows = db((db.sm_depot.cid == cid) ).select(db.sm_depot.name, db.sm_depot.depot_id, orderby=db.sm_depot.name)
      							
	
	return dict(depotRows=depotRows)


def delivery_schedule_add():	
	cid=session.cid	
	branch_code=session.branch_code
	year=str(request.vars.year).strip()
	month=str(request.vars.month).strip()
	branch_name=str(request.vars.branch_name).strip()
	

	response.title='Delivery Schedule'
	depot_id=str(request.vars.delivery_schedule_format_belt_name)

	d_man_id=str(request.vars.delivery_schedule_format_sallary_id)
	
	
	if str(depot_id)=='None':
		depot_id_C=''
		belt_name=''		
	else:	
		depot_id_C=depot_id.strip().split('|')[0]		
		belt_name=depot_id.strip().split('|')[1]

	if str(d_man_id)=='None':
		d_man_id_C=''
		d_man_name=''		
	else:	
		d_man_id_C=d_man_id.strip().split('|')[0]		
		# return d_man_id_C
		d_man_name=d_man_id.strip().split('|')[1]
		
    
	belt_category=''
	belt_id=''	
	beltRows = db((db.sm_depot_belt.cid == cid)& (db.sm_depot_belt.depot_id == depot_id_C) ).select(db.sm_depot_belt.field1, db.sm_depot_belt.note, orderby=db.sm_depot_belt.depot_id)
	if beltRows:
		belt_category=beltRows[0].note
		belt_id=beltRows[0].field1
		
	
	dp_type=''
	dpRows = db((db.sm_delivery_man.cid == cid)& (db.sm_delivery_man.d_man_id == d_man_id_C) ).select(db.sm_delivery_man.name, db.sm_delivery_man.field1, orderby=db.sm_delivery_man.name)
	if dpRows:		
		dp_type=dpRows[0].field1
	
	form =SQLFORM(db.delivery_schedule_format,
                  fields=['field1'],
                  submit_button='Save'          
                  )
	
	form.vars.year=session.year
	form.vars.month=session.month
	form.vars.branch_code=session.branch_code
	form.vars.branch_name=session.branch_name
	
	form.vars.belt_id=belt_id
	form.vars.belt_name=belt_name
	form.vars.belt_category=belt_category
	
	form.vars.sallary_id=d_man_id_C
	form.vars.dp_name_designation=d_man_name
	form.vars.type_van_man=dp_type

	if form.accepts(request.vars,session):
		response.flash = 'Saved Successfully'


	btn_sve=request.vars.btn_sve
	
	day_1=str(request.vars.d_1)	
	day_2=str(request.vars.d_2)
	day_3=str(request.vars.d_3)
	day_4=str(request.vars.d_4)
	day_5=str(request.vars.d_5)
	day_6=str(request.vars.d_6)
	day_7=str(request.vars.d_7)
	day_8=str(request.vars.d_8)
	day_9=str(request.vars.d_9)
	day_10=str(request.vars.d_10)
	day_11=str(request.vars.d_11)
	day_12=str(request.vars.d_12)
	day_13=str(request.vars.d_13)
	day_14=str(request.vars.d_14)
	day_15=str(request.vars.d_15)
	day_16=str(request.vars.d_16)
	day_17=str(request.vars.d_17)
	day_18=str(request.vars.d_18)
	day_19=str(request.vars.d_19)
	day_20=str(request.vars.d_20)
	day_21=str(request.vars.d_21)
	day_22=str(request.vars.d_22)
	day_23=str(request.vars.d_23)
	day_24=str(request.vars.d_24)
	day_25=str(request.vars.d_25)
	day_26=str(request.vars.d_26)
	day_27=str(request.vars.d_27)
	day_28=str(request.vars.d_28)
	day_29=str(request.vars.d_29)
	day_30=str(request.vars.d_30)
	day_31=str(request.vars.d_31)



	if day_1=='None':
		day_1=0
	if day_2=='None':
		day_2=0
	if day_3=='None':
		day_3=0
	if day_4=='None':
		day_4=0
	if day_5=='None':
		day_5=0
	if day_6=='None':
		day_6=0
	if day_7=='None':
		day_7=0
	if day_8=='None':
		day_8=0
	if day_9=='None':
		day_9=0
	if day_10=='None':
		day_10=0
	if day_11=='None':
		day_11=0
	if day_12=='None':
		day_12=0
	if day_13=='None':
		day_13=0
	if day_14=='None':
		day_14=0
	if day_15=='None':
		day_15=0
	if day_16=='None':
		day_16=0
	if day_17=='None':
		day_17=0
	if day_18=='None':
		day_18=0
	if day_19=='None':
		day_19=0
	if day_20=='None':
		day_20=0
	if day_21=='None':
		day_21=0
	if day_22=='None':
		day_22=0
	if day_23=='None':
		day_23=0
	if day_24=='None':
		day_24=0
	if day_25=='None':
		day_25=0
	if day_26=='None':
		day_26=0
	if day_27=='None':
		day_27=0
	if day_28=='None':
		day_28=0
	if day_29=='None':
		day_29=0
	if day_30=='None':
		day_30=0
	if day_31=='None':
		day_31=0
	

	f2_d_qnt=str(request.vars.f2_d_qnt)
	f3_d_qnt=str(request.vars.f3_d_qnt)
	f4_d_qnt=str(request.vars.f4_d_qnt)
	f5_d_qnt=str(request.vars.f5_d_qnt)
	# return f2_d_qnt
	if f2_d_qnt=='':
		f2_d_qnt=0
	if f3_d_qnt=='':
		f3_d_qnt=0
	if f4_d_qnt=='':
		f4_d_qnt=0
	if f5_d_qnt=='':
		f5_d_qnt=0





	ord_sub_time=str(request.vars.ord_sub_time)
	# return ord_sub_time

	f1_st=str(request.vars.f1_st)
	f2_nd=str(request.vars.f2_nd)
	f3_rd=str(request.vars.f3_rd)
	f4_th=str(request.vars.f4_th)
	f5_th=str(request.vars.f5_th)
	f6_th=str(request.vars.f6_th)
	f7_th=str(request.vars.f7_th)
	f8_th=str(request.vars.f8_th)
	f9_th=str(request.vars.f9_th)
	f10_th=str(request.vars.f10_th)
	f11_th=str(request.vars.f11_th)
	f12_th=str(request.vars.f12_th)
	f13_th=str(request.vars.f13_th)
	f14_th=str(request.vars.f14_th)
	f15_th=str(request.vars.f15_th)
	f16_th=str(request.vars.f16_th)
	f17_th=str(request.vars.f17_th)
	f18_th=str(request.vars.f18_th)
	f19_th=str(request.vars.f19_th)
	f20_th=str(request.vars.f20_th)
	f21_th=str(request.vars.f21_th)
	f22_th=str(request.vars.f22_th)

	if f1_st=='None':
		f1_st=0
	if f2_nd=='None':
		f2_nd=0
	if f3_rd=='None':
		f3_rd=0
	if f4_th=='None':
		f4_th=0
	if f5_th=='None':
		f5_th=0
	if f6_th=='None':
		f6_th=0
	if f7_th=='None':
		f7_th=0
	if f8_th=='None':
		f8_th=0
	if f9_th=='None':
		f9_th=0
	if f10_th=='None':
		f10_th=0
	if f11_th=='None':
		f11_th=0
	if f12_th=='None':
		f12_th=0
	if f13_th=='None':
		f13_th=0
	if f14_th=='None':
		f14_th=0
	if f15_th=='None':
		f15_th=0
	if f16_th=='None':
		f16_th=0
	if f17_th=='None':
		f17_th=0
	if f18_th=='None':
		f18_th=0
	if f19_th=='None':
		f19_th=0
	if f20_th=='None':
		f20_th=0
	if f21_th=='None':
		f21_th=0
	if f22_th=='None':
		f22_th=0


	no_of_scdle=str(request.vars.no_of_scdle)


	if no_of_scdle=='':
		no_of_scdle=0

	d_id=request.vars.id

	if btn_sve:
		db((db.delivery_schedule_format.cid==cid)& (db.delivery_schedule_format.id==d_id)).update(d_1=day_1,d_2=day_2,d_3=day_3,d_4=day_4,d_5=day_5,d_6=day_6,d_7=day_7,d_8=day_8,d_9=day_9,d_10=day_10,d_11=day_11,d_12=day_12,d_13=day_13,d_14=day_14,d_15=day_15,d_16=day_16,d_17=day_17,d_18=day_18,d_19=day_19,d_20=day_20,d_21=day_21,d_22=day_22,d_23=day_23,d_24=day_24,d_25=day_25,d_26=day_26,d_27=day_27,d_28=day_28,d_29=day_29,d_30=day_30,d_31=day_31,days2_qnt=f2_d_qnt,days3_qnt=f3_d_qnt,days4_qnt=f4_d_qnt,days5_qnt=f5_d_qnt,ord_submisson_time=ord_sub_time,ord_1st=f1_st,ord_2nd=f2_nd,ord_3rd=f3_rd,ord_4th=f4_th,ord_5th=f5_th,ord_6th=f6_th,ord_7th=f7_th,ord_8th=f8_th,ord_9th=f9_th,ord_10th=f10_th,ord_11th=f11_th,ord_12th=f12_th,ord_13th=f13_th,ord_14th=f14_th,ord_15th=f15_th,ord_16th=f16_th,ord_17th=f17_th,ord_18th=f18_th,ord_19th=f19_th,ord_20th=f20_th,ord_21st=f21_th,ord_22nd=f22_th,no_of_schedule=no_of_scdle)		
		session.flash='Updated Successfully' 
	else:					
		session.flash='Failed'

	records=db((db.delivery_schedule_format.cid==cid) & (db.delivery_schedule_format.year==year) & (db.delivery_schedule_format.month==month) & (db.delivery_schedule_format.branch_name==branch_name)).select(db.delivery_schedule_format.ALL,orderby=db.delivery_schedule_format.id)						
			#
	depotRows = db((db.sm_depot.cid == cid) ).select(db.sm_depot.name, db.sm_depot.depot_id, orderby=db.sm_depot.name)
      							
	
	return dict(depotRows=depotRows,records=records,form=form,year=year,month=month,branch_name=branch_name)
    




def get_belt():
	resStr = ''
	cid = session.cid
	branch_code=session.branch_code
	# return branch_code
	rows = db((db.sm_depot_belt.cid == cid) & (db.sm_depot_belt.depot_id == branch_code)).select(db.sm_depot_belt.depot_id,db.sm_depot_belt.belt_name, orderby=db.sm_depot_belt.depot_id, groupby=db.sm_depot_belt.depot_id)
	# return rows
	for row in rows:
		depot_id = str(row.depot_id)
		belt_name = str(row.belt_name)        
		if resStr == '':
			resStr = depot_id + '|' + belt_name
		else:
			resStr += ',' + depot_id + '|' + belt_name
	return resStr  



def get_dp():
    redStr = ''
    cid = session.cid
    
    rows = db(db.sm_delivery_man.cid == cid).select(db.sm_delivery_man.d_man_id,db.sm_delivery_man.name, orderby=db.sm_delivery_man.d_man_id, groupby=db.sm_delivery_man.d_man_id)
    for row in rows:
        d_man_id = str(row.d_man_id) 
        name  = str(row.name)      
        if redStr == '':
            redStr = d_man_id + '|' + name
        else:
            redStr += ',' + d_man_id + '|' + name
    return redStr  

# def delivery_schedule():    
# 	cid=session.cid	
# 	year=str(request.vars.year).strip()
# 	month=str(request.vars.month).strip()
# 	branch_name=str(request.vars.branch_name).strip()
# 	btn_set=request.vars.btn_set 
# 	session.year=year
# 	session.month=month
# 	session.branch_name=branch_name
# 	depot_id=session.depot_id
# 	# return depot_id
# 	branch_code=''
# 	chkbCode=db((db.delivery_schedule_format.cid==cid) & (db.delivery_schedule_format.branch_name==branch_name)).select(db.delivery_schedule_format.branch_code,limitby=(0,1))        	    
	
# 	if chkbCode:
# 		branch_code=chkbCode[0].branch_code
# 	session.branch_code=branch_code
	
# 	if year=='' or month=='':               
# 		response.flash='Valid Year-Month required'
# 	else:
# 		first_date=year+'-'+month+'-01'
    
# 	if  year!='' and month!='' and btn_set=='Set Schedule':		
		
# 		chkIDRows=db((db.delivery_schedule_format.cid==cid) & (db.delivery_schedule_format.year==year) & (db.delivery_schedule_format.month==month) ).select(db.delivery_schedule_format.year,db.delivery_schedule_format.month,limitby=(0,1))        	    
		
# 		if not chkIDRows:
# 			session.flash='Please Contact with Admin' 
# 		# 	insStr="INSERT INTO  delivery_schedule_format (cid,branch_code,branch_name,year,month,belt_id,belt_name,belt_category,mso_tr_code,sallary_id,dp_name_designation,type_van_man) SELECT cid,branch_code,branch_name, '"+year+"','"+month+"',belt_id,belt_name,belt_category,mso_tr_code,sallary_id,dp_name_designation,type_van_man FROM delivery_schedule_basic where branch_name='"+branch_name+"'"
# 		# 	insRun=db.executesql(insStr)			
# 		# 	redirect(URL(c='delivery_schedule',f='delivery_schedule_add',vars=dict(year=year,month=month)))    			
# 		else:
# 			# session.flash='Already Added' 
# 			redirect(URL(c='delivery_schedule',f='delivery_schedule_add',vars=dict(year=year,month=month)))		
					
			
	
# 	return dict()   
