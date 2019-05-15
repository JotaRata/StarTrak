from skimage import io
import matplotlib.pyplot as plt
#plt.rcParams['image.cmap'] = 'gray'
import numpy as np


def green(name):
	#name e.g. "star.jpg", string
	plt.rcParams['image.cmap'] = 'gray'
	#im = plt.imread(name, format='jpg')
	im=io.imread(name)
	#im=np.ndarray.astype(im,float)
	im=im[:,:,1]
	return im
