import pyfits
import numpy as np
import pylab as py
import img_scale

Target_name = str(raw_input('Object Name:'))
print ''
R = str(raw_input('R filter filename:'))
print ''
B = str(raw_input('B filter filename:'))
print ''
V = str(raw_input('V filter filename:'))
print ''

r=pyfits.getdata(R)
v=pyfits.getdata(V)
b=pyfits.getdata(B)

img = np.zeros((b.shape[0], b.shape[1], 3), dtype=float)
img[:,:,0] = img_scale.linear(r, scale_min=0, scale_max=10000)
img[:,:,1] = img_scale.linear(v, scale_min=0, scale_max=10000)
img[:,:,2] = img_scale.linear(b, scale_min=0, scale_max=10000)
py.clf()
py.imshow(img, aspect='equal')
py.title('Blue = B, Visible = V, Red = R')
py.savefig(Target_name+'_RGB.png')