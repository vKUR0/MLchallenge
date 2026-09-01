import os
import torch
from PIL import Image
from skimage.color import rgb2lab
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms

class FlowerDataset(Dataset):
    def __init__(self, filepath="./Flowers"):
        self.filepath = filepath
        self.dataset = []

        all_images = [f for f in os.listdir(filepath) if f.endswith('.jpg')]
        transform = transforms.Compose([
            transforms.Resize((128, 128)),
        ])

        for f in all_images:
            path = os.path.join(filepath, f)
            img = Image.open(path)

            img_rgb = img.convert('RGB')
            img_rgb_resized = transform(img_rgb)
            img_lab = rgb2lab(img_rgb_resized)

            img_L = img_lab[:, :, 0:1] / 100
            img_ab = (img_lab[:, :, 1:3] + 128) / 255

            L_tensor = torch.from_numpy(img_L.transpose((2, 0, 1)))
            ab_tensor = torch.from_numpy(img_ab.transpose((2, 0, 1)))

            self.dataset.append((L_tensor, ab_tensor))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]