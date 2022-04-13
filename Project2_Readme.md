

Readme

Crypto Price Discovery Tool

Antonio Parolini,

Edgar Pocaterra,

Meina Bian,

CU ArgoML Project 2

Major Procedure and NN

showcase case(window=

5,7,8,15,20)

Michael Adut,

Maxwell Snyder





Main Process

Alpacha API,

• Close price(Decide for Crypto), 92 Technical Indicators;

• <https://alpaca.markets/>

• API for Stock and Crypto Trading

Apply PCA for feature deduction

• identify the underlying dependencies of a dataset and to reduce its dimensionality

significantly attending to them.

• This technique is beneficial for processing data sets with hundreds of variables while

maintaining, at the same time, most of the information from the original data set.

• Once we have selected the principal components, the data must be projected onto them.

A projection for one dimension

• The final reduced dataset will explain certain of the variance of the original one

Build the Neural Network Model

• Two Hidden Layers





Process 1 PCA

•**Features dimensionality deduction**

**through standardization.**

•**PCA analysis which suggested using K=3**

**for the # of primary components**

•**Trans\_fit feature data matrix to 3**

**Features Data for building the model**

• Standardize the data (Center and scale).

Standardize

• Calculate the Eigenvectors and Eigenvalues from the covariance matrix or correlation matrix (One could also use

Singular Vector Decomposition).

Calculate

• Sort the Eigenvalues in descending order and choose the K largest Eigenvectors (Where K is the desired number of

dimensions of the new feature subspace k ≤ d). (In our case K=3)

Sort

• Construct the projection matrix W from the selected K Eigenvectors.

Construct

Transform





Alternative to PCA

Process CNN

Applying CNNs to a univariate 1D time series Data:

•1) Import Keras libraries and dependencies

•2) Define a function that extracts features and outputs from the sequence.

•3) Reshape the input X in a format that is acceptable to CNN models

•4) Design the CNN model architecture of convolutional layers

•5)Train the model and test it on our univariate sequence.

•(Conv-1D),

•pooling(max-pooling in our case ),

•flattening layer

•fully connected neural layers.

Primary components of a Deep CNN model for time series forecasting. The primary layers of an ordinary CNN model.

•1. Convolutional Layer

•2. Pooling Layer

•3. Fully Connected Layer

CNN vs RNN

•CNNs are **computationally cheaper** than RNNs: CNN learns by batch while RNNs train sequentially. As such, RNN can’t use parallelization because it must wait

for the previous computations.

•CNNs don’t have the assumption that history is complete: Unlike RNNs, CNNs learn patterns within the time window. If you have**missing data, CNNs should be**

**useful**.

•CNNs can look forward: RNN models only learn from data before the timestep it needs to predict.**CNNs (with shuffling) can see data** from a broader

perspective.

•More active research in CNN: there are some arguments that **RNN / LSTM is becoming irrelevant**. Whether it’s true or not, I think it depends on how we look at

it.





MLP

**Metric** for optimality criterion

Neural Networks & Statistics,

Minimize mean squared error (MSE).

Model **Performance Tuning:**

Reduce Overfitting With Dropout

Accelerate Training With Batch Normalization

Halt Training, Early Stopping,

• monitor the loss on the training dataset a validation dataset ( a subset training set, not used to fit the

model).

• as loss for the validation set starts to show signs of overfitting, the training process can be stopped.





Requirement for

main.v2

vast ai (GPU)version

hvplot==0.7.3

matplotlib==3.5.0

numpy==1.20.3

pandas==1.3.4

requests==2.26.0

scikit-learn==1.0.1

seaborn==0.11.2

ta==0.9.0

tensorflow==2.8.0





Requirement for

main.v3

jupyter notebook version

jupyter core : 4.6.3

jupyter-notebook : 5.7.11

qtconsole

ipython

: 5.2.2

: 7.18.1

: 5.3.4

ipykernel

jupyter client : 6.1.7

jupyter lab

nbconvert

ipywidgets

nbformat

traitlets

: not installed

: 5.6.1

: 7.6.5

: 5.1.3

: 5.0.5

\*all module version check file

"requirement\_jupyter.txt" as is shown in the right





Metric Mse

frequently adopted optimality criterion, in both the

neural networks and the statistics communities, is

minimizing the mean squared error (MSE).

Model

Summary

**Model**

**PCA**

**NN WINDOW(step)**

**MSE**

**Overfit**

**(Loss Figure)**

nn1\_5

nn1\_7

nn1\_8

nn1\_13

nn1\_15

nn1\_20

3

3

3

3

3

3

5

7

1764.1593

1588.5481

2178.061

2159.9355

3100.3516

3095.867

No

No

No

8

13

15

20

Yes(tail/verysmall)

YES(tail/small)

No





•

1588.5481





•

•





•





•





•

