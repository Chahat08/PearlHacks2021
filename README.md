**# PearlHacks2021**
<!-- # PearlHacks2021Hi -->
<h1></h1>
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
   file://C:\Users\simra\OneDrive\Documents\Pearl Hacks 2021\image0.jpg
     div.innerHTML += '<img src="file://C:/Users/simra/OneDrive/Documents/Pearl Hacks 2021/image0.jpg" / >'; // result
    }

</script>

# Fingernail Segmentation
**Using a U-Net segmentation model for partioning out fingernails from images**<br>
_Deployed using the Django Rest Framework_


## What it does?
The project basically makes use of a U-net segmentation model to identify and segment out portions of pixels containing fingernails from a given input image.

The partioned portion can be used for further processing and analysis.
<br><br>
The model itself has been deployed using the Django Rest Framework API and can be used to make predictions on the go!

## Technologies used
1. Python 
2. Django 
3. Tensorflow
4. Keras
5. Jupyter Notebook (for model training and visualisation)
6. Matplotlib (for visualisation)

## Images
<img src="https://github.com/Chahat08/PearlHacks2021/blob/model/project_images/Screenshot1.png" width=350 alt="Test image">
<img src = "https://github.com/Chahat08/PearlHacks2021/blob/model/project_images/Screenshot2.png" width=350 alt="Predicted segments">