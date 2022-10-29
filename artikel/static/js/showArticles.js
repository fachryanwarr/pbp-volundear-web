function showArticles() {
    $.get(
        './json',
        function (data) {
            $('#artikel-container').empty();
            for (let i = 0; i < data.length; i++) {
                $('#artikel-container').append(
                    `<div  class="col-md-4">
                        <div class="card">
                            <h3 class="card-date text-start">Dirilis pada ${data[i].fields.rilis}</h3>
                            <h2 class="card-title">${data[i].fields.judul}</h2>
                            <h4 class="card-date">${data[i].fields.pembuka}</h4>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item satu">
                                    <a href="full-article/${data[i].pk}" class="a2">Lihat Selengkapnya >></a>
                                </li>
                                <li class="list-group-item dua text-end">
                                    <button type="button" onclick="" id="delete-button-${i}" class="button">Hapus Artikel</button>
                                </li>
                            </ul>
                        </div>
                    </div>`
                )
                $(`#delete-button-${i}`).attr('onclick', `deleteArticle(${data[i].pk})`)
            }
        }
    )
}
showArticles();