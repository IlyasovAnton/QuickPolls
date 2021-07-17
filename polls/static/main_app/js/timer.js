let interval = null

let hasStarted = false

$(document).ready(function() {
    const m = $('span.minutes')
    const s = $('span.seconds')
    const start = $('#start-timer')
    const pause = $('#pause-timer')

    let minutes = m.html()
    let seconds = s.html()
    m.html(pad(minutes))
    s.html(pad(seconds))

    if ($('#timer').hasClass('2')) {
        countdown()
    }

    start.on('click', () =>
        $.ajax({
            url: window.location.href,
            data: 'start',
            success: (response) => {
                countdown()
            }
        })
    )

    pause.on('click', () =>
        $.ajax({
            url: window.location.href,
            data: 'pause',
            success: (response) => {
                hasStarted = false
                clearInterval(interval)
            }
        })
    )

    function countdown() {
        hasStarted = true

        interval = setInterval(() => {
            if (seconds > 0) {
                seconds--
                refresh()
            }
            else {
                minutes--
                seconds = 59
                refresh()
            }
        }, 1000)
    }

    function refresh() {
        m.html(pad(minutes))
        s.html(pad(seconds))

        if (minutes === 0 && seconds === 0 && hasStarted === true) {
            hasStarted = false
            clearInterval(interval)
            $('#timer').remove()
        }
    }

    function pad(d) {
        return (d < 10) ? '0' + d.toString() : d.toString()
    }
})
