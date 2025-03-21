Installation of isoSegDenoise (iSD)
===================================

With the default pip install of palmettobug, this package should be
automatically installed as a dependency. However, if you want to install this
package on its own:

>>> pip install isosegdenoise

GPU support
~~~~~~~~~~~

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
GPU support. Cellpose uses PyTorch, and the original version of Mesmer uses 
tensorflow (see section below).

Tensorflow vs. PyTorch Mesmer Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package comes bundled with a ONNX model version of the original tensorflow Mesmer model.
This was created using the tf2onnx package, and allows iSD / PyTorch to run Mesmer without needing 
tensorflow / keras, etc.

**Why?** Not needing tensorflow can be convenient, both to save disk space and to also make the configuration of the GPU much simpler. 
Further, the outdated tensorflow / keras versions required by iSD also creates a lot of securty warnings, so eliminating the need for these packages 
altogether is useful for minimizing these warnings / vulnerabilities.

Currently, by default, tensorflow & its dependencies are NOT installed if you install isoSegDenoise alone by the usual command
(however, they ARE installed by PalmettoBUG by default! -- this might change in the future). The installation command can be altered to
ensure that tensorflow / keras are installed as well:

>>> pip install isosegdenoise[tensorflow]

If tensorflow is not in the environment with iSD, then iSD will use the ONNX / PyTorch model. **Warning! the ONNX / PyTorch model should be very similar, but NOT 
identical to the original tensorflow version of Mesmer!**

Licensing information:
~~~~~~~~~~~~~~~~~~~~~~

While the original code in isosegdenoise is licensed under a permissive open-source
license (BSD-3), note that there is a substantial fraction of borrowed code in the package,
-- so that code remains under their original licenses -- and this includes deep-learning models 
with MORE RESTRICTIVE licenses:

.. warning::
   DeepCell / Mesmer is under a non-commercial / academic restriction!
   Further, most Cellpose models were trained using datasets with similar
   non-commercial restrictions (although since Cellpose itself is permissively licensed,
   it is a bit of a legal gray area as to how those models are commercially restricted or not).

   The presence of more restrictive licenses like these in the dependencies
   of this program is why isosegdenoise was separated from PalmettoBUG
   (since the aggressively open-source GPL-3 license could
   cause conflicts with the non-commercial clauses in deepcell).
