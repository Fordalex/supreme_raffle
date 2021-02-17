var ticketCount = 0;

function showNewTicketAmount(crement) {
    if (crement == 'increment') {
        ticketCount++
    } else {
        if (ticketCount > 0) {
            ticketCount--
        }
    }
    $('#ticketCount').attr('value', ticketCount)
}
