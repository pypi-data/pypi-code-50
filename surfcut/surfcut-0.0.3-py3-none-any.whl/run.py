import tifffile
from scipy.ndimage import filters
import numpy as np
from datetime import datetime
from skimage.morphology import binary_erosion, binary_dilation, ball

from surfcut.cli import surfcut_parser
from surfcut.viewer.viewer import view


def main():
    start_time = datetime.now()
    args = surfcut_parser().parse_args()

    image_path = args.image_path

    print("Loading data")
    data = tifffile.imread(image_path)

    print("Converting to 8 bit")
    data = data.astype(np.uint8)

    print("Smoothing")
    filtered = np.copy(data)
    for idx, plane in enumerate(filtered):
        filtered[idx] = filters.gaussian_filter(plane, args.gauss_sigma)

    print("Thresholding")
    binary = filtered > args.threshold

    del filtered
    print("Detecting edges")
    binary = edge_detect(binary)

    if args.morphology:
        print("Eroding to depth")
        eroded_surface = binary_erosion(binary, selem=ball(args.shift))

        print("Dilating and eroding")
        dilated = binary_dilation(eroded_surface, selem=ball(args.depth))
        eroded = binary_erosion(eroded_surface, selem=ball(args.depth))
        del eroded_surface

        print("Obtaining border")
        border = dilated ^ eroded

        print("Masking data")
        masked = data * border

    else:
        print("Shifting binary object down")
        shift_mag = int(args.shift + (args.depth / 2))
        down_shift = binary[0:-shift_mag]
        padding = np.zeros((shift_mag, binary.shape[1], binary.shape[2]))
        down_shift = np.append(padding, down_shift, axis=0)

        print("Shifting binary object up")
        shift_mag = int(args.shift - (args.depth / 2))
        up_shift = binary[0:-shift_mag]
        padding = np.zeros((shift_mag, binary.shape[1], binary.shape[2]))
        up_shift = np.append(padding, up_shift, axis=0)
        del binary

        print("Generating mask")
        mask = up_shift - down_shift
        del up_shift
        del down_shift
        mask = mask > 0

        print("Masking data")
        masked = data * mask

    print("Projecting data")
    projection = np.max(masked, axis=0)

    print(f"Finished. Total time taken: {format(datetime.now() - start_time)}")

    if not args.no_viewer:
        print("Opening viewer")
        if args.morphology:
            view(data, border, projection)
        else:
            view(data, masked, projection)


def edge_detect(image):
    edges = np.zeros_like(image)
    for idx, _ in enumerate(image):
        if idx < len(image):
            edges[idx, :, :] = np.max(image[0 : idx + 1], axis=0)

    return edges


if __name__ == "__main__":
    main()
