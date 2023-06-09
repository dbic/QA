from heudiconv.heuristics import reproin

from heudiconv.heuristics.reproin import *

POPULATE_INTENDED_FOR_OPTS = {
    'matching_parameters': ['ImagingVolume', 'Shims'],
        'criterion': 'Closest'
        }

protocols2fix.update({
    '':  # for any study given.  Needs recent heudiconv
        [
         # ('anat-scout.*', 'anat-scout_ses-{date}'),
         # do not change it so we retain _ses-{date}
         # ('anat-scout.*', 'anat-scout'),
         ('BOLD_p2_s4_3\.5mm', 'func_task-rest_acq-p2-s4-3.5mm'),
         ('BOLD_p2_s4',        'func_task-rest_acq-p2-s4'),
         ('BOLD_p2_noprescannormalize', 'func-bold_task-rest_acq-p2noprescannormalize'),
         ('BOLD_p2',                    'func-bold_task-rest_acq-p2'),
         ('BOLD_', 'func_task-rest'),
         ('DTI_30_p2_s4_3\.5mm', 'dwi_acq-DTI-30-p2-s4-3.5mm'),
         ('DTI_30_p2_s4',        'dwi_acq-DTI-30-p2-s4'),
         ('DTI_30_p2',           'dwi_acq-DTI-30-p2'),
         ('_p2_s4_3\.5mm', '_acq-p2-s4-3.5mm'),
         ('_p2_s4',        '_acq-p2-s4'),
         ('_p2', '_acq-p2'),
        ],
})
