import random
import numpy as np
from PIL import Image

import torch
import torch.nn.functional as F
import torchvision.transforms.functional as TF
from . import functional as CF
import scipy.ndimage.filters as FI

class BiImageTransform:
    pass

class Compose(BiImageTransform):
    def __init__(self, transforms):
        self.transforms = transforms
    def __call__(self, img, mask):
        for tf in self.transforms:
            img, mask = tf(img, mask)
        return img, mask

class ToTensor(BiImageTransform):
    def __call__(self, img, mask):
        img = TF.to_tensor(img)
        if isinstance(mask, Image.Image):
            mask = TF.to_tensor(mask)
        return img, mask

class Grayscale(BiImageTransform):
    def __call__(self, img, mask):
        img = img.convert(mode='L')
        return img, mask

# PIL.Image
class GaussianMask(BiImageTransform):
    def __init__(self, sigma=8, normalize=True):
        self.sigma = sigma
        self.normalize = normalize

    def __call__(self, img, mask):
        is_pil = isinstance(mask, Image.Image)

        if is_pil:
            np_mask = np.asarray(mask)
        else:
            np_mask = mask.numpy().transpose((1, 2, 0))

        np_mask = FI.gaussian_filter(np_mask, self.sigma)
        if self.normalize:
            mx = np_mask.max()
            if mx != 0:
                scale = 255 if is_pil else 1
                np_mask = np_mask / np_mask.max() * scale

        if is_pil:
            mask = Image.fromarray(np_mask)
        else:
            mask = torch.from_numpy(np_mask.transpose((2, 0, 1)))

        return img, mask

class ColorJitter(BiImageTransform):
    def __init__(self, brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2):
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.hue = hue
    def __call__(self, img, mask):
        is_alpha = img.mode == 'RGBA'
        if is_alpha:
            alpha = img.split()[-1]

        def u1(x):
            d = random.uniform(1 - x, 1 + x)
            return max(0, min(d, 2))
        def u2(x):
            d = random.uniform(-x, x)
            return max(-0.5, min(d, 0.5))
        b = u1(self.brightness)
        c = u1(self.contrast)
        s = u1(self.saturation)
        h = u2(self.hue)

        img = TF.adjust_brightness(img, b)
        img = TF.adjust_contrast(img, c)
        img = TF.adjust_saturation(img, s)
        img = TF.adjust_hue(img, h)

        if is_alpha:
            img.putalpha(alpha)

        return img, mask

class Normalize(BiImageTransform):
    def __init__(self, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
        self.mean = mean
        self.std = std
    def __call__(self, img, mask):
        mean = self.mean
        std = self.std

        if img.shape[0] == 4:
            img[:3, :, :] = TF.normalize(img[:3, :, :], mean=mean, std=std)
        else:
            img = TF.normalize(img, mean=mean, std=std)
        return img, mask

class Resize(BiImageTransform):
    def __init__(self, size=224):
        self.size = size
    def __call__(self, img, mask):

        if img.mode == 'RGBA':
            np_img = np.array(img)
            np_img_rgb = np_img[:, :, :3]
            np_img_alpha = np_img[:, :, 3]

            pil_img_rgb = Image.fromarray(np_img_rgb)
            pil_img_rgb = TF.resize(pil_img_rgb, size=self.size)
            pil_img_alpha = Image.fromarray(np_img_alpha)
            pil_img_alpha = TF.resize(pil_img_alpha, size=self.size)

            np_img_rgb = np.array(pil_img_rgb)
            np_img_alpha = np.array(pil_img_alpha).reshape([pil_img_alpha.height, pil_img_alpha.width, 1])

            np_img = np.concatenate([ np_img_rgb, np_img_alpha ], axis=2)
            img = Image.fromarray(np_img)
        else:
            img = TF.resize(img, size=self.size)

        if isinstance(mask, Image.Image):
            mask = TF.resize(mask, size=self.size)
        else:
            mask = F.interpolate(mask.unsqueeze(dim=0), size=self.size)[0]

        return img, mask

class RandomHorizontalFlip(BiImageTransform):
    def __init__(self, p=.5):
        self.p = p
    def __call__(self, img, mask):
        if random.random() < self.p:
            img = TF.hflip(img)

            if isinstance(mask, Image.Image):
                mask = TF.hflip(mask)
            else:
                mask = torch.flip(mask, dims=[2, ])

        return img, mask

class ExpandToSquare(BiImageTransform):
    def __init__(self, image_bgcolor=0, mask_bgcolor=0):
        self.image_bgcolor = image_bgcolor
        self.mask_bgcolor = mask_bgcolor

    def __call__(self, img, mask):
        image_bgcolor = self.image_bgcolor
        mask_bgcolor = self.mask_bgcolor
        w = img.width
        h = img.height

        img = CF.expand2square(img, background_color=image_bgcolor)
        mask = CF.expand2square(mask, background_color=mask_bgcolor)

        return img, mask
