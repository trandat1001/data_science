
## Predict server's bandwidth and number of users
### Problem:
A company providing entertainment platform that allows users to use music, video, live stream, chat services, etc. The company system is divided into zones according to geographical area. To meet the growing number of users, the company wants to predict the total bandwidth of each server and the maximum number of concurrent users accessing the server within the next month to plan operations.
See more detail on link: https://www.aivivn.com/contests/5
### Data Decription:
#### Training data
Training data (file train.csv) includes more than 35 thousand rowa. Here are the first five rows.

UPDATE_TIME, ZONE_CODE, HOUR_ID, BANDWIDTH_TOTAL, MAX_USER <br>
2017-10-01, ZONE01,0,16096.71031272728,212415.0 <br>
2017-10-01, ZONE01,1,9374.20790727273,166362.0 <br>
2017-10-01, ZONE01,2,5606,225750000003,146370.0 <br>
2017-10-01, ZONE01,3,4155.654660909094,141270.0 <br>
2017-10-01, ZONE01,4,3253.9785936363623,139689.0 <br>
..... <br>
**UPDATE_TIME**: execution date for retrieving data <br>
**HOUR_ID**: time to retrieve data <br>
**ZONE_CODE**: area code <br>
**BAND_WIDTH_TOTAL**: the total access bandwidth within 1 hour <br>
**MAX_USER**: maximum number of concurrent users within 1 hour (an interger number) <br>
#### Test data
Test data (file test.csv) includes 2227 rowws:

id, UPDATE_TIME, ZONE_CODE, HOUR_ID <br>
0.2019-03-10, ZONE01.0 <br>
1,2019-03-10, ZONE01,1 <br>
2,2019-03-10, ZONE01,2 <br>
3,2019-03-10, ZONE01,3 <br>
4,2019-03-10, ZONE01,4 <br>
5,2019-03-10, ZONE01,5 <br>
...<br>
In which **UPDATE_TIME**, **HOUR_ID**, **ZONE_CODE** are defined as above.
**id** is the corresponding code for the submission file. 
Teams need **BANDWIDTH_TOTAL**, and **MAX_USER** predictions for each row.
#### Final result
The required submission file is a .csv file similar to the sample_submission.csv file. For example:<br> 
id, label <br>
0 35.74 271 <br>
1 0.77 143 <br>
.... <br>
Note: 
**id** is the id column on test data above <br>
The first value of label is **BANDWIDTH_TOTAL** rounded to two decimal places, the second value is **MAX_USER**, a natural number. These two values are exactly one space apart. Note there are no spaces after the **MAX_USER** value

## Data analyst and pre-processing the dataset
Please see file: [analyze_and_visualization.ipynb](analyze_and_visualization.ipynb)

## Build predict model
This is regressor case, we can solve it by using these algorithms:
* Linear Regression, see file [linear_regression.ipynb](linear_regression.ipynb)
* KNN Regression, see file [knn_regression.ipynb](knn_regression.ipynb)
* Random Forest Regression, see file [random_forest.ipynb](random_forest.ipynb)
* SVM Regression, see file [svm_regression.ipynb](svm_regression.ipynb)

## Final Solution
Base on these algorithm above, we see the KNN Regression and Random Forest have high percent of accuracy. Therfore, we build some final solutions to predict maxUser and bandwidth.
* [solution_random_forest_independence_prediction.ipynb](solution_random_forest_independence_prediction.ipynb): Build seprate model to predict max user and bandwidth independently.
* [solution_random_forest_predict_one.ipynb](solution_random_forest_predict_one.ipynb): Build a model to predict max user and a model(+ maxUser column) to predict bandwidth.
* [solution_random_forest_relative_prediction](solution_random_forest_relative_prediction): Build a model to predict max user, then from maxuser we build a model to predict bandwidth.




```python

```
