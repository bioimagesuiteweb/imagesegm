<h1> BioImage Suite Web Image Segmentation</h1>
<p>Deep learning based image segmentation based on PyTorch. </p>

<p><I>NOTE: the current version of this repository can only work with 3D images. More features will be available in the future.</I> </p>




<h3>PREREQUISITE</h3>


<h4>System Requirements:</h4>
<li>CUDA-capable GPU</li>
<li><a href="https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html ">NVIDIA CUDA </a></li>
<li> <a href="https://developer.nvidia.com/CUDA-toolkit">NVIDIA CUDA Toolkit</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html">NVIDIA cuDNN</a></li>


<h4>Software Requirement:</h4>
<p><b>NOTE: </b> In order to avoid version conflicts among the packages, we recommend to run this project in Anaconda virtual environemnt. Please check the <a href="https://docs.anaconda.com/anaconda/install/"> Anaconda Installation Webpage</a> for more information.</p>
<li>python>=3.6</li> 
<li><a href="https://docs.monai.io/en/latest/installation.html">MONAI=0.3.0rc4</a></li>
<li>pytorch-lightning=0.9.0</li>
<li>nibabel</li> 
<li>pandas</li> 
<li>scikit-image</li>


<h4>Tested Environment:</h4>
<p>This package has been tested with:</p>
<li>GPU Name: Quadro K1200</li>
<li>NVIDIA CUDA Version: 10.2.89</li>
<li>python=3.7.9</li>
<li>MONAI=0.3.0rc4</li>
<li>pytorch-lightning=0.9.0</li>
<li>nibabel=3.1.1</li> 
<li>pandas=1.1.2</li> 
<li>scikit-image=0.17.2</li>


 <I><b>Example Commands:</b></I>
 <p>Once the Anaconda is installed, you can follow the steps below to install all the necessary softwares:</p>
 <p>Create a virtual environment with python package with version=3.7.9: </p>
<code>
conda create -n yourVirEnvName python=3.7.9
</code>
<p>Install MONAI library with version=0.3.0rc4</p>
<code>
pip3 install monai==0.3.0rc4
</code>
<p>Install pytorch-lightning library with version=0.9.0</p>
<code>
pip3 install pytorch-lightning==0.9.0
</code>
<p>Install pandas, nibabel and scikit-image libraries.</p>
<code>
pip3 install pandas nibabel scikit-image
</code>




<h3>HOW TO USE IT</h3>
<b>1. Clone the biswebMonaiSegm repository</b>
<p>Go to any folder you like and clone this repository using the command below:</p>
<code>
git clone git@github.com:bioimagesuiteweb/imagesegm.git
</code>

<b>2. Prepare the input parameter file</b>
<p>Go to <samp>imagesegm/bisImgSeg</samp> subfolder:</p>
<code>
cd imagesegm/bisImgSeg
</code>
<p>Check the help message:</p>
<code>
python3 biswebMonaiSegm.py -h
</code>

<p>In the help message, only <samp>--jobfile</samp> is necessarily required. For detailed information of how to create a jobfile, you can use the command below:</p>
<code>
python3 biswebMonaiSegm.py --showexample full(or short)
</code>

<p>You can also check the jobFileExample.json in the <samp>imagesegm</samp> folder for reference and design it as you need by following the requirements in the <samp>--showexample</samp> flag.</p>
<p>Regarding the <samp>--debug</samp> flag, it is defaultly set as True and will print the logging messages during the learning/predicting process. You can turn it off by specifying False after this flag.</p>

<b>3. Monitor the learning process</b>
<p>You can monitor the learning process by using TensorBorad application:</p>
<code>
tensorboard --logdir outputmodelpath
</code>

<p>Where the <samp>outputmodelpath</samp> should be specified in your jobfile. Then search <samp>http://localhost:6006/</samp> in your browser. You will see the statistics and visualizations in this webpage. For more information on Tensorboard, please check <a href="https://github.com/tensorflow/tensorboard">Tensorboard github.</a> </p>

<b>Results</b>
<p>The trained model can be found in <samp>outputmodelpath/saved_model/</samp>, where the <samp>outputmodelpath<samp> should be specified in your jobfile. </p>
<p>The segmented results can be found in <samp>outputmodelpath/results/.</samp></p>
