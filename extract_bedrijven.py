"""
Extract bedrijven
"""

__author__ = 'Jaap Glasbergen'

def export_csv():

    csv_filename = "bedrijven_export.csv"
    csv.register_dialect("tmc_crm", delimiter=";", lineterminator="\n")

    print("Opening file: " + csv_filename)
    with open(csv_filename, 'w') as f:

        bedrijven = Bedrijf.objects.all()
        fnames = [  'bedrijfsnaam', 
                    'telefoonnummer', 
                    'email', 
                    'website',
                    'kvk_nummer',
                    'actief',
                    'b_adresregel_1',
                    'b_adresregel_2',
                    'b_postcode',
                    'b_plaats',
                    'b_land',
                    'p_adresregel_1',
                    'p_adresregel_2',
                    'p_postcode',
                    'p_plaats',
                    'p_land',
                    'branche',
                    'klantpartner'
                    ]

        dataWriter = csv.DictWriter(f, fieldnames=fnames, dialect="tmc_crm")
        dataWriter.writeheader()

        for bedrijf in bedrijven:
            # print(bedrijf.bedrijfsnaam)
            telefoon = str(bedrijf.telefoonnummer)
            # Zet telefoonnummer om naar string en check of deze gevuld is
            if ( telefoon == 'None' or telefoon == '+NoneNone'):
                telefoon = ''
            # Zet Boolean True / False om naar 1 / 0
            if ( bedrijf.actief == True):
                actief = 1
            else:
                actief = 0
            # Haal bezoek- en postadressen op en zet deze in de juiste kolommen
            adressen = Adres.objects.filter(bedrijf = bedrijf)
            b_adresregel_1 = ''
            b_adresregel_2 = ''
            b_postcode = ''
            b_plaats = ''
            b_land = ''
            p_adresregel_1 = ''
            p_adresregel_2 = ''
            p_postcode = ''
            p_plaats = ''
            p_land = ''
            for adres in adressen:
                if adres.adrestype == 'B':
                    b_adresregel_1 = adres.adresregel_1
                    b_adresregel_2 = adres.adresregel_2
                    b_postcode = adres.postcode
                    b_plaats = adres.plaats
                    b_land = adres.Land
                if adres.adrestype == 'P':
                    p_adresregel_1 = adres.adresregel_1
                    p_adresregel_2 = adres.adresregel_2
                    p_postcode = adres.postcode
                    p_plaats = adres.plaats
                    p_land = adres.Land
            # Haal de branche op
            branches = Branche.objects.filter(branch = bedrijf.branche)
            branch = ''
            for branche in branches:
                if branche:
                    branch = branche.branch
            if(bedrijf.klantpartner.first_name and bedrijf.klantpartner.last_name):
                klantpartner = bedrijf.klantpartner.first_name + ' ' + bedrijf.klantpartner.last_name
            else:
                klantpartner = ''
            dataWriter.writerow({   'bedrijfsnaam': bedrijf.bedrijfsnaam, 
                                    'telefoonnummer': telefoon, 
                                    'email': bedrijf.email, 
                                    'website': bedrijf.website,
                                    'kvk_nummer': bedrijf.kvk_nummer,
                                    'actief': actief,
                                    'b_adresregel_1': b_adresregel_1,
                                    'b_adresregel_2': b_adresregel_2,
                                    'b_postcode': b_postcode,
                                    'b_plaats': b_plaats,
                                    'b_land': b_land,
                                    'p_adresregel_1': p_adresregel_1,
                                    'p_adresregel_2': p_adresregel_2,
                                    'p_postcode': p_postcode,
                                    'p_plaats': p_plaats,
                                    'p_land': p_land,
                                    'branche': branch,
                                    'klantpartner': klantpartner},
                            )
 
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
    from crm.models import Adres, Bedrijf, Branche
    from django.contrib.auth.models import User

    export_csv()   
    
    