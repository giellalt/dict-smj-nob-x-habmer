Konvertering: ./convert.py nosa eller ./convert.py sano
Skriv lulesamiske ord, alle på en linje: ./print_sami.py

Lage missinglist: ./print_sami.py | hfst-tokenise <lulesamisk-sti>/tokeniser-disamb-gt-desc.pmhfst|husmj|grep ?| cut -f1