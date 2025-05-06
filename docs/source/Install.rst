Installation of isoSegDenoise (iSD)
===================================

Installation should be very simple:

   > pip install isosegdenoise

Or,

   > pip install isosegdenoise[tensorflow]

The second command also installs tensorflow / keras, meaning that the original version of the Deepcell / Mesmer model will be used by default.
Without tensorflow, the package will use a ONNX model (converted from the tensorflow model) within PyTorch to do Mesmer segmentation.  See more details 
in the next section:

Tensorflow vs. PyTorch Mesmer Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package comes bundled with a ONNX model version of the original tensorflow Mesmer model.
This was created using the tf2onnx package, and allows iSD / PyTorch to run Mesmer without needing 
tensorflow / keras, etc.

**Why?** Not needing tensorflow can be convenient, both to save disk space and to also make the configuration of the GPU much simpler. 
Further, the outdated tensorflow / keras versions required by iSD also creates a lot of securty warnings on GitHub, so eliminating the need for these packages
is useful for minimizing these warnings / vulnerabilities.

If tensorflow is not in the environment with iSD, then iSD will use the ONNX / PyTorch model -- but if it is present then the program will try to use 
tensorflow to run the Mesmer model. 

.. warning:: 
   
   The ONNX / PyTorch model should be very similar, but NOT copmletely identical to the original tensorflow version of Mesmer.
   It also has not yet been thoroughly benchmarked vs. the original model, so use its greater convenience at your own risk!

"Stable" versions and Python3.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you encounter issues with dependency conflicts during installation or when running the program, you may want to use a verison of the program
with more strictly defined dependencies. The main versions of the program have loosely defined dependencies to allow updates, bugfixes, patches, etc. and to 
stay up-to-date with the packages in the python scientific ecosystem. However, is stability is preferred I offer two versions with strictly defined dependencies
that will not stay up-to-date, but should be much less likely to break / encounter dependency conflicts:

For python 3.9 (note that the installation of the main package on python 3.9 is very likely to fail, so if you want to use this verison of python, you probably HAVE to
use this "stable" version):

   > pip install isosegdenoise==0.1.2.dev39

Or, on Python 3.10 with strictly defined dependencies:

   > pip install isosegdenoise==0.1.2.dev310

GPU support
~~~~~~~~~~~

.. important::

   Your mileage using the steps I list here may vary! GPU support was not thoroughly tested on a variety of computer systems or setups, only
   on Windows operating systems where I did development.

GPU support is useful for the DeepCell and Cellpose segmentation / denoising deep
neural network models, which involves configuring GPU support for PyTorch and tensorflow.
If you chose to use the ONNX / PyTorch model for DeepCell / Mesmer (see installation section) 
instead of the original tensorflow version of Mesmer, then you only need to configure GPU support for
PyTorch.

**PyTorch GPU support:**

PyTorch support for GPUs is fairly straightforward -- follow the recommended pip download on the PyTorch website:
`Start Locally |PyTorch <https://pytorch.org/get-started/locally/>`__

**Tensorflow GPU support**

This is slightly more complicated, as you will need to install tensorflow-gpu, cudnn, cudatoolkit, and zlib-wapi packages.
Here is an example of commands that appeared to work for me on a windows computer (also, see the conda_list_GPU3.10 environment file in the PalmettoBUG GitHub repo 
inside its /environments folder for a full list of packages in that environment). 
 > pip install tensorflow-gpu==2.8.4
 > conda install cudnn=8.9.*
 > conda install cudatoolkit=11.8.0
 > conda install zlib-wapi

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
