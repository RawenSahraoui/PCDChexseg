import numpy as np
import cv2

def overlay_mask_on_image(image, mask, alpha=0.5):
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
    mask_color = np.zeros_like(image)
    mask_color[:, :, 1] = (mask * 255).astype(np.uint8)  # green
    overlay = cv2.addWeighted(image, 1.0, mask_color, alpha, 0)
    return overlay
