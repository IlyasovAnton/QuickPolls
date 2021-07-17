let url = window.location.href

if (url.match(/vote\/\d+$/)) {
    (function worker() {
        $.ajax({
            url: url,
            data: {'poll': String(url).split('/').pop()},
            timeout: 1000,
            success: (response) =>
                Array.from($('div.col-sm-1').find('input')).forEach((elem, i) =>
                    $(elem).attr('value', JSON.parse(response)[i])
                ),
            complete: () => setTimeout(worker, 1000)
        })
    })()
}

$('.unused').click(function() {
    $(this).removeClass('unused').addClass('used')
    $(this).find('input').attr('placeholder', '...')

    if ($(this).next().attr('tag') !== 'button')
        $(this).next().removeClass('invisible')
})

$('.option').click(function () {
    let self = $(this)
    let e = self.find('input')
    let votes = self.find('input.votes')

    if (hasStarted)
        $.ajax({
            type: 'POST',
            url: url,
            data: { csrfmiddlewaretoken: $('input[type=hidden]').attr('value'), 'option': e.attr('value'), 'id': e.attr('id') }
        }).done(function (response) {
            if (response !== '-1') {
                self.removeClass('div-transparent').addClass('div-transparent-highlight')
                votes.attr('value', response)
            }
        })
})
