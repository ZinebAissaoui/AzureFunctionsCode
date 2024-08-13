from unidecode import unidecode
import pandas as pd
import logging
def generate_email(row,conventions):
    mails = []
    company = row['Company']
    if isinstance(company, str):  # Vérifier si la valeur est une chaîne de caractères
        company = unidecode(str(company)).strip().lower()  # Convertir en minuscules

        if company.strip() in conventions.keys():
            if conventions[company] :
                #print(f"l'adresse est {email_address}")
                #if pd.isnull(email_address) or email_address.split('@')[1].split('.')[0] in personal_email_domains:
                first_name = unidecode(row['First Name'].lower()).strip().replace(" ", "")
                last_name = unidecode(row['Last Name'].lower()).strip().replace(" ", "")
                for x in conventions[company]:
                    conv = x['convention']
                    domain = x['domain']
                    if conv == 'first.last':
                        mails.append(first_name + '.' + last_name + '@' + domain)
                    elif conv == 'last.first':
                        mails.append(last_name + '.' + first_name + '@' + domain)
                    elif conv == 'last.f':
                        mails.append(last_name + '.' + first_name[0] + '@' + domain)
                    elif conv =='first':
                        mails.append(first_name + '@' + domain)
                    elif conv =='firstlastexterne':
                        mails.append(first_name  + last_name + 'externe' + '@' + domain)
                    elif conv =='firstlast':
                        mails.append(first_name  + last_name  + '@' + domain)
                    elif conv =='last':
                        mails.append( last_name  + '@' + domain)
                    elif conv == 'first_last':
                        mails.append(first_name + '_' + last_name + '@' + domain)
                    elif 'first.last-'in conv:
                        element3=conv.split('first.last')[1]
                        mails.append(first_name + '.' + last_name + element3 + '@' + domain)
                    
                    elif conv == 'f.last-ext':
                        mails.append(first_name[0] + '.' + last_name + '-ext' + '@' + domain)
                    elif conv == 'f.last':
                        mails.append(first_name[0] + '.' + last_name + '@' + domain)
                    elif conv == 'f-last':
                        mails.append(first_name[0] + '-' + last_name + '@' + domain)
                    elif conv == 'first.l':
                        mails.append(first_name + '.' + last_name[0] + '@' + domain)
                    elif conv == 'l.first':
                        mails.append(last_name[0] + '.' + first_name + '@' + domain)
                    elif conv == 'last.first':
                        mails.append(last_name + '.' + first_name + '@' + domain)
                    elif conv == 'lastfirst':
                        mails.append(last_name  + first_name + '@' + domain)
                    elif conv == 'f_last':
                        mails.append(first_name[0] + '_' + last_name + '@' + domain)
                    elif conv == 'flast':
                        mails.append(first_name[0] + last_name + '@' + domain)
                    elif conv == 'lastf':
                        mails.append(  last_name+first_name[0] + '@' + domain)
                    elif conv == 'firstl':
                        mails.append(first_name + last_name[0] + '@' + domain)
                    elif conv == 'fl':
                        mails.append(first_name[0] + last_name[0] + '@' + domain)
                    elif 'flast-' in conv :
                        element3 = conv.split('flast')[1]
                        mails.append(first_name[0] + last_name + element3 + '@' + domain)
                    elif 'f.last-' in conv :
                        element3 = conv.split('f.last')[1]
                        mails.append(first_name[0]+ '.' + last_name + element3 + '@' + domain)
                    elif conv == 'flast_' in conv:
                        element3 = conv.split('flast')[1]
                        mails.append(first_name[0] + last_name + element3 + '@' + domain)

                    
                    
                
    
                    
    return ';'.join(mails) if mails else None

