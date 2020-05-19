# TIEF AI Library

TIEF.ai is an AI library for research and study purpose. This library is very easy to use. If you found some lack of performance or some issues, just tell me. I'll upgrade it as soon as possible.

## Features

Dillinger uses a number of open source projects to work properly:

* [Association Rule] - a rule-based machine learning method for discovering interesting relations between variables
* [KNN, etc] - Coming Soon!

### Installation
TIEF AI requires [Python](https://www.python.org/downloads/) v3.6+ to run. Make sure you already installed python.
Now install 

## Association Rule
a rule-based machine learning method for discovering interesting relations between variables


### Usage
Make sure you already installed python and tief library. Now import association rule module


```python
from tief.association import apriori
from tief.association import association_rule
```

This is an example of data transaction. Data should contain list of list of string like example below.


```python
data = [
    ["bread", "jam", "butter"],
    ["bread", "butter"],
    ["bread", "milk", "butter"],
    ["chocolate", "bread", "milk", "butter"],
    ["chocolate", "milk"]
]
```

Now we called apriori module to get apriori itemset with each support values.


```python
apriori_df = apriori(data, min_support=0.3)
apriori_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ItemSet</th>
      <th>Count</th>
      <th>Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>[bread]</td>
      <td>4</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>1</td>
      <td>[milk]</td>
      <td>3</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>2</td>
      <td>[butter]</td>
      <td>4</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>3</td>
      <td>[chocolate]</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>[bread, milk]</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>5</td>
      <td>[bread, butter]</td>
      <td>4</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>6</td>
      <td>[milk, butter]</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>7</td>
      <td>[milk, chocolate]</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>8</td>
      <td>[bread, milk, butter]</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
  </tbody>
</table>
</div>



Before we called association_rule module, we must convert apriori itemset column into list


```python
itemset = apriori_df['ItemSet'].tolist()
conf_df = association_rule(itemset, min_confidence=0.8)
conf_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Notasi</th>
      <th>Antecedent</th>
      <th>Consequents</th>
      <th>Antecedent Support</th>
      <th>Consequents Support</th>
      <th>Confidence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>['bread'] --&gt; ['butter']</td>
      <td>[bread]</td>
      <td>[butter]</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>['butter'] --&gt; ['bread']</td>
      <td>[butter]</td>
      <td>[bread]</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>['chocolate'] --&gt; ['milk']</td>
      <td>[chocolate]</td>
      <td>[milk]</td>
      <td>0.4</td>
      <td>0.6</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>['bread', 'milk'] --&gt; ['butter']</td>
      <td>[bread, milk]</td>
      <td>[butter]</td>
      <td>0.4</td>
      <td>0.8</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>['milk', 'butter'] --&gt; ['bread']</td>
      <td>[milk, butter]</td>
      <td>[bread]</td>
      <td>0.4</td>
      <td>0.8</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



License
----

MIT


**Lest Rock!**


```python

```
