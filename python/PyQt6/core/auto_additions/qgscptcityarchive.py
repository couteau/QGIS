# The following has been generated automatically from src/core/symbology/qgscptcityarchive.h
QgsCptCityDataItem.ColorRamp = QgsCptCityDataItem.Type.ColorRamp
QgsCptCityDataItem.Collection = QgsCptCityDataItem.Type.Collection
QgsCptCityDataItem.Directory = QgsCptCityDataItem.Type.Directory
QgsCptCityDataItem.Selection = QgsCptCityDataItem.Type.Selection
QgsCptCityDataItem.AllRamps = QgsCptCityDataItem.Type.AllRamps
QgsCptCityBrowserModel.Authors = QgsCptCityBrowserModel.ViewType.Authors
QgsCptCityBrowserModel.Selections = QgsCptCityBrowserModel.ViewType.Selections
QgsCptCityBrowserModel.List = QgsCptCityBrowserModel.ViewType.List
try:
    QgsCptCityDataItem.__attribute_docs__ = {'beginInsertItems': 'Emitted before child items are added to this item.\n\nThis signal *must* be followed by\n:py:func:`~QgsCptCityDataItem.endInsertItems`.\n\n:param parent: the parent item having children added\n:param first: index of first child item to be added\n:param last: index last child item, after the addition has occurred\n\n.. seealso:: :py:func:`endInsertItems`\n', 'endInsertItems': 'Emitted after child items have been added to this data item.\n\nThis signal will always be preceded by\n:py:func:`~QgsCptCityDataItem.beginInsertItems`.\n\n.. seealso:: :py:func:`beginInsertItems`\n', 'beginRemoveItems': 'Emitted before child items are removed from this data item.\n\nThis signal *must* be followed by\n:py:func:`~QgsCptCityDataItem.endRemoveItems`.\n\n:param parent: the parent item having children removed\n:param first: index of first child item to be removed\n:param last: index of the last child item to be removed\n\n.. seealso:: :py:func:`endRemoveItems`\n', 'endRemoveItems': 'Emitted after child items have been removed from this data item.\n\nThis signal will always be preceded by\n:py:func:`~QgsCptCityDataItem.beginRemoveItems`.\n\n.. seealso:: :py:func:`beginRemoveItems`\n'}
    QgsCptCityDataItem.findItem = staticmethod(QgsCptCityDataItem.findItem)
    QgsCptCityDataItem.__virtual_methods__ = ['leafCount', 'refresh', 'createChildren', 'populate', 'addChildItem', 'deleteChildItem', 'removeChildItem', 'equal', 'paramWidget', 'acceptDrop', 'handleDrop', 'icon']
    QgsCptCityDataItem.__signal_arguments__ = {'beginInsertItems': ['parent: QgsCptCityDataItem', 'first: int', 'last: int'], 'beginRemoveItems': ['parent: QgsCptCityDataItem', 'first: int', 'last: int']}
    QgsCptCityDataItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityArchive.defaultBaseDir = staticmethod(QgsCptCityArchive.defaultBaseDir)
    QgsCptCityArchive.findFileName = staticmethod(QgsCptCityArchive.findFileName)
    QgsCptCityArchive.copyingInfo = staticmethod(QgsCptCityArchive.copyingInfo)
    QgsCptCityArchive.description = staticmethod(QgsCptCityArchive.description)
    QgsCptCityArchive.initArchives = staticmethod(QgsCptCityArchive.initArchives)
    QgsCptCityArchive.initArchive = staticmethod(QgsCptCityArchive.initArchive)
    QgsCptCityArchive.initDefaultArchive = staticmethod(QgsCptCityArchive.initDefaultArchive)
    QgsCptCityArchive.clearArchives = staticmethod(QgsCptCityArchive.clearArchives)
    QgsCptCityArchive.defaultArchive = staticmethod(QgsCptCityArchive.defaultArchive)
    QgsCptCityArchive.archiveRegistry = staticmethod(QgsCptCityArchive.archiveRegistry)
    QgsCptCityArchive.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityDirectoryItem.dataItem = staticmethod(QgsCptCityDirectoryItem.dataItem)
    QgsCptCityDirectoryItem.__overridden_methods__ = ['createChildren', 'equal']
    QgsCptCityDirectoryItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityColorRampItem.__overridden_methods__ = ['equal', 'leafCount', 'icon']
    QgsCptCityColorRampItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCitySelectionItem.__overridden_methods__ = ['createChildren', 'equal']
    QgsCptCitySelectionItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityAllRampsItem.__overridden_methods__ = ['createChildren']
    QgsCptCityAllRampsItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityBrowserModel.__overridden_methods__ = ['flags', 'data', 'headerData', 'rowCount', 'columnCount', 'index', 'parent', 'hasChildren', 'canFetchMore', 'fetchMore']
    QgsCptCityBrowserModel.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCptCityCollectionItem.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
