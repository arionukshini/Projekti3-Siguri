
## Implementimi i Kriptimit sipas Hill Cipher

Ky projekt është realizuar në Python dhe implementon algoritmin **Hill Cipher** për enkriptim dhe dekriptim të tekstit.

Sipas kërkesës së detyrës, aplikacioni ofron mundësinë e përdorimit të matricave me rang:
- `2x2`
- `3x3`
- `4x4`

## Përmbajtja e projektit

Projekti përmban këto file:

- `hill_cipher.py`
  - përmban funksionet bazë për enkriptim
  - pastrimin e tekstit
  - ndarjen e tekstit në blloqe
  - kthimin e shkronjave në numra dhe anasjelltas
  - shumëzimin e matricës me blloqet e tekstit

- `decrypt_utils.py`
  - përmban funksionet për dekriptim
  - llogaritjen e determinantit
  - kontrollin nëse matrica është e invertueshme
  - gjetjen e inversit të matricës modulo 26

- `main.py`
  - përmban menunë kryesore të aplikacionit
  - lejon zgjedhjen e operacionit:
    - enkriptim
    - dekriptim
    - dalje nga programi
  - lejon zgjedhjen e matricës sipas rangut

## Si funksionon programi

Programi punon me alfabetin anglez me 26 shkronja:
- `A = 0`
- `B = 1`
- ...
- `Z = 25`

Gjatë përpunimit:
- teksti shndërrohet në shkronja të mëdha
- largohen karakteret jo alfabetike
- nëse gjatësia e tekstit nuk pjesëtohet me madhësinë e matricës, shtohet `X` si padding

## Si të ekzekutohet

Në terminal, nga folderi i projektit, ekzekuto:

```bash
python main.py
