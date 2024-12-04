#%%
import cv2 as cv
from ultralytics import YOLO,checks

from IPython.display import display
import PIL.Image as Image

checks()
# %%
model = YOLO('yolo11n.pt')
model.info()
# %%
img = cv.imread("bus.jpg")
# %%
display(Image.fromarray(cv.cvtColor(img,cv.COLOR_BGR2RGB)))

# %%
results = model(img)

for result in results :
    print(result)
# %%
result = results[0]
result_img = img.copy()

for box in result.boxes :
    #print(box)
    x1,y1,x2,y2 = box.xyxy[0]
    
    print( int(box.cls.cpu().item()) )
    print(box.conf.cpu().item())
    _class = int(box.cls.cpu().item())
    if _class == 5 :
        cv.rectangle(result_img,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
    else :
        cv.rectangle(result_img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)        
        
        
# %%

display(Image.fromarray(
    cv.cvtColor(result_img,cv.COLOR_BGR2RGB)) )

# %%
