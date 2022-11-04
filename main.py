from Database.Database import Database
from Artificial_Intelligence.Artificial_Intelligence import Artificial_Intelligence

import pandas as pd
import numpy as np

if __name__=="__main__":

    # Criando conexão com o banco de dados 
    host = '127.0.0.1'
    user = 'root'
    password = ''

    # Criando um objeto de banco de dados para permitir opera-lo
    db = Database(host, user, password)
    db.createDatabase() 
    # Criando um objeto de IA para permitir opera-la
    ai = Artificial_Intelligence(db.searchData())
    # Criando o banco de dados

    #db.createDatabase()   
    #db.exportDataset()
    
    #print("-"*15)
    # Criando a ia para treino 

    flag =True
    while flag:
        print('''

                SISTEMA INTERNO DE ACESSO DO BANCO

                    [1] - AVALIAR CLIENTE
                    [2] - MOSTRAR PRECISÃO DO SISTEMA
                    [3] - SAIR
        ''')
        opcao=int(input('DIGITE SUA OPÇÃO: '))
        if(opcao==1):
            listSeries = []

            # laufkont -> Status 
            status=None
            while((status!=1 and status!=2 and status!=3 and status!=4)):
                status=int(input('Status: '))
            listSeries.append(status)

            # laufzeit -> Duration
            duration=int(input('Duration: '))
            listSeries.append(duration)
            # Moral -> Credit hist
            credit_his=None
            while((credit_his!=1 and credit_his!=2 and credit_his!=3 and credit_his!=4)):
                credit_his=int(input('Credit History: '))

            listSeries.append(credit_his)
            # Verw -> purpose
            purpose=None
            while((purpose!=1 and purpose!=2 and purpose!=3 and purpose!=4 and
            purpose!=5 and purpose!=6 and purpose!=7 and purpose!=8 
            and purpose!=9 and purpose!=10)):
                purpose=int(input('Purpose: '))

            listSeries.append(purpose)

            # hoehe -> amount
            amount=int(input('amount: '))
            listSeries.append(amount)

            # Sparkont -> Saving
            savings=None
            while((savings!=1 and savings!=2 and savings!=3 and savings!=4 and savings!=5)):
                savings=int(input('Savings: '))

            listSeries.append(savings)

            # Beszeit -> Employed duration
            employed=None
            while((employed!=1 and employed!=2 and employed!=3 and employed!=4 and employed!=5)):
                employed=int(input('Employed duration: '))

            listSeries.append(employed)

            # Rate -> Installment rate
            rate=None
            while((rate!=1 and rate!=2 and rate!=3 and rate!=4)):
                rate=int(input('Installment rate: '))

            listSeries.append(rate)

            # famges -> Personal status sex
            personal_status=None
            while((personal_status!=1 and personal_status!=2 
                and personal_status!=3 and personal_status!=4)):
                personal_status=int(input('Personal Status: '))    
            listSeries.append(personal_status)

            # buerge -> other_debtors
            debtors=None
            while((debtors!=1 and debtors!=2 and debtors!=3)):
                debtors=int(input('Other debtors: '))    

            listSeries.append(debtors) 
            # wohnzeit -> Present residence
            pres_res=None
            while((pres_res!=1 and pres_res!=2 and pres_res!=3 and pres_res!=4)):
                pres_res=int(input('Present Residence: '))
            
            listSeries.append(pres_res)

            # verm -> property
            property=None
            while((property!=1 and property!=2 and property!=3 and property!=4)):
                property=int(input('Property: '))
            listSeries.append(property)

            # alter -> age
            age=int(input('Age: '))    
            listSeries.append(age)

            # weitkerd -> other_installment_plans
            plans=None
            while((plans!=1 and plans!=2 and plans!=3)):
                plans=int(input('Other Installment Plans: '))          
            listSeries.append(plans)

            # wohn -> housing
            housing=None
            while((housing!=1 and housing!=2 and housing!=3)):
                housing=int(input('Housing: '))    
            listSeries.append(housing)

            # bishkred -> number_credits
            nmb_credits=None
            while((nmb_credits!=1 and nmb_credits!=2 and nmb_credits!=3 and nmb_credits!=4)):
                nmb_credits=int(input('Credits Number: '))
            listSeries.append(nmb_credits)   

            # beruf -> job
            job=None
            while((job!=1 and job!=2 and job!=3 and job!=4)):
                job=int(input('Job: '))
            listSeries.append(job)

            # pers -> people_liable
            nmb_liable=None
            while((nmb_liable!=1 and nmb_liable!=2)):
                nmb_liable=int(input('People liable: '))
            listSeries.append(nmb_liable)

            # telef -> telephone
            telephone=None
            while((telephone!=1 and telephone!=2)):
                telephone=int(input('Telephone: '))
            listSeries.append(telephone)

            # gastarb -> foreign worker
            worker=None
            while((worker!=1 and worker!=2)):
                worker=int(input('Foreign worker: '))
            listSeries.append(worker)  
             
            df = pd.DataFrame([listSeries],columns=['laufkont','laufzeit','moral','verw','hoehe','sparkont','beszeit','rate','famges','buerge','wohnzeit','verm','alter','weitkred','wohn','bishkred','beruf','pers','telef','gastarb'])
            
            ai.evaluate_client(df)


        if(opcao==2):
            ai.train()
            pass
        if(opcao==3):
            flag=False
            break
    
    

