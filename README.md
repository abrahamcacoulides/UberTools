# UberTools
For AutoCAD R13 only.
*************************************************************************************************

********************************************
UberTitle Current Version 4.0
*************************************************************************************************

********************************************
Mark the browse check button to browse trough you folders and select the folder where the 

drawings and the ENG file are located.

The ENG file should be named ENG.eng for simplex jobs and ENGX.eng for Duplex/Groups, where X 

should be the car label.

The Title block should be named "TITLE.dwg" and should be located in the same path as the 

drawings.
*************************************************************************************************

*********************************************
Buttons:
Browse: Use this button to locate the folder where your job is located
OK!:Generates the script file
GO!:Opens Autocad and runs the script

After closing the GUI the script file is deleted
*************************************************************************************************

*********************************************
V1.01 Differentiation between BLD pages for R&R and HAPS fixed
V1.01 Pages GND, PI, UDC and L3 for DI and SI LS's had been differentiated as horizontal. 
V1.01 Adds the word GROUP to the title block when car label == 'z'
V1.02 Support for horizontal page 2DI as well as INT
V2.0 Works with the new TITLE.lsp
V2.1 New buttons added. Can Modify titles from GUI.
V2.2 Minor modifications to how it opens Autocad and how it runs the script
V3.0 Path to job and Browse button added.
V3.1 Scripts removal fixed
V4.0 Button to remove 'READ ONLY' feature from DWG's added (KLEINERTITLE contribution)
V4.01 Fixed bugs: Capital letters in ENG are now supported;TITLE.dwg is now also unlocked through 

the UI
V4.02 Fixed major bug: It was adding the title to CP and N, issue solved.
V4.03 Fixed bug: GitHUB issue #1
