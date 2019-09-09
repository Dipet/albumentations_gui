from PyQt5.QtCore import *

import inspect
import albumentations as albu


class TransformsModel(QAbstractItemModel):
    def __init__(self, parent):
        super().__init__(parent)

        self.transforms = self.get_transforms()
        (self.pixel_transforms,
         self.spatial_transforms) = self.split_pixel_spatial_transforms(self.transforms)

        self.name_to_transform = {transform.__name__: transform for transform in self.transforms}

        self.pixel_spatial = {'Pixel transforms': self.pixel_transforms,
                              'Spatial transforms': self.spatial_transforms}

    @staticmethod
    def split_pixel_spatial_transforms(transforms):
        pixel_transforms = []
        spatial_transforms = []

        for transform in transforms:
            if issubclass(transform, (albu.ImageOnlyTransform, albu.ImageOnlyIAATransform)):
                pixel_transforms.append(transform.__name__)
            elif issubclass(transform, (albu.DualTransform, albu.DualIAATransform)):
                spatial_transforms.append(transform.__name__)

        return pixel_transforms, spatial_transforms

    @staticmethod
    def get_transforms():
        not_include = [
            albu.BasicTransform,
            albu.BasicIAATransform,
            albu.ImageOnlyTransform,
            albu.DualTransform,
            albu.ImageOnlyIAATransform,
            albu.DualIAATransform,
            albu.Compose,
        ]

        transforms = []
        for name in dir(albu):
            item = getattr(albu, name)

            if not inspect.isclass(item):
                continue

            if issubclass(item, (albu.BasicTransform, albu.BasicIAATransform)):
                if item not in not_include:
                    transforms.append(item)

        return transforms

    def index(self, row, column, parent: QModelIndex=None, *args, **kwargs):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            return self.createIndex(row, column, list(self.pixel_spatial.keys())[row])
        else:
            parent = parent.internalPointer()

        return self.createIndex(row, column,
                                self.pixel_spatial[parent][row])

    def parent(self, index: QModelIndex=None):
        if not index.isValid():
            return QModelIndex()

        child = index.internalPointer()

        if child in self.pixel_spatial:
            return QModelIndex()

        if child in self.pixel_transforms:
            return self.createIndex(index.row(), 0, 'Pixel transforms')

        return self.createIndex(index.row(), 0, 'Spatial transforms')

    def rowCount(self, index: QModelIndex=None, *args, **kwargs):
        value = index.internalPointer()

        if value is None:
            return len(self.pixel_spatial)

        if value not in self.pixel_spatial:
            return 0

        count = len(self.pixel_spatial[value])
        return count

    def columnCount(self, parent=None, *args, **kwargs):
        return 1

    def data(self, index: QModelIndex, role=None):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()

        parent = index.parent().internalPointer()
        if parent is None:
            return index.internalPointer()

        data = self.pixel_spatial[parent][index.row()]
        return data

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags

        return super().flags(index)

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Transform'

        return QVariant()

    def transform_name_by_index(self, index):
        data = self.data(index, Qt.DisplayRole)

        if data in self.pixel_spatial:
            data = None

        return None if isinstance(data, QVariant) else data

    def transform_by_name(self, name):
        return self.name_to_transform[name]

    def get_docstring(self, index):
        if isinstance(index, QModelIndex):
            name = self.transform_name_by_index(index)
        else:
            name = index

        if not name:
            return None

        transform = self.transform_by_name(name)

        signature = inspect.signature(transform.__init__)
        doc = inspect.getdoc(transform)
        return f'{transform.__name__}{signature}\n\n{doc})'
