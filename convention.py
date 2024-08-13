import pandas as pd
from unidecode import unidecode

def remove_empty_values(conventions):
    # Utilisation de la compréhension de dictionnaire pour filtrer les entrées avec des valeurs non vides
    return {k: v for k, v in conventions.items() if v}
def convention_(df_mail,conventions):
    # List of personal email domains to exclude
    personal_email_domains = ['icloud', 'hotmail', 'gmail', 'yahoo']
    df_mail['Company Names'] = df_mail['Company Names'].str.strip().str.lower()
    companies = df_mail['Company Names'].unique()
    # Supprimer les lignes où la colonne 'Emails' est vide ou contient une liste vide
    df_mail = df_mail[~df_mail['Emails'].astype(str).eq('[]')]
    # Réinitialiser les index après la suppression
    df_mail.reset_index(drop=True, inplace=True)
    
    for company in companies:
        if company in conventions :
            company_conventions=conventions[company]
        else:
            company_conventions = []  # Liste des conventions pour cette entreprise
        df_company = df_mail[df_mail['Company Names'].str.lower().eq(company)]
        for index, row in df_company.iterrows():
            if not pd.isnull(row['Last Name']) and not pd.isnull(row['First Name']):
                last_name = unidecode(str(row['Last Name'])).strip().lower()
                first_name = unidecode(str(row['First Name'])).strip().lower()
                for email in str(row['Emails']).split(','):
                
                    email = email.replace("'", "").replace("[", "").replace("]", "")

                    dns = email.split('@')[1]
                    left_part = email.split('@')[0].lower()
                    if len(left_part)==2:
                        if left_part[0]==first_name[0] and left_part[1]== last_name[0]:
                             if not any(c['convention'] == 'fl'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                company_conventions.append({'domain': dns, 'convention': 'fl'})
                        if left_part[1]==first_name[0] and left_part[0]== last_name[0]:
                             if not any(c['convention'] == 'lf'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                company_conventions.append({'domain': dns, 'convention': 'lf'})
                                  
                    else :

                        if dns.split('.')[0].replace("'","") not in personal_email_domains:
                            if '.' in left_part:
                                element_1 = left_part.split('.')[0].lower()  # Convertir en minuscules
                                element_2 = left_part.split('.')[1].lower()  # Convertir en minuscules
                                
                                if element_1 == first_name and element_2 == last_name:
                                    if not any(c['convention'] == 'first.last'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'first.last'})
                                        
                                elif len(element_1) == 1 and element_1.lower() == first_name[0] and element_2 == last_name:
                                    if not any(c['convention'] == 'f.last' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'f.last'})
                                elif len(element_2) == 1 and element_1.lower() == first_name and element_2 == last_name[0]:
                                    if not any(c['convention'] == 'first.l' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'first.l'})
                                elif element_2 != last_name and  last_name in element_2:
                                    element_3=element_2.split(last_name)[1]
                                    element_2=last_name
                                    if element_1 == first_name:
                                        if not any(c['convention'] == 'first.last' + element_3 and c['domain'] == dns for c in company_conventions):

                                            company_conventions.append({'domain': dns, 'convention': 'first.last'+element_3})
                                    elif len(element_1) == 1 and element_1.lower() == first_name[0]:
                                        if not any(c['convention'] == 'f.last'+element_3 and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'f.last'+element_3})
                                else:
                                    element_1 = left_part.split('.')[0].lower()  # Convertir en minuscules
                                    element_2 = left_part.split('.')[1].lower()  # Convertir en minuscules
                                    
                                    if element_2 == first_name and element_1 == last_name:
                                        if not any(c['convention'] == 'last.first'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'last.first'})
                                            
                                    elif len(element_1) == 1 and element_1.lower() == last_name[0] and element_2 == first_name:
                                        if not any(c['convention'] == 'l.first' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'l.first'})
                                    elif len(element_2) == 1 and element_1.lower() == last_name and element_2 == first_name[0]:
                                        if not any(c['convention'] == 'last.f' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'last.f'})
                                    elif element_2 != first_name and  first_name in element_2:
                                        element_3=element_2.split(first_name)[1]
                                        element_2=first_name
                                        if element_1 == last_name:
                                            if not any(c['convention'] == 'last.first' + element_3 and c['domain'] == dns for c in company_conventions):

                                                company_conventions.append({'domain': dns, 'convention': 'last.first'+element_3})
                                        elif len(element_1) == 1 and element_1.lower() == last_name[0]:
                                            if not any(c['convention'] == 'l.first'+element_3 and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'l.first'+element_3})






                            elif '_' in left_part and '_ext' not  in left_part:
                                element_1 = left_part.split('_')[0].lower()  # Convertir en minuscules
                                element_2 = left_part.split('_')[1].lower()  # Convertir en minuscules
                                
                                if element_1 == first_name and element_2 == last_name:
                                    if not any(c['convention'] == 'first_last'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'first_last'})
                                        
                                elif len(element_1) == 1 and element_1.lower() == first_name[0] and element_2 == last_name:
                                    if not any(c['convention'] == 'f_last' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'f_last'})
                                elif element_2 != last_name and  last_name in element_2:
                                    element_3=element_2.split(last_name)[1]
                                    element_2=last_name
                                    if element_1 == first_name:
                                        if not any(c['convention'] == 'first_last' + element_3 and c['domain'] == dns for c in company_conventions):

                                            company_conventions.append({'domain': dns, 'convention': 'first_last'+element_3})
                                    elif len(element_1) == 1 and element_1.lower() == first_name[0]:
                                        if not any(c['convention'] == 'f_last'+element_3 and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'f_last'+element_3})
                                
                            elif '-' in left_part and '-ext' not  in left_part:
                                element_1 = left_part.split('-')[0].lower()  # Convertir en minuscules
                                element_2 = left_part.split('-')[1].lower()  # Convertir en minuscules
                                
                                if element_1 == first_name and element_2 == last_name:
                                    if not any(c['convention'] == 'first-last'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'first-last'})
                                        
                                elif len(element_1) == 1 and element_1.lower() == first_name[0] and element_2 == last_name:
                                    if not any(c['convention'] == 'f-last' and c['domain'] == dns  for c in company_conventions)  : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'f-last'})
                                elif element_2 != last_name and  last_name in element_2:
                                    element_3=element_2.split(last_name)[1]
                                    element_2=last_name
                                    if element_1 == first_name:
                                        if not any(c['convention'] == 'first-last' + element_3 and c['domain'] == dns for c in company_conventions):

                                            company_conventions.append({'domain': dns, 'convention': 'first-last'+element_3})
                                    elif len(element_1) == 1 and element_1.lower() == first_name[0]:
                                        if not any(c['convention'] == 'f-last'+element_3 and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'f-last'+element_3})
                                





                            else:
                                if  last_name == left_part:
                                    if not any(c['convention'] == 'last' and c['domain'] == dns  for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                        company_conventions.append({'domain': dns, 'convention': 'last'})
                                    
                                elif last_name in left_part:
                                    element_1 = left_part.split(last_name)[0]
                                    element_2 = last_name

                                    element_3=''
                                    
                                    if len(left_part.split(last_name))>1:
                                        element_3 = left_part.split(last_name)[1]
                                    elif len(left_part.split(last_name))==1 and element_1== '' :
                                        element_3 = left_part.split(last_name)[1]


                                    if element_1 == first_name and element_2 == last_name:
                                        if element_3 == '':
                                            if not any(c['convention'] == 'firstlast' and c['domain'] == dns  for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'firstlast'})
                                        else:
                                            if not any(c['convention'] == 'firstlast' + element_3 and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'firstlast' + element_3})
                                    elif len(element_1) == 1 and element_1.lower() == first_name[0] and element_2 == last_name:
                                        if element_3 == '':
                                            if not any(c['convention'] == 'flast' and c['domain'] == dns  for c in company_conventions): #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'flast'})
                                        else:
                                            if not any(c['convention'] == 'flast' + element_3 and c['domain'] == dns  for c in company_conventions): #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'flast' + element_3})
                                    if element_2 == last_name and element_3 == first_name[0]:
                                        if not any(c['convention'] == 'lastf' + element_3 and c['domain'] == dns  for c in company_conventions): #vérifier que la convention n'existe pas déjà
                                                company_conventions.append({'domain': dns, 'convention': 'lastf' + element_3})
                                    
                                if  str(left_part) == str(first_name) :
                                    if not any(c['convention'] == 'first'  and c['domain'] == dns for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'first' })
                                elif first_name in left_part and len(left_part.split(first_name))>1:
                                    element_2 = left_part.split(first_name)[1]
                                    element_1 = first_name

                                    if element_1 == first_name and element_2 == last_name[0]:
                                        if not any(c['convention'] == 'firstl' and c['domain'] == dns  for c in company_conventions) : #vérifier que la convention n'existe pas déjà
                                            company_conventions.append({'domain': dns, 'convention': 'firstl'})
                                   

        conventions[company] = company_conventions  # Ajouter les conventions pour cette entreprise dans le dictionnaire global
    return conventions
