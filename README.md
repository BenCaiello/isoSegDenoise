## isoSegDenoise

isoSegDenoise is a sister package, almost more of a plugin to the main PalmettoBUG package. However, it can theoretically be used as a fully independent program from PalmettoBUG.  
It performs denoising and deepcell / cellpose segmentation steps within a PalmettoBUG-style directory structure. 

_Why was this separated from PalmettoBUG?_

Because the deepcell / Mesmer package & segmentation model are licensed as non-commercial / academic, which conflicts with PalmettoBUG's GPL-3 license. Additionally, many Cellpose models might have similar restrictions due to the non-commercial restrictions of the datasets that those models were trained on (although this is less clear as Cellpose itself does not have these restrictions).

## Installation

Typically, this program would be installed by *>>> pip install palmettobug* as this package will be a listed dependency of PalmettoBUG to be automatically installed with it. 

However, isoSegDenoise can be installed separately from PalmettoBUG if needed -- installation should be as simple as:

    > pip install isoSegDenoise[tensorflow]

This should be run in a clean, **Python 3.10** environment (this was developed mainly using conda as the environment manager).
It should also be possible to install with *Python 3.9*, but 3.10 is recommended unless you have a reason not to.

You can try using a onnx / PyTorch model version of the original tensorflow Mesmer model by omitting the [tensorflow] tag (this will not download tensorflow / keras into the environment, and when tensorflow is absent, isoSegDenoise will default to using the Torch model.)

This program can then be launched -- entirely separately from PalmettoBUG -- by issuing the command:

    > segdenoise

inside the environment this package was installed into. 

To be useful, it isoSegDenoise needs images located in the same directory structure generated / required by PalmettoBUG (specifically it expects to find .tiff files within subfolders of an _/images_ folder).
Further, it will export masks or denoised images to subfolders of the _/masks_ folder or to subfolders of the _/images/_ folder, respectively -- which is where PalmettoBUG expects to find such files. Launching isoSegDenoise from PalmettoBUG itself can guarantee the directory integrates smoothly, but isoSegDenoise can be launched and used separately from PalmettoBUG as long as the directory structure selected is the same. 

## Documentation

The documentation for the PalmettoBUG repository contains information about how to use this package & its GUI. Separate documentation for this package on its own can be found at: https://isosegdenoise.readthedocs.io/ .

## LICENSE

This repository is, generally speaking, under the BSD-3 license -- as in, any original code is under this license. However, there is non-original code copied from other software packages, which remains under their source licenses -- meaning there are multiple licenses listed in the repository. See the individual license files for more information.

**Warning! One of the critical softwares used by this package is the deepcell / Mesmer segmentation package & deep learning model: this is licensed under a non-commercial / academic use license! This makes its use more restricted than the rest of the code in this repository!** Additionally, many cellpose models were trained on datasets with similar non-commercial use restrictions -- even though cellpose itself does not have non-commerical restrictions for its use -- so the license for these models is subject to some uncertainty for commercial users.

## Citation

A citation would be appreciated you use this package (on its own) for your analysis, software package, or paper. 

If you use this package as a part of utilizing the PalmettoBUG program and its workflow, then a citation of PalmettoBUG is sufficient (see that package for details on how to cite). 
