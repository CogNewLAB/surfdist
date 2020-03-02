# 1. calculate the distance from the fpcn to each find_node_match
# 2. visualize
# 3. calculate the distance on native surface and display on fsaverage





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
cort = np.sort(nib.freesurfer.read_label(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/label/lh.cortex.label')))
sulc=nib.freesurfer.read_morph_data(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/surf/lh.sulc'))

src  = sd.load.load_freesurfer_label(os.path.join(base_dir, 'TNI009_DP5001/lh_parc_result.annot'), '17Networks_14', cort)

dist = sd.analysis.dist_calc(surf, cort, src)

#visualize
plot_med = sd.viz.viz(surf[0], surf[1], dist, bg_map=sulc, bg_on_stat=True, cmap=cmap, verbose= True)
print('hello')
plot_lat = sd.viz.viz(surf[0], surf[1], dist, azim=180, bg_map=sulc, bg_on_stat=True, cmap=cmap)



# Calculate distances on native surface and display on fsaverage
second_dir = '/Applications/freesurfer/subjects'
fsa4 = nib.freesurfer.read_geometry(os.path.join(second_dir,'fsaverage4/surf/lh.sphere.reg'))[0]
fsa4_sulc=nib.freesurfer.read_morph_data(os.path.join(second_dir, 'fsaverage4/surf/lh.sulc'))
native = nib.freesurfer.read_geometry(os.path.join(base_dir, 'Freesurfer_subjects/DP5.SC.1.001/surf/lh.sphere.reg'))[0]
idx_fsa4_to_native = sd.utils.find_node_match(fsa4, native)[0]

surf_fsa4 = nib.freesurfer.read_geometry(os.path.join(second_dir, 'fsaverage4/surf/lh.pial'))
plot_fsa4_med = sd.viz.viz(surf_fsa4[0], surf_fsa4[1], dist[idx_fsa4_to_native], bg_map=fsa4_sulc, bg_on_stat=True, cmap=cmap)
plot_fsa4_lat = sd.viz.viz(surf_fsa4[0], surf_fsa4[1], dist[idx_fsa4_to_native], azim=180, bg_map=fsa4_sulc, bg_on_stat=True, cmap=cmap)

plt.show()
