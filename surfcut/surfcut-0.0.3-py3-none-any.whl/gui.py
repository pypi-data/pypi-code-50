import tifffile
from tifffile import imwrite
from scipy.ndimage import filters
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import napari
from PIL import Image, ImageTk, ImageEnhance


def main():
    root = tk.Tk()
    root.title("Surfcut")
    Main_window = initial_frame(root)
    root.mainloop()


class initial_frame:
    def __init__(self, master):
        self.master = master
        self.import_button = tk.Button(
            self.master, text="Import", command=self.import_
        )
        self.import_button.grid(row=0, column=0)
        self.gauss_sigma = tk.IntVar()
        self.gauss_sigma.set(3)
        self.gauss_sigma_label = tk.Label(self.master, text="Gaussian Sigma: ")
        self.gauss_sigma_label.grid(row=1, column=0)
        self.gauss_entry = tk.Entry(self.master, textvariable=self.gauss_sigma)
        self.gauss_entry.grid(row=1, column=1)
        self.threshold = tk.IntVar()
        self.threshold.set(20)
        self.threshold_label = tk.Label(self.master, text="Threshold: ")
        self.threshold_label.grid(row=1, column=2)
        self.threshold_entry = tk.Entry(
            self.master, text="Guassian sigma", textvariable=self.threshold
        )
        self.threshold_entry.grid(row=1, column=3)
        self.calibrate_button = tk.Button(
            self.master, text="Calibrate", command=self.calibrate_
        )
        self.calibrate_button.grid(row=1, column=4)
        self.shift = tk.IntVar()
        self.shift.set(14)
        self.shift_label = tk.Label(self.master, text="Shift: ")
        self.shift_label.grid(row=2, column=0)
        self.shift_entry = tk.Entry(
            self.master, text="Shift", textvariable=self.shift
        )
        self.shift_entry.grid(row=2, column=1)
        self.depth = tk.IntVar()
        self.depth.set(4)
        self.depth_label = tk.Label(self.master, text="Depth: ")
        self.depth_label.grid(row=2, column=2)
        self.depth_entry = tk.Entry(
            self.master, text="Depth", textvariable=self.depth
        )
        self.depth_entry.grid(row=2, column=3)
        self.mask_button = tk.Button(
            self.master, text="Mask", command=self.mask_
        )
        self.mask_button.grid(row=2, column=4)
        self.export_button = tk.Button(
            self.master, text="Export", command=self.export_
        )
        self.export_button.grid(row=3, column=0)
        self.binary = []
        self.data = []
        self.projection = ""

    def import_(self):
        image_path = askopenfilename()
        self.data = tifffile.imread(image_path).astype(np.uint8)

    def calibrate_(self):
        self.threshold_()
        self.calibrate_window = tk.Toplevel(self.master)
        self.calibrate_window.title("Calibration")
        self.calibration_app = calibrate_window(
            self.calibrate_window, self.data, self.binary
        )

    def threshold_(self, *args):
        filtered = np.copy(self.data)
        for idx, plane in enumerate(filtered):
            filtered[idx] = filters.gaussian_filter(
                plane, int(self.gauss_sigma.get())
            )
        self.binary = filtered > int(self.threshold.get())
        del filtered
        edges = np.zeros_like(self.binary)
        for idx, _ in enumerate(self.binary):
            if idx < len(self.binary):
                edges[idx, :, :] = np.max(self.binary[0 : idx + 1], axis=0)
        self.binary = edges
        del edges

    def mask_(self):
        self.threshold_()
        print("Shifting binary object down")
        shift_mag = int(int(self.shift.get()) + (int(self.depth.get()) / 2))
        down_shift = self.binary[0:-shift_mag]
        padding = np.zeros(
            (shift_mag, self.binary.shape[1], self.binary.shape[2])
        )
        down_shift = np.append(padding, down_shift, axis=0)
        print("Shifting binary object up")
        shift_mag = int(int(self.shift.get()) - (int(self.depth.get()) / 2))
        up_shift = self.binary[0:-shift_mag]
        padding = np.zeros(
            (shift_mag, self.binary.shape[1], self.binary.shape[2])
        )
        up_shift = np.append(padding, up_shift, axis=0)
        del self.binary

        print("Generating mask")
        mask = up_shift - down_shift
        del up_shift
        del down_shift
        mask = mask > 0

        print("Masking data")
        masked = self.data * mask

        self.projection = np.max(masked, axis=0)

        with napari.gui_qt():
            v = napari.Viewer(title="Surfcut")
            v.add_image(self.data, name="Raw data")
            v.add_image(masked, name="Surf stack")
            v.add_image(self.projection, name="Projection")

    def export_(self):
        export_path = askdirectory()
        imwrite(
            "{}/projection.tif".format(export_path),
            self.projection.astype(np.uint8),
        )


class calibrate_window:
    def __init__(self, master, data, binary):
        self.master = master
        self.binary = binary
        self.data = data
        self.original_canvas = tk.Canvas(self.master, width=500, height=500)
        self.original_canvas.grid(row=0, column=0)
        self.calibrate_canvas = tk.Canvas(self.master, width=500, height=500)
        self.calibrate_canvas.grid(row=0, column=1)
        self.plane = 0
        self.show_img()
        self.plane_chooser = tk.Scale(
            self.master,
            from_=0,
            to=len(self.binary) - 1,
            command=self.plane_change,
        )
        self.plane_chooser.grid(row=0, column=3)

    def plane_change(self, *args):
        self.plane = self.plane_chooser.get()
        self.show_img()

    def show_img(self, *args):
        z, x, y = self.data.shape
        # self.original_canvas.configure(width=y, height=x)
        # self.calibrate_canvas.configure(width=y, height=x)
        self.img = Image.fromarray(self.data[self.plane]).resize(
            (500, 500), Image.ANTIALIAS
        )
        # self.img = np.array(self.img.resize((y_resize,x_resize), Image.ANTIALIAS))
        # self.img = Image.fromarray(self.img)
        self.img = ImageTk.PhotoImage(self.img)
        self.original_canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.original_canvas.image = self.img

        self.bin_img = Image.fromarray(self.binary[self.plane]).resize(
            (500, 500), Image.ANTIALIAS
        )
        # self.bin_img = np.array(self.bin_img.resize((y_resize,x_resize), Image.ANTIALIAS))
        # self.bin_img = Image.fromarray(self.bin_img)
        self.bin_img = ImageTk.PhotoImage(self.bin_img)
        self.calibrate_canvas.create_image(
            0, 0, image=self.bin_img, anchor="nw"
        )
        self.calibrate_canvas.image = self.bin_img


if __name__ == "__main__":
    main()
