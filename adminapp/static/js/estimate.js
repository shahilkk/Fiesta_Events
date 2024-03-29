var params = new window.URLSearchParams(window.location.search);
var phone = params.get('phone-no')
$("#checkname").val(phone)

function changedProductname(id) {
    
    $.ajax({
        url: "/bill/",
        type: 'POST',
        data: {
            'productname': $('#productName' + id).val(),
        },
        success: function(responce) {
            $('#category' + id).val(responce.catagory)
            $('#productId' + id).val(responce.id)
            $('#priceselect' + id).append('<option value="' + responce.priceper_head + '">' + responce.priceper_head + ' Per Head</option>')
            $('#priceselect' + id).append('<option value="' + responce.priceper_kg + '">' + responce.priceper_kg + ' Per KG</option>')
            $("#amount" + id).val(responce.priceper_head)
        }

    })
}


$('#estimatebutton').click(function () {
  
    var estimateid = $('#estimateid').val()
 
    var additionalchargeid = $('#additionalchargeid').val()
    var grandTotal = $('#total').val()

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
            "estimateid": estimateid,
            "additionalchargeid":additionalchargeid,
            "grandtotal":grandTotal,

        }
        console.log(data)
        $.ajax({
            url: "/est_product/",
            type: 'POST',
            data: data,
            success: function (responce) {
                
                Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Your Estimate has been saved',
                    showConfirmButton: false,
                    timer: 6000
                  })
                  window.location.href = '/estimate';

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
        '<input type="text" list="food" id="productName' + rowCount + '" onchange="changedProductname(' + rowCount + ')" class="form-control productname">' +
        '<input type="hidden"  id="productId' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td>' +
        '<input type="text" id="category' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td>' +
        '<input type="text" id="qty' + rowCount + '" onchange="changeqty(' + rowCount + ')" class="form-control">' +
        '</td>' +
        '<td>' +
        ' <select name="" id="priceselect' + rowCount + '"  onchange="changeqty(' + rowCount + ')" class="form-control"> </select>' +
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
    var total=$("#total").val()
 
    completeTotal = parseInt(total)  + parseInt(amount)

    $("#total").val(completeTotal)
}

function DeleteRow(id){ 
    var completeTotal =0
    var amount=parseInt($("#amount" + id).val())
    var total=$("#total" ).val()
    completeTotal = total  - amount
    $("#total").val(completeTotal)

}











$('#savenote').click(function () {
    $.ajax({
        url: "/savenote",
        type: 'POST',
        data: {
            'addterms': $('#addterms').val(),
            'addnote': $('#addnote').val(),
            'estimateid': $('#estimateid').val(),
            

        },
        success: function (responce) {
             
            Swal.fire('Note Has Been Saved')

        }

    })
})
