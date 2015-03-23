Jupyter-based Teaching & Learning
===

<div align="center">
    <img width=400 src="http://www.nature.com/polopoly_fs/7.21336.1415199590!/image/Toolbox.jpg_gen/derivatives/landscape_630/Toolbox.jpg" title="Illustration by the Project Twins"</img>
</div>

## Intro

The IPython environment lends itself to **teaching and learning**: 

* immediate feedback, 
* flexible visualisation, 
* easy access to docstrings and 
* ability to explore modules.

The release of the IPython Notebook in 2011 made it even more attractive as an **eLearning tool**, by providing browser-based access to an iPython environment with the ability to share notebooks with others, embed output products and annotate code.

With the launch of the **project Jupyter** last July, it went a step further, enabling the evolution of the language-agnostic parts of Python (R, Julia, Ruby, etc.) into an open platform for **interactive education**.

Within the School of Geosciences of the Univeristy of Sydney, we think that Jupyter/IPython could give both teachers and students new tools to communicate with and document good code practices as well as subject matter in fields such as 

* Math, 
* Physics, 
* Social Sciences, 
* Earth Sciences, 
* Medical Sciences or 
* Economy. 
 
Since the beginning of the first semester of 2015, I have been starting to create interactive IPython teaching notebooks in some of our Units of Study:

* MARS5001: <a href='https://github.com/t-salles/notebooks/tree/master/MARS5001'>Coastal Processes & Systems<a/>
* GEOS3102: Global Energy & Resources

As a quite recent IPython user, most of the materials from these notebooks are inspired from the work of others... Some of these notebooks could be used with the <a href='https://github.com/damianavila/RISE'>RISE slideshow extension</a> for lecture presentation, where others are more for practice. 

So far, I've been using the *Amazon Web Services* cloud infrastructure and *Dropbox* to deploy and share my modules and notebooks through the Web with the students.


For an introduction to IPython, I will recommend this <a href='https://dl.dropboxusercontent.com/u/31110214/Learning%20IPython%20for%20Interactive%20Computing%20and%20Data%20Visualization.pdf'>book</a> from Cyrille Rossant.

# MARS5001 lectures material

### Session 1: Query data & models from the Web

* Overview &mdash;  <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session1/Lecture-overview.ipynb'>nbviewer<a/>
* Ocean Radar Data Query &mdash;  <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session1/NB1-ACORN.ipynb'>nbviewer<a/>
* Historical records and past models &mdash;  <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session1/NB2-BuoyWW3.ipynb'>nbviewer<a/>
* Access data from Forecast Model &mdash;  <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session1/NB3-Forecast.ipynb'>nbviewer<a/>
* Compute Ekman current from wind data &mdash;  <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session1/NB4-Ekman.ipynb'>nbviewer<a/>

### Session 2: Wave propagation on 1D beach profile

* Overview &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session2/Lecture-overview.ipynb'>nbviewer<a/>
* Shallow Water Equation 1D &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session2/NB1-SWE1D.ipynb'>nbviewer<a/>
* Using XBeach to analyse wave propagation &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session2/NB2-BeachProfileDefault.ipynb'>nbviewer<a/>
* Hands-on exercise with your own profile &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session2/NB3-myBeachProfile.ipynb'>nbviewer<a/>

### Session 3: Ocean circulation & wave propagation on real bathymetry

* Overview &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session3/Lecture-overview.ipynb'>nbviewer<a/>
* Shallow Water Equation 2D &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session3/NB1-SWE2D.ipynb'>nbviewer<a/>
* Sydney Coastal Region Bathymetry &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session3/NB2-BathymetryGen.ipynb'>nbviewer<a/>
* Coupled ocean circulation wave model on real topography &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session3/NB3-OceanSim.ipynb'>nbviewer<a/>
* Coupled ocean circulation wave model for Offshore Sydney &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/MARS5001/Modelling-session3/NB4-SydSim.ipynb'>nbviewer<a/>

# GEOS3102 lectures & practise material

### Sediment Geomorphology

* **Prac:** Exploring grain settling &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/SedimentGeomorphology/GrainSettling.ipynb'>nbviewer<a/>
* **Prac:** Global variation in submarine channel sinuosity  &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/SedimentGeomorphology/SubChannelSinuosity.ipynb'>nbviewer<a/>
* Diffusion equation in IPython &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/SedimentGeomorphology/DiffusionEq.ipynb'>nbviewer<a/>

### Well Analysis

* **Prac:** Digital Well Log Analysis &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/WellAnalysis/WellLogViewer.ipynb'>nbviewer<a/>
* Quantitative interpretation: Synthetic data from well log &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/WellAnalysis/SyntheticWell.ipynb'>nbviewer<a/>

### Seismic

* **Prac:** Read Seismic Line (SEG-Y) &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/Seismic/SEGYread.ipynb'>nbviewer<a/>
* **Prac:** Slice Seismic Volume &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/Seismic/SliceSeismic.ipynb'>nbviewer<a/>
* **Prac:** Synthetic Seismogram 1 &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/Seismic/SyntheticSeismogram.ipynb'>nbviewer<a/>
* **Prac:** Synthetic Seismogram 2 &mdash; <a href='http://nbviewer.ipython.org/github/t-salles/notebooks/blob/master/GEOS3102/Seismic/SeismicNMOapp.ipynb'>nbviewer<a/>

