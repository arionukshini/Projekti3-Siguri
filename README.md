# Projekti 3 - Siguri

## Implementimi i Kriptimit sipas Hill Cipher

Ky projekt është realizuar në Python dhe implementon algoritmin **Hill Cipher** për enkriptim dhe dekriptim të tekstit.

Sipas kërkesës së detyrës, aplikacioni ofron mundësinë e përdorimit të matricave me rang:
- `2x2`
- `3x3`
- `4x4`

## Përshkrimi i projektit

Hill Cipher është një algoritëm klasik i kriptografisë që përdor matrica dhe operacione modulo `26` për të transformuar tekstin e zakonshëm në tekst të enkriptuar dhe anasjelltas.

Në këtë projekt:
- teksti pastrohet dhe shndërrohet në shkronja të mëdha
- largohen karakteret jo alfabetike
- teksti ndahet në blloqe sipas madhësisë së matricës
- kryhet enkriptimi duke shumëzuar blloqet me matricën e çelësit
- kryhet dekriptimi duke përdorur inversin e matricës modulo `26`

## Përmbajtja e projektit

Projekti përmban këto file:

### `hill_cipher.py`
Ky file përmban funksionet bazë për enkriptim:
- pastrimin e tekstit
- ndarjen e tekstit në blloqe
- kthimin e shkronjave në numra
- kthimin e numrave në shkronja
- shumëzimin e matricës me blloqet e tekstit
- funksionin `encrypt()`

### `decrypt_utils.py`
Ky file përmban funksionet për dekriptim:
- llogaritjen e determinantit për matricat `2x2`, `3x3` dhe `4x4`
- kontrollin nëse matrica është e invertueshme
- gjetjen e inversit të matricës modulo `26`
- funksionin `decrypt()`

### `main.py`
Ky file përmban menunë kryesore të aplikacionit dhe ndërveprimin me përdoruesin:
- zgjedhjen e operacionit:
  - `Encrypt`
  - `Decrypt`
  - `Exit`
- zgjedhjen e mënyrës së përdorimit të matricës:
  - matricë automatike
  - matricë manuale
- mbështet futjen e matricave me rang `2`, `3` dhe `4`

## Si funksionon programi

Programi punon me alfabetin anglez me 26 shkronja:

- `A = 0`
- `B = 1`
- `C = 2`
- ...
- `Z = 25`

Gjatë përpunimit:
- teksti shndërrohet në shkronja të mëdha
- hiqen karakteret jo alfabetike
- nëse gjatësia e tekstit nuk pjesëtohet me madhësinë e matricës, shtohet `X` si padding

## Përdorimi i matricave

Programi ofron dy mënyra për përdorimin e matricës:

### 1. Matricë automatike
Përdoruesi mund të zgjedhë një matricë të gatshme sipas rangut:
- `2x2`
- `3x3`
- `4x4`

### 2. Matricë manuale
Përdoruesi mund të zgjedhë rangun `2`, `3`, ose `4` dhe të shkruajë vetë elementet e matricës rresht për rresht.

Programi kontrollon nëse matrica është e invertueshme modulo `26`. Nëse matrica nuk është e vlefshme për Hill Cipher, përdoruesi njoftohet me mesazh gabimi.

## Shembuj të matricave automatike

### Matrica `2x2`
```text
3 3
2 5
