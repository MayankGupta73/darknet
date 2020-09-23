data_path = '/home/mayankg/darknet/gb_dataset_new/gb_imgs/'
count = 0

file_train = open("train.txt","w")
file_valid = open("valid.txt","w")

file_train_split = open(split_path + "train_"+ str(count) + ".txt")
file_valid_split = open(split_path + "val_"+ str(count) + ".txt")

for name in file_train_split:
    img_path = data_path + name
    file_train.write(img_path)

for name in file_valid_split:
    img_path = data_path + name
    file_valid.write(img_path)

file_train_split.close()
file_valid_split.close()
file_train.close()
file_valid.close() 