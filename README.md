[//]: # (Image References)

<!--[image1]: ./images/skin_disease_classes.png "Skin Disease Classes"-->
[image1]: ./images/index.png "Lesion Images"

# [Discontinued] Dermatologist AI

![Lesion Images][image1]

## Overview / Usage

Skin cancer is a major public health problem, with over 5 million newly diagnosed cases in the US each year. [Melanoma](http://www.skincancer.org/skin-cancer-information/melanoma), is responsible for over 9,000 deaths each year.
As pigmented lesions occuring on the surface of the skin, melanoma is amenable to early detection by expter visual inspection. It is also amenable to automated detection with images analysis. Given the widespread of high-resolution cameras, algorithms that can improve our ability to screen and detect troublsome lesions, can be of great value. [ISIC]

This project is a deep learning model that aims to visually diagnose melanoma, the deadliest form of skin cancer. In particular, the algorithm will distinguish this malignant skin tumor from two types of benign lesions ([nevi](http://missinglink.ucsf.edu/lm/dermatologyglossary/nevus.html) and [seborrheic keratoses](https://www.aad.org/public/diseases/bumps-and-growths/seborrheic-keratoses)).

The problem being addressed here apart from visually dignosing the malignant skin tumor is, trying to come up with a noninvasive, easy to use system that can be used by actual dermatologists in their work. It's also meant to reduce miss-classification of lesions and diagnosis time.

## Methodology / Approach

### Methodology and Architecture

1. Dataset. The data and objective are pulled from the [2017 ISIC Challenge on Skin Lesion Analysis Towards Melanoma Detection](https://challenge.kitware.com/#challenge/583f126bcad3a51cc66c8d9a).  As part of the challenge, participants were tasked to design an algorithm to diagnose skin lesion images as one of three different skin diseases (melanoma, nevus, or seborrheic keratosis).

2. Architecture. The project uses the pre-trained DenseNet201 network with the classifier linear layer output being set to 3, to represent the three classes of this task. This network was chosen due to its physical smaller size, allowing it to be efficiently packaged into a mobile application. Testing has not yet been done, but through quantization, this task can be made more efficient.

3. Back-end Framework. PyTorch.

4. Loss and Accuracy. These were the two metrics chosen to monitor how well the model was training, and how well it performed on the test data. It was able to achieve a test loss of 1.207794 and an accuracy of 46%, which  was 160 images correctly classified over the total 347 images in the testing set. This should improve with time.

### Approach

1. The dataset was split into test, train and valid sets, with a total of ~2,000 combined. Each dataset contained the malignant skin tumour, melanoma, and the two forms of benign lesions, nevus and seborrheic keratosis.

2. Only two forms of transforms were perfomed on the images. Center Cropping and Transforming to Tensors.

3. Cross Entropy Loss was used since this task is a classification task, together with Stocastic Gradient Descent (SGD) as an optimizer.

4. All training was done on CPU.

## Technologies Used

### Hardware

1. Intel® Core™ i5-3320M CPU @ 2.60GHz × 4  Processor

2. Intel® Ivybridge Mobile Graphics

### Software and Libraries

1. Ubuntu 18.04.3 LTS

2. Python 3.6.9

3. Power by the PyTorch Deep Learning Framework
