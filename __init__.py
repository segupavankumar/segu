class crop_details: 
     def bargraph(self):
         import xlrd
         loc = (r"C:\Users\pavan\Desktop\CropsDataFile.xlsx")
         wb = xlrd.open_workbook(loc)
         sheet = wb.sheet_by_index(0)
         sheet.cell_value(0, 0)
         import matplotlib.pyplot as plt
         x=list()
         y=list() 
         for i in range(2,sheet.nrows) :
             if sheet.cell_value(i,4)==self:
                 x.append(sheet.cell_value(i,2))
                 y.append(sheet.cell_value(i,6))
         plt.bar(x, y) 
         plt.xlabel('Year') 
         plt.ylabel('Production') 
         plt.title('Crop Production')  
         plt.show() 
     def yeardetails(self):
         f=open(r"C:\Users\pavan\Desktop\codes\file.txt","w")
         import xlrd
         loc = (r"C:\Users\pavan\Desktop\CropsDataFile.xlsx")
         wb = xlrd.open_workbook(loc)
         sheet = wb.sheet_by_index(0)
         sheet.cell_value(0, 0)
         #f.write(str(sheet.row_value(0,0)))
         # f.write('\n')
         # f.write(str(sheet.row_values(1,0)))
         # f.write('\n')
         for i in range(sheet.nrows): 
             if sheet.cell_value(i,2)==self:
                 f.write(str(sheet.row_values(i,0)))
                 f.write('\n')


           
