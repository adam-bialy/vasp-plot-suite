# DosApp 
### (C) AG 2022

DosApp is an application for plotting electronic density of states (eDOS) data
from output of DFT calculations using VASP package.

Its use is very straightforward.

- "Browse": select a <code>vasprun.xml</code> file
- "Load" the system
- Select atoms using dropdown menu or by listing their symbols or ordinal numbers
in the structure
- Select states: subshells or orbitals
- Select spin states
- Choose a display name for the system and line color for the plot
- Add or remove dataset to/from the list
- Add total eDOS without selecting any atoms and states with "Add total DOS" button
- Export a selected dataset as .csv file
- You can manipulate and save the plot using built-in <code>matplotlib</code> toolbar

### Executables
This program can be compliled into an executable.
I can provide ones for Windows or MacOS upon request.

### This program is still being tested
If you notice any errors or discrepancies, or if you have any practical suggestions,
I would be grateful if you report them.
I have also included sample data for AgF2 system if you want to give it a try.

### Contact
contact@adamgrzelak.com

### Update history
10.05.2022 - incorporated <code>matplotlib</code> widget into the main window<br>
05.05.2022 - refactored the application to read <code>vasprun.xml</code><br>
21.03.2022 - incorporated exception handling into vasp-dos-tools and refactored frontend to
display them