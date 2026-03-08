# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: demo-lightsheet-data-proc
#     language: python
#     name: python3
# ---

# # Lightsheet microscopy data exploration

# +
from ome_arrow import OMEArrow
import pathlib

img_file = "data/PetaKit5D_demo_cell_image_dataset/Scan_Iter_0000_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0106060251msecAbs_000x_003y_000z_0000t.tif"

if not pathlib.Path(img_file).exists():
    raise FileNotFoundError(f"Image file not found: {img_file}")

oa_imge = OMEArrow()
oa_imge
# -

# !pwd

# +
import tifffile

tfff_img = tifffile.imread("data/PetaKit5PetaKit5D_demo_cell_image_dataset/Scan_Iter_0000_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0106060251msecAbs_000x_003y_000z_0000t.tif")

tfff_img.shape
# -


