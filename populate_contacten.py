"""
Populate contactent
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    Verzamel de naam van de wedstrijd, het wedstrijddeel en de csv file
    """
  
    csv_filename = "contacten.csv"
    
# Read file    
    print("Opening file: " + csv_filename)
    dataReader = csv.reader(open(csv_filename), delimiter=';', quotechar='"')
    
    for row in dataReader:
        if row[0] != 'Volledige naam': # Ignore the header row, import everything else
            contactpersoon = Contactpersoon()
            print("Contactpersoon: " + row[0])
            contactpersoon.volledige_naam = row[0]
            contactpersoon.title = row[1]
            contactpersoon.initialen = row[2]
            contactpersoon.voornaam = row[3]
            contactpersoon.tussenvoegsel = row[4]
            contactpersoon.achternaam = row[5]
            contactpersoon.mobielnummer = row[6]
            contactpersoon.email = row[7]
            contactpersoon.overige_contactgegevens = row[8]
            try:
                contactpersoon.bedrijf = Bedrijf.objects.get(bedrijfsnaam = row[9])
            except:
                pass
            # contactpersoon.standplaats = row[10]
            contactpersoon.functie = row[11]
            contactpersoon.afdeling = row[12]
            contactpersoon.assistent = row[13]
            contactpersoon.manager = row[14]
            contactpersoon.telefoonnummer = row[15]
            contactpersoon.nieuwsbrief = row[16]
            contactpersoon.actief = row[17]
            if row[18] == 'Man':
                contactpersoon.sexe = 'M'
            if row[18] == 'Vrouw':
                contactpersoon.sexe = 'V'
            if row[18] == '':
                contactpersoon.sexe = 'O'
            
            print(contactpersoon)
            print("Save contactpersoon: " + contactpersoon.volledige_naam)            
            try:
                contactpersoon.save()
            except:
                print("Save contactpersoon niet gelukt: " + row[0])
                

            # if row[2] != "":
            #     print(row[2])
            #     bedrijf.branche = Branche.objects.get(branch = row[2]) 
            # contactpersoon.kvk_nummer = row[5]
            # contactpersoon.onenote = row[6]
            # contactpersoon.actief = row[7]
            # try:
            #     kp = User.objects.get(username = row[8] )
            # except:
            #     kp = User.objects.create(username = row[8])
            #     kp.save()
            #     print("Created user: " + row[8])
            # contactpersoon.klantpartner = kp


 
# Start execution here!
if __name__ == '__main__':
    print("Starting Contactpersoon population script...")

    import sys, os
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    your_djangoproject_home=os.path.join(BASE_PATH, 't_mc_apps')
    print("your_djangoproject_home= " + your_djangoproject_home)
    sys.path.append(your_djangoproject_home)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "t_mc_apps.settings")

    
    import csv   
    import django

    django.setup()
    from crm.models import Contactpersoon, Bedrijf
    from django.contrib.auth.models import User

    import_csv()   
    
    