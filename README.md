# MENPs_as_nanoelectrodes
This repository contains all the code relevant to my PhD dissertation entitled "Magnetoelectric Nanoparticles as Wireless Nanoelectrodes for Neuromodulation."
The dissertation can be found at the following link: https://scholarship.miami.edu/esploro/outputs/doctoral/Magnetoelectric-Nanoparticles-as-Wireless-Nanoelectrodes-For/991031815720402976?institution=01UOML_INST

Guidelines to reproduce the figures in the dissertation are as follows.
- Figure 5.3, page 83: Simply run the file "compartmentalValidation.py"
  
- Figure 5.4, page 84: Uncomment line 98 in "Simple Myelinated Axon.py" and run the file
  
- Figure 5.5, page 85: Uncomment line 112 in "Simple Myelinated Axon.py" and run the file
  
- Figure 5.6, page 86: Uncomment line 114 in "Simple Myelinated Axon.py" and run the file
  
- Figure 5.8, page 91: Uncomment line 102 in "Simple Myelinated Axon.py" and run the file to produce the data ("strength_duration.pkl")
                       Uncomment line 106 in "Simple Myelinated Axon.py" and run the file to produce the figure
  
- Figure 5.9, page 94: Uncomment lines 37-43 in "menpsCharacterization.py", uncomment line 8, set the duty cycle to 0.5 for biphasic or 1 for monophasic, and run the file
  
- Figure 5.10, page 99: Uncomment lines 12-22 in "menpsCharacterization.py", uncomment line 9, set the ac field magnitude under the variable "h_amp" in "menpsCharacterization.py", and run the file
  
- Figure 5.11, page 100: Uncomment lines 25-34 in "menpsCharacterization.py", uncomment line 8, set the duty cycle to 0.5 for biphasic or 1 for monophasic, and run the file
  
- Figure 5.12, page 101: Uncomment line 104 in "Simple Myelinated Axon.py" and run the file to produce the data ("distance_numparts.pkl")
                         Uncomment line 108 in "Simple Myelinated Axon.py" and run the file to produce the figure
  
- Figure 5.13, page 102: Uncomment line 100 in "Simple Myelinated Axon.py" and run the file to produce the data ("menplayers_800_Oe.pkl")
                         Uncomment line 110 in "Simple Myelinated Axon.py" and run the file to produce the figure

Note that this work relies on Brian 2: https://brian2.readthedocs.io/en/stable/

Further note that this code makes use of C++ code generation: https://brian2.readthedocs.io/en/stable/introduction/install.html#requirements-for-c-code-generation

The code can also be run without C++ code generation, but that requires an additional line: prefs.codegen.target = "numpy"
