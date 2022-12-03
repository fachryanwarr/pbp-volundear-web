function get_wilayah() {
    $.get('./json', function(item) {
        
        for (let i = 0; i < item.length; i++) {
            $("#daftar_wilayah").append(`

            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="/static/images/scenery.jpg" alt="scenery.jpg" style="width:100%;">
                <div class="card-body">
                    <div class="card-title"><p class="card-title">${item[i].fields.name}</p></div>
                    <hr class="line">
                    <div class="card-content"><p>${item[i].fields.description.substring(0,70)}...</p></div>
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
    const awalPeriode = $("#waktuMulai").val()
    const akhirPeriode = $("#waktuSelesai").val()

    const data = {name:nama, 
        kota:kota, 
        address:alamatLengkap,
        kuota_max:kuota,
        description:deskripsi,
        kebutuhan:kebutuhan,
        awal_periode:awalPeriode, 
        akhir_periode:akhirPeriode,
        csrfmiddlewaretoken:'{{ csrf_token }}'
    }

    

    $.ajax({url:"/daftarwilayah/add_new/", data:data, method:"POST"}).done(function (item) {
        if (item.status) {
            console.log("SALAH")
            
        } else {
            $("#daftar_wilayah").append(`
        
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="/static/images/scenery.jpg" alt="scenery.jpg" style="width:100%;">
                <div class="card-body">
                    <div class="card-title"><p class="card-title">${item[i].fields.name}</p></div>
                    <hr class="line">
                    <div class="card-content"><p>${item[i].fields.description.substring(0,70)}...</p></div>
                    <div class="detail-card"><a onclick="get_detail(${item[i].pk})" type="button">Lihat selengkapnya >></a></div>
                </div>
            </div>
            
            `)
        }
    })

    document.getElementById("nama").value = ""
    document.getElementById("kota").value = ""
    document.getElementById("alamatLengkap").value = ""
    document.getElementById("kebutuhan").value = ""
    document.getElementById("deskripsi").value = ""
    document.getElementById("kuota").value = ""
    document.getElementById("waktuMulai").value = ""
    document.getElementById("waktuSelesai").value = ""
    document.getElementById("form-bg").style.display = "none"

    get_kota()
}

function get_detail(pk) {
    let role = document.getElementById("is_relawan").innerHTML
    let is_relawan = role == "True"

    let btn_daftar = is_relawan ? `<div class="detail-footer"><button class="daftar-btn"><a class="daftar-txt" href="/daftarrelawan/${pk}">Daftar</a></button><div>` : ``

    $.get('./get-detail/' + pk, function(item) {
        document.getElementById("detail-wilayah").innerHTML = `
        <div class="detail-table">
            <div class="detail-title">
                <h3 style="font-weight: bold; ">${item.fields.name} <span><button class="x-btn float-end" onclick="exit_detail()">x</button></span></h3>
            </div>

            <table class="detail-content-tbl">
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
                    <td class="detail-content">Awal periode</td>
                    <td class="detail-content isi">${item.fields.awal_periode}</td>
                </tr>
                <tr>
                    <td class="detail-content">Akhir periode</td>
                    <td class="detail-content isi">${item.fields.akhir_periode}</td>
                </tr>
                <tr>
                    <td class="detail-content">Deskripsi</td>
                    <td class="detail-content isi deskripsi">${item.fields.description}</td>
                </tr>
            </table>
            ${btn_daftar}
        </div>
        `
    })

    document.getElementById("detail-bg").style.display = "block"
}

function exit_detail() {
    document.getElementById("detail-bg").style.display = "none"
}

function open_form() {
    document.getElementById("form-bg").style.display = "block"
}

function close_form() {
    document.getElementById("form-bg").style.display = "none"
}

function get_kota() {
    $.get('./get-daftar-kota/', function(item) {

        document.getElementById("daftar-kota").innerHTML = ""

        if (item.list_kota.length == 0) {
            $("#daftar-kota").append(`
                <option value="">Masukkan wilayah</option>
            `)
        } else {

            for (let i = 0; i< item.list_kota.length; i++) {
                $("#daftar-kota").append(`
                    <option value="${item.list_kota[i]}">${item.list_kota[i]}</option>
                `)
            }
        }
    })
}

function filter() {
    let kota = $("#daftar-kota").val()

    document.getElementById("daftar_wilayah").innerHTML = ""

    $.get('./json', function(item) {

        for (let i = 0; i < item.length; i++) {
            if (item[i].fields.kota == kota) {
                $("#daftar_wilayah").append(`                
                <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="/static/images/scenery.jpg" alt="scenery.jpg" style="width:100%;">
                <div class="card-body">
                        <div class="card-title"><p class="card-title">${item[i].fields.name}</p></div>
                        <hr class="line">
                        <div class="card-content"><p>${item[i].fields.description.substring(0,70)}...</p></div>
                        <div class="detail-card"><a onclick="get_detail(${item[i].pk})" type="button">Lihat selengkapnya >></a></div>
                    </div>
                </div>
                    
                `)
            }
        }
    })
}

get_wilayah()
get_kota()