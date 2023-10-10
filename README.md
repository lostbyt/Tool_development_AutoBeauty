# Tool development AutoBeauty

![Image](https://github.com/lostbyt/Tool_development_AutoBeauty/blob/main/capture01.PNG)



### Brief
This project aims to enhance the quality of life for VFX artists in their daily tasks.
One of the common tasks that a VFX compositor/Lighter must perform is **reconstructing a "beauty" pass**
from the various layers generated during CG rendering.


The goal is to achieve complete control over the render's appearance by being able to independently adjust each layer.

For example, typically rendered layers include *diffuse, specular, shadows, depth*, and so on.
These passes can vary from one rendering engine to another, but the overarching concept remains consistent: separate all components of light and its behavior.

Since the pipeline I was working on used the Blender and RedShift rendering engines, I incorporated their rendering patterns into this tool.

**Developer:** Emmanuel Moulun
**Studio:** Budos
**Demo:** https://vimeo.com/858283846




##### Blender Cycle passes:
* Diffuse direct
* Diffuse indirect
* Diffuse color
* Emit
* Glossy direct
* Glossy indirect
* Glossy color
* Transmission direct
* Transmission indirect
* Transmission color
* Beauty

##### RedShift passes:
* Diffuse lighting
*  Global illumination
* Specular
* Reflections
* Beauty

### Final product
The tool streamlines the entire process for artists. 
They can effortlessly import their passes, choose the rendering engine used to generate these passes, 
and then access a range of grading and denoising tools for precise adjustments following the automated reconstruction.

