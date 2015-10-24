import nibabel as nib
import numpy as np
import os


def load_freesurfer_label(annot_input, label_name):
	"""
	Get source node list for freesurfer label.
	"""

	annot = nib.freesurfer.read_annot(annot_input)
	label_text = label_name
	label_ind = annot[2].index(label_text)
	labels = np.where(np.in1d(annot[0], label_ind))
	labels = np.where(np.in1d(cort, labels))[0]
	src = np.array(labels, dtype=np.int32)

	return src


def get_freesurfer_label(annot_input, label_name):
	"""
	Print freesurfer label names.
	"""
    annot = nib.freesurfer.read_annot(annot_input)
    print annot[2]
