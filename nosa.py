#!/usr/bin/env python3
from lxml import etree


def line_pairs():
    with open("nosa.txt") as nosa_stream:
        prev = ""
        for line in nosa_stream.readlines():
            if prev:
                yield prev, line.strip()
                prev = ""
            else:
                prev = line.strip()


def convert():
    root = etree.Element("r")
    for pair in line_pairs():
        if pair[1]:
            e = etree.SubElement(root, "e")
            lg = etree.SubElement(e, "lg")
            for lemma in [lem.strip() for lem in pair[0].split(",")]:
                l = etree.SubElement(lg, "l")
                l.set("pos", "N")
                l.text = lemma

            for translation in [tran.strip() for tran in pair[1].split(";")]:
                tg = etree.SubElement(e, "tg")
                tg.set("lang", "smj")
                t = etree.SubElement(tg, "t")
                t.set("pos", "N")
                t.text = translation

    with open("nosa.xml", "w") as nosa_xml:
        print(
            etree.tostring(root, pretty_print=True, encoding="unicode"), file=nosa_xml
        )


if __name__ == "__main__":
    convert()
