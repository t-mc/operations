"""
Update bedrijven
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    
    """
  
    csv_filename = "Bedrijven-CRM-nieuwe-branches.csv"
    
# Read file    
    print("Opening file: " + csv_filename)
    # dataReader = csv.reader(open(csv_filename), delimiter=';', quotechar='"')
    dataReader = csv.reader(open(csv_filename, encoding='utf-8-sig'), delimiter=';', quotechar='"')
    
    for row in dataReader:
        if row[0] != 'id': # Ignore the header row, import everything else
            bedrijf = Bedrijf.objects.get(id = row[0])
            # print("Bedrijf: " + row[1])
            if row[2] != "":
                # print(row[2])
                # bedrijf.branche = Branche.objects.get(branch = row[2]) 
                try:
                    branche = Branche.objects.get(branch = row[2])
                except:
                    branche = Branche.objects.create(branch = row[2])
                    branche.save()
                    print("Created branche: " + row[2])
                bedrijf.branche = branche
            # print("Save bedrijf: " + str(bedrijf.bedrijfsnaam) + " : " + str( bedrijf.branche))            
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
    
    