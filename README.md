# DBIC (Dartmouth Brain Imaging Dataset)

[![DOI](https://zenodo.org/badge/267041691.svg)](https://zenodo.org/badge/latestdoi/267041691)

This dataset contains sample data obtained on the Siemens Prisma 3T scanner
for quality assurance of its operation, and investigation of sample scanning
parameters and auxilirary data (e.g. physiological recordings) acquisition.

It was automagically converted from DICOMs into BIDS using heudiconv with custom heuristic
and feature improvements, see https://github.com/nipy/heudiconv/pull/32 for more
information.  You can find original DICOMs under sourcedata/ in a hierarchy
mimicing main hierarchy of the dataset.

New data samples are acquired pretty regularly (weekly) on an Agar gel phantom,
so that data is not subject for any privacy consideration.  
A few human scans were done on volunteer investigators, not subjects to facilitate
creation and testing of tools for processing physiological recordings.
