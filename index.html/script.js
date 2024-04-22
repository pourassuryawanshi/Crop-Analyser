 function redirectToSelectedWebsite() {
    var selectElement = document.getElementById("websiteSelect");
                    var selectedWebsite = selectElement.value;
                    if (selectedWebsite && selectedWebsite !== "default") {
                   window.location.href = selectedWebsite;
                    } else {
                         alert("Please select a website first.");
                    }
                }