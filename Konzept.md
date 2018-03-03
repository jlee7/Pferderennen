Horse Racer
======================

Inhaltsverzeichnis
----------------------
1. Idee
2. Technische Umsetzung
3. Design


Idee
----------------------
Grundlegende Spielidee ist das Pferderennen, wie man es von Volksfesten kennt. Dabei treten mehrere Spieler gleichzeitig geneneinader an und versuchen durch gezieltes Werfen von Bällen auf eine Zielscheibe Punkte zu erhalten, die Ihr Pferd vorantreibt. Sieger ist, wer als ersten mit seinem Pferd im Ziel ist. Diese Idee wandeln wir in ein mobiles Spiel um. 

Wir erstellen eim Spiel für bis zu **XX** Spieler gleichzeitig. Jeder Spieler spielt mit seinem eigen mobilen Gerät. Durch Lösen von kleinen Aufgaben (**Hier müssen wir festlegen, was wir machen wollen! Rechenaufgaben? Quizfragen? Gesten ausführen?**) können Punkte gesammelt werden, die das Pferd vorantreiben.

Technische Umsetzung
----------------------
Server mit Web-Socket sorgen für Synchronisierung zwischen Spielern.
Server sendet Daten im JSON Format
...

Design
----------------------
### 3.1 Start-Screen

Hier wird ein Logo angezeigt.
Der Spieler kann in einer Maske direkt seinen Spielernamen eingeben.

### 3.2 Spiel-Screen
In der oberen Hälfte wird das Spielfeld samt Gegenspieler angezeigt.
Die untere Hälfte ist für Interaktionen (Aufgaben) gedacht.

### 3.3 Resultate-Screen
Hier wird das Resultat des Spiels angezeigt (Rangfolge).
Optionen wie "Erneut spielen" oder "Beenden" sollten möglich sein.


offene Fragen
----------------------

* Wieviele Spieler?
2 - 4 Spieler

