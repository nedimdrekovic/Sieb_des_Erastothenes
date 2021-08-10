# Sieb des Erastothenes

Bei diesem Projekt handelt es sich um eine Visualisierung des "Sieb des Erastothenes"-Algorithmus zur Darstellung und Bestimmung aller Primzahlen im Intervall [2, n] für einen gegebenen Wert von n, der als obere Schranke dient. Diese werden nacheinander in einem roten Bereich gelb markiert.

<p float='left'>
  <img src="https://user-images.githubusercontent.com/73491052/128611579-9286c315-ca85-484c-b6fb-0ffa083d9050.png" width=300 align="left">
  <img src="https://user-images.githubusercontent.com/73491052/128611583-b13d24d2-291c-44df-b881-e928d1a095d3.png" width=300 align="left">
  <img src="https://user-images.githubusercontent.com/73491052/128611582-421b0069-0430-409d-adac-e0f1a99109d3.png" width=300 align="center">
</p>

<br></br>

# Funktionsweise des Algorithmus
1) Der Algorithmus durchläuft eine aufsteigend sortierte Liste, die alle Zahlen in [2, n] enthält, beginnend mit 2.
2) Dabei werden alle Vielfachen der aktuell betrachteten Zahl x aus der Liste gestrichen und x als Primzahl markiert.
3) Dann wird das nächste Element aus der Liste ausgewählt und 2) erneut ausgeführt, solange bis das Ende der Liste erreicht ist.
