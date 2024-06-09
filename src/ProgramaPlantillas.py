from docx import Document
import os

docPath=0
dirname = r'ProgramasPlantillas/docx/Manual_Fulfilled/Manual_FulfilledTemplatesV1.docx'
doc = Document(dirname)
#print(os.getcwd())
#print(dirname)
tablas=doc.tables
#print([tuple(c.text for c in r.cells) for r in tablas[0].rows])

for row in tablas[3].rows:
    print(tuple(cell.text for cell in row.cells))
    #print("\n")

#for tables in tablas:
#    print(str(tables)+"\n")



# Check whether the specified 
# path exists or not 
#isExist = os.path.exists('ProgramasPlantillas/docx/Manual_FulfilledTemplatesV2.docx') 
#print(os.path.join(os.getcwd(),'\ProgramasPlantillas'))
#print(isExist)