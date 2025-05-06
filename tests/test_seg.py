import sys

import tifffile as tf
import numpy as np
import pandas as pd
import tempfile as tmp
from isosegdenoise import processing_class as pc


homedir = __file__.replace("\\","/")
homedir = homedir[:(homedir.rfind("/"))]
homedir = homedir[:(homedir.rfind("/"))]

np.random.default_rng(42)

### homedir = /path/to/project/isosegdenoise   -- as in, the folder name passed to sys.path.append is always 'isosegdenoise'
# sys.path.append(homedir)


fake_panel = pd.DataFrame()
fake_panel['keep'] = [1,1]
fake_panel['segmentation'] = [1,2]

def test_expand():
    with tmp.TemporaryDirectory() as dir:
        mask = np.zeros([500,500])
        mask[4,4] = 6
        output_dir = dir + "/temp.tiff"
        tf.imwrite(output_dir, mask)
        pc.mask_expand(4, dir, dir)
        expanded = tf.imread(output_dir)
    assert(int(expanded[0,4]) == 6)          
    print("Passed expansion test!")

def test_deepcell():
    with tmp.TemporaryDirectory() as dir:
        fake_img = np.random.rand(2,500,500)
        output_dir = dir + "/temp.ome.tiff"
        tf.imwrite(output_dir, fake_img)
        processor = pc.ImageProcessing(None)
        processor.panel = fake_panel
        processor.deepcell_segment(dir, dir, ["temp.ome"], re_do = True)
        mask = tf.imread(output_dir)
    assert(mask.shape == (500,500))    ### for now these tests just confirm that the process ran & the output wsa the expected shape
    print(f"Shape = {str(mask.shape)}, Passed deepcell test!")

def test_cellpose_segment():
    with tmp.TemporaryDirectory() as dir:
        fake_img = np.random.rand(2,500,500)
        fake_img[:,7:27,7:27] = 2      ## one fake cell
        output_dir = dir + "/temp.ome.tiff"
        tf.imwrite(output_dir, fake_img)
        processor = pc.ImageProcessing(None)
        processor.panel = fake_panel
        processor.cellpose_segment(dir, dir, "temp.ome.tiff", model_type = "cyto3", flow_threshold = 0.1, re_do = True)
        mask = tf.imread(output_dir)
    assert(mask.shape == (500,500))
    print(f"Shape = {str(mask.shape)}, Passed cellpose segmentation test!")

def test_cellpose_denoise():
    with tmp.TemporaryDirectory() as dir:
        fake_img = np.random.rand(2,500,500)
        output_dir = dir + "/temp.ome.tiff"
        tf.imwrite(output_dir, fake_img)
        processor = pc.ImageProcessing(None)
        processor.panel = fake_panel
        processor.cellpose_denoise([1], dir, dir, "temp.ome.tiff", model_type = "cyto3")
        image = tf.imread(output_dir)
    assert(image.shape == (2,500,500))
    similarity = (image[1] == fake_img[1]).sum()
    assert(similarity == 0)
    print(f"Shape = {str(image.shape)}, and similarity in denoised channel = {str(similarity)}. Passed cellpose denoising test!")

def test_simple_denoise():
    with tmp.TemporaryDirectory() as dir:
        fake_img = np.random.rand(2,500,500)
        output_dir = dir + "/temp.ome.tiff"
        tf.imwrite(output_dir, fake_img)
        processor = pc.ImageProcessing(None)
        processor.panel = fake_panel
        processor.simple_denoise(dir, dir, [1], "temp.ome.tiff")
        image = tf.imread(output_dir)
    assert(image.shape == (2,500,500))
    similarity = (image[1] == fake_img[1]).sum()
    assert(similarity == 0)
    print(f"Shape = {str(image.shape)}, and similarity in denoised channel = {str(similarity)}. Passed simple denoising test!")


if __name__ == "__main__":
    tests = [test_expand, test_deepcell, test_cellpose_segment, test_cellpose_denoise, test_simple_denoise]
    test_names = ["test_expand", "test_deepcell", "test_cellpose_segment", "test_cellpose_denoise", "test_simple_denoise"]
    test_fail = []
    for i,ii in zip(tests, test_names):
        try:
            i()
        except AssertionError:
            test_fail.append(ii)
    if len(test_fail) == 0:
        print("Passed all tests!")
    else:
        print(f"Failed the following tests: {str(', '.join(test_fail))}")