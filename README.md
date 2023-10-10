# Tool development AutoBeauty

## Brief
This project aims to enhance the quality of life for VFX artists in their daily tasks.
One of the common tasks that a VFX compositor/Lighter must perform is **reconstructing a "beauty" pass**
from the various layers generated during CG rendering.


The goal is to achieve complete control over the render's appearance by being able to independently adjust each layer.

For example, typically rendered layers include *diffuse, specular, shadows, depth*, and so on.
These passes can vary from one rendering engine to another, but the overarching concept remains consistent: separate all components of light and its behavior.

Since the pipeline I was working on used the Blender and RedShift rendering engines, I incorporated their rendering patterns into this tool.

##### Developer: Emmanuel Moulun
##### Studio: Budos
##### Demo: https://vimeo.com/858283846

##### Blender Cycle passes:
1. Diffuse direct
2. Diffuse indirect
3. Diffuse color
4. Emit
5. Glossy direct
6. Glossy indirect
7. Glossy color
8. Transmission direct
9. Transmission indirect
10. Transmission color
11. Beauty

##### RedShift passes:
1. Diffuse lighting
2. Global illumination
3. Specular
4. Reflections
5. Beauty

## Final product
The tool streamlines the entire process for artists. 
They can effortlessly import their passes, choose the rendering engine used to generate these passes, 
and then access a range of grading and denoising tools for precise adjustments following the automated reconstruction.

