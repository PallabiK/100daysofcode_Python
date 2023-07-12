import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageMergerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Merger")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.main_image = None
        self.watermark_image = None
        self.merged_image = None

        self.main_image_button = tk.Button(self.inner_frame, text="Add Main Picture", command=self.add_main_image)
        self.main_image_button.pack(pady=10)

        self.watermark_button = tk.Button(self.inner_frame, text="Add Watermark Picture", command=self.add_watermark_image)
        self.watermark_button.pack(pady=10)

        self.merge_button = tk.Button(self.inner_frame, text="Merge Pictures", command=self.merge_images)
        self.merge_button.pack(pady=10)

        self.download_button = tk.Button(self.inner_frame, text="Download Merged Picture", state=tk.DISABLED,
                                         command=self.download_merged_image)
        self.download_button.pack(pady=10)

        self.inner_frame.bind("<Configure>", self.on_inner_frame_configure)

        self.root.mainloop()

    def add_main_image(self):
        file_path = filedialog.askopenfilename(title="Select Main Picture",
                                               filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if file_path:
            self.main_image = Image.open(file_path)
            self.show_image(self.main_image)

    def add_watermark_image(self):
        file_path = filedialog.askopenfilename(title="Select Watermark Picture",
                                               filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if file_path:
            self.watermark_image = Image.open(file_path)
            self.show_image(self.watermark_image)

    def merge_images(self):
        if self.main_image and self.watermark_image:
            main_width, main_height = self.main_image.size

            watermark_width = 50
            watermark_height = int((self.watermark_image.height / self.watermark_image.width) * watermark_width)
            watermark_resized = self.watermark_image.resize((watermark_width, watermark_height))

            watermark_x = main_width - watermark_width - 10
            watermark_y = main_height - watermark_height - 10

            self.merged_image = self.main_image.copy()
            self.merged_image.paste(watermark_resized, (watermark_x, watermark_y), mask=watermark_resized)

            self.show_image(self.merged_image)

            self.download_button.config(state=tk.NORMAL)  # Enable the download button
        else:
            print("Please select both main and watermark pictures.")

    def download_merged_image(self):
        if self.merged_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
            if save_path:
                self.merged_image.save(save_path)
                print("Merged picture saved successfully.")
        else:
            print("No merged picture available.")

    def show_image(self, image):
        image.thumbnail((400, 400))
        tk_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.inner_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_inner_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=event.width)


if __name__ == "__main__":
    app = ImageMergerApp()
