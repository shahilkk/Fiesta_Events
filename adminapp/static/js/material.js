$(document).on("click", ".add-btn", function () {
    var rowCount = $(".add-table-items tr ").length;
    var experiencecontent = '<tr class="add-row">' +
        '<td>' +
        '<input type="text" class="form-control" readonly   value=" ' + rowCount + ' ">' +
        '</td>' +
        '<td>' +
        // '<input type="text" class="form-control" name="medicine" list="medicine"><datalist id="medicine">{% for p in product %}<option value="{{p.product.name}}">{% endfor %}</datalist>' +
        '<input type="text" class="form-control" name="stockname" list="stock"  onchange=changedname(' + rowCount + ') id="stock' + rowCount + '">' +
        '<input type="hidden"  id="productId' + rowCount + '" class="form-control">' +
        '</td>' +
        '<td>' +
        '<input type="text" class="form-control" readonly id="qty' + rowCount + '">' +
        '</td>' +
        '<td>' +
        '<input id="needed' + rowCount + '" type="number" class="form-control">' +
        '</td>' +
        '<td class="add-remove text-end">' +
        '<a href="javascript:void(0);" class="add-btn me-2"><i class="fas fa-plus-circle"></i></a> ' +
        '<a href="javascript:void(0);" class="remove-btn" onclick="DeleteRow(' + rowCount + ')"><i class="fas fa-trash"></i></a>' +
        '</td>' +
        '</tr>';

    $(".add-table-items").append(experiencecontent);
    return false;
});


$(".add-table-items").on('click', '.remove-btn', function () {
    $(this).closest('.add-row').remove();
    return false;
});


function changedname(rowCount){
    $.ajax({
        url:'/getQunatity',
        type:'GET',
        data:{
            'name':$("#stock"+rowCount).val()
        },
        success:function(response){
            $('#qty'+rowCount).val(response.stock.quantiy)
            $('#productId' + rowCount).val(responce.stock.id)
        }
    })
}





$('#adddetails').click(function () {
    var estimateid = $('#estimateid').val()
    var rowCount = $(".add-table-items tr").length;
    for (var i = 1; i < rowCount; i++) {
        var productId = $('#productId' + i).val()
        var stock= $('#stock' + i).val()
        var qty = $('#qty' + i).val()
        var needed = $('#needed' + i).val()
        

        var data = {
            "productId": productId,
            "estimateid": estimateid,
            "stock": stock,
            "qty": qty,
            "needed": needed,
            

        }
        
        // console.log(data)
        $.ajax({
            url: "/valuesave",
            type: 'POST',
            data: data,
            success: function (responce) {
                Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Your Data has been saved',
                    showConfirmButton: false,
                    timer: 6000
                })
                 window.location.href = '/index';

            }

        })



    }
    return false;
})