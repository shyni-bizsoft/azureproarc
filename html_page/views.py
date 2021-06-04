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
            "shortcode": row[2],
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
def hsncode_length_data(request):
    if request.method == "POST":
        cnid = request.POST.get("cnid", "")
        cname = request.POST.get("cname", "")
        #print(searchStr)
    mydb = MySQLdb.connect(
        host="103.120.178.186",
        user="techinsig_midi",
        password="cn3qdUp3Q*P!",
        database="techinsig_midi"
        )
    cursor = mydb.cursor()
    searc=cnid		
    searchaptername=cname		
    qry ='SELECT hsn_code FROM trs_master WHERE LENGTH(REPLACE(hsn_code,".","")) = '+searc+' AND chapter_name LIKE "%" '+searchaptername+' ORDER BY `trs_master`.`hsn_code` ASC '
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
def product_code_data(request):
    if request.method == "POST":
        hsnid = request.POST.get("hsnid", "")
        cname = request.POST.get("cname", "")
        searc = str(hsnid)[1:-1]
        #print(searchStr)
    mydb = MySQLdb.connect(
        host="103.120.178.186",
        user="techinsig_midi",
        password="cn3qdUp3Q*P!",
        database="techinsig_midi"
        )
    cursor = mydb.cursor()	
    searchaptername=cname		
    qry ='SELECT pdt_hsncode FROM trs_master WHERE hsn_code IN ('+searc+') AND  chapter_name = '+searchaptername+' ORDER BY `trs_master`.`pdt_hsncode` ASC '
    cursor.execute(qry)
    #records = cursor.fetchall()
    row = [item[0] for item in cursor.fetchall()]

    output = []
    for x in row:
        if x not in output:
            output.append(x)
    #print(output)
    data = {
        'pdt_hsncode':output,
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
def ajaxcall_append_selectcountrycode(request):
    searchStr = request.POST.get("autoid", "")
    searchcname = request.POST.get("cname", "")
    searchchapterlength = request.POST.get("chapterlength", "")
    searc = str(searchStr)[1:-1]
    searchclngth = searchchapterlength
    #print(res)
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #searc=searchStr
    #searchsn=searchStrhsncode
    if(searchclngth !=""):
        qry ='SELECT * FROM trs_master WHERE LENGTH(REPLACE(hsn_code,".","")) = '+searchclngth+' ORDER BY `trs_master`.`chapter_name` ASC'
    if(searc != ""):
        qry ='SELECT * FROM trs_master WHERE country_code IN ('+searc+') ORDER BY `trs_master`.`chapter_name` ASC'
    if(searchcname != ""):
        qry ='SELECT * FROM trs_master WHERE chapter_name LIKE "%" '+searchcname+' ORDER BY `trs_master`.`chapter_name` ASC'
    if(searc != "" and searchcname != "" and searchclngth != ""):
        qry ='SELECT * FROM trs_master WHERE country_code IN ('+searc+') AND LENGTH(REPLACE(hsn_code,".","")) = '+searchclngth+' AND chapter_name LIKE "%" '+searchcname+' ORDER BY `trs_master`.`chapter_name` ASC'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    data = {
        'hsn_code':row,
    }
    return JsonResponse(data)

def ajaxcall_append_selectcountrycode_hsncode(request):
    searchStr = request.POST.get("autoid", "")
    searchcname = request.POST.get("cname", "")
    searchhsncodeid1 = request.POST.get("hsncode", "")
    chkstrng = isinstance(searchhsncodeid1, str)
    if str(chkstrng)==True:
        searchhsncodeid = [searchhsncodeid1]
    else:
        searchhsncodeid=searchhsncodeid1
    #print("searchhsncodeid")
    #print(searchhsncodeid)
    searc = str(searchStr)[1:-1]
    searchhsncode = str(searchhsncodeid)[1:-1]
    #print(res)
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #searc=searchStr
    #searchsn=searchStrhsncode
    qry ='SELECT * FROM trs_master WHERE country_code IN ('+searc+') AND hsn_code IN ('+searchhsncode+') AND chapter_name LIKE "%" '+searchcname+' ORDER BY `trs_master`.`chapter_name` ASC'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    data = {
        'hsn_code':row,
    }
    return JsonResponse(data)

def comparison_mrs(request):
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
            "shortcode": row[2],
            "chap_name": row[3]
        }
        context1.append(info)    
        context={'contexts':context1}
        print(context)
    return render(request,'comparison_mrs.html', context)
def compardesign(request):
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
            "shortcode": row[2],
            "chap_name": row[3]
        }
        context1.append(info)    
        context={'contexts':context1}
        print(context)
    return render(request,'compardesign.html', context)

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
	if searchsn == '"Select"':
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

def hsn_product_code_data(request):
    search_hsid1 = request.POST.get("hsnid", "")
    search_prdid1 = request.POST.get("prdid", "")
    search_chaptername = request.POST.get("cname", "")

    chkstrnghsn = isinstance(search_hsid1, str)
    if str(chkstrnghsn)==True:
        search_hsid = [search_hsid1]
    else:
        search_hsid=search_hsid1

    chkstrng = isinstance(search_prdid1, str)
    if str(chkstrng)==True:
        search_prdid = [search_prdid1]
    else:
        search_prdid=search_prdid1

    searchsnid = str(search_hsid)[1:-1]
    searchprdid = str(search_prdid)[1:-1]
    print('searchprdid')
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #searc=searchStr
    #searchsn=searchStrhsncode
    qry ='SELECT trs_master.*,country_code.countryname,country_code.shortcode FROM trs_master left join country_code on country_code.id=trs_master.country_code WHERE pdt_hsncode IN ('+searchprdid+') AND hsn_code IN ('+searchsnid+') AND chapter_name = '+search_chaptername+' ORDER BY `trs_master`.`chapter_name` ASC'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    data = {
        'pdt_hsncode':row,
    }
    return JsonResponse(data)
def chaptermaster(request):
    return render(request,'chaptermaster.html')
def ajaxcall_chaptermaster(request):
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
    qry ='SELECT * FROM chapter_master'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    vy=[]
    for i in row:
        mydict = {'id':i[0],'chapter_code':i[1],'chapter_name':i[3],'status': i[4],'option': i[0]}
        vy.append(mydict) 		
        data = {
        'chapter_master':vy,
         }		
    return JsonResponse(data)

def ajaxcall_chapterlengthdata(request):
    countryid = request.POST.get("countryid", "")
    chapternme = request.POST.get("chapternme", "")
    searc = str(countryid)[1:-1]
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #print(searc)
    #qry1 ='SELECT * FROM psr_master WHERE fromval LIKE '+searc	
    qry1 ='SELECT LENGTH(REPLACE(hsn_code,".","")) AS hsn_length FROM trs_master WHERE country_code IN ('+searc+') AND hsn_code != "" AND chapter_name LIKE "%" '+chapternme+' GROUP BY LENGTH(REPLACE(hsn_code,".","")) ORDER BY LENGTH(REPLACE(hsn_code,".","")) ASC '
    #print(qry1)
    cursor.execute(qry1)
    row = [item[0] for item in cursor.fetchall()]

    output = []
    for x in row:
        if x not in output:
            output.append(x)
    #print(output)
    data = {
        'countrycode':output,
    }	
    return JsonResponse(data)
def ajaxcall_chapterlengthall(request):
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    qry1 ='SELECT LENGTH(REPLACE(hsn_code,".","")) AS hsn_length FROM trs_master WHERE hsn_code != "" GROUP BY LENGTH(REPLACE(hsn_code,".","")) ORDER BY LENGTH(REPLACE(hsn_code,".","")) ASC'
    print(qry1)
    cursor.execute(qry1)
    row = cursor.fetchall()	
    data = {
        'chapterlengthall':row,
    }	
    return JsonResponse(data)
def ajaxcall_append_selectchapterlength_all(request):
    searchStr = request.POST.get("autoid", "")
    searchhsncode = request.POST.get("hsncode", "")
    searchsnid = str(searchhsncode)[1:-1]
    #print(res)
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #searc=searchStr
    #searchsn=searchStrhsncode
    if searchStr != '':
        qry ='SELECT * FROM trs_master WHERE LENGTH(REPLACE(hsn_code,".","")) = '+searchStr+' ORDER BY `trs_master`.`chapter_name` ASC'
    if searchsnid != '':
        qry ='SELECT * FROM trs_master WHERE hsn_code IN ('+searchsnid+') ORDER BY `trs_master`.`chapter_name` ASC'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    data = {
        'chapter_length_all':row,
    }
    return JsonResponse(data)

def multiplecountry_chapter_hsncode_productcode(request):
    search_countryid = request.POST.get("countryid", "")
    search_chaptername = request.POST.get("chap_nme", "")
    search_hsid1 = request.POST.get("hsncode", "")
    search_prdid1 = request.POST.get("prdcode", "")

    chkstrnghsn = isinstance(search_hsid1, str)
    if str(chkstrnghsn)==True:
        search_hsid = [search_hsid1]
    else:
        search_hsid=search_hsid1

    chkstrng = isinstance(search_prdid1, str)
    if str(chkstrng)==True:
        search_prdid = [search_prdid1]
    else:
        search_prdid=search_prdid1

    searchcid = str(search_countryid)[1:-1]
    searchsnid = str(search_hsid)[1:-1]
    searchprdid = str(search_prdid)[1:-1]
    print('searchprdid')
    mydb = MySQLdb.connect(
            host="103.120.178.186",
            user="techinsig_midi",
            password="cn3qdUp3Q*P!",
            database="techinsig_midi"
            )
    cursor = mydb.cursor()
    #searc=searchStr
    #searchsn=searchStrhsncode
    qry ='SELECT trs_master.*,country_code.countryname,country_code.shortcode,chapter_master.chapter_name FROM trs_master left join country_code on country_code.id=trs_master.country_code left join chapter_master on chapter_master.chapter_code=trs_master.chapter_name WHERE trs_master.country_code IN ('+searchcid+') AND trs_master.pdt_hsncode IN ('+searchprdid+') AND trs_master.hsn_code IN ('+searchsnid+') AND trs_master.chapter_name = '+search_chaptername+' ORDER BY `trs_master`.`chapter_name` ASC'
    cursor.execute(qry)
    row = cursor.fetchall()
    print(row)
    data = {
        'country_chapter_hsncode_pdtcode':row,
    }
    return JsonResponse(data)

def get_hsncode_description(request):
    mydb = MySQLdb.connect(
        host="103.120.178.186",
        user="techinsig_midi",
        password="cn3qdUp3Q*P!",
        database="techinsig_midi"
        )
    search_c_id = request.POST.get("c_id", "")
    search_ch_name = request.POST.get("ch_name", "")
    search_hsn_code = request.POST.get("hsn_code", "")
    cursor = mydb.cursor()
    qry ='SELECT * FROM trs_master WHERE country_code = '+search_c_id+' AND chapter_name = '+search_ch_name+' AND hsn_code = '+search_hsn_code+' AND pdt_hsncode = "" '
    cursor.execute(qry)
    records  = cursor.fetchall()
    data = {
        'get_hsncode_description':records,
    }
    return JsonResponse(data)
