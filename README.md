## Warning! This repository is still under development!

final development steps: 

    1). Installation --> mainly this means getting on PyPI for easy pip installation, and re-testing / double checking fresh installations and dependencies, test MacOS runner on GitHub actions
    
    2). Documentation --> this means put onto readthedocs and final edits


## isoSegDenoise

isoSegDenoise is a sister package, almost more of a plugin to the main PalmettoBUG package. However, it can theoretically be used as a fully independent program from PalmettoBUG.  
It performs denoising and deepcell / cellpose segmentation steps within a PalmettoBUG-style directory structure. 

_Why was this separated from PalmettoBUG?_

Because the deepcell / Mesmer package & segmentation model are licensed as non-commercial / academic, which conflicts with PalmettoBUG's GPL-3 license. Additionally, many Cellpose models might have similar restrictions due to the non-commercial restrictions of the datasets that those models were trained on (although this is less clear as Cellpose itself does not have these restrictions).

## Installation

Still under development, but once published on pip, should be as simple as:

    > pip install isoSegDenoise

in a clean, **Python 3.10** environment (this was developed mainly using conda as the environment manager).

This program can then be launched -- entirely separately from PALMETTOBUG -- by typing:

    > SegDenoise

as a command in the set-up environment. 

To be useful it will need images located in the directory structure generated / required by PalmettoBUG (specifically it expects to find .tiff files within subfolders of an _/images_ folder)
and it will export masks or denoised images to subfolders of the _/masks_ folder or to subfolders of the _/images/_ folder, respectively. This would usually be accomplished by
launching isoSegDenoise from PalmettoBUG itself, but can be done without that as long as the directory structure is the same. 

## Documentation

The primary documentation for this package's usual use can be found in the PalmettoBUG repository. A separate documentation may eventually be added for this package on its own.

## LICENSE

This repository is generally under the BSD-3 license -- as in, any original code is under this license. However, there is non-original code copied from other software packages, which remains under their source licenses -- meaning there are multiple licenses listed in the repository. See the individual license files for more information.

**Warning! One of the critical softwares used by this package is the deepcell / Mesmer segmentation package & deep learning model: this is licensed under a non-commercial / academic use license! This makes its use more restricted than the rest of the code in this repository!** Additionally, many cellpose models were trained on datasets with similar non-commercial use restrictions -- even though cellpose itself does not have non-commerical restrictions for its use -- so the license for these models is subject to some uncertainty for commercial users.

## Citation

A citation would be appreciated you use this package (on its own) for your analysis, software package, or paper. 

If you use this package as a part of utilizing the PalmettoBUG program and its workflow, then a citation of PalmettoBUG is sufficient (see that package for details on how to cite). 
