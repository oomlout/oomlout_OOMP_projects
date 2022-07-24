# oomlout_OOMP_projects
OOpen Organization Method for parts. This is all the project details.

### Part Files
* Summaries
	Readme's are generated using mdutils (https://github.com/didix21/mdutils). Generation is done in OOMPsummaries.py
	* Readme.md (generated)  --  A summary of the part in markdown.

* Images
	Images also have extra resolutions generated these are, _140, _450, _600.
	* image.jpg  --  Main image.
	* image_RE.jpg  --  Image for size reference (usually beside a sharpened pencil).
	* image_TOP.jpg  --  Image of the top of the part.
	* image_BOTTOM.jpg  --  Image of the bottom of the part.
	
* Diagrams
	Diagrams are generated from tags, they can use templates (templates/diag/), which can use a parts tags as input. These are compiled to a python script that uses the Simple Inkscape Scripting Extension (https://github.com/spakin/SimpInkScr/) to draw and save svgs, these svgs are then used to genearate pngs, dxfs, and pdfs.
	* diagBBLS.py (generated)  --  A diagram for adding a part to a breadboard layout sheet.
	* diagDIAG.py (generated)  --  A diagram for adding a part to a layout.
	* diagIDEN.py (generated)  --  A diagram for adding a part to a PCB with details.
	* diagSCHEM.py (generated)  --  A diagram for adding a part to a schematic.
	* diagSIMP.py (generated)  --  A diagram with only the parts outline, and link.
    * diagFritz.fzpz  --  A diagram in Fritzing format
    * working.cdr  --  A file for working on the component drawing in Corel Draw format

* Datasheets
	* datasheet.pdf  --  Datasheet for the part.
	* datasheet-C-SUPL  --  If more than one datasheet exists the manufacturers four letter code is added.
	* datasheet.txt (generated)  --  If the datasheet is a duplicate this file has the location in it, if it is hosted externally a link.
	
* 3D Models
	3D models are generated programatically these routines are in OOMPscad.py, they use SolidPython (https://github.com/SolidCode/SolidPython) to generate .scad files from which stls and pngs are generated.
	* 3dmodel.scad (generated)  --  Scad model of the part. Programatically generated in OOMPscad.py
	* 3dmodel.stl (generated)  --  STL version of 3dmodel.scad
	* 3dmodel.png (generated)  --  Rendered image of 3dmodel.scad (ortho)
	
* Labels
	Labels are generated using tags and templates these are in templates/label/ they are svgs and use search and replace to generate labels. (%%ID%% is replaced by part ID and tags are format @@%%ID%%,oompPart.oompID,tagName@@). From the svgs pdfs are generated.
	* label-front.svg (generated)  --  A label for the front of a bag.
	* label-inventory.svg (generated)  --  A label for keeping inventory organized.
	* label-spec.svg (generated)  --  A label listing part specifications.

* EDA
    Design files
    * boardEagle.brd  --  Board file in Eagle format
    * schematicEagle.scm  --  Schematic File in Eagle format
    * boardKicad.brd  --  Board file in Kicad format
    * schematicKicad.scm  --  Schematic File in Kicad format