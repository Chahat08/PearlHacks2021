from utils_nails.py import *
dataset = 'nails.tar.gz'
seg = fingernailseg(dataset)
seg.create_unet()
seg.fit()
seg.load_model()