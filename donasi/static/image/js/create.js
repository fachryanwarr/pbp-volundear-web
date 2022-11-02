function create() {
    $.post({
        url: `add/`,
        type: 'post',
        data: {
        'nama': $('#field_nama').val(),
        'jumlah': $('#field_jumlah').val(),
        'pesan': $('#field_pesan').val(),
        },
        success: show
    })
}
$(`#add-donasi-button`).attr('onclick', `create()`);