from PIL import Image
import torch

# https://note.nkmk.me/python-pillow-add-margin-expand-canvas/
def expand2square_pil(pil_img, background_color):
    width, height = pil_img.size
    if width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def expand2square_torch(th_img, background_color):
    ch, h, w = th_img.shape
    s = max(w, h)

    result = torch.full((ch, s, s), background_color, dtype=th_img.dtype)
    left = s//2 - w//2
    top = s//2 - h//2
    right = left + w
    bottom = top + h

    result[:, top:bottom, left:right] = th_img

    return result

def expand2square(img, background_color):
    if isinstance(img, Image.Image):
        return expand2square_pil(img, background_color)
    else:
        return expand2square_torch(img, background_color)
