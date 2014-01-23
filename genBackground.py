import pylab as plt
import numpy as np

Z = np.random.random((500,500))  
plt.imshow(Z, cmap='Spectral', interpolation='nearest')
plt.show()


/* 
import numpy, Image

imarray = numpy.random.rand(100,100,3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA') //convert('L') for grayscale
im.save('result_image.png')

*/
