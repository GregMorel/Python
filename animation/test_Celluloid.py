#%%
from celluloid import Camera
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
from IPython.display import Video

plt.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg.exe' # si ffmpeg pas dans le PATH

colours=pl.cm.jet(np.linspace(0,1,500))
#Defining a colormap to pass to matplotlib's color parameter,
#just for aesthetics

def parametric_spiral(t,k=1):
    return (t)*np.cos((k*t)),(t)*np.sin((k*t))
#Defining the function we'll use
t_list=np.linspace(0,100)
#The values of t we'll graph over

fig, ax = plt.subplots(figsize=(4, 4))
#Set up our canvas-- we need to specify our figure size here

camera=Camera(fig)#Make a camera of the figure

for K in np.linspace(0,np.pi,500):
    #Our animation will have each frame be a different value of k from the list above    
    ax.plot(*parametric_spiral(t_list,k=K),c=colours[int(500*(np.pi-K)/np.pi)])
    #For a given value of k, we'll plot our function with that k-value   
    camera.snap()

animation=camera.animate();#Make the animation
plt.close() #Stop the empty plot from displaying
animation.save('spiral_animation.mp4',fps=500/45) #Save the animation-- notes below
Video("spiral_animation.mp4") #Show the video you've just saved
# %%
