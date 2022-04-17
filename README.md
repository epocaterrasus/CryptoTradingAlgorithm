# Crypto Price Forecasting Tool using Deep Learning <br/>

During this project, we aimed to explore the possibility of using deep learning to forecast future cryptocurrency token prices. We used technical analysis indicators as parameters to train and test the model, we started with over ninety different technical indicators and used correlation analysis and dimensionality reduction techniques to synthetize the information to get fewer inputs. Applying this procedure also helped us reduce model overfitting problems, achieving a better bias-variance trade-off. 

## Technologies

* Python
* Pandas
* hvPlot
* matplotlib
* numpy
* requests
* scikit-learn
* seaborn
* ta
* tensorflow
* vastAI

## Data

We acquired our data using the KuCoin API database to acquire Open, High, Low, Close and Volume Information for individual tokens. If you would like to learn more about this API please follow the following link: [KuCoin](https://docs.kucoin.com/ "KuCoin")

## Installation and User Guide

For you convenience, all necessary libraries are pre-installed in the Notebook, however if you wish to install them in your local machine you can run the following command:
```pip install requirements.txt```

### Download Repository

To download the project repository please run the following command in your GitBash window:
``` git clone https://github.com/epocaterrasus/CryptoTradingAlgorithm.git ```

### Launching the Application

To launch the application, run the following command in GitBash (inside the main folder of the repo).
```jupyter lab```

Locate the ```main_v2_vast.ipynb``` within Jupyter Lab and start exploring our project!

## What we want to figure it out?

* Can we generate alpha in cryptocurrency trading by using technical analysis indicators?
* Is the efficiency of using technical analysis higher in cryptocurrencies than in regular equities?
* Do we get better or worse results when analyzing established vs emerging tokens?
* Is there an inherent loop, meaning that in the absence of fundamental changes (upgrades to the chain i.e. proof of stake deployment in Ethereum) will the model continue to work indefinetely?

## Our process

* Outline - Identify goals, data sources and technologies to be used.
* Technical Analysis Indicators - Creating over ninety technical indicators using the TA library, for more information on the indicators and what they represent please visit [TA Library](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ "TA Library").
* Data Processing - Scaling, Dimensionality Reduction and Windowing.
* Model Creation - Secuential Model
* Tuning - Changing number of components, adjusting lookback window

## Model Summary

![image](https://user-images.githubusercontent.com/94983278/163725567-a98a7a8f-3081-4369-9ef2-810b48997886.png)


## Detailed Powerpoint/PDF of our Iterations in Creating and Adjusting the Model

### ReadMe file: <br/>
* check Project2_Readme.pdf or Project2_Readme.pptx (Project Introduction/Process/Model Result/ Requirements for running the model are included)<br/>
### Presentation file: <br/>
* Presentation_CUBtcamp_Project2_To the Moon LLC..pdf<br/>

## Contributors

Edgar Pocaterra 

Antonio Parolini

Michael Adut

Meina Bian

Maxwell Snyder

---

## License

MIT License

Copyright (c) 2022 epocaterrasus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.







