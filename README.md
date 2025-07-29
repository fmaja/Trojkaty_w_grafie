## Szukanie trójkątów w grafach nieskierowanych i spójnych

Aplikacja webowa służąca do wykrywania wszystkich **trójkątów** w nieskierowanym, spójnym grafie. Trójkąt to zestaw trzech wierzchołków, między którymi istnieją wszystkie trzy możliwe krawędzie.

Projekt zrealizowany z użyciem frameworka **Flask** w języku **Python**.

## Format danych

Dane wejściowe zapisane są jako lista sąsiedztwa w formacie JSON:

```json
{
  "A": ["B", "C"],
  "B": ["A", "C"],
  "C": ["A", "B"]
}
```

- Klucze i wartości muszą być typu `string`  
- Dla każdej krawędzi (A → B) musi istnieć odwrotna (B → A)

## Algorytm

- **Weryfikacja grafu** – DFS i sprawdzanie symetrii krawędzi  
  Złożoność: `O(V + E)`

- **Wykrywanie trójkątów** – sprawdzanie kombinacji `[v, u, w]`, gdzie `v < u < w`  
  Złożoność: `O(V³)` w najgorszym przypadku

## Uruchamianie

W folderze `dist/` znajduje się gotowy plik `.exe`.  

## Struktura projektu

- `app.py` – główny plik aplikacji Flask (logika działania)
- `dist/` – gotowa aplikacja `.exe` do uruchomienia
- `trójkąty.spec` – plik konfiguracyjny PyInstaller
- `przyklad.txt`, `przyklad.json`  – przykładowe dane wejściowe

##  Autorzy
- Maja Fiszer
- Marta Czarnecka

