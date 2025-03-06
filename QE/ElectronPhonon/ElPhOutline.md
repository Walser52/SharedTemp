# Electron Phonon Interaction
## Files
### EPW Output Folder

### File Descriptions
#### fmt files
- crystal.fmt
- epwdata.fmt
- selecq.fmt
- vmedata.fmt

- decay.dynmat = Spatial decay of Dynamical matrix in Wannier basis
- decay.epmate
- decay.v = Spatial decay of Velocity matrix element in Wannier basis

- epw.out 

- lambda.phself.200:    Lambda phonon self-energy
- linewidth.phself.200: Phonon frequency and phonon lifetime in meV

- {prefix}.phdos.01.200
- {prefix}.res.01.200: Resistivity for different Phonon smearing

#### {prefix} - Wannier90?
- .bvec
- .chk
- .epb1
- .epb2
- .epmatwp
- .kgmap
- .kmap
- .mmmn
- .nnkp
- .ukk
- .wfc1
- .win
- .wout
- _hr.dat
- _wsvec.dat



#### Unknown
- {prefix}a2f.01.200
- {prefix}a2f_tr.01.200
### PH Output Folder

- {prefix}.dyn0
- {prefix}.dyn1
- ph.out

### File Descriptions


## Data Handling Methods
(See 'Theoretical Considerations' for background)

### Phonon - Dispersion
- pw.x
- ph.x
- q2r.x
- matdyn.x

### Phonon - DoS



### Phonon Linewidths

#### From epw.x
[Phonon linewidths for the highest optical mode of B-doped diamond. Density of k-points and the smearing parameter reported.](https://docs.epw-code.org/_images/Bdiamond3.png)



#### From ph.x

### Eliashberg spectral function alpha^2 F
Contributions from scattering processes, in which the electrons are scattered by the phonons on the Fermi surface. Important for finding the critical temperature of superconductors.

### Transport counterpart of alpha^2 F
Transport counterpart

### Resistivity using Ziman formula

### Electron and Hole Mobilities

### gauge-invariant g_q
[Link](https://docs.epw-code.org/doc/GaN.html)


### Spectral function


### Electron self-energy
(Is the spectral function enough)

### SOC incorporation

### Electron-Phonon Coupling Strength (lambda)



## Theoretical Considerations
### Eliashberg Spectral function
characterizes how phonons (vibrational modes) couple to the electrons. It essentially weighs the phonon density of states with the square of the electron–phonon coupling matrix elements. This function is central to Eliashberg theory of superconductivity, where it determines quantities like the superconducting gap and mass renormalization.

#### Usage:
alpha^2F enters the Eliashberg equations to self-consistently determine the electron self-energy due to phonons and predict superconducting properties.

### Spectral function
$$
\begin{equation*}
 A_{n\mathbf{k}}(\omega,T) = \frac{1}{\pi} \frac{|\Im \Sigma_{n\mathbf{k}}(\omega,T)|}{|\omega - \varepsilon_{n\mathbf{k}}-\Re \Sigma_{n\mathbf{k}}(\omega,T)|^2 + |\Im \Sigma_{n\mathbf{k}}(\omega,T)|^2}.
\end{equation*}
$$

This equation is the expression for the spectral function Ank(ω,T) of an electronic state. This is the one-particle (or quasiparticle) spectral function, often derived from the Green’s function formalism. It shows how the interacting electronic states (or quasiparticles) are broadened and shifted by the self-energy Σnk(ω,T)Σnk​(ω,T).

It shows how the "bare" electronic energy εnk​ is renormalized and broadened by many-body interactions encoded in the self-energy Σnk(ω,T).

[Involves: Debye-Waller and Fan-Migdal term. EPW does not compute Debye-Waller term.]

#### Usage:
to analyze:
- quasiparticle lifetimes, 
- band renormalization, 
- spectral weight distribution observable 
in, for example, angle-resolved photoemission spectroscopy (ARPES).

### Debye-Waller and Fan-Migdal Term

### Electron Self-Energy


## Questions

### Intepretation of phonon and electron linewidths
- When to study
- Consequences 




### 

