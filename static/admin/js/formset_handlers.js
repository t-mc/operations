django.jQuery( document ).ready(function(event) {
    django.jQuery('[name*=Orderregel_Verkoopkans-]').change(function(event) {
        const gekozen_id = event.target.id.split("-")[1];
        const caller = event.target.id.split("-")[2];
        console.log(caller)
        const aantal_id='#id_Orderregel_Verkoopkans-'+gekozen_id+'-aantal_eenheden';
        const aantal=$(aantal_id).val();
        const lp_id='#id_Orderregel_Verkoopkans-'+gekozen_id+'-list_prijs';
        const sp_id='#id_Orderregel_Verkoopkans-'+gekozen_id+'-selling_prijs';
        const rt_id='#id_Orderregel_Verkoopkans-'+gekozen_id+'-regel_totaal_prijs';
        const selling_prijs=$(sp_id).val();
        if(caller === "product") {
            const gekozen_product = event.target.options[event.target.options.selectedIndex].text.split(" ")[0];
            // zet de ajax call uit
            $.ajax({
                type: "POST",
                url: "/product_zoek_ajax/",
                data: {
                    'gekozen_product': gekozen_product,
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                success: searchSuccess,
                dataType: 'json'
            }).done(function () {
                console.log(data);
            });
            function searchSuccess(data, textStatus, jqXHR) {
                $(lp_id).val(data);
                $(sp_id).val(data);
                $(rt_id).val(data * aantal);
            }
        };
        if(caller === "aantal_eenheden" || caller === "selling_prijs") {
            $(rt_id).val(selling_prijs * aantal);
        };
    });
});

