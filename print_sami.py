#!/usr/bin/env python3
import sys
from lxml import etree


def words(name):
    xml = etree.parse(f"{name}.xml")
    if name == "sano":
        for l in xml.iter("l"):
            if l.text is not None:
                # print(l.text)
                yield l.text
    if name == "nosa":
        for t in xml.iter("t"):
            if t.text is not None:
                # print(t.text)
                yield t.text


def printer():
    print(" ".join([word for name in ["sano", "nosa"] for word in words(name)]))


if __name__ == "__main__":
    printer()
