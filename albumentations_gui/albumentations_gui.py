from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainwindow_ui import Ui_MainWindow

import cv2 as cv
from PIL import Image, ImageQt

from transforms import TransformsModel

import albumentations

import numpy as np


IMG_EXTENSIONS = {
    'BMP': '*.bmp *.dib',
    'JPEG': '*.jpeg *.jpg *.jpe',
    'JPEG 2000': '*.jp2',
    'PNG': '*.png',
    'WEBP': '*.webp',
    'Portable': '*.pbm *.pgm *.ppm *.pxm *.pnm',
    'PFM': '*.pfm',
    'Sun': '*.sr *.ras',
    'TIFF': '*.tiff *.tif',
    'OpenEXR': '*.exr',
    'HDR': '*.hdr *.pic',
}


class AlbumentationsGui(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.image = None
        self.tmp_image = None
        self.code_header = 'albumentations.Compose(transforms=['
        self.code_tail = '])'

        self.transforms_model = TransformsModel(self)
        self.transforms_tree.setModel(self.transforms_model)

        self.connect()

        self.update_code()

    def connect(self):
        self.button_open_image.clicked.connect(self.open_image)
        self.button_clear.clicked.connect(self.clear_augs)
        self.button_update_image.clicked.connect(self.update_code)

        self.transforms_tree.doubleClicked.connect(self.add_transform)
        self.list_widget_selected_transforms.doubleClicked.connect(self.remove_transform)

        self.transforms_tree.clicked.connect(self.tree_clicked)
        self.list_widget_selected_transforms.clicked.connect(self.list_added_clicked)

    def open_image(self):
        all_extension = ' '.join([item for key, item in IMG_EXTENSIONS.items()])
        filter = f'All ({all_extension});;'
        for key, item in IMG_EXTENSIONS.items():
            filter += f'{key} ({item});;'

        path, _ = QFileDialog.getOpenFileName(parent=self,
                                              caption='Open Image',
                                              filter=filter)
        if not path:
            return

        self.image = cv.imread(path, cv.IMREAD_COLOR)

        if self.image is not None:
            self.image = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
            self.line_edit_image_path.setText(path)
        else:
            self.line_edit_image_path.setText('')

        self.update_image()

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

        self.update_code(add=transform)

    def _get_transforms_from_code(self):
        code = self.text_edit_code.toPlainText()

        try:
            transform: albumentations.Compose = eval(code)
            return transform.transforms.transforms
        except Exception:
            return []

    def _get_transform_str(self,
                           code_transform: albumentations.BasicTransform):
        transform = code_transform.__class__()

        params1 = {
            **transform.get_transform_init_args(),
            **transform.get_base_init_args()
        }
        params2 = {
            **code_transform.get_base_init_args(),
            **code_transform.get_base_init_args()
        }
        diff_params = {}

        for key, value in params2.items():
            if np.all(value != params1[key]):
                diff_params[key] = value

        str_transform = ' ' * 4 + 'albumentations.{}({}),\n'
        str_params = ''
        for key, value in diff_params.items():
            str_params += f'{key}={value}, '

        return str_transform.format(str(transform.__class__.__name__), str_params[:-2])

    def update_list(self, transforms):
        transforms = [i.__class__.__name__ for i in transforms]

        self.list_widget_selected_transforms.clear()
        self.list_widget_selected_transforms.insertItems(0, transforms)

    def update_code(self, add='', remove=None):
        transforms = self._get_transforms_from_code()

        if remove is not None:
            if remove == 'all':
                transforms = []
            else:
                transforms = transforms[:remove] + transforms[remove + 1:]

        if add:
            transforms.append(self.transforms_model.transform_by_name(add)())

        code = ''.join([self._get_transform_str(i) for i in transforms])

        if code and not code.startswith('\n'):
            code = '\n' + code
        self.text_edit_code.setText(f'{self.code_header}{code}{self.code_tail}')

        self.update_image()
        self.update_list(transforms)

    def remove_transform(self, index: QModelIndex):
        self.list_widget_selected_transforms.takeItem(index.row())
        self.update_code(remove=index.row())

    def tree_clicked(self, index: QModelIndex):
        doc = self.transforms_model.get_docstring(index)
        if doc is None:
            return

        self.list_widget_selected_transforms.clearSelection()

        self.text_edit_docstring.setText(doc)

    def list_added_clicked(self, index: QModelIndex):
        name = self.list_widget_selected_transforms.item(index.row()).text()

        doc = self.transforms_model.get_docstring(name)
        if doc is None:
            return

        self.transforms_tree.clearSelection()

        self.text_edit_docstring.setText(doc)

    def update_image(self):
        if self.image is None:
            return

        code = self.text_edit_code.toPlainText()
        try:
            transform = eval(code)
            image = transform(image=self.image)['image']
            self.show_image(image)
        except Exception as err:
            self.label_image.setText(str(err))

    def clear_augs(self):
        self.update_code(remove='all')


if __name__ == '__main__':
    app =QApplication([])
    gui = AlbumentationsGui()
    gui.show()
    app.exec_()
