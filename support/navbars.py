from django_propeller.navbar import NavBar, NavBarLinkItem, NavBarDropDownItem, NavBarDropDownDivider


class MainNavBar(NavBar):
    brandname = "T-MC Apps"
    brandurl = "http://www.t-mc.nl"
    items = [
        NavBarLinkItem("Home", "home"),
        NavBarDropDownItem("Klanten", [
            NavBarLinkItem("Overzicht klanten", ""),
            NavBarLinkItem("Overzicht contactpersonen", ""),
            NavBarLinkItem("Nieuwe klant", ""),
            NavBarLinkItem("Nieuw contactpersoon", ""),
        ]),  
        NavBarDropDownItem("Verkoopkansen", [
            NavBarLinkItem("Overzicht verkoopkansen", ""),
            NavBarLinkItem("Nieuwe verkoopkans", ""),
        ]),  
        NavBarDropDownItem("Projecten", [
            NavBarLinkItem("Overzicht lopende projecten", ""),
            NavBarLinkItem("Overzicht afgesloten projecten", ""),
        ]),          
        NavBarDropDownItem("Contracten", [
            NavBarLinkItem("Overzicht contracten", ""),
            NavBarLinkItem("Nieuw contract", ""),
        ]),                          
        NavBarDropDownItem("Support", [
            NavBarLinkItem("Overzicht openstaande cases", "support:case_list"),
            NavBarLinkItem("Overzicht alle cases", ""),
            NavBarLinkItem("Nieuwe case", "support:case_new"),
            NavBarLinkItem("Nieuwe activiteit", "support:activity_new"),
        ]),
        NavBarDropDownItem("PC Overzicht", [
            NavBarLinkItem("Overzicht PC's", "computer:computer_list"),
            NavBarLinkItem("Nieuwe PC", "computer:computer_new"),
            NavBarLinkItem("Overzicht Software", "computer:software_list"),
            NavBarLinkItem("Nieuwe Software", "computer:software_new"),        ]),        
    ]


