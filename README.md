# taucauto
Python script that automatically extracts the bandgap of a material by the Tauc method [1].
Tauc plots are also generated. A windows '.exe' standalone is also provided. 

### Function
Transforms spectrum '.txt' files within a directory into Tauc plots, which are generated as '.jpg' files. From these plots, the bang gap is extrapolated as outlined in ref [1].

### Using taucauto

`taucauto` should be used within a directory containing spectrum files. These files should have the following format:
```python
"example1 - RawData"
"Wavelength nm." "Abs."
X1 Y1
X2 Y2
 .  .
 .  .
 .  .
```
where Xi and Yi are the recorded wavelengths and absorption coefficients, respectively. 

1. Python on command line

Within the directory containing spectrum files, do:
```python
python taucauto.py
```
Which will return '.jpg' files containing the Tauc plots, annotated with the extrapolation line used to obtain the band gap. If multiple spectrum files are present, this will be done for each of these and an output file *output.dat* will be created containing a list of spectrum files and their corresponding computed band gaps. 

2. Using the Windows executable

The Windows executable has been created using pyinstaller (https://www.pyinstaller.org/).
To use, place `taucauto.exe` in a folder containing the spectrum files and double click. 

### Tauc plots
A Tauc plot [1] is used to determine the optical bandgap, or Tauc gap, in semiconductors. The Tauc gap is often used to characterize practical optical properties of amorphous materials.

Jan Tauc showed that the optical absorption spectrum of amorphous germanium resembles the spectrum of the indirect transitions in crystalline germanium (plus a tail due to localized states at lower energies), and proposed an extrapolation to find the optical gap of these crystalline-like states. Typically, a Tauc plot shows the quantity hν (the energy of the light) on the abscissa and the quantity (αhν)^(1/r) on the ordinate, where α is the absorption coefficient of the material. The value of the exponent r denotes the nature of the transition.

* r = 1/2 for direct allowed transitions
* r = 3/2 for direct forbidden transitions.
* r = 2 for indirect allowed transitions
* r = 3 for indirect forbidden transitions

Here, direct allowed transitions are assumed (i.e. r = 1/2). 

The resulting plot has a distinct linear regime which denotes the onset of absorption. Thus, extrapolating this linear region to the abscissa yields the energy of the optical band gap of the material.

[1] Tauc, J. (1968). Materials Research Bulletin. 3: 37–46. doi:10.1016/0025-5408(68)90023-8

### Files



