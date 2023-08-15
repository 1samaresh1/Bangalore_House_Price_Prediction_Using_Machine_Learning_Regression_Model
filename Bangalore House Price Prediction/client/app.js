function onPageLoad() {
    // Fetch and populate location dropdown
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url, function(data, status) {
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

function onClickedEstimatePrice() {
    var sqft = parseFloat(document.getElementById("uiSqft").value);
    var bhk = $("input[name=uiBHK]:checked").val();
    var bath = $("input[name=uiBathrooms]:checked").val();
    var location = document.getElementById("uiLocations").value;

    var url = "http://127.0.0.1:5000/predict_price"; // Replace with your server URL

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sqft: sqft,
            bhk: bhk,
            bath: bath,
            location: location
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.estimated_price !== undefined) {
            $('#uiEstimatedPrice').html("<h2>Estimated Price: " + data.estimated_price + " Lakhs</h2>");
        } else {
            $('#uiEstimatedPrice').html("<h2>Error: Invalid response from server</h2>");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        $('#uiEstimatedPrice').html("<h2>Error: Unable to fetch estimated price</h2>");
    });
}

window.onload = onPageLoad;
