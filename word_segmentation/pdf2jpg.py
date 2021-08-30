import os
path = './docs_for_test/'
directory_contents = os.listdir(path)
print(directory_contents)

from pdf2image import convert_from_path
for item in directory_contents:
    if '.pdf' in item:
        print(path+item)
        images = convert_from_path(path+item)
        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save(item+'_'+'page'+ str(i) +'.jpg', 'JPEG')