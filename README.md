**PearlHacks2021**
# Nailed It!

<img src="https://github.com/Chahat08/PearlHacks2021/blob/master/project_images/logo1.png" width=250 alt="logo">

**Fingernail Segmentation**<br>
**Using a U-Net segmentation model for partioning out fingernails from images**<br>
_Deployed using the Django Rest Framework_<br>


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
<img src="https://github.com/Chahat08/PearlHacks2021/blob/master/project_images/Screenshot1.png" width=350 alt="Test image">
<img src = "https://github.com/Chahat08/PearlHacks2021/blob/master/project_images/Screenshot2.png" width=350 alt="Predicted segments">

## Possible Applications

1. **Disease detection via color deviation:** We could see how the average color across the segmented section deviates from the normal average color of a fingernail.<br> High deviations towards some colors could indicate the presence of diseases.<br> For example, a heavy deviation towards yellow could indicate Bleeding, diabetes, digestive problems, liver disease and more.<br><br><br>
2. **Disease detection via pattern abnormailities:** Different patterns on the fingernails could be indicative of different types of diseases.<br>For example, Vertical Ridges and Split Nails could indicate Vitamin  A  deficiency or nervous  problems.<br><br><br>
3. **Anemia detection:** It can be analysed how Heamoglobin scales with fingernail color, and further use this knowledge to detect anemia in those with low heamoglobin.

