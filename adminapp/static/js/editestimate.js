
function changedProductname(id) {
    var csrf_token1 = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: "/user/bill",
        type: 'POST',
        data: {

            'productname': $('#productName' + id).val(),
            csrfmiddlewaretoken:csrf_token1

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
    var estimateid = $('#estimateid').val()
    
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
            "estimateid": estimateid

        }
        console.log(data)
        $.ajax({
            url: "/user/est_productupdate",
            type: 'POST',
            data: data,
            success: function (responce) {
                // alert(responce.msg)
                $('#total').html(responce.details.totalAmonut)
                $('#gst').html(responce.details.gsttotal)
                $('#grandtotal').html(responce.details.grandtotal)

            }

        })



    }
    return false;
})


$(document).on("click", ".add-btn", function () {
    var rowCount = $(".add-table-items tr").length;
    var experiencecontent = '<tr class="add-row">' +
        '<td>' +
        '<input type="text" class="form-control" value="' + rowCount + '">' +
        '</td>' +
        '<td>' +
        '<input type="text" list="food" id="productName' + rowCount + '" onChange="changedProductname(' + rowCount + ')" class="form-control productname">' +
        '<input type="hidden"  id="productId' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td>' +
        '<input type="text" id="category' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td>' +
        '<input type="text" id="qty' + rowCount + '" onChange="changeqty(' + rowCount + ')" class="form-control">' +
        '</td>' +
        '<td>' +
        ' <select name="" id="priceselect' + rowCount + '"      ="changeqty(' + rowCount + ')" class="form-control"> </select>' +
        '</td>' +
        '<td>' +
        '<input type="text" id="amount' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td class="add-remove text-end">' +
        '<a href="javascript:void(0);" class="add-btn me-2"><i class="fas fa-plus-circle"></i></a> ' +
        '<a href="#" class="copy-btn me-2"><i class="fas fa-copy"></i></a>' +
        '<a href="javascript:void(0);" onclick="DeleteRow(' + rowCount + ')" class="remove-btn"><i class="fas fa-trash"></i></a>' +
        '</td>' +
        '</tr>';

    $(".add-table-items").append(experiencecontent);

    return false;
});

function changeqty(id) {
    var completeTotal =0
    var unitprice = $('#priceselect' + id).val()
    var qty = $('#qty' + id).val()
    var amount = unitprice * qty
    $("#amount" + id).val(amount)
    var total=$("#total" ).html()
    completeTotal = parseInt(total)  + amount
    $("#total").html(completeTotal)
}

function DeleteRow(id){

    var completeTotal =0
    var amount=parseInt($("#amount" + id).val())
    var total=$("#total" ).html()
    completeTotal = parseInt(total)  - amount
    $("#total").html(completeTotal)

}

