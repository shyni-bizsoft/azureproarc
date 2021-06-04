from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import requests, json
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
#import mysql
import MySQLdb

# Create your views here.
def under_maintenance(request):
	if request.method == "POST":
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		row = Login.objects.filter(username = username)
		print(row)
		# cursor = connection.cursor()
		# cursor.execute('SELECT count(*) FROM login where username= %s', [username])
		# row = cursor.fetchone()
		# #print(row)
		if len(row) >= 1:
			return render(request,'dashboard.html')
		else:
			print(row)
	return render(request,'project_index.html')

def master_trs(request):
	mydb = MySQLdb.connect(
		host="103.120.178.186",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	qry ='SELECT * FROM chapter_master'
	cursor.execute(qry)
	records  = cursor.fetchall()
	context1 = []
	for row in records:
		info = {
			"id":row[0],
			"code": row[1],
			"chap_name": row[3]
		}
		context1.append(info)    
		context={'contexts':context1}
		print(context)
	return render(request,'master_trs.html',context)
def hsncode_chapter_master_count(request):
	if request.method == "POST":
		cnid = request.POST.get("cnid", "")
		#print(searchStr)
	mydb = MySQLdb.connect(
		host="103.120.178.186",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	searc=cnid		
	qry ='SELECT LENGTH(REPLACE(hsn_code,".","")) AS lenhsn_code FROM trs_master WHERE chapter_name = '+searc+' AND hsn_code != "" GROUP BY hsn_code'
	cursor.execute(qry)
	#records = cursor.fetchall()
	row = [item[0] for item in cursor.fetchall()]

	output = []
	for x in row:
		if x not in output:
			output.append(x)
	#print(output)
	data = {
		'hsn_code':output,
	}
	return JsonResponse(data) 
   
def single_trs(request):
    pid = request.GET.get('pid', '')
    return render(request,'project_index_old1.html')
def get_chaptercode(request):
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	#print(searc)
	#qry1 ='SELECT * FROM psr_master WHERE fromval LIKE '+searc	
	qry1 ='SELECT * FROM chapter_master'
	print(qry1)
	cursor.execute(qry1)
	row = cursor.fetchall()	
	data = {
		'chaptercode':row,
	}	
	return JsonResponse(data)
def ajaxcall_master_trs(request):
	if request.method == "POST":
		searchStr = request.POST.get("searchStr", "")
		print(searchStr)
	mydb = MySQLdb.connect(
		host="103.120.178.186",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	#qry ='SELECT * FROM trs_master WHERE hsn_code LIKE "'+searchStr+'%" order by chapter_name'REPLACE(yourColumnName,’yourSpecialCharacters’,’’)
	searc=searchStr		
	#print(searc)
	qry ='SELECT * FROM trs_master WHERE REPLACE(hsn_code,".","") LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` ASC'
	#print(qry)
	#qry ='SELECT * FROM trs_master WHERE hsn_code="'+searchStr+'" order by chapter_name'
	#cursor.execute('SELECT * FROM `trs_master` WHERE `hsn_code` = %s', [searchStr] )
	cursor.execute(qry)
	row = cursor.fetchall()
	# row = TrsMaster.objects.filter(hsn_code__contains = searc)
	print(row)
	for i in row:
		print(i)

	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)
	#return HttpResponse(json.dumps({'message' : row},ensure_ascii=False), content_type='application/json')

def ajaxcall_append(request):
	searchStr = request.POST.get("autoid", "")
	#print(searchStr)
	#searchStr = request.POST.get("searchStr", "")
	print(searchStr)
	mydb = MySQLdb.connect(
		host="103.120.178.186",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	searc=searchStr
	print(searc)
	qry ='SELECT * FROM trs_master WHERE REPLACE(hsn_code,".","") LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` ASC'
	print(qry)
	cursor.execute(qry)
	row = cursor.fetchall()
	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)
def ajaxcall_append_select(request):
	searchStr = request.POST.get("autoid", "")
	#print(searchStr)
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	searc=searchStr
	print(searc)
	qry ='SELECT * FROM trs_master WHERE id = '+searc+'ORDER BY `trs_master`.`hsn_code` ASC'
	print(qry)
	cursor.execute(qry)
	row = cursor.fetchall()
	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)
def ajaxcall_appendprs(request):
	searchStr = request.POST.get("hsncodes", "")
	#print("testttttttttttt")
	#print(searchStr)
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	searc=searchStr
	#print(searc)
	#qry1 ='SELECT * FROM psr_master WHERE fromval LIKE '+searc
	
	qry1 ='SELECT * FROM prs_master WHERE '+searc+' > fromval AND '+searc+' <= toval'
	print(qry1)
	cursor.execute(qry1)
	row = cursor.fetchall()	
	data = {
		'hsn_codess':row,
	}
	# mydb = mysql.connector.connect(
	# 	host="localhost",
	# 	user="techinsig_midi",
	# 	password="cn3qdUp3Q*P!",
	# 	database="techinsig_midi"
	# 	)
	#cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	#searc=searchStr
	#print(searc)
	# qry ='SELECT * FROM trs_master WHERE hsn_code LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` DESC'
	# print(qry)
	# cursor.execute(qry)
	# row = cursor.fetchall()
	# data = {
	# 	'hsn_code':row,
	# }
	return JsonResponse(data)
def countrycode(request):
	return render(request,'countrycode.html')
def ajaxcall_country(request):
	mydb = MySQLdb.connect(
		host="103.120.178.186",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))	
	qry ='SELECT * FROM country_code'
	cursor.execute(qry)
	row = cursor.fetchall()
	print(row)
	vy=[]
	for i in row:
		mydict = {'id':i[0],'name':i[1],'shortcode':i[2],'status': i[3],'option': i[0]}
		vy.append(mydict) 		
		data = {
		'hsn_code':vy,
	 	}		
	return JsonResponse(data)
def ajaxcall_countrycode(request):
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	#print(searc)
	#qry1 ='SELECT * FROM psr_master WHERE fromval LIKE '+searc	
	qry1 ='SELECT * FROM country_code'
	print(qry1)
	cursor.execute(qry1)
	row = cursor.fetchall()	
	data = {
		'countryvode':row,
	}	
	return JsonResponse(data)
def ajaxcall_append_selectcountrycode(request):
	searchStr = request.POST.get("autoid", "")
	searchStrhsncode = request.POST.get("hsncode", "")
	#print(searchStr)
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	searc=searchStr
	searchsn=searchStrhsncode
	#print(searc)
	#AND REPLACE(hsn_code,".","") = '+searchsn+' 
	qry ='SELECT * FROM trs_master WHERE country_code = '+searc+' AND (REPLACE(hsn_code,".","") LIKE "%" '+searchsn+') ORDER BY `trs_master`.`chapter_name` ASC'
	#if(searc != ""):
		
	#if(searchsn != ""):
		#qry ='SELECT * FROM trs_master WHERE REPLACE(hsn_code,".","") = '+searchsn+' ORDER BY `trs_master`.`chapter_name` ASC'
	#print(qry)
	cursor.execute(qry)
	row = cursor.fetchall()
	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)
def ajaxcall_append_selectcountrycodesing(request):
	searchStr = request.POST.get("autoid", "")
	searchStrhsncode = request.POST.get("hsncode", '')
	#print(searchStr)
	mydb = MySQLdb.connect(
			host="103.120.178.186",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	searc=searchStr
	searchsn=searchStrhsncode.strip()
	print(searchsn)
	print(len(searchsn))
	#AND REPLACE(hsn_code,".","") = '+searchsn+' 
	if searchsn == '""':
		qry ='SELECT * FROM chapter_master'	
		print(qry)
	else:
		qry ='SELECT * FROM chapter_master WHERE chapter_code LIKE '+searchsn+' ORDER BY `chapter_master`.`id` ASC'		
		print('else condition')
	#if(searc != ""):		
	#if(searchsn != ""):
	#qry ='SELECT * FROM trs_master WHERE REPLACE(hsn_code,".","") = '+searchsn+' ORDER BY `trs_master`.`chapter_name` ASC'
	#print(qry)
	cursor.execute(qry)
	row = cursor.fetchall()
	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)
def comparison_trs(request):
	return render(request,'comparison_trs.html')

