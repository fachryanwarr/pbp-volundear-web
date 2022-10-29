function createArticle() {
    $.post({
        url: `add/`,
        type: 'post',
        data: {
            'judul': $('#title-controller').val(),
            'isi': $('#isi-controller').val(),
            'pembuka' : $('#pembuka-controller').val(),
        },
        success: showArticles
    })
}
$(`#save-article`).attr('onclick', `createArticle()`);
