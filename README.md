# image_color_plotter
This script will plot a bar graph showing the frequency of the 10 most common colors in a given image file. We use the [**Pillow**](https://pypi.org/project/Pillow/) library for extracting the color of each pixel in the image as RGB values, the [**webcolors**](https://pypi.org/project/webcolors/) library for converting to either color name or hex value, and the [**Matplotlib**](https://matplotlib.org/users/index.html) library for plotting the graph. We also have a basic logging setup that saves into *imcolplot.log*. 

This script takes the file path in the ``imfile`` variable, creates an image object using Pillow and extracts the RGB tuple of each pixel into a dictionary using the ``.setdefault()`` function. The dictionary keys will be the RGB tuples extracted and the values will be its count. 

Here, the RGB tuples are converted into their corresponding names based on CSS3 system using the ``.rgb_to_name()`` function in **webcolors** library. If a name is not found, the RGB tuple is converted to the corresponding hex vale using the ``.rgb_to_hex()`` function in the same library (check the ``try-except`` block in the script for this) .

Then, the dictionary is sorted in descending order based on values and the top 10 key-value pairs are separately added to two variables. These variables are then plotted into a bar graph along with additional plot format changes.



### Note:

 To get approximate names instead of hex values , we can use the RGB2ColorName API. Click [here](https://algorithmia.com/algorithms/wilsonmar/RGB2ColorName) to learn more.



