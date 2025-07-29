## Szukanie trójkątów w grafach nieskierowanych i spójnych

Aplikacja webowa służąca do wykrywania wszystkich **trójkątów** w nieskierowanym, spójnym grafie. Trójkąt to zestaw trzech wierzchołków, między którymi istnieją wszystkie trzy możliwe krawędzie.

Projekt zrealizowany z użyciem frameworka **Flask** w języku **Python**.

## Format danych

Dane wejściowe zapisane są jako lista sąsiedztwa w formacie JSON:

```json
{
  "A": ["B", "C"],
  "B": ["A", "C", "D"],
  "C": ["A", "B"],
  "D": ["B", "E"],
  "E": ["D"]
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

## Podgląd strony

 <img width="400" alt="Screenshot 1" src="https://github.com/user-attachments/assets/ded7de6d-7052-44b3-80fc-909fe117a65f" /> | <img width="400" alt="Screenshot 2" src="https://github.com/user-attachments/assets/7771c00b-7791-4418-ad2b-6477ef066ae1" /> 


## Struktura projektu

- `app.py` – główny plik aplikacji Flask (logika działania)
- `dist/` – gotowa aplikacja `.exe` do uruchomienia
- `trójkąty.spec` – plik konfiguracyjny PyInstaller
- `przyklad.txt`, `przyklad.json`  – przykładowe dane wejściowe

##  Autorzy
- Maja Fiszer
- Marta Czarnecka

