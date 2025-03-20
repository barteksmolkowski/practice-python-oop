> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e02-python-basics` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Python: Programowanie obiektowe

Twoim zadaniem jest stworzenie **klasy `Employee`**, reprezentującej ogólnego pracownika, oraz **klasy `Teacher`**, która będzie dziedziczyć po `Employee`. Klasa `Teacher` powinna rozszerzać funkcjonalność klasy bazowej poprzez dodatkowy atrybut i zmianę sposobu wyświetlania informacji o pracowniku.


### ✅ Wymagania

1. **Zdefiniuj klasę `Employee`**, która będzie posiadać:
   - `name` – imię i nazwisko pracownika,
   - `position` – stanowisko.

2. **Zaimplementuj metodę `describe(self)`**, która zwróci informację o pracowniku w formacie:
   ```
   Jan Kowalski pracuje na stanowisku Menedżer.
   ```

3. **Zdefiniuj klasę `Teacher`, która dziedziczy po `Employee`** i dodaje nowy atrybut:
   - `subject` – przedmiot, którego nauczyciel uczy.

4. **Nadpisz metodę `describe(self)` w klasie `Teacher`**, aby uwzględniała przedmiot:
   ```
   Anna Nowak jest nauczycielem i uczy matematyki.
   ```

5. **Stwórz obiekty `Employee` i `Teacher`, a następnie przetestuj metodę `describe()`**.



### 💡 Podpowiedzi
- Obie klasy utwórz w pliku `app.py`.
- Zwróć uwagę, że metoda `describe()` w `Teacher` **całkowicie zastępuje** metodę z `Employee`.  
- **Czy potrafisz wykorzystać `super()`**, aby uniknąć powielania kodu w `describe()`?
- Możesz dodać więcej klas, np. `Doctor`, `Engineer`, które również dziedziczą po `Employee`.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-basics)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
