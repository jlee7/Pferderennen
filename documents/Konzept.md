Horse Racer / Pferderennen
======================

Inhaltsverzeichnis
----------------------
1. Idee
2. Technische Umsetzung
3. Design
4. Events für das Spiel

Idee
----------------------
Grundlegende Spielidee ist das Pferderennen, wie man es von Volksfesten kennt. Dabei treten mehrere Spieler gleichzeitig geneneinader an und versuchen durch gezieltes Werfen von Bällen auf eine Zielscheibe Punkte zu erhalten, die Ihr Pferd vorantreibt. Sieger ist, wer als ersten mit seinem Pferd im Ziel ist. Diese Idee wandeln wir in ein mobiles Spiel um.

Wir erstellen eim Spiel für bis zu 2-4 Spieler gleichzeitig. Jeder Spieler spielt mit seinem eigen mobilen Gerät. Durch Lösen von kleinen Aufgaben (**Hier müssen wir festlegen, was wir machen wollen! Rechenaufgaben? Quizfragen? Gesten ausführen?**) können Punkte gesammelt werden, die das Pferd vorantreiben.

Technische Umsetzung
----------------------------------------------
Server mit Web-Socket sorgen für Synchronisierung zwischen Spielern.
Server sendet Daten im JSON Format...
Verschiedene Spieler können sich in
Räumen treffen und miteinander spielen.
(vgl. Chaträume)

* Hochformat

### Anmelden-Screen
* Wer sich als erster Teinehmer für das Spiel anmeldet is Ho(r)st
  * Host kann das Spiele start
* Alle Spieler sehen den Status der anderen Spieler

Design
----------------------
### 3.1 Start-Screen
Hier wird ein Logo angezeigt.
Der Spieler kann in einer Maske direkt seinen Spielernamen eingeben.
* "Anmelde-Button" für alle Spieler
* Host bekomt noch zusätzlich den Button "Spiel starten"
* Alle Spieler sehen den Namen der anderen Spieler und den Status
* Anzahl der freien Plätze ist sichtbar für alle

### 3.2 Spiel-Screen
In der oberen Hälfte wird das Spielfeld samt Gegenspieler angezeigt.
Die untere Hälfte ist für Interaktionen (Aufgaben) gedacht.

Rechenaufgabe

### 3.3 Resultate-Screen
Hier wird das Resultat des Spiels angezeigt (Rangfolge).
Optionen wie "Erneut spielen" oder "Beenden" sollten möglich sein.


Events für das Spiel
----------------------
* Vom Server an Client
Start
Ende
Du hast gewonnen
Du hast nicht gewonnen
Frage mit richtiger Antwort
Anzahl der Schritte für das Pferd
Highscore

* Vom Client an Server
Name des Spielers oder IP
Gewählte Antwort
Beenötigte Sekunden (Schritte)


offene Fragen
----------------------

ToDos
----------------------

#### Josef:
* limitieren auf 4 Spieler
* Status des Spielers (ready?)
* Pfad zum Html-Template anpassen

#### Manu:
* CSS Framework installieren
* Grobes Screendesign anfertigen
