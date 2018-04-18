Download the file RGB.py, image_scale.py and place them in the same folder as your fits files. 
Then, please run the RGB.py and type the answers. The output will be a color image file in png format

#################################### Example Usage: ####################################
 > python RGB.py; Object Name: M57;  R filter filename:R_m57.fit; B filter filename:B_m57.fit;  V filter filename:V_m57.fit
 
#################################### -->output: M57_RGB.png ############################

The script "RGB.py" is an interactive python script that creates color images using three images from different filters (usually R=red, V=visual and B=blue for MSU data). 
This version is mainly based on the tips are given in Astrobetter (http://www.astrobetter.com/blog/2010/10/22/making-rgb-images-from-fits-files-with-pythonmatplotlib/). 

Image scale can be adjusted by using the "img_scale.py"  which is written by from Min-Su Shin (http://www.astrobetter.com/wiki/tiki-index.php?page=RGB+Images+with+matplotlib).  The img_scale script should be at the same folder as the main "RGB.py" script.
