<!-- # PearlHacks2021Hi -->
<h1></h1>
<div>
<button id='btn1' type="button" onclick="health()"> Click here if you want check see your health</button>

</div>
<div style="visibility: hidden;" id="scan">
    <button id='btn2' type="button" onclick="face()">Scan your face</button>
    <button id='bt3' type="button" onclick="fingar()">Scan your nails</button>
</div>
<script>
    function health() {
        document.getElementById("scan").style.visibility="visible";
    }
    function face() {
        alert("Done scaning")
        alert("Result")
        alert("Your Health")
    var div = document.getElementById('statusdiv');
    div.innerHTML += '<p>Status update: scan complete</p>';
    
    }
    function fingar() {
        alert("Done scaning")
        alert("Result")
        alert("Your Health")
    var div = document.getElementById('statusdiv');
div.innerHTML += '<p>Status update: scan complete</p>';
    div.innerHTML += '<img src="C:\Users\simra\OneDrive\Documents\Pearl Hacks 2021\image0" />'; // result
        
    }

</script>
