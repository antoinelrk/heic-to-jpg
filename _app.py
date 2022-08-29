import os

os.system('mkdir _CONVERTED/')

for x in os.listdir():
    if x.endswith('.HEIC') or x.endswith('.heic') or x.endswith('.heif'):
        pathname, ext = os.path.splitext(x)
        cmd = 'heif-convert ' + x + ' ' + pathname + '.jpg && rm ' + x
        os.system(cmd)
        
os.system('mv *.jpg _CONVERTED/')