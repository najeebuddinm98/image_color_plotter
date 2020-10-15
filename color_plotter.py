from PIL import Image
import os, logging
import matplotlib.pyplot as mlt
import webcolors as wbc

logging.basicConfig(filename='imcolplot.log', level=logging.INFO, format='%(levelname)s:%(asctime)s:%(lineno)d:%(message)s')
mlt.style.use('seaborn') #graph style

def esort(d):
    #for sorting dictionaries by value
    return d[1]

imfile='testimage.jpg' #edit file path here to try with other images
imfilename = os.path.splitext(imfile)[0]
imobject = Image.open(imfile)
logging.info(f'{imfilename} is made into image object')

fig, ax = mlt.subplots(figsize=(12,8), dpi=80)

width, height = imobject.size
logging.info(f'The dimensions of the file are {width}x{height}')

cc=dict() #color counter

for x in range(width):
    for y in range(height):
        pxcol = imobject.getpixel((x,y))
        
        try:
            pxname = wbc.rgb_to_name(pxcol) #saved with color name
        except ValueError:
            pxname = wbc.rgb_to_hex(pxcol) #saved with color hex code as the RGB values do not have an assigned name according to CSS3
            
        cc.setdefault(pxname,0) #updating our color counter dictionary
        cc[pxname]+=1

sortedcc = sorted(list(cc.items()), key=esort, reverse=True)
logging.info('Sorting of dictionary completed')

labels=[]
values=[]
for scc in sortedcc[:10]:
    labels.append(str(scc[0]))
    values.append(scc[1])
    if scc[0].startswith('#'):
        logging.warning(f'Name not found for {scc[0]}')

#plotting statements
ax.bar(labels, values)
ax.set_title('10 most common colors in '+imfile)
ax.set_xlabel('Color name by CSS3 or hex value')
ax.set_ylabel('Frequency')
ax.grid(True)

fig.savefig('plot for '+imfilename+'.jpg')
logging.info('Plot saved')
mlt.show()


        
        


