# Program extracting first column
import xlrd
import re
 
loc = ("D:\cfdtcr\docs\data_transform.xlsx")
ID = "005"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(24)
sheet.cell_value(0, 0)
f= open("values.txt","w+")

for i in range(sheet.nrows):
	if (i==0):
		hdr=sheet.row_values(i)
	else:
		fld = sheet.row_values(i)
		for j in range(sheet.ncols):
			if (j==0):
				f.write("	xls."+hdr[j]+" = fld["+str(j)+"]\n")
			else:
				f.write("	xls."+hdr[j]+" = fld["+str(j)+"]\n")
f.close()
		
			