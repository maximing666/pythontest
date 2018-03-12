# -*- coding: gbk -*-
import xlrd
import uniout 


print "欢迎查询企业员工信息表"
print "-----------------------"
lognum=0
while True:
	lognum=lognum+1
	if lognum>3:
		print "还能不能好好玩耍了？"
		quit()
	inquire_no=int(raw_input("请输入要查询项前面的代号：1姓名 2性别 3年龄 4部门 5入职日期\n").strip())
	if inquire_no in range(1,6):
		inquire_value = (raw_input("请输入查询内容：")).strip(' ')
		print "您要查询的内容是：",inquire_value
		break
print "----------------------------------"

datafile = xlrd.open_workbook(u'd:\pythontest\employeeinfo.xlsx')	
table = datafile.sheet_by_name('Sheet1')
nrows=int(table.nrows)
col=(table.col_values(inquire_no-1))
rownum=0
cell=table.cell(rownum,inquire_no-1).value


if inquire_no == 1 or inquire_no == 2 or inquire_no == 4:
	for cols in (col):	
		if cols.encode('gbk')==inquire_value:		
			print "找到符合查询条件的记录：",(table.row_values(rownum))	
		rownum=rownum+1
		#print rownum,"------",cols.decode,"----",inquire_value.decode
elif inquire_no == 3  or inquire_no == 5:
		for cols in (col):
			
			print "inquire_value:",type(inquire_value.decode('original_encoding'))
			print "cols:",type(cols)

			if cols.encode == inquire_value.decode:
				print "找到符合查询条件的记录：",(table.row_values(rownum))	
			print cols.encode,'----',inquire_value.decode
			rownum=rownum+1
			#print rownum,"------",cols.encode('utf-8'),"----",inquire_value,'\n'
			




