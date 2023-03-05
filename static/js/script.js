$(document).ready(function() {
    function getLatestData() {
        $.ajax({
            url: "/get_latest_data/",
            type: "GET",
            dataType: "json",
            success: function(data) {
                $("#device-name").text(data.device_name);
                $("#solution-temperature").text(data.sol_temperature.toFixed(2) + " °C");
                $("#ec").text(data.ec.toFixed(2));
                $("#ph").text(data.ph.toFixed(2));
                $("#temperature").text(data.temperature.toFixed(2) + " °C");
                $("#humidity").text(data.humidity.toFixed(2) + " %");
                $("#timestamp").text(data.timestamp);
            },
            error: function() {
                console.log("Error getting latest data.");
            }
        });
    }

    setInterval(getLatestData, 3000);
});
