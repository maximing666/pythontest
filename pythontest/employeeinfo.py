# -*- coding: gbk -*-
import xlrd
import uniout 


print "��ӭ��ѯ��ҵԱ����Ϣ��"
print "-----------------------"
lognum=0
while True:
	lognum=lognum+1
	if lognum>3:
		print "���ܲ��ܺú���ˣ�ˣ�"
		quit()
	inquire_no=int(raw_input("������Ҫ��ѯ��ǰ��Ĵ��ţ�1���� 2�Ա� 3���� 4���� 5��ְ����\n").strip())
	if inquire_no in range(1,6):
		inquire_value = (raw_input("�������ѯ���ݣ�")).strip(' ')
		print "��Ҫ��ѯ�������ǣ�",inquire_value
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
			print "�ҵ����ϲ�ѯ�����ļ�¼��",(table.row_values(rownum))	
		rownum=rownum+1
		#print rownum,"------",cols.decode,"----",inquire_value.decode
elif inquire_no == 3  or inquire_no == 5:
		for cols in (col):
			
			print "inquire_value:",type(inquire_value.decode('original_encoding'))
			print "cols:",type(cols)

			if cols.encode == inquire_value.decode:
				print "�ҵ����ϲ�ѯ�����ļ�¼��",(table.row_values(rownum))	
			print cols.encode,'----',inquire_value.decode
			rownum=rownum+1
			#print rownum,"------",cols.encode('utf-8'),"----",inquire_value,'\n'
			




