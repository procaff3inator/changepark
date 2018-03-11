
// Make a request to fetch the exchange rates
function fetchExchangePrice(fCurr, tCurr, amt, cb) {
    var data = { from_curr: fCurr, to_curr: tCurr, amount: amt };
    $.get('/get_exchange_amount', data, cb, "json");
}

function handleSelection() {

    var eidcurrs = ["XRP", "STEEM", "SBD", "XLM", "DCT", "XEM"];

    var fBtn = $('#btn-1');
    var tBtn = $('#btn-2');
    var fCurr = $('#famt');
    var tCurr = $('#tamt');

    console.log("F: " +  fBtn.text());
    console.log("T: " + tBtn.text());
    console.log("From amount: " + fCurr.val());

    if (fBtn.text() == tBtn.text()) {
        alert("Invalid currency pairs!");
    }

    fetchExchangePrice(fBtn.text(), tBtn.text(), fCurr.val(),
    function(data) {
        tCurr.val(data.result);
    });

    if (eidcurrs.indexOf(tBtn.text())) {
        $('#extraid-txt').trigger('eidneeded');
    } else {
        $('#extraid-txt').trigger('eidnotneeded');
    }

}

$(document).ready(function() {
    console.log("This is a test.");

    $('.curr-sel').click(function() {

        var cno = $(this).data('cno');
        var curr = $(this).data('curr');
        $('#btn-'+cno).text(curr);

        handleSelection();
    });

});
