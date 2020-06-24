import os
import numpy as np
import torch
from torchvision import datasets, models, transforms
from PIL import Image
from skimage import io, transform
model_dir = "../model/"
device = device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
TEST = 'test'
TRAIN = 'train'
VAL = 'val'

def data_transforms(phase):
    if phase == TRAIN:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])

    if phase == VAL:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])

    if phase == TEST:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])

    return transform



def predict_single_img(img_file, modelID=-1):

    model_list = os.listdir(model_dir)
    img = io.imread(img_file)
    img = np.expand_dims(img, axis=2)
    img = np.concatenate((img, img, img), axis=-1)
    #print(img.shape)
    img = Image.fromarray(img)
    transform = data_transforms(TEST)
    model = torch.load(model_dir+model_list[modelID], map_location='cpu')
    input = transform(img).unsqueeze(0).to(device)
    print(input.shape)
    out = model(input)
    out = torch.softmax(out, -1)
    print(out)
    prob = out.detach().cpu().numpy()[0]
    print("Likelihood of NORMAL is {} and PNEUMONIA is {}.".format(prob[0], prob[1]))

if __name__ == '__main__':
    #evaluate_model()
    predict_single_img("./img/test.jpeg")