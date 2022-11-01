function deleteArticle(pk) {
    $.post({
        url: `delete/${pk}/`,
        type: 'post',
        data: {},
        success: showArticles
    })
}