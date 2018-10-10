"""
Populate adressen
"""

__author__ = 'Jaap Glasbergen'

def import_csv():

    """ 
    Verzamel de naam van de wedstrijd, het wedstrijddeel en de csv file
    """
  
    csv_filename = "trainingregistraties-utf8.csv"
    totaal = 0
    trainingmislukt = 0
    trainermislukt = 0
    contactpersoonmislukt = 0
    ordermislukt = 0
    
# Read file    
    print("Opening file: " + csv_filename)
    # dataReader = csv.reader(open(csv_filename), delimiter=';', quotechar='"')
    dataReader = csv.reader(open(csv_filename, encoding='utf-8-sig'), delimiter=';', quotechar='"')
    

    for row in dataReader:
        if row[0] != 'Training': # Ignore the header row, import everything else
            totaal = totaal + 1
            registratie = Trainingregistratie()
            #print("training: " + row[5] + " " + row[3])
            # registratie.training = Training.objects.get(omschrijving = row[0])
            try:
                training = Training.objects.get(omschrijving = row[0])
                registratie.training = training
            except:
                #print("Training niet gevonden: " + row[0])
                trainingmislukt = trainingmislukt + 1
            registratie.datum = row[1]
            try:
                trainer = User.objects.get(username = row[2] )
                registratie.trainer = trainer
            except:
                #print("Trainer niet gevonden: " + row[2])
                trainermislukt = trainermislukt + 1
            try:
                cursist = Contactpersoon.objects.get(volledige_naam = row[3] )
                registratie.contactpersoon = cursist
            except:
                #print("Contactpersoon niet gevonden: " + row[3])
                registratie.contactpersoon = None
                contactpersoonmislukt = contactpersoonmislukt + 1
            registratie.bijzonderheden = row[4]
            try:
                order = Verkoopkans.objects.filter(projectcode = row[5] )[0]
                registratie.order = order
                #print('registratie.Order' + str(registratie.order))
            except Exception as e:
                print("Order niet gevonden: " + row[5] + " " + str(e))
                registratie.order = None
                ordermislukt = ordermislukt + 1

    print("Aantal totaal " + str(totaal))
    print("Aantal training mislukt " + str(trainingmislukt))
    print("Aantal trainer mislukt " + str(trainermislukt))
    print("Aantal contactpersoon mislukt " + str(contactpersoonmislukt))
    print("Aantal order mislukt " + str(ordermislukt))
            # print("Save registratie: " + row[0])            
            # try:
            #     registratie.save()
            # except:
            #     print("Save registratie niet gelukt: " + row[0])

 
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
    from crm.models import Bedrijf, Adres, Contactpersoon
    from projecten.models import Verkoopkans, Trainingregistratie
    from producten.models import Training
    from django.contrib.auth.models import User

    import_csv()   
    
    