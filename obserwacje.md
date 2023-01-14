Dla funkcji liniowej przy funkcji kosztu zależnej tylko od ilości outputu wynik jest zaskakująco dobry:
Best program:  IF(96>X2)X1=31;;print(X1);
wzorcowy: print(X1*2);

X1=X1;print(39);LOOP(((98==42)OR(X1<X2))OR((22<84)OR(X2!=95)))IF(X1*X1+91>X3)LOOP(((49!=X2)OR(84==3))AND((24==14)AND(36>X2)))LOOP(73>X2)LOOP(X6<X4)X2=61;;;X8=83;;;;

------------------------

Problem:
Jeśli GP znalzało stosunkowo dobre rozwiązanie, to utykało w minimum lokalnym. Np. dla problemu wypisania liczby 789 na wyjściu program potrafił utknąć z liczbą 83 lub 94:
- outputs\example11_B\log789_stuck_with_84.txt
- outputs\example11_B\log789_stuck_with_93.txt

Rozwiązanie:
- dodanie parametru patience (u nas równe 5), który mówi ile epok może nie być poprawy w najlepszej wartości fitness
- jeśli zostanie przekroczony limit epok bez poprawy 40% populacji jest generowane na nowo (z pominięciem najlepszego osobnika)
- w sytuacjach, kiiedy najlepszy osobnik rozrósł się na całą populację ponowna generacja 40% nie wiele dawała, dlatego z każdą kolejną generacją % generowanej populacji się zwiększał

```python
    if self.epochs_without_improvement >= self.patience:
        self.epochs_without_improvement = 0
        self.nr_of_regenerations += 1
        ratio_to_generate = min(0.4 + 0.05 * self.nr_of_regenerations, 0.9)
        for idx in range(0, int(ratio_to_generate * self.population_size)):
            if idx == self.best_indiv_idx:
                continue # leave the best indiv
            self.population[idx] = self.create_random_individual()
            program_str = self.generate_program_str(self.population[idx])
            self.fitness[idx] = self.compute_fitness(program_str)
        print(int(ratio_to_generate * self.population_size), "  generated again")
```

--------------------

Problem: ten sam co wyżej
Poprzednie rozwiązanie pomagało wyjść z lokalnego minimum, ale powodowało ono utratę pamięci, które drzewa były bliżej sukcesu niż pozostałe - drzewa były randomo generowane od początku.

Rozwiązanie:
Prawdopodobieństwo mutacji jest zależne od tego czy fitness jest mniejszy od średniej - drzewo chętniej mutuje jeżeli ma gorszy fitness:
```python
def mutate(self, root: Node, node_idx = -1) -> Node:
        queue = [root]
        while queue:
            node = queue.pop()
            try:
                if self.fitness[node_idx] < self.avg_fitness or random.random() < self.mutation_rate:  # 50%
                    # higher prob to mutate if fitness is worse than average
                    if random.random() < 1/2**(log(root.height + 1, 4)):
```

---------------------

Problem:
W mutacji częściej mutowały nody położone wyżej, często zmieniały się raczej bardziej ogólne części programu (np. LOOP na IF) zamiast bardziej szczegółowych (np. + na -).

Rozwiązanie:
Prawdopodobieństwo mutacji zależy od wysokości danego node'a zgodnie ze wzorem:

$0.5^{(log(root.height + 1, 4))}$

Crossover jest tym większy im gorszy jest fitness (przepinany jest node wyżej)

---------------------

Problem:
Generowane rozwiązania miały bardzo duże drzewa

Rozwiązanie:
Dodanie długości programu jako parametru funkcji fitness

---------------------

Problem:
Overflow w funkcji kosztu

Rozwiązanie:
Dodanie parametru max_fitness, który mówi jaki jest minimalny fitness programu, ustawione na -milion

---------------------

Problem:
Przy próbie wyskoczenia z lokalnego optimum nowe programy nie miały czasu dopasować się do danych, przez co znowu były na nowo losowane

Rozwiązanie:
Resetowanie licznika epoki bez poprawy fitness po każdej próbie ucieczki z optimum

---------------------

Problem:
Program niepoprawnie wczytywał dane z pliku

Rozwiązanie:
Zmiana gramatyki, dodanie konstrukcji read(x); do wczytywania danych

---------------------

Problem:
Program nie potrafił znaleźć rozwiązania dla problemu ze wczytywaniem liczby

Rozwiązanie:
Dodanie różnych prawdopodobieństw mutacji dla różnych typów node'ów

---------------------

Problem:
Błędna implementacja agregacji outputu wierzchołków w bibliotece ANTLR

Rozwiązanie:
Naprawa błędu w bibliotece lokalnie. Próbowaliśmy zrobić PR na oficjalne repo, ale zostało odrzucone, przez błędy z kompatybilnością wsteczną.

---------------------
