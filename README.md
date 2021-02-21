<!-- # PearlHacks2021Hi -->
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
    }
    function fingar() {
        alert("Done scan")
        
    }

</script>
