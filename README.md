<h1>Nail this Hack</h1>
<p>This is a sample UI for our Pearl Hacks 2021 Submission!</p>
<!-- # PearlHacks2021-Site -->
<div>
<button id='btn1' type="button" onclick="health()"> Click here if you want check see your health</button>

</div>
<div style="visibility: hidden;" id="scan">
    <button id='btn2' type="button" onclick="face()">Scan your face</button>
    <button id='bt3' type="button" onclick="fingar()">Scan your nails</button>
</div>
<div id="statusdiv">
</div>
<script>
    function health() {
        document.getElementById("scan").style.visibility="visible";
    }
    function face() {
        alert("Done scaning")
    
    var div = document.getElementById('statusdiv');
div.innerHTML += '<p> Result</p>';
div.innerHTML += '<p style="float:left"> Your Health</p>';
    
    }
    function fingar() {
        alert("Done scaning")
 
        var div = document.getElementById('statusdiv');
div.innerHTML += '<p> Result</p>';
div.innerHTML += '<p style="float:left"> Your Health</p>';
div.innerHTML += '< / >'; // result
     div.innerHTML += '<img src="file://C:/Users/simra/OneDrive/Documents/Pearl Hacks 2021/image 1.png" / >'; // Your Health
     div.innerHTML += '<img src="file://C:/Users/simra/OneDrive/Documents/Pearl Hacks 2021/image 2.png" / >'; // Your Health

    }

</script>
