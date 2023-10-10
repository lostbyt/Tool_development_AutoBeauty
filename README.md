# Tool development AutoBeauty

**Developer:** Emmanuel Moulun<br>
**Studio:** Budos<br>
**Demo:** https://vimeo.com/858283846

![Image](https://github.com/lostbyt/Tool_development_AutoBeauty/blob/main/capture01.PNG)

### Description:
This project aims to enhance the quality of life for VFX artists in their daily tasks.
One of the common tasks that a VFX compositor/Lighter must perform is **reconstructing a "beauty" pass**
from the various layers generated during CG rendering.

The goal is to achieve complete control over the render's appearance by being able to independently adjust each layer.

For example, typically rendered layers include *diffuse, specular, shadows, depth*, and so on.
These passes can vary from one rendering engine to another, but the overarching concept remains consistent: separate all components of light and its behavior.

Since the pipeline I was working on used the Blender and RedShift rendering engines, I incorporated their rendering patterns into this tool.

### Features:
1. automate the reconstruction of the beauty pass
2. Compatible with Blender Cycle
3. Compatible with RedSchift
4. Grade tool incorporated
5. Denoise/Sharpen tool incorporated
6. Quality check control incorporated
7. Export (Alpha, RGB and RGBA) incorporated

![Image](https://github.com/lostbyt/Tool_development_AutoBeauty/blob/main/mindMap.jpg)


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

### Technologies:
Python V3 with Nuke Python API

### License:
GNU GPLv3

### Final product
The tool streamlines the entire process for artists. 
They can effortlessly import their passes, choose the rendering engine used to generate these passes, 
and then access a range of grading and denoising tools for precise adjustments following the automated reconstruction.

![Image](https://github.com/lostbyt/Tool_development_AutoBeauty/blob/main/autoBeauty_denoise.jpg)

