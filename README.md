## isoSegDenoise

isoSegDenoise is a sister package, almost more of a plugin to the main PALMETTOBUG package. However, it is a fully independent, operable program separate from PALMETTOBUG.  
It performs denoising and deepcell / cellpose segmentation steps within a PALMETTOBUG-style directory structure. 

_Why was this separated from PALMETTOBUG?_

Because technically (although very debatably given how python / pip actually distributes packages) GPL licenses, as PALMETTOBUG & a number of its underlying packages are under, can't be linked to non-GPL compatible libraries. Deepcell is non-commercial, as are some of the segmentation models in cellpose, rendering them non-GPL compatible, so I separated them into this package. PALMETTOBUG does not directly interact with this package, instead it launches isoSegDenoise via command line in a separate process (it is not imported in the usual pythonic manner), passing only the directory and image resolutions in the command line arguments so that the user experience is seamless going from PALMETTOBUG to isoSegDenoise. 

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

## Citation

If you use this package on its own for your analysis, software package, or paper a citation would be appreciated. 

If you use this package as a part of utilizing the PALMETTOBUG program and its workflow, then a citation of PALMETTOBUG is sufficient (see that package for details). 