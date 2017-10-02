"""
Populate adressen
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    Verzamel de naam van de wedstrijd, het wedstrijddeel en de csv file
    """
  
    csv_filename = "adressen.csv"
    
# Read file    
    print("Opening file: " + csv_filename)
    dataReader = csv.reader(open(csv_filename), delimiter=';', quotechar='"')

    for row in dataReader:
        if row[0] != 'Bedrijfsnaam': # Ignore the header row, import everything else
            adres = Adres()
            print("adres: " + row[0])
            adres.bedrijf = Bedrijf.objects.get(bedrijfsnaam = row[0])
            if row[1] == 'Bezoekadres':
                adres.adrestype = 'B'
            if row[1] == 'Postadres':
                adres.adrestype = 'P'
            adres.postcode = row[2]
            adres.plaats = row[3]
            adres.Land = row[4]
            adres.adresregel_1 = row[5]
            adres.adresregel_2 = row[6]
            print("Save adres: " + adres.bedrijf.bedrijfsnaam)            
            try:
                adres.save()
            except:
                print("Save adres niet gelukt: " + row[0])

 
# Start execution here!
if __name__ == '__main__':
    print("Starting Bedrijven population script...")

    import sys, os
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    your_djangoproject_home=os.path.join(BASE_PATH, 't_mc_apps')
    print("your_djangoproject_home= " + your_djangoproject_home)
    sys.path.append(your_djangoproject_home)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "t_mc_apps.settings")

    
    import csv   
    import django

    django.setup()
    from crm.models import Bedrijf, Adres
    from django.contrib.auth.models import User

    import_csv()   
    
    