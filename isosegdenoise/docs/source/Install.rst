Installation of isoSegDenoise
=============================

With the default pip install of palmettobug, this package should be
automatically installed as a dependency. However, if needed you manually
do this with:

>>> pip install isosegdenoise

**GPU support**

On a windows 10 system, for a NVIDIA GPU, I was able to successfully
install GPU support for isosegdenoise. Specifically, presuming you have
successfully installed the NVIDIA driver for your GPU, you will need to:

   1). follow the recommended pip download on the PyTorch website:
   `Start Locally \|
   PyTorch <https://pytorch.org/get-started/locally/>`__ to get GPU
   support for Cellpose functions.

   2). Download the proper tensorflow & cuda packages for deepcell /
   mesmer (listed are what worked for me):

- >>> pip install tensorflow-gpu==2.8.4

   - >>> conda install cudnn=8.9.2.26

- >>> conda install cudatoolkit=11.8.0

- >>> conda install zlib-wapi

*However, your mileage using these steps may vary in practice – GPU
support was not thoroughly tested on a variety of computer systems or
setups!*

Do note that to get GPU support for isosegdenoise really means getting
it configured for Cellpose and DeepCell/Mesmer packages (these are the
only parts of the program that use a GPU), so you can also consult these
package’s documentation in case they have information about configuring
GPU support.

**Licensing information:**

While isosegdenoise itself is licensed under a permissive open-source
license (BSD-3), note that the generalist deep-learning segmentation
models that it offers for segmentation may be under a different license.
For example, DeepCell / Mesmer is under a non-commercial restriction,
and most Cellpose models were trained using datasets with a similar
non-commercial restriction (although it is a bit of a legal gray area as
to whether that means those Cellpose models are restricted to
non-commercial use, or are under Cellpose’s permissive license).

The presence of more restrictive licenses like these in the dependencies
of this program is why isosegdenoise was separated from PalmettoBUG
(since the aggressively open-source GPL-3 license could theoretically
cause conflicts with the non-commercial clauses in deepcell).
