# Program extracting first column
import xlrd
import re
 
loc = ("D:\cfdtcr\docs\cfd_data.xlsx")
ID = "006"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(5)
sheet.cell_value(0, 0)
f= open("models.txt","w+")
f.write("class D"+ID+"(models.Model):\n")
f.write("	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)\n")
for i in range(sheet.nrows):
    #fld = sheet.cell_value(i, 1).value
	fld = sheet.row_values(i)
	f.write("	"+fld[1]+" = models.IntegerField(null = True)\n")
f.close()

f= open("forms.txt","w+")
f.write("class F"+ID+"(forms.Form):\n")

for i in range(sheet.nrows):
    #fld = sheet.cell_value(i, 1).value
	fld = sheet.row_values(i)
	f.write("	"+fld[1]+" = forms.IntegerField(required = False)\n")
f.close()	

f= open("view.txt","w+")
f.write("class F"+ID+"(view.view):\n")

f.write("	 data"+ID+".lsgd_code_and_year = lsgd_code + str(data_entry_year)\n")
for i in range(sheet.nrows):
    #fld = sheet.cell_value(i, 1).value
	fld = sheet.row_values(i)
	f.write("	 data"+ID+"."+fld[1]+" = data_form"+ID+".cleaned_data['"+fld[1]+"']\n")
f.close()	

f= open("html.txt","w+")
f.write("HTML ID"+ID+"\n")
f.write("			<table border=0px width=100%>\n")
lr = 1
box = 9
for i in range(sheet.nrows):
	fld = sheet.row_values(i)
	if (box==5):
		f.write('		<td align="right"><button type="submit" name="save_details" class="btn btn-primary">Save</button></td>\n')
		f.write ('		\n')
		f.write('		</tr></table><div class="box-footer"></div></div></div></div>\n')
		f.write('		<div class="box box-solid bg-blue-gradient">\n')
		f.write('     	<div class="box-header with-border">\n')
		f.write('		<h3 class="box-title"><i class="fa fa-tag"></i> &nbsp; Rivers, Forest and Coastal Details</h3>\n')
		f.write('		</div><div class="box-footer text-black"><div class="box-body">\n')	
		f.write ('		\n')
		f.write('		<table border=0px width=100%>\n')
		lr = 1
		box = 1
	else:
		box = box + 1
		
	if (lr==1):
		lr = 2
		f.write("		<tr height=70px><td>\n")
		f.write('		<label for="'+fld[1]+'" class="col-sm-8">'+str(i+1)+'. {{ questions.'+str(i)+'.question_text }}</label>\n')
		f.write('		<input id="'+fld[1]+'" name="'+fld[1]+'" type="text" size="7" value="{{ answers.0.'+fld[1]+ '}}"></td>\n')
		f.write('		<td> <label for="inputEmail3" class="col-sm-8"></label> </td>\n')
	else:
		lr = 1
		
		f.write('		<td><label for="'+fld[1]+'" class="col-sm-8">'+str(i+1)+'. {{ questions.'+str(i)+'.question_text }}</label>\n')
		f.write('		<input id="'+fld[1]+'" name="'+fld[1]+'" type="text" size="7" value="{{ answers.0.'+fld[1]+ '}}"></td></td></tr>\n\n')
	
	
f.close()	
		
		