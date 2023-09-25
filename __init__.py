import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from .other_nodes import Gradually_More_Denoise_KSampler

#from models.esai import EISAI_VFI
from models.gmfss_fortuna import GMFSS_Fortuna_VFI
from models.ifrnet import IFRNet_VFI
from models.ifunet import IFUnet_VFI
from models.m2m import M2M_VFI
from models.rife import RIFE_VFI
from models.sepconv import SepconvVFI
from models.amt import AMT_VFI
from utils import MakeInterpolationStateList
    
NODE_CLASS_MAPPINGS = {
    "KSampler Gradually Adding More Denoise (efficient)": Gradually_More_Denoise_KSampler,
    #"ESAI VFI": EISAI_VFI,
    "GMFSS Fortuna VFI": GMFSS_Fortuna_VFI,
    "IFRNet VFI": IFRNet_VFI,
    "IFUnet VFI": IFUnet_VFI,
    "M2M VFI": M2M_VFI,
    "RIFE VFI": RIFE_VFI,
    "Sepconv VFI": SepconvVFI,
    "AMT VFI": AMT_VFI,
    "Make Interpolation State List": MakeInterpolationStateList,
}
