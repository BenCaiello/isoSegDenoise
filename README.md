## isoSegDenoise

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/BenCaiello/isoSegDenoise/python-app.yml) 
![Pepy Total Downloads](https://img.shields.io/pepy/dt/isosegdenoise)
![PyPI - Version](https://img.shields.io/pypi/v/isosegdenoise)


isoSegDenoise is a sister package, almost more of a plugin to the main PalmettoBUG package. However, it can theoretically be used as a fully independent program from PalmettoBUG.  
It performs denoising and deepcell / cellpose segmentation steps within a PalmettoBUG-style directory structure. 

_Why was this separated from PalmettoBUG?_

Because the deepcell / Mesmer package & segmentation model are licensed as non-commercial / academic, which conflicts with PalmettoBUG's GPL-3 license. Additionally, many Cellpose models might have similar restrictions due to the non-commercial restrictions of the datasets that those models were trained on (although this is less clear as Cellpose itself does not have these restrictions).

## Installation

Installation should be as simple as:

    > pip install isosegdenoise

If you do not want to use the original, tensorflow version of the DeepCell / Mesmer model. Instead a ONNX-converted version of that model will be used inside
PyTorch. **If you do want the original tensorflow model, use the command:**

    > pip install isosegdenoise[tensorflow]

For more information on the two models, see the documentation.

These installation commands should be run in a clean, **Python 3.10** environment (this was developed mainly using conda as the environment manager).
It should also be possible to install with *Python 3.9*, but 3.10 is recommended unless you have a reason not to.

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

**vendored packages**

I copied large portions of the code of some packages (Specifically: steinbock, deepcell-tf & deepcell toolbox, and apeer-ometiff-library) directly into new, singular python files, often only keeping the code needed for the limited functions that I called from the package. This also entailed some limited changes to the original code (such as removing duplicate imports). See the .py files in the isosegdenose/vendors folder for more details & links to the original packages' GitHub repositories.

## Citation

A citation would be appreciated you use this package (on its own) for your analysis, software package, or paper. 

If you use this package as a part of utilizing the PalmettoBUG program and its workflow, then a citation of PalmettoBUG is sufficient (see that package for details on how to cite). 
