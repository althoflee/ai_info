#%%
import cv2 as cv
import numpy as np
from ultralytics import YOLO,checks

from IPython.display import display
import PIL.Image as Image

checks()
#%%
img = cv.imread('bus.jpg')
display(Image.fromarray( cv.cvtColor(img,cv.COLOR_BGR2RGB)))
# %%
model = YOLO('yolo11x-seg.pt')

results = model(img)
print(results)

# %%
result = results[0]
result_img = img.copy()

#%%
print(result.masks)

# %%
for mask_data in result.masks.data :
    mask_img = mask_data.cpu().numpy()
    mask_img = np.where(mask_img > 0.5,255,0).astype('uint8')
    display(Image.fromarray( cv.cvtColor(mask_img,cv.COLOR_BGR2RGB)))
# %%
img_h,img_w,_ = result_img.shape

for _segment in result.masks.xyn:
    np_cnt = (_segment *(img_w,img_h)).astype(np.int32)
    cv.polylines(result_img,[np_cnt],True,(0,255,0),2)
display(Image.fromarray( cv.cvtColor(result_img,cv.COLOR_BGR2RGB)))
    
# %%
