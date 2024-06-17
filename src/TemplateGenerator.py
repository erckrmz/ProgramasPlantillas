import os
import ConsoleManager
from EmptyTemplates import selectEmptyOption
from FulfilledTemplates import selectFilledOption

if __name__ == "__main__":
    exit=False
    while(exit==False):
        opc=ConsoleManager.startProgram()
        match opc:
            case 1:
                select=ConsoleManager.generateEmptyTemplate()
                if(select==1 or select==2):
                    selectEmptyOption(select)
                elif(select==4):
                    exit=True
            case 2:
                select=ConsoleManager.generateFulfilledTemplate()
                if(select==1 or select==2):
                    selectFilledOption(select)
                elif(select==4):
                    exit=True
                
            