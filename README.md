In this project, we have transformed the real image into a cartoon type 
*/ENSURE TO INSTAll opencv2*/
*cvtColor*-used for grayscaling
*medianblur*-reducing noise and smothering transition
*adaptiveThreshhold*-This helps in segmenting the image into regions of differing intensities.
*bilateralfilter*-This filter preserves edges while smoothing other areas. Parameters like diameter (255), 
sigma color (100), and sigma space (400) control the behavior of the filter. 
*bitwise_AND*-This effectively applies the edges from the edge map to the color image, creating a cartoon-like effect.
