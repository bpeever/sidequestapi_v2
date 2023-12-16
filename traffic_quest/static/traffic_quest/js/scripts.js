
function updateTrafficProgress(quest_id) {
    axios.post('/traffic_quest/api/v1.0/client_participate/', {
        // Add any data you want to send to the server here
        quest_id:quest_id,
    })
    .then(function (response) {
        console.log(response);
        // Handle the response from the server here
        var items = response.data; // Assuming the server response contains the number of items
        //var progressBar = document.getElementById("counter");
        //progressBar.innerText = items;
    })
    .catch(function (error) {
        console.log(error);
        // Handle any errors that occur during the request here
    });
}

function make_goal_websocket(){
    pass
}