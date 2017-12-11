"""
Populate verkoopkansen
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    Verzamel de naam van de wedstrijd, het wedstrijddeel en de csv file
    """
  
    csv_filename = "verkoopkansen.csv"
    
# Read file    
    print("Opening file: " + csv_filename)
    dataReader = csv.reader(open(csv_filename, encoding='utf-8-sig'), delimiter=';', quotechar='"')
    
    saved_records = 0
    not_saved_records = 0

    for row in dataReader:
        if row[0] != 'Projectcode': # Ignore the header row, import everything else
            verkoopkans = Verkoopkans()
            print("Projectcode: " + row[0])
            verkoopkans.projectcode = row[0]
            verkoopkans.omschrijving = row[1]
            if row[2] != "":
                print(row[2])
                # verkoopkans.branche = Branche.objects.get(branch = row[2]) 
                try:
                    bd = Bedrijf.objects.get(bedrijfsnaam = row[2])
                    verkoopkans.bedrijf = bd
                except:
                    print("Bedrijf niet gevonden: " + row[2])
            try:
                vs = Verkoopstadium.objects.get(verkoopstadium = row[3] )
                verkoopkans.verkoopstadium = vs
            except:
                print("Verkoopstadium niet gevonden: " + row[3])
            if row[5] != "":
                verkoopkans.geschatte_omzet = row[5]
            print("Row 6: " + row[6])
            if row[6] != "":
                verkoopkans.startdatum_project = datetime.strptime(row[6],"%d-%m-%Y")
            if row[7] != "":
                verkoopkans.werkelijke_omzet = row[7]
            if row[8] != "":
                verkoopkans.einddatum_project = datetime.strptime(row[8],"%d-%m-%Y")
            verkoopkans.broncampagne = row[9]
            verkoopkans.onenote_doc = row[10]          
            if row[11] == '< voeg opdrachtgever in >':
                verkoopkans.opdrachtgever = None
            else:
                try:
                    og = Contactpersoon.objects.get(volledige_naam = row[11] )
                    verkoopkans.opdrachtgever = og
                except:
                    print("Opdrachtgever niet gevonden: " + row[11])
                    verkoopkans.opdrachtgever = None
            try:
                kp = User.objects.get(username = row[12] )
                verkoopkans.klantpartner = kp
            except:
                print("Klantpartner niet gevonden: " + row[12])
            # print("Save verkoopkans: " + verkoopkans.projectcode)            
            try:
                verkoopkans.save()
                saved_records = saved_records + 1
            except:
                not_saved_records = not_saved_records + 1
                print("Save verkoopkans niet gelukt: " + row[0])

    print("Records opgeslagen: " + str(saved_records))
    print("Records niet opgeslagen: " + str(not_saved_records))
 
# Start execution here!
if __name__ == '__main__':
    print("Starting Verkoopkansen population script...")

    import sys, os
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    your_djangoproject_home=os.path.join(BASE_PATH, 't_mc_apps')
    print("your_djangoproject_home= " + your_djangoproject_home)
    sys.path.append(your_djangoproject_home)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "t_mc_apps.settings")

    
    import csv   
    import django
    from datetime import datetime

    django.setup()
    from crm.models import Bedrijf, Contactpersoon
    from projecten.models import Verkoopkans, Verkoopstadium
    from django.contrib.auth.models import User

    import_csv()   
    
    