# The following has been generated automatically from src/gui/symbology/qgsrendererpropertiesdialog.h
try:
    QgsRendererPropertiesDialog.__attribute_docs__ = {'layerVariablesChanged': 'Emitted when expression context variables on the associated vector\nlayers have been changed. Will request the parent dialog to\nre-synchronize with the variables.\n', 'widgetChanged': 'Emitted when something on the widget has changed. All widgets will fire\nthis event to notify of an internal change.\n', 'showPanel': 'Emit when you require a panel to be show in the interface.\n\n:param panel: The panel widget to show.\n\n.. note::\n\n   If you are connected to this signal you should also connect\n   given panels showPanel signal as they can be nested.\n'}
    QgsRendererPropertiesDialog.__overridden_methods__ = ['keyPressEvent']
    QgsRendererPropertiesDialog.__signal_arguments__ = {'showPanel': ['panel: QgsPanelWidget']}
    QgsRendererPropertiesDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
