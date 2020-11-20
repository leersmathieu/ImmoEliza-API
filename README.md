# ImmoEliza-API

API for ImmoEliza Project

Link to the challenge description :  [Here](https://github.com/becodeorg/CRL-Turing-4.22/blob/master/Projects/4.Prediction_api/README.md)

## Step to realise

### 1. Data cleaning

Normally, the first step would be to take a cleaned dataset and iron it to match our needs.  

But we preferred to start again from the uncleaned dataset to redo the cleaning from the beginning, this time directly for our prediction model.  
Since there are two usable raw datasets, we are going to exchange our data with another group and choose the most optimized one for our project.

We must therefore recover and clean the previously scrapped "ImmoCollect" dataset and compare its values with those of our colleague to then choose the most reliable one for our predictions.

## Realisation

### 1. Data cleaning

After recovering and cleaning the different dataset we were able to compare them.  

#### First dataset "ImmoCollect18"
   
Input : 18 0000 row  
Output : 11 000 row  

No missing values !

```
Prix                    int64
Type de propriété       int64
Bien neuf                bool
Code Postal             int64
Surface habitable       int64
Nombre de chambre(s)    int64
Jardin                   bool
Terrasse                 bool
```

Heatmap (correlation) 

![heatmap](./assets/hm1.png "heatmap du dataset ImmoCollect18")
