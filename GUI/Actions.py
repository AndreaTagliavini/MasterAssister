"""
This module is used to store the actions used by the GUI.
No logic should be ever implemented in the GUI, only bindings, all the logic is stored here.
"""
from AnyQt import QtWidgets
from XMLParser.Parser import XMLParser


def on_click_load(filename: str, charm_viewer: QtWidgets.QTextBrowser, charm_list: str):
    """
    Function called by the "load" button which reads a list of charm names and sets the charm viewer with the result
    The method instances a new XML parser and then searches for the charm list, finally sets the charm_viewer text to
    the result of the previous step.
    :param filename: name of the XML file
    :param charm_viewer: the QTextBrowser widget
    :param charm_list: a string containing charm titles, separated by a comma ","
    :return: 0 on a successful run, 0 otherwise
    TODO replace hardcoded URL with appropriate path
    """
    try:
        parser = XMLParser(
            "XMLParser/XMLFiles/" +
            str(filename) +
            "Charms.xml"
        )
        charm_viewer.setText(parser.prepare_charm_list(charm_list))
        return 0

    except FileNotFoundError:
        print("File not found")
    return 1
