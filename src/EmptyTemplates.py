import os
import shutil

def selectEmptyOption(select):
    doc0 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE0.docx'
    doc1 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE1.docx'
    doc2 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE2.docx'
    doc3 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE3.docx'
    doc4 = r'ProgramasPlantillas/docx/Manual_Etapas/Empty_Files/Manual_EmptyTemplatesE4.docx'
    tupleDoc=(doc0,doc1,doc2,doc3,doc4)
    if(select==1):
        generateEmpty()
    elif(select==2):
        generateSeparateEmpty(tupleDoc)
    else:
        print("ERROR! Algo no salió bien al generar las plantillas vacías [err00]")


def generateSeparateEmpty(tupleDoc):
    print("generateSeparateEmpty")
    countEtapa=0
    for doc in tupleDoc:
        shutil.copy2(doc,os.path.join('Resultados','Manual_EmptyTemplatesGeneratedE'+str(countEtapa)+'.docx'))
        countEtapa+=1
    

def generateEmpty():
    print("generateEmpty")
    shutil.copy2(r'ProgramasPlantillas/docx/Manual_Empty/Manual_EmptyTemplates.docx','Resultados/Manual_EmptyTemplatesGenerated.docx')