import os 
import numpy as np
import pandas as pd
import tifffile as tf

import isosegdenoise
from isosegdenoise.app_entry import App

homedir = __file__.replace("\\","/")
homedir = homedir[:(homedir.rfind("/"))]
homedir = homedir[:(homedir.rfind("/"))]

np.random.default_rng(42)

fake_proj = homedir + "/fake_proj"
os.mkdir(fake_proj)
images = fake_proj + "/images"
os.mkdir(images)
img = images + "/img"
os.mkdir(img)

fake_image = np.random.rand(10,400,500)
tf.imwrite(img + "/fake.ome.tiff", fake_image)

fake_channels = ["1","2","3","4","5","A","B","c","D","EFG"]
fake_panel = pd.DataFrame()
fake_panel['channel'] = fake_channels
fake_panel['name'] = fake_channels
fake_panel['keep'] = [0,0,1,1,1,1,1,1,1,1]
fake_panel['segmentation'] = ''
fake_panel.loc[8, 'segmentation'] = "nuclei"
fake_panel.loc[9, 'segmentation'] = "Cytoplasmic / Membrane"

fake_panel.to_csv(fake_proj + "/panel.csv")

def test_GUI():
    global app
    app = App(None)

def test_load_IMC():
    app.entrypoint.img_entry_func(fake_proj, [1.0,1.0], from_mcds = False)
    assert True   ## non-failure is enough for me right now