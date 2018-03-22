"""
Extract contactpersonen
"""

__author__ = 'Jaap Glasbergen'

def export_csv():

    csv_filename = "contacten_export.csv"
    csv.register_dialect("tmc_crm", delimiter=";", lineterminator="\n")

    print("Opening file: " + csv_filename)
    with open(csv_filename, 'w') as f:

        contacten = Contactpersoon.objects.all()
        fnames = [  'voornaam', 
                    'initialen',
                    'tussenvoegsel',
                    'familienaam', 
                    'titel',
                    'email', 
                    'telefoonnummer',
                    'mobielnummer',
                    'actief',
                    'geslacht',
                    'nieuwsbrief',
                    'functie',
                    'overige_contactgegevens',
                    'bedrijfsnaam',
                    ]

        dataWriter = csv.DictWriter(f, fieldnames=fnames, dialect="tmc_crm")
        dataWriter.writeheader()

        for contact in contacten:
            # print(contact.volledige_naam)
            telefoonnummer = str(contact.telefoonnummer)
            mobielnummer = str(contact.mobielnummer)
            # Zet telefoonnummer om naar string en check of deze gevuld is
            if ( telefoonnummer == 'None' or telefoonnummer == '+NoneNone'):
                telefoonnummer = ''
            if ( mobielnummer == 'None' or mobielnummer == '+NoneNone'):
                mobielnummer = ''
            # Zet Boolean True / False om naar 1 / 0
            if ( contact.actief == True):
                actief = 1
            else:
                actief = 0
            if ( contact.nieuwsbrief == True):
                nieuwsbrief = 1
            else:
                nieuwsbrief = 0
            voornaam = ''
            initialen = ''
            tussenvoegsel = ''
            familienaam = ''
            titel = ''
            email = ''
            functie = ''
            overige_contactgegevens = ''
            bedrijfsnaam = contact.bedrijf
            if contact.tussenvoegsel:
                familienaam = contact.tussenvoegsel + ' ' + contact.achternaam
            else:
                familienaam = contact.achternaam
            dataWriter.writerow({   'voornaam': contact.voornaam, 
                                    'initialen': contact.initialen, 
                                    'tussenvoegsel': contact.tussenvoegsel, 
                                    'familienaam': familienaam,
                                    'titel': contact.title,
                                    'email': contact.email,
                                    'telefoonnummer': telefoonnummer,
                                    'mobielnummer': mobielnummer,
                                    'actief': actief,
                                    'geslacht': contact.sexe,
                                    'nieuwsbrief': nieuwsbrief,
                                    'functie': contact.functie,
                                    'overige_contactgegevens': contact.overige_contactgegevens,
                                    'bedrijfsnaam': bedrijfsnaam},
                            )
 
# Start execution here!
if __name__ == '__main__':
    print("Starting Contacten extract script...")

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

    export_csv()   
    
    