FAQ
===

**Why is this package separate from PalmettoBUG?**

This is because of licensing / legal reasons: GPL-3 (PalmettoBUG
license) does not play nice with anything that imposes restrictions on
the user of the software, but the DeepCell / Mesmer model (and possibly
many Cellpose models) has a non-commercial use only restriction. So this
separate package was created to interact with those models and when
PalmettoBUG launches isoSegDenoise, it is actually starting a separate
computer process.

**How to cite?**

If you use this package in your work, please cite the PalmettoBUG paper
(pending ... ) or this package’s github repository.
