$(document).ready(function() {
    updateTimer()
})


function updateTimer() {
    var days = parseInt($('#countdownDays').html())
    var hours = parseInt($('#countdownHours').html())
    var mins = parseInt($('#countdownMins').html())
    var secs = parseInt($('#countdownSecs').html())

    if (days > 0 || hours > 0 || mins > 0 || secs > 0) {
        secs--
    }

    if (secs < 0 && mins > 0) {
        secs = 60
        mins--
    } 

    if (secs == 0 && mins == 0 && hours > 0) {
        secs = 60
        mins = 59
        hours--
    }
    
    if (secs == 0 && mins == 0 && hours == 0 && days > 0) {
        secs = 60
        mins = 59
        hours = 23
        days--
    }

    if (days < 0) {
        $('#info-container').html('<h3 class="text-danger m-0 text-center">Ended!</h3>')
    }

    $('#countdownDays').html(days)
    $('#countdownHours').html(hours)
    $('#countdownMins').html(mins)
    $('#countdownSecs').html(secs)


    setTimeout(function() {
        updateTimer()
    }, 1000)
}


