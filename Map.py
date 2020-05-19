import sys

#Eine implementierte Version der Karte. Ein Kartenobjekt speichert alle Straßen und deren Anzahl.
class Map:

    #Der Standardkonstruktor erzeugt ein Kartenobjekt indem er die eine input-Liste einliest und diese in Straßen
    #konvertiert.
    def __init__(self, input):
        self.input = input
        self.street_list = []
        self.street_count = int(self.input[0][0])

        for i in range(3, self.street_count-1):
            print(i)
            self.add_street(Street(Kreuzung(input[i][0]), Kreuzung(input[i][1])))

    #Eine Straße wird der dem Attribut "Straßenliste" hinzugefügt
    def add_street(self, street):
        self.street_list.append(street)


#Ein Objekt, dass den Start und Endpunkt, sowie die Länge einer Straße speichert
class Street:

    #Der Standardkonstruktor gibt ein Straßenobjekt zurück.
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


#Eine Kreuzung beschreibt einen Punkt, an dem eine Straße aufhört und eine weitere beginnt
class Kreuzung:

    #Der Standardkonstruktor wandelt einen String in Form (x,y) in ein Kreuzungsobjekt um.
    def __init__(self, way_string):
        self.x = int(way_string[1])
        self.y = int(way_string[3])


#Öffnen der Datei
with open("abbiegen0.txt") as f:
    input = f.readlines()

#Entfernen der Linebreaks
altinput = [x[:-1] for x in input]

#Aufteilen der Kreuzungen
input =  [x.split(" ") for x in altinput]

#Erzeugen der Karte
map1 = Map(input)

print("done")