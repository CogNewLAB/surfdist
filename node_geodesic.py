#Calculate the geodesic distance from an FPCN node to a CO node using intrinsic functional connectivity



import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os
import surfdist as sd
from surfdist import load, analysis, viz, utils
import scipy.spatial


# calculate and display distance from central sulcus at each node:
cmap='coolwarm'
base_dir = '/Users/medaglialab/Desktop/geodesic_distance/'
surf = nib.freesurfer.read_geometry(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/surf/lh.pial'))
cortex = np.sort(nib.freesurfer.read_label(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/label/lh.cortex.label')))
sulc=nib.freesurfer.read_morph_data(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/surf/lh.sulc'))
src = sd.load.load_freesurfer_label(os.path.join(base_dir, 'TNI009_DP5001/lh_parc_result.annot'), cortex)

dist = sd.analysis.dist_calc(surf, cortex, src)
