import os
import shutil
from docx import Document
from docxcompose.composer import Composer
from DocxItem import DocxItem

def selectFilledOption(select):
    doc0 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE0.docx'
    doc1 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE1.docx'
    doc2 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE2.docx'
    doc3 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE3.docx'
    doc4 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE4.docx'
    tupleDoc=(doc0,doc1,doc2,doc3,doc4)
    if(select==1):
        listFilledDoc=generateSeparateFulfilled(tupleDoc)
        generateFulfilled(listFilledDoc)
    elif(select==2):
        generateSeparateFulfilled(tupleDoc)
    else:
        print("ERROR! Algo no salió bien al generar las plantillas con información [err01]")


def generateSeparateFulfilled(tupleDoc)->list:
    print("generateSeparateFulfilled")
    countEtapa=0
    listFilledDoc = list()
    for doc in tupleDoc:
        docPath = os.path.join('Resultados','Manual_FulfilledTemplatesGeneratedE'+str(countEtapa)+'.docx')
        shutil.copy(doc,docPath)
        listFilledDoc.append(DocxItem(docPath,Document(docPath)))
        countEtapa+=1
    #TODO: Insertar datos en las tablas por etapa
    return listFilledDoc
    

def generateFulfilled(listFilledDoc):
    print("generateFullfilled")
    #print(listFilledDoc[0].docDocument)
    composer = Composer(listFilledDoc[0].docDocument)
    for i in range(1,len(listFilledDoc)):
        composer.append(listFilledDoc[i].docDocument)
    composer.save(os.path.join('Resultados','Manual_FulfilledTemplatesGenerated.docx'))
    for j in range(0,len(listFilledDoc)):
        if (os.path.exists(listFilledDoc[j].docpath)):
            #print(f"'{j}' exists")
            os.remove(listFilledDoc[j].docpath)
    input("Presiona cualquier tecla para continuar...")
