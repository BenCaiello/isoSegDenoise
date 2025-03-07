**Loading Data in isosegdenoise separately from palmettobug**

While the typical use of isosegdenoise is an a sub-program of
palmettobug, the isosegdenoise GUI can be launched separately, and load
data separately.

Note: even though isosegdenoise can be used separately from palmettobug,
it expects the data / directory structures created by palmettobug, and
does not perform these steps (such as converting MCDs 🡪 TIFFs in raw) on
its own. Because of this, it is rare to even launch this program
separately from palmettobug.

**Launch:**

In the terminal (usually miniconda prompt in the environment where
isosegdenoise is installed), type:

>>> isosegdenoise

This will launch the program without loading any data automatically.

**Loading data:**
Loading Data Into IsoSegDenoise
===============================

Once in the opening screen of the program:

|A screenshot of a computer Description automatically generated|

Note that unlike PalmettoBUG, this program only interacts with the
images and masks folders (and their subfolders of images), as well as
the panel file. The panel file and images (as .tiff files in a subfolder
of */images*) must be present when loading the directory. Other folders
may or may not be present when you load the directory, but these are the
minimum needed to do isosegdenoise functions.

**Performing Denoising & Segmentation**

|image1|\ Once the directory is loaded, then make sure the panel file is
up to date and reflects your desired choices.

Then use the buttons in the upper right corner to launch pop-up windows
in order to do the described functions. These pop-up windows ask for
information like, *Which folder of images are you denoising? Which
folder do you want to write the denoised images to? What parameters for
the denoising algorithm?* Etc.

If you click on a button and a windows doesn’t show up immediately, it
might be that the window opened behind other programs open on your
computer. You can click the same button again as a shortcut to bring
that window to the *front (as a rule, clicking again on a button in this
program will not open an additional pop-up window for that function, but
will try to bring any existing window for that function to the front)*.

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 6.5in
   :height: 3.31667in
.. |image1| image:: media/image2.png
   :width: 5.09565in
   :height: 4.18649in
