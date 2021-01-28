# LICENSE
#
# _This file is Copyright 2018 by the Image Processing and Analysis Group (BioImage Suite Team). Dept. of Radiology & Biomedical Imaging, Yale School of Medicine._
#
# BioImage Suite Web is licensed under the Apache License, Version 2.0 (the "License");
#
# - you may not use this software except in compliance with the License.
# - You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)
#
# __Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.__
#
# ENDLICENSE


#   imageSegmentation.py
#
#   Created on: Oct 6, 2020
#   Authors:   John Onofrey, An Qu, Xenophon Papademetris
#



import os
import sys
import json
import argparse



class imageSegmentation():

    def __init__(self):
        super().__init__();
        self.name='imageSegmentation';

    def createDescription(self):
        return {
            "name": "imageSegmentation",
            "description": "Image Segmentation(3D) Using Deep Learning Library MONAI.",
            "version": "1.0",
            "authors": "John Onofrey, An Qu, Xenophon Papademetris"
        }



    def jobFileExample(self, ex_type):
        if ex_type == 'full':
            example = """ {
                        "module" : "imageSegmentation",
                        "params" :
                        {
            		        "inputpath": "(string) path of input csv file. Three colums are required with the unchangable headers(top) , 'IMAGE', 'SEGM' and 'DATA_SPLIT'. 'IMAGE' and 'SEGM' colums should be filled with image and mask pathes. The 'DATA_SPLIT' colum should only contain 'Training', 'Validation' and 'Testing' keywords.",
                            "outputmodelpath": "(string) path of the output model folder.",
                            "cachepath": "(OPTINAL string) path of the data cache directory.",
                            "gpu_device": "(integer) the ID of GPU you want to use for the training/testing.",
                            "defaulttransformation":
                            {
        					  "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) Default preprocessing for the input training, validation and testing data, which includes 1)changing the input images' orientation into the specified direction, 2)resampling input images into the specified pixel dimenstion, and 3) applying intensity normalization to the input images. For the training images, a random crop function to extract random patches from the original images will be applied.",
        					  "orientation": "(OPTINAL string) reoriente images to the direction you specified here. Default to LPS.",
                              "patch_size": "(list of float number) the spatial size of the cropped patches.",
                              "spacing": "(list of float number) pixel dimension that is used to resample the input images."
                             },

                            "model":
                            {
                			  "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) Define a model for your training, validation and testing. For more information/options, please check MONAI Nets, https://docs.monai.io/en/latest/networks.html#nets.",
                			  "name": "(string) name of the network. Now only UNet3d is available. For more information/options, please check MOONAI UNet, https://docs.monai.io/en/latest/networks.html#monai.networks.nets.UNet",
                			  "in_channels": "(OPTIONAL integer) number of input channels.",
                			  "out_channels": "(OPTIONAL integer) number of output channels.",
                              "normalization": "(OPTIONAL string) Feature normalization type and arguments. Defaults to BATCH",
                              "num_res_units": "(OPTIONAL integer) Number of residual units. Defaults to 2",
                              "strides": "(OPTIONAL list of integer) convolution stride.",
                			  "channels": "(OPTIONAL list of integer) sequence of channels. TOP block first.",
                			  "lossfunction":
                              {
                        		  "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(OPTIONAL dictionary) The loss function you choose for your model. Default to MONAI DiceLoss function and the example usage is shown as below. For more informatin/options, please check MONAI Segmentation Losses, https://docs.monai.io/en/latest/losses.html#module-monai.losses.",
    	                          "functionname": "(string) Function name is required if you specified a loss function.",
                        		  "to_onehot_y": "(OPTIONAL) Please check the MONAI Loss Function document and the defination of each parameter. Parameters not specified will use the default value in the document.",
                        		  "softmax": "(OPTIONAL) Please check the MONAI Loss Function document and the defination of each parameter. Parameters not specified will use the default value in the document."
                              },
                			  "optimfunction":
                              {
    	 		                  "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(OPTIONAL dictionary) The optimizer you choose for your model. Default to torch.optim.Adam. For more informatin/options, please check TORCH.OPTIM, https://pytorch.org/docs/stable/optim.html#module-torch.optim."
                    	  	  }
                            },
                            "train":
                            {
                			  "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) functions and parameters for your training procedure. If the key 'train' is specified in the 'params' dict, the module will perform the training procedure with the model you specified above. For more information, please check PyTorch Lightning Trainer, https://pytorch-lightning.readthedocs.io/en/latest/trainer.html#trainer.",
                			  "augmentation":
                              {
            					   "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(OPTINAL dictionary) Augmentation you want to apply on your training data. Below is an example of adding rotation augmentation for the training data. For more information/options, please check MONAI Dictionary Transformation, https://pytorch.org/docs/stable/optim.html#module-torch.optim.",
            					   "RandRotated":
                                   {
        							  "keys":"(OPTINAL list of string) Define whether the images or the segmentations you want to apply this augmenation. Or for both. Default to ['IMAGE', 'SEGM']",
        			                  "range_x":"(OPTIONAL) Please check the transformations and the defination of each parameter. Parameters not specified will use the default value in the document",
        							  "range_y":"(OPTIONAL) Please check the transformations and the defination of each parameter. Parameters not specified will use the default value in the document",
        							  "range_z":"(OPTIONAL) Please check the transformations and the defination of each parameter. Parameters not specified will use the default value in the document",
        							  "prob":"(OPTIONAL) Please check the transformations and the defination of each parameter. Parameters not specified will use the default value in the document"
                                    }
                              },
                                 "max_epochs": "(OPTIONAL integer) Stop training once this number of epochs is reached. Default to 2000.",
                                 "check_val_every_n_epoch": "(OPTIONAL integer) Check validation every n train epochs. Default to 10.",
                                 "batch_size": "(OPTIONAL integer) The number of training examples per batch to load. Default to 16."
                            },
                            "test":
                            {
                    		   "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) functions and parameters for your testing procedure. If the key 'test' is specified in the 'params' dict, the module will perform the testing procedure on your testing data with the model you specified above.",
                    		   "augmentation":
                               {
        					       "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(OPTINAL dictionary) Augmentation you want to apply on your testing data, such as padding, crop and ect. For more information, please check MONAI Dictionary Transforms, https://docs.monai.io/en/latest/transforms.html#dictionary-transforms"
                    		   },
                			   "batch_size": "(OPTIONAL integer) The number of testing examples per batch to load. Default to 1.",
                               "postprocessing": "(OPTIONAL boolean) Whether or not to perform post processing function(MONAI KeepLargestConnectedComponent, https://docs.monai.io/en/latest/transforms.html#keeplargestconnectedcomponent). Default to true."
                    	       }
                            }
                      }"""

        elif ex_type == "short":

            example = """{
               "module" : "imageSegmentation",
               "params" :
               {
                   "inputpath": "(string) path of input csv file. Three colums are required with the unchangable headers(top) , 'IMAGE', 'SEGM' and 'DATA_SPLIT'. 'IMAGE' and 'SEGM' colums should be filled with image and mask pathes. The 'DATA_SPLIT' colum should only contain 'Training', 'Validation' and 'Testing' keywords.",
                   "outputmodelpath": "(string) path of the output model folder.",
                   "gpu_device": "(integer) the ID of GPU you want to use for the training/testing.",
                   "defaulttransformation":
                   {
        	   	      "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) Default preprocessing for the input training, validation and testing data, which includes 1)changing the input images' orientation into the specified direction, 2)resampling input images into the specified pixel dimenstion, and 3) applying intensity normalization to the input images. For the training images, a random crop function to extract random patches from the original images will be applied.",
                      "patch_size": "(list of float number) the spatial size of the cropped patches.",
                      "spacing": "(list of float number) pixel dimension that is used to resample the input images."
                   },
                   "model":
                   {
                      "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) Define a model for your training, validation and testing. For more information/options, please check MONAI Nets, https://docs.monai.io/en/latest/networks.html#nets.",
                	  "name": "(string) name of the network. Now only UNet3d is available. For more information/options, please check MOONAI UNet, https://docs.monai.io/en/latest/networks.html#monai.networks.nets.UNet"
                   },
                   "train":
                   {
                      "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) functions and parameters for your training procedure. If the key 'train' is specified in the params, the module will perform the training procedure with the model you specified above. For more information, please check PyTorch Lightning, https://pytorch-lightning.readthedocs.io/en/latest/trainer.html#trainer."
                   },
                   "test":
                   {
                      "DESCRIPTION-DO-NOT-INCLUDE-IN-JOBFILE": "(dictionary) functions and parameters for your testing procedure. If the key 'test' is specified in the params, the module will perform the testing procedure on your testing data with the model you specified above."
                   }
                }
            }"""

        else:
            print("Please specify 'full' or 'short' after the showexample flag.")
            print("Short example will only display the minimum required parameters in the jobfile.")
            return


        example_json = json.dumps(json.loads(example), indent=4)
        print(example_json)



    def invokeAlgorithm(self,vals, imgSegm):

        if vals.showexample:
            self.jobFileExample(vals.showexample)
            return True

        else:
            try:
                with open(vals.jobfile) as jf:
                    jfile = json.load(jf)
                    if jfile['module'] != self.name:
                        print ("Double check if the module name of the jobfile corrects!")
                        raise ValueError
            except:
                e = sys.exc_info()[0]
                print('---- Failed to load the jobfile ----',e);
                return False

            try:
                imgSegm.imageSegmentation(jfile['params'], vals.debug)

            except:
                e = sys.exc_info()[0]
                print('---- Failed to invoke algorithm ----',e);
                return False


            return True




def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')





def main():

    import bisImgSeg.utilities.imgSegm as imgSegm;


    parser = argparse.ArgumentParser(
        description = 'Image Segmentation(3D) Using Deep Learning Library MONAI.'
    )

    parser.add_argument('-jf', '--jobfile', help='User-defined parameter file of deep learning.')
    parser.add_argument('--debug', help='Toggles debug logging.', default=True, type=str2bool)
    parser.add_argument('--showexample', help='(optional) Produce an example input jobfile. \
                         Please specify either full or short after this flag. \
                         Short example will only display the minimum required parameters in the jobfile.')

    args = parser.parse_args()

    anisc = imageSegmentation()
    anisc.invokeAlgorithm(args, imgSegm)




if __name__ == '__main__':

    my_path=os.path.dirname(os.path.realpath(__file__));
    # Make sure bisImgSeg is in your path
    n=os.path.abspath(my_path+'/..')
    sys.path.insert(0,n);

    main()
