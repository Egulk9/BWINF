import copy
from typing import List

import math


# Eine implementierte Version der Karte. Ein Kartenobjekt speichert alle Straßen und deren Anzahl.
class Map:

    # Der Standardkonstruktor erzeugt ein Kartenobjekt indem er die eine input-Liste einliest und diese in Straßen
    # konvertiert.
    def __init__(self, map_input):
        self.map_input = map_input
        self.street_list = []
        self.kreuzung_strasse_dict = {}
        self.street_count = int(self.map_input[0][0])

        # Da die ersten drei Zeilen Anzahl der Straßen und Start/Endpunkt enthält
        # startet die Schleife erst bei inklusive 3 und endet bei dem Gesamt-Index (Straßenzahl + 3)
        # Die Straßen und ein Dictionary mit den Verbindungen zwischen den Straßen wird erstellt.
        for i in range(3, self.street_count + 3):

            # Die Straßennummer ist äquivalent zu den Indizes der Straßenliste
            street_no: List[int] = [i - 3]

            # Wenn ein Knotenpunkt im Dictionary noch nicht vorkommt,
            # dann wird dieser mit der zugehörigen Straße gespeichert.
            # Ansonsten wird die aktuelle Straße hinzugefügt.
            if not (self.map_input[i][0] in self.kreuzung_strasse_dict):
                self.kreuzung_strasse_dict[(self.map_input[i][0])] = street_no
            else:
                self.kreuzung_strasse_dict[(self.map_input[i][0])] += copy.deepcopy(street_no)

            if not (self.map_input[i][1] in self.kreuzung_strasse_dict):
                self.kreuzung_strasse_dict[(self.map_input[i][1])] = copy.deepcopy(street_no)
            else:
                self.kreuzung_strasse_dict[(self.map_input[i][1])] += copy.deepcopy(street_no)

            self.add_street(Street(Kreuzung(self.map_input[i][0]), Kreuzung(self.map_input[i][1])))

        for i in self.street_list:
            if i.start_point.x == i.end_point.x:
                i.add_dir("NS")
            elif i.start_point.y == i.end_point.y:
                i.add_dir("WO")
            elif i.start_point.y < i.end_point.y and i.start_point.x < i.end_point.x or (
                    i.start_point.y > i.end_point.y and i.start_point.x > i.end_point.x):
                i.add_dir("ON")
            elif i.start_point.y > i.end_point.y and i.start_point.x < i.end_point.x or (
                    i.start_point.y < i.end_point.y and i.start_point.x > i.end_point.x):
                i.add_dir("WN")

    # Eine Straße wird der Liste "street_list" hinzugefügt
    def add_street(self, street):
        self.street_list.append(street)


# Ein Objekt, dass den Start und Endpunkt, sowie die Länge einer Straße speichert
class Street:

    # Der Standardkonstruktor gibt ein Straßenobjekt zurück.

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = math.sqrt((end_point.x - start_point.x) ** 2 + (end_point.y - start_point.y) ** 2)
        self.dir = None

    # Eine Straße enthält den Start und Endpunkt als Kreuzungsobjekt und die Richtung als String
    # WO(West-Ost), NS(Nord-Süd), ON(Ost-Nord - Diagonal), WN(West-Nord - Diagonal)
    def add_dir(self, direction):
        self.dir = direction


# Eine Kreuzung beschreibt einen Punkt, an dem eine Straße aufhört und eine weitere beginnt
class Kreuzung:

    # Der Standardkonstruktor wandelt einen String in Form (x,y) in ein Kreuzungsobjekt um.
    def __init__(self, way_string):
        self.original_string = way_string
        way_string = way_string[1:-1]
        way_string = way_string.split(",")
        self.x = int(way_string[0])
        self.y = int(way_string[1])


def render(tmpmap):
    print("digraph map1 {")
    for i in range(tmpmap.street_count - 1):
        print(str(tmpmap.street_list[i].start_point.x) + str(tmpmap.street_list[i].start_point.y) + "->" + str(
            tmpmap.street_list[i].end_point.x) + str(tmpmap.street_list[i].end_point.y))
    print("}")


# Öffnen der Datei
with open("abbiegen0.txt") as f:
    imap_input = f.readlines()

# Entfernen der Linebreaks (\n)
altinput = [x[:-1] for x in imap_input]

# Aufteilen der Anfangs und End Kreuzungen
imap_input = [x.split(" ") for x in altinput]

# Erzeugen der Karte
map1 = Map(imap_input)
render(map1)
