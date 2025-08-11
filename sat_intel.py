import rasterio
import numpy as np
import matplotlib.pyplot as plt

def gamma_correct(image_band, gamma=2.0):
    # Normalize to 0-1 range first
    normalized = (image_band - image_band.min()) / (image_band.max() - image_band.min())
    # Apply gamma correction
    corrected = np.power(normalized, 1/gamma)
    return corrected

def save_ndvi(filepath):
    with rasterio.open(filepath) as dataset:
        b_img=dataset.read(1).astype('float64')
        g_img=dataset.read(2).astype('float64')
        r_img=dataset.read(3).astype('float64')
        nir_img=dataset.read(4).astype('float64')

        np.seterr(divide='ignore', invalid='ignore')
        ndvi=(nir_img-r_img)/(nir_img+r_img)
        ndvi[np.isnan(ndvi)] = 0
        image = plt.imshow(ndvi, cmap='winter')
        plt.colorbar(image,label='NDVI')
        plt.savefig('static/ndvi_result.png')
        plt.close()

