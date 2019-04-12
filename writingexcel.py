# writing to an exce;
#sheet using python

import xlwt
from xlwt import Workbook

# workbook is created

wb= Workbook()

#add_sheet is used to cretae sheet

sheet1 = wb.add_sheet('Sheet 2') 

sheet1.write(1,0,'edu')
sheet1.write(2,0,'cate')
sheet1.write(3,0,'tom')
sheet1.write(4,0,'zabu')
sheet1.write(5,0,'vicky')
wb.save('tony.example.xls')