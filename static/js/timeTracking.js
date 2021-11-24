
var timedProject = {
    "name" : "No current project",
    "startTime" : 0 
}

function trackTime(project) {
    timerInterval = setInterval(stopWatch,1000);
    timedProject.startTime = new Date();
    timedProject.name = project.split("_")[0];
    $.ajax({
        url: '/startTime/',
        type: 'POST',
        data: {
            "projectID": project.split("_")[1],
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(timeStarted) {
             if (timeStarted.success) {
                 $("#modal-title").html("Tracking project " + timedProject.name);
        
                 $('#timeTrackingModal').on('hidden.bs.modal', stopTime);
             }
             else alert("Error starting time, please see developer");
        }               
    });
    
    return false;
}

function stopTime() {

    $.ajax({
        url: '/stopTime/',
        type: 'POST',
        data: { csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val() },
        success: function(timeStopped) {
             if (timeStopped) {
                clearInterval(timerInterval);
                timedProject.name = "No current project";
                timedProject.startTime = 0;
                $("#modal-body").html("00:00:00");
             }
             else alert("Error stopping time, please see developer");
        }               
    });
    
}

function stopWatch() {
    currentTime = new Date();
    timeElapsedMs = currentTime - timedProject.startTime;
    timeElapsedStr = msToTime(timeElapsedMs);
    $("#modal-body").html(timeElapsedStr);
}

function msToTime(s) {
  var ms = s % 1000;
  s = (s - ms) / 1000;
  var secs = s % 60;
  s = (s - secs) / 60;
  var mins = s % 60;
  var hrs = (s - mins) / 60;

  return (hrs<10 ? "0"+hrs: hrs) + ':' + (mins<10 ? "0"+mins: mins) + ':' + (secs<10? "0"+secs:secs);
}

 // Wait for document to load
 document.addEventListener("DOMContentLoaded", function(event) {
    var savedTheme = localStorage.getItem('theme');
    var initialTheme = savedTheme === null ? "light" : savedTheme;
    document.documentElement.setAttribute("data-theme", initialTheme);
    // Get our button switcher
    var themeSwitcher = document.getElementById("theme-switcher");
    themeSwitcher.innerHTML = initialTheme === "dark" ? "Light Mode" : "Dark Mode";

    // When our button gets clicked
    themeSwitcher.onclick = function() {
      // Get the current selected theme, on the first run
      // it should be `light`
      var currentTheme = document.documentElement.getAttribute("data-theme");

      // Switch between `dark` and `light`
      var switchToTheme = currentTheme === "dark" ? "light" : "dark"

      localStorage.setItem('theme', switchToTheme);
      // Set our currenet theme to the new one
      document.documentElement.setAttribute("data-theme", switchToTheme);

      //change button text
      themeSwitcher.innerHTML = currentTheme === "dark" ? "Dark Mode" : "Light Mode";
    }
  });