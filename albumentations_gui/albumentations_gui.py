from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainwindow_ui import Ui_MainWindow

import cv2 as cv
from PIL import Image, ImageQt

from transforms import TransformsModel

import albumentations as albu


class AlbumentationsGui(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.image = None
        self.tmp_image = None

        self.transforms_model = TransformsModel(self)
        self.transforms_tree.setModel(self.transforms_model)

        self.connect()

    def connect(self):
        self.button_open_image.clicked.connect(self.open_image)
        self.button_clear.clicked.connect(self.clear_augs)
        self.button_update_image.clicked.connect(self.update_image)

        self.transforms_tree.doubleClicked.connect(self.add_transform)
        self.list_widget_selected_transforms.doubleClicked.connect(self.remove_transform)

        # self.transforms_tree.selectionChanged.connect(self.all_docs)
        # self.list_widget_selected_transforms.selectionChanged.connect(self.added_docs)
        # self.list_widget_selected_transforms.selectionChanged.connect(self.set_params)

    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(parent=self,
                                              caption='Open Image',
                                              filter='BMP (*.bmp *.dib);;'
                                                     'JPEG (*.jpeg *.jpg *.jpe);;'
                                                     'JPEG 2000 (*.jp2);;'
                                                     'PNG (*.png);;'
                                                     'WEBP (*.webp);;'
                                                     'Portable (*.pbm *.pgm *.ppm *.pxm *.pnm);;'
                                                     'PFM (*.pfm);;'
                                                     'Sun (*.sr *.ras);;'
                                                     'TIFF (*.tiff *.tif);;'
                                                     'OpenEXR (*.exr);;'
                                                     'HDR (*.hdr *.pic)')
        if not path:
            return

        self.image = cv.imread(path, cv.IMREAD_COLOR)

        if self.image is not None:
            self.image = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
            self.line_edit_image_path.setText(path)
        else:
            self.line_edit_image_path.setText('')

        self.show_image(self.image)

    def show_image(self, image):
        if image is None:
            self.label_image.setText('Empty image')
            return

        try:
            self.tmp_image = ImageQt.ImageQt(Image.fromarray(image))
            self.label_image.setPixmap(QPixmap.fromImage(self.tmp_image))
        except Exception as err:
            self.label_image.setText(str(err))

    def add_transform(self, index: QModelIndex):
        transform = self.transforms_model.transform_name_by_index(index)
        if not transform:
            return

        self.list_widget_selected_transforms.addItem(QListWidgetItem(transform))

        self.update_image()

    def remove_transform(self, index: QModelIndex):
        self.list_widget_selected_transforms.takeItem(index.row())

        self.update_image()

    def all_docs(self, *_, **__):
        pass

    def added_docs(self, *_, **__):
        pass

    def set_params(self, *_, **__):
        pass

    def update_image(self):
        if self.image is None:
            return

        transforms = [self.list_widget_selected_transforms.item(i) for i in range(self.list_widget_selected_transforms.count())]
        transforms = [self.transforms_model.transform_by_name(i.text())() for i in transforms]
        transform = albu.Compose(transforms)

        try:
            image = transform(image=self.image)['image']
            self.show_image(image)
        except Exception as err:
            self.label_image.setText(str(err))

    def clear_augs(self):
        self.list_widget_selected_transforms.clear()
        self.update_image()


if __name__ == '__main__':
    app =QApplication([])
    gui = AlbumentationsGui()
    gui.show()
    app.exec_()
