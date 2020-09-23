
import json
import os

dataset_path = '/home/mayankg/darknet/gb_dataset_new/gb_imgs/'
json_path = '/home/mayankg/darknet/gb_dataset_new/gb_225.json'

for file in os.scandir(dataset_path):
    filename = os.path.relpath(file, dataset_path)
    if filename.endswith(".jpg"):

        img_path = dataset_path + filename
        txt_path = img_path[:-4] + ".txt"

        print("Img Path: ", img_path)
        print(filename)

        file_annot = open(txt_path, "w")

        with open(json_path) as f:
            annots = json.load(f)

        ann = annots[filename]
        width = ann['dim'][0]
        height = ann['dim'][1]

        for bb in ann['bbs']:
            
            #category = obj.find('name').text
            xmin, ymin, xmax, ymax = None, None, None, None
            xmin = bb[1][0]
            ymin = bb[1][1]
            xmax = bb[1][2]
            ymax = bb[1][3]

            center_x = float(((xmin + xmax)/2)/width)
            center_y = float(((ymin + ymax)/2)/height)
            w = float((xmax - xmin)/width)
            h = float((ymax - ymin)/height)

            file_annot.write('0 {:f} {:f} {:f} {:f}\n'.format(center_x, center_y, w, h))
        file_annot.close()

  