Zrobione:
- [x] finess jako parametr
- [x] dodać mechanizm zapobiegający wpadaniu w lokalne optimum - dodane patience czyli liczba iteracji po której na nowo jest generowane 40% populacji
- [x] naprawienie błędu OverflowError: integer division result too large for a float
- [x] naprawienie błędu z wyświetlaniem pustej tablicy - okazało się że problem był znowu z kopiowaniem tablic - interpreter 
    działał na orginale i po wczytaniu wartości z tablicy usuwał ją sobie i potem inne programy miały puste inputy
- [x] dodanie opcji, żeby najsilniejszy potomek zawsze przechodził do następnej generacji

Do Zrobienia:
- [ ] popracowac nad crossoverem
- [x] dodac w wierzchołakch drzewa informacje o liczbie wszystkich jego dzieci i szansa na mutacje to 1/2^log10(liczba dzieci + 1) - możliwe że trzeba będzie i tak zwiększyć podstawę logarytmu, bo na 100 dzieci mutuje tylko kilka nodów (im większa podstawa tym większe szanse na zmutowanie)
- [ ] szansa na crossover zalezy od poziomu?
- [ ] mutacja całego poddrzewa
- [ ] dynamiczne zmienianie parametrow szansy na mutacje i crossover
- [ ] fitness powinien od pewnego momentu promować rozwiązania krótkie