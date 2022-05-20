from xml.dom.minidom import parse
import os

def setDates(departDate, returnDate):
    # create a backup of original file
    output_file_name = 'dates_output.xml'

    # parse xml file
    doc = parse("Inputs/test_payload1.xml")
    # change text value of element
    depart_node = doc.getElementsByTagName('DEPART')
    depart_node[0].firstChild.nodeValue = departDate

    return_node = doc.getElementsByTagName('RETURN')
    return_node[0].firstChild.nodeValue = returnDate

    # write output to output.xml
    xml_file = open(output_file_name, "w")
    doc.writexml(xml_file, encoding="utf-8")
    xml_file.close()

if __name__ == "__main__":
  setDates(20221010, 20221111)