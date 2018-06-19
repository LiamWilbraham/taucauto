# taucauto
Python script that automatically extracts the bandgap of a material by the Tauc method [1].
Tauc plots are also generated.

## Function
Transforms spectrum '.txt' files within a directory into Tauc plots, which are generated as '.jpg' files. From these plots, the bang gap is extrapolated as outlined in ref [1].

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


