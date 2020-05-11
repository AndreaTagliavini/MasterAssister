import xml.etree.ElementTree as ET

"""
This class is responsible of parsing Charms XML files, that uses the following syntax:

<root>
    <ability name="ability name">
        <charm>
            <title>charm name</title>
            <inner>charm content</inner>
        </charm>
        ...
        
    </ability>
    ...
</root>

It implements method for charm retrieval based on ability name.
Example usage


    parser = XMLParser("XMLFiles/DragonBloodedCharms.xml")
    ability = parser.get_ability("Archery")
    charms = parser.get_all_charms_from_ability(ability)

This snippet retrieves all Archery charms related to the DragonBlooded.
Note: in order to work properly the xml file must be named as such:
    <ExaltType>Charms.xml
    
"""


class XMLParser:
    def __init__(self, name: str):
        self.tree = ET.parse(name)
        self.root = self.tree.getroot()

    # util methods
    def clean(self, string:str):
        """
        Removes spaces and newlines from a string
        :param string: the string
        :return: the cleaned string
        """
        return string.replace('\n', '').replace(' ', '').lower()

    # parser methods
    def get_all_charms_from_ability(self, ability: ET.Element, verbose=False):
        """
        Search and return all charms of the given ability
        :param ability: a sting containing the ability name
        :param verbose: print matched charms
        :return: list of charm XML elements
        """
        try:
            buf = []
            charm_list = list(ability)
            for charm in charm_list:
                if verbose:
                    self.print_charm(charm)
                buf.append(charm)
            return buf
        except IndexError:
            print("[ERROR] Index Error, unsupported ability specified")

    def print_charm(self, charm):
        """
        Given a charm element, print in the format:
            TITLE TEXT
        :param charm: The charm element (XML)
        :return: None
        """
        title = charm[0]
        inner = charm[1]
        print(str(title.text) + " " + str(inner.text))

    def get_charm(self, charm):
        """
        Given a charm element, return two subsequent strings: Title, Content
        :param charm: the charm XML Element
        :return: CharmTitle, CharmText
        """
        return charm[0].text, charm[1].text

    def get_ability(self, name: str):
        """
        Return a reference to an ability
        :param name: the ability name
        :return: the XML reference
        """
        ability_list = list(self.root)
        for a in ability_list:
            if a.attrib['name'] == name:
                return a

        return None

    def get_all_abilities(self):
        """
        Matches all "Ability" XML elements and return their names
        :return: the ability list
        """
        ability_list = list(self.root)
        buf = []

        for x in ability_list:
            buf.append(x.attrib['name'])
        return buf

    def get_all_charms(self):
        """
        Return all charms in the XML file
        :return: as above
        """
        charm_list = []
        for ability in self.get_all_abilities():
            for charm in (self.get_all_charms_from_ability(self.get_ability(ability))):
                charm_list.append(charm)
        return charm_list

    def get_charms_from_list(self, charm_list: str):
        """
        Return all charms, which titles are contained in a comma separated string.
        :param charm_list: Charm titles contained in a comma separated string
        :return: A list containing Title + Content of all matched charms
        """
        titles = charm_list.split(",")
        all_charms = self.get_all_charms()
        buf = []
        for title in titles:
            for charm in all_charms:
                if self.clean(charm[0].text) == self.clean(title):
                    buf.append(charm)
                    break
        return buf

    def prepare_charm_list(self, charm_list):
        """
        Wrapper to get_charms_from_list method, convert its output to a string
        :param charm_list: Charm titles contained in a comma separated string
        :return: a string containing all matched charms
        """
        print("hey")
        result = self.get_charms_from_list(charm_list)
        buffer = ""
        for x in result:
            buffer += str(x[0].text) + "\n" + str(x[1].text) + "\n\n"
        return buffer
