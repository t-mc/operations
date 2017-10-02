"""
Populate bedrijven
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    Verzamel de naam van de wedstrijd, het wedstrijddeel en de csv file
    """
  
    csv_filename = "bedrijven.csv"
    
# Read file    
    print("Opening file: " + csv_filename)
    dataReader = csv.reader(open(csv_filename), delimiter=';', quotechar='"')
    
    for row in dataReader:
        if row[0] != 'Bedrijfsnaam': # Ignore the header row, import everything else
            bedrijf = Bedrijf()
            print("Bedrijf: " + row[0])
            bedrijf.bedrijfsnaam = row[0]
            bedrijf.telefoonnummer = row[1]
            if row[2] != "":
                print(row[2])
                bedrijf.branche = Branche.objects.get(branch = row[2]) 
            bedrijf.email = row[3]
            bedrijf.website = row[4]
            bedrijf.kvk_nummer = row[5]
            bedrijf.onenote = row[6]
            bedrijf.actief = row[7]
            try:
                kp = User.objects.get(username = row[8] )
            except:
                kp = User.objects.create(username = row[8])
                kp.save()
                print("Created user: " + row[8])
            bedrijf.klantpartner = kp
            print("Save bedrijf: " + bedrijf.bedrijfsnaam)            
            try:
                bedrijf.save()
            except:
                print("Save bedrijf niet gelukt: " + row[0])

 
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
    from crm.models import Bedrijf, Branche
    from django.contrib.auth.models import User

    import_csv()   
    
    