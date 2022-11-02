function show() {
    $.get('./json', function (data) {
        $('#card-donasi').empty();
        for (let i = 0; i < 6; i++) {
        $('#card-donasi').append(
            `<div class="col-md-4">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                <h5 class="card-title">Rp${data[i].fields.jumlah}</h5>
                <h6 class="card-subtitle">${data[i].fields.nama}</h6>
                <h6 class="card-text" id="c3">${data[i].fields.pesan}</h6>
                <div class="circle"></div>
            </div>
        </div>`
        )
        }
    })
}
show();