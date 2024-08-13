import pandas as pd
import emoji
 
def assign_group(position):
    dsi_cto_keywords = [
        'Dsi', 'Cto', 'Cio', 'Chief Information Officer',"Directeur des Systèmes d'Information", "Directrice des Systèmes d'information",
        'Directrice Digital' ,'Chief Technical Officer','Directeur IT', 'Directrice IT', "Directeur informatique", 'Directrice informatique','Directeur digital',
        'Head of Tech', 'head of IT', 'Chief Technology Officer' ,  'Chief Technical Officer'
    ]
 
 
    chef_projet_keywords = [
        'Scrum Master','Business Analyst','Chief Product','IT Domain Lead', 'Solution Engineer', 'Solutions Engineer', 'resp crm','head of e-commerce',
        'CP front', 'CP Back','CP', 'Product Management','technical lead','management','team leader','Coach agil','Coach agile',
        'CP Technique','Business Project Analyst','PO','Product Owner','Project Manager','PMO','VP IT manager','moe','head of digital','Head of Product','CP Info','Senior PM',
        'resp tranfo', 'responsable transfo','qa lead','chef equipe it', "chef d'equipe",'Chef Projet', 'Chef de Projet','Responsable Projet', 'Manager','resp seo',
        'responsable seo', 'Responsable du SEO','Chef d’Équipe', 'Project Lead','Head of Engineering' ,'Chief Digital Officer', 'Chief Marketing Officer' ,'enginering manager','QA manager','chief data','PM','PM Group','Lead PM','Lead Back', 'Lead Front','resp adjoint si gestion'
    ]
 
 
    recrutement_keywords = [
        'Talent Acquisition','Head of Human Resources',  'Chief of staff','Recrutement Stratégique','senior talent acquisition','talent manager',
        'resp dev rh','head of people','recrut','tech talent ac','resp recrute','tech recrut','chargé de recrutement','charge de recrutement',
        'Recrutement', 'Ressources Humaines', 'responsable recrutement it', 'responsable recrut it',
        'head of leadership','denicheur de talent','talent acquisition spé','lead talent acquisition', 'RH', 'DRH',
        'Leader talent dev','talent acquisition','head of recrutement','recrutement','rrh',
        'chargé rh','staff people', 'HR specialist','Head of Human Resources'
    ]
    achat_keywords = [
        'Achat', 'Acheteur', 'Purchaser', 'Buyer', 'Acheteuse', 'Responsable achat'
        , 'acheteur IT', 'acheteuse IT'
        ,'Direct achat',"Responsable d'achat'",'responsable des achats','achat it', "achat d'it"
    ]
    direction_generale_keywords = [
        'Fondateur', 'Cheffe', 'Dirigeant', 'Coo', 'Chief Operating Officer' ,'Dirigeante', 'Ceo', 'C E O', 'chief executive officer',
        'fondatrice','Chief Executive Officer', 'Président', 'Dg', 'Directeur Général', 'Présidente', 'vice Présidente',
        'Directeur General', 'Cofounder', 'Cofondateur', 'Créatrice', 'Gérante', 'Cofondatrice',
        'Cogérant', 'Gérant', 'President', 'Vice Président', 'Pdg', 'Vp', 'Associé', 'Associée',
        'Présidente', 'Presidente', 'Owner', 'Propriétaire',
        'Chairman', 'Founder','Gerant','Direction', 'Product owner', 'Directeur', 'directrice'
    ]
 
    developpeur_keywords = [
    'Analyste de Données', 'Ingénieur informatique','Consultant données','Consultant informatique','Business Analyst',"Consultant Systèmes d'Information",'Data Analyst', "Ingénieur d'Études", 'Consultant', 'Consultante', 'Security Analyst',
    'Analyste de Sécurité', 'IT Infrastructure', 'Consultant IT','Infrastructure IT', 'Développement Front-End', 'Développement Frontend','analyst', 'analyste', 'cybersecurity',
    'Architecte Cloud', 'Consultant Fonctionnel', 'Consultante Fonctionnelle', 'Tech Lead', 'Lead Tech', 'Coach Agile',
    'Cloud', 'Développeur', 'Développeuse', 'Developer', 'SQL', 'Digitalisation', 'Progiciel', 'Data', 'BI',
    'Ansible', 'LoadRunner', 'NeoLoad', 'UI', 'UX', 'Java', 'Backend', 'Front End', 'Opentext', 'Performance',
    'Terraform', 'Python', 'Tricentis', 'Test', 'Charge', 'Full Stack', 'Logiciel', 'Software', 'Frameworks', 'PHP',
    '.Net', 'SSIS', 'Power BI', 'React', 'Vue.js', 'AS/400', 'Application', 'CI/CD', 'Ops', 'QA', 'PBI', 'Angular',
    'Architect', 'Architecte', 'Artificial Intelligence' , 'IA','Back-end', 'Conseil IT', 'Ingénieur de données', 'Symfony', 'Laravel', 'Drupal', 'NodeJS', 'NetJS', 'DevOps', 'vue'
]
 
    if not isinstance(position, str):
        position = str(position)
 
    position_lower = position.lower()
    if any(keyword.lower() in position_lower for keyword in direction_generale_keywords):
        return "Direction générale"
    elif any(keyword.lower() in position_lower for keyword in dsi_cto_keywords):
        return "DSI/CTO"
    elif any(keyword.lower() in position_lower for keyword in chef_projet_keywords):
        return "Chef de projet"
    elif any(keyword.lower() in position_lower for keyword in achat_keywords):
        return "Achat"
    elif any(keyword.lower() in position_lower for keyword in recrutement_keywords):
        return "Recrutement"
    elif any(keyword.lower() in position_lower for keyword in developpeur_keywords):
        return "Développeur"
    else:
        return "Autre"
def remove_emojis(text):
    return ''.join(c for c in text if not emoji.is_emoji(c))
def segmentation_processing(df):
    df = df[~df['Company'].str.contains('Aerow', case=False, na=False)]
    df['First Name'] = df['First Name'].astype(str).apply(remove_emojis)
    df['Last Name'] = df['Last Name'].astype(str).apply(remove_emojis)
    df['Position Stratégique'] = df['Position'].apply(assign_group)
    df['Domaine'] = df['Position'].apply(assign_domain)
    df = df[df['Position Stratégique']!='Autre']
 
    return df
 
 
def assign_domain(position):
    data_keywords = ['Data', 'Powerbi', 'Etl','ssis', 'Ingénieur de données', 'informatica','redshift','sql','pytorch','query','analyst', 'salesforce', 'hubspot','tensorflow','Données', 'Donnees',
                     'Warehouse', 'Bi','Consultant donnée', 'Qlik', 'Crm', 'Snowflake', 'Talend', 'Machine Learning', 'Analyst','analytics', 'analytic', 'analysis','Business Intelligence','données','donnees','IA', 'Intelligence']
    infra_keywords = ['Architect', 'aws','azure','infra et prod','S/4HANA','erp','Infrastructure', 'Infrastructures', 'Sap', 'Architecte', 'Devops', 'Ansible',
                      'Api', 'Cicd', 'Terraform', 'Sysops','Amdin', 'Sys', 'Cloud', 'Cegid', 'Qualiac','CI/CD','docker','iac','gcp', 'administrator', 'administrateur', 'api','SAP HANA']
    digital_keywords = ['Digital', 'IT','MOE','seo','sem','UI','UX','agile', 'scrum','e-commerce', 'e commerce','Services informatiques']
    performance_keywords = ['Test', 'Performance', 'Neoload', 'Dynatrace', 'jmeter', 'loadrunner','QA', 'Test Automation','Security Testing','OWASP ZAP', 'Burp Suite','Monitoring']
 
    if not isinstance(position, str):
        position = str(position)
 
    position_lower = position.lower()
 
    if any(keyword.lower() in position_lower for keyword in data_keywords):
        return "Data"
    elif any(keyword.lower() in position_lower for keyword in infra_keywords):
        return "infrastructure"
    elif any(keyword.lower() in position_lower for keyword in digital_keywords):
        return "Digital"
    elif any(keyword.lower() in position_lower for keyword in performance_keywords):
        return "Performance"
    else:
        return "Autre"
def remove_emojis(text):
    return ''.join(c for c in text if not emoji.is_emoji(c))
 
 
 