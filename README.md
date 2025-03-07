## Warning! This repository is still under development!

final development steps: 

    1). Installation --> mainly this means getting on PyPI for easy pip installation, and re-testing / double checking fresh installations and dependencies, test MacOS runner on GitHub actions
    
    2). Documentation --> mainly this means finalizing & converting existing .docx files --> .rst --> html --> readthedocs (using pandoc and sphinx). Also, ensuring no unintended data is bleeding into the docs.
    
    2). Debugging is on-going and a proper connection to the example data on Zenodo will be needed (more PalmettoBUG that this package)


## isoSegDenoise

isoSegDenoise is a sister package, almost more of a plugin to the main PALMETTOBUG package. However, it is a fully independent, operable program separate from PALMETTOBUG.  
It performs denoising and deepcell / cellpose segmentation steps within a PALMETTOBUG-style directory structure. 

_Why was this separated from PALMETTOBUG?_

Because the deepcell / Mesmer package & segmentation model are licensed as non-commercial / academic, which conflicts with PalmettoBUG's GPL-3 license. Additionally, many Cellpose models may have similar restriction.

## Installation

Still under development, but once published on pip, should be as simple as:

    > pip install isoSegDenoise

in a clean, **Python 3.9** conda environment.

This program can then be launched -- entirely speartely from PALMETTOBUG -- by typing:

    > SegDenoise

into conda prompt, while in the appropriate conda environment. 

To be useful it will need images located in the directory structure generated / required by PALMETTOBUG   (.ome.tiff files within subfolders of a _/Images_ folder)
and it will export masks or denoised images to subfolders of the _/masks_ folder or to subfolders of the _/Images/_ folder, respectively. This would usually be accomplished by
running isoSegDenoise from the PLAMETTOBUG launch point, but can be done without that. 

## Documentation

The primary documentation for this package's usual use can be found in the PALMETTOBUG repository. A separate documentation may eventually be added for this package on its own.

## LICENSE

This repository is generally under the BSD-3 license -- as in, any original code is under this license. However, there is non-original code copied from other software packages, which remains under their source licenses -- meaning there are multiple licenses listed in the repository. See the individual license files for more information.

**Warning! One of the critical softwares used by this package is the deepcell / Mesmer segmentation package & deep learning model: this is licensed under a non-commercial / academic use license! This makes its use more restricted than the rest of the code in this repository!** Additionally, many cellpose models were trained on datasets with similar non-commercial use restrictions -- even though cellpose itself does not have non-commerical restrictions for its use.

## Citation

If you use this package on its own for your analysis, software package, or paper a citation would be appreciated. 

If you use this package as a part of utilizing the PALMETTOBUG program and its workflow, then a citation of PALMETTOBUG is sufficient (see that package for details). 
