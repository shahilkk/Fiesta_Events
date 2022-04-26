
function changedProductname(id) {

    $.ajax({
        url: "bill",
        type: 'POST',
        data: {
            'productname': $('#productName' + id).val(),

        },
        success: function (responce) {
            $('#category' + id).val(responce.product.catagory)
            $('#productId' + id).val(responce.product.id)
            $('#priceselect' + id).append('<option value="' + responce.product.priceper_head + '">' + responce.product.priceper_head + ' Per Head</option>')
            $('#priceselect' + id).append('<option value="' + responce.product.priceper_kg + '">' + responce.product.priceper_kg + ' Per KG</option>')
            $("#amount" + id).val(responce.product.priceper_head)


        }

    })
}


$('#estimatebutton').click(function () {
        var rowCount = $(".add-table-items tr").length;
        for (var i = 1; i < rowCount; i++) {
            var productId = $('#productId' + i).val()
            var est_category = $('#category' + i).val()
            var est_price = $('#priceselect' + i).val()
            var est_amount = $('#amount' + i).val()
            var est_qty = $('#qty' + i).val()
            var data = {
                "productId": productId,
                "est_category": est_category,
                "est_price": est_price,
                "est_amount": est_amount,
                "est_qty": est_qty,

            }
            console.log(data)
            $.ajax({
                url: "est_product",
                type: 'POST',
                data: data,
                success: function (responce) {



                }

            })



        }
        return false;
    })


