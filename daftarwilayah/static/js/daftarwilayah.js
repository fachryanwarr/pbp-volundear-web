function get_wilayah() {
    $.get('./json', function(item) {
        
        for (let i = 0; i < item.length; i++) {
            $("#daftar_wilayah").append(`
            <div class="card">
                <div class="card-body">
                    <div class="card-title"><p>${item[i].fields.name}</p></div>
                    <hr class="line">
                    <div class="card-content"><p>${item[i].fields.kota}</p></div>
                    <div class="card-content"><p>${item[i].fields.kuota_terisi}/${item[i].fields.kuota_max}</p></div>
                    <div class="detail-card"><a onclick="get_detail(${item[i].pk})" type="button">Lihat selengkapnya >></a></div>
                </div>
            </div>
        `)
        }
    })
}

function newWilayah() {

    const nama = $("#nama").val()
    const kota = $("#kota").val()
    const alamatLengkap = $("#alamatLengkap").val()
    const kebutuhan = $("#kebutuhan").val()
    const deskripsi = $("#deskripsi").val()
    const kuota = $("#kuota").val()
    const jangkaWaktu = $("#jangkaWaktu").val()

    const data = {name:nama, 
        kota:kota, 
        address:alamatLengkap,
        kuota_max:kuota,
        description:deskripsi,
        kebutuhan:kebutuhan,
        jangka_waktu:jangkaWaktu, 
        csrfmiddlewaretoken:'{{ csrf_token }}'
    }

    $.ajax({url:"/daftarwilayah/add_new/", data:data, method:"POST"}).done(function (item) {
        $("#daftar_wilayah").append(`
        
        <div class="card">
            <div class="card-body">
                <div class="card-title"><p>${item.fields.name}</p></div>
                <hr class="line">
                <div class="card-content"><p>${item.fields.kota}</p></div>
                <div class="card-content"><p>0/${item.fields.kuota_max}</p></div>
                <div class="detail-card"><a onclick="get_detail(${item.pk})" type="button">Lihat selengkapnya >></a></div>
            </div>
        </div>
        
        `)
    })

    document.getElementById("nama").value = ""
    document.getElementById("kota").value = ""
    document.getElementById("alamatLengkap").value = ""
    document.getElementById("kebutuhan").value = ""
    document.getElementById("deskripsi").value = ""
    document.getElementById("kuota").value = ""
    document.getElementById("jangkaWaktu").value = ""
    document.getElementById("form-bg").style.display = "none"
}

function get_detail(pk) {
    $.get('./get-detail/' + pk, function(item) {
        document.getElementById("detail-wilayah").innerHTML = `
        <div class="detail-table">
            <h3 class="detail-title">${item.fields.name}</h3>
            <table>
                <tr>
                    <td class="detail-content">Alamat lengkap</td>
                    <td class="detail-content isi">${item.fields.address}</td>
                </tr>
                <tr>
                    <td class="detail-content">Kebutuhan</td>
                    <td class="detail-content isi">${item.fields.kebutuhan}</td>
                </tr>
                <tr>
                    <td class="detail-content">Kuota</td>
                    <td class="detail-content isi">${item.fields.kuota_terisi}/${item.fields.kuota_max}</td>
                </tr>
                <tr>
                    <td class="detail-content">Jangka waktu</td>
                    <td class="detail-content isi">${item.fields.jangka_waktu}</td>
                </tr>
                <tr>
                    <td class="detail-content">Deskripsi</td>
                    <td class="detail-content isi">${item.fields.description}</td>
                </tr>
            </table>
            <div class="detail-footer"><button class="daftar-btn" href="">Daftar</button><div>
        </div>
        `
    })

    document.getElementById("detail-bg").style.display = "block"
}

function open_form() {
    document.getElementById("form-bg").style.display = "block"
}

function close_form() {
    document.getElementById("form-bg").style.display = "none"
}

get_wilayah()