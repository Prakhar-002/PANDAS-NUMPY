
#? WHAT IS PANDAS

#* Pandas is an open source data analysis library written in python

#* It leverages the power and speed of numpy to make data analysis and preprocessing easy for data scientists

#* It provides rich and highly robust data operations


#? PANDAS DATA STRUCTURE

""" 
Pandas has two types of data structures:

• a) Series — It's a one dimensional array with indexes, it stores a single column or row of data in a Dataframe

• b) Dataframe — It's a tabular spreadsheet like structure representing rows each of which contains one or multiple columns

A one-dimensional array(labeled) capable Of holding any type Of data— Series

A two-dimensional data (labeled) structure with columns of potentially different types of data - DataFrame
"""


#!----------------------------------------- 

#? JUPYTER NOTEBOOK

"""
• The Jupyter Notebook is an open-source web application that allows you to create
and share documents that contain live code, equations, visualizations and narrative
text.

• The Notebook has support for over 40 programming languages, including Python, R,
Julia. and Scala.

• Notebooks can be shared with others using email, Dropbox, GitHub and the Jupyger
Notebook Viewer.

• Your code can produce rich, interactive output: HTML, images, videos, LaTeX, and
custom MIME types.
"""


import pandas as pd
import numpy as np 

ser = pd.Series(np.random.rand(10))

print(ser) #* one dim array of random num

print(type(ser)) #* <class 'pandas.core.series.Series'>

"""
0    0.334642
1    0.485808
2    0.347748
3    0.653292
4    0.620390
5    0.955707
6    0.175644
7    0.026256
8    0.544996
9    0.465944
dtype: float64
"""

new_df = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334)) 

print(new_df.head(5))

"""
      0         1         2         3         4
0  0.701935  0.862503  0.330369  0.514057  0.921794
1  0.584902  0.557335  0.776350  0.062654  0.100291
2  0.028153  0.392451  0.849276  0.734145  0.601189
3  0.379644  0.040674  0.774293  0.331304  0.544946
4  0.099819  0.787814  0.735571  0.727910  0.161975
"""

print(type(new_df)) #* <class 'pandas.core.frame.DataFrame'>

print(new_df.describe())

"""

            0               1  ...           3           4
count  334.000000  334.000000  ...  334.000000  334.000000      
mean     0.498410    0.480881  ...    0.518987    0.482112      
std      0.283619    0.287988  ...    0.291884    0.299845      
min      0.013866    0.002922  ...    0.008859    0.001332      
25%      0.256254    0.247529  ...    0.288658    0.203750      
50%      0.494313    0.447008  ...    0.527035    0.456477      
75%      0.740788    0.729924  ...    0.775705    0.739666      
max      0.993021    0.998259  ...    0.995475    0.996945      

[8 rows x 5 columns]
"""

print(new_df.index) #* Give all indexes

"""
Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
       ...
       324, 325, 326, 327, 328, 329, 330, 331, 332, 333],       
      dtype='int64', length=334)
"""

print(new_df.columns) #* RangeIndex(start=0, stop=5, step=1)

print(new_df.to_numpy) #* Convert it into numpy

"""
<bound method DataFrame.to_numpy of            
            0         1         2         3         4
0    0.953662  0.082791  0.118658  0.906491  0.732316
1    0.504137  0.618579  0.547893  0.470372  0.853628
2    0.180120  0.194004  0.110749  0.642041  0.439867
3    0.541882  0.639145  0.843326  0.563375  0.554818
4    0.420927  0.400223  0.918987  0.068785  0.870360
..        ...       ...       ...       ...       ...
329  0.688209  0.097015  0.853687  0.819691  0.452312
330  0.224869  0.154175  0.291139  0.288598  0.085196
331  0.640813  0.589281  0.412271  0.401171  0.866458
332  0.518416  0.678775  0.407671  0.211345  0.371296
333  0.643833  0.109395  0.237993  0.444614  0.230895

[334 rows x 5 columns]>
"""

print(new_df.sort_index(axis=1, ascending=False))

"""
            4         3         2         1         0
0    0.591026  0.350008  0.294658  0.700453  0.052283
1    0.741663  0.901411  0.023460  0.404007  0.893294
2    0.014126  0.436194  0.354126  0.348350  0.284576
3    0.768252  0.689839  0.896475  0.865617  0.491340
4    0.796995  0.383001  0.573390  0.612866  0.705167
..        ...       ...       ...       ...       ...
329  0.099300  0.108627  0.831903  0.060863  0.009594
330  0.735754  0.836353  0.708693  0.369438  0.045193
331  0.039889  0.884366  0.907489  0.687140  0.621234
332  0.227907  0.003836  0.952075  0.701316  0.167459
333  0.642643  0.530170  0.695468  0.582298  0.198616

[334 rows x 5 columns]
"""

new_df_view = new_df  #* change in view will effect original too

new_df_copy = new_df.copy() #* Create a copy of 

#!---------------------------------------------------------------------------------

#? Updating dataframe

new_df.loc[0, 0] = 452

print(new_df.head())

"""
            0         1         2         3         4
0  452.000000  0.318647  0.749283  0.497287  0.939965
1    0.974439  0.340900  0.858901  0.147286  0.936594
2    0.396198  0.284039  0.889474  0.953356  0.223671
3    0.092456  0.682895  0.968252  0.530525  0.493377
4    0.735236  0.612460  0.008840  0.823664  0.569608

"""
new_df.columns = list("ABCDE")

print(new_df.head())

"""
            A         B         C         D         E
0  452.000000  0.448559  0.776770  0.967850  0.620384
1    0.572211  0.002564  0.877975  0.817600  0.583272
2    0.140359  0.636161  0.471139  0.540216  0.932550
3    0.173522  0.073332  0.864767  0.164196  0.508074
4    0.502390  0.310478  0.989604  0.406777  0.473277
"""

new_df.loc[0, "B"] = 2

print(new_df.head())

"""
            A         B         C         D         E
0  452.000000  2.000000  0.550963  0.622829  0.541868
1    0.564080  0.150106  0.003533  0.290057  0.340008
2    0.263181  0.923126  0.148388  0.289850  0.957182
3    0.834313  0.062927  0.053419  0.897478  0.704399
4    0.236601  0.083916  0.980036  0.858017  0.267479
"""

new_df.loc[0, 0] = 12 

print(new_df.head())

"""
            A         B         C         D         E     0     
0  452.000000  2.000000  0.843355  0.650252  0.471714  12.0     
1    0.467215  0.911697  0.599272  0.587906  0.798616   NaN     
2    0.438476  0.364233  0.073672  0.732810  0.436846   NaN     
3    0.296671  0.793247  0.451116  0.403749  0.675200   NaN     
4    0.821624  0.459104  0.375803  0.817546  0.262093   NaN     
"""

new_df.drop(0, axis=1)

print(new_df.head())

"""
            A         B         C         D         E
0  452.000000  2.000000  0.860945  0.394233  0.907775
1    0.417586  0.029887  0.761005  0.990832  0.926859
2    0.802681  0.820617  0.283442  0.872386  0.638927
3    0.365042  0.840169  0.547410  0.018415  0.728075
4    0.594464  0.277047  0.430595  0.990842  0.499272
"""

print(new_df.loc[[1, 2], ['C', 'D']]) #* return view of these

"""
      C         D
1  0.344145  0.303900
2  0.259340  0.395185
"""

print(new_df.loc[[1, 2], :])  #* Return two row and all columns

"""
      A           B         C         D         E
1  0.915948  0.832512  0.323910  0.356876  0.614985
2  0.443888  0.337708  0.624149  0.261256  0.032540
"""

#!------------------------------------------------------------------------------

print(new_df.loc[(new_df['A']<0.1) & (new_df['C']>0.9)])

"""
            A         B         C         D         E
146  0.014772  0.847636  0.999770  0.411269  0.605346
298  0.064141  0.809339  0.983445  0.743342  0.511777
328  0.035381  0.696177  0.963905  0.981965  0.904004
"""

print(new_df.iloc[0, 0]) #* 452.0 (indexes value)

print(new_df.drop([2]).head()) #* Drop one Row

"""
            A         B         C         D         E
0  452.000000  2.000000  0.084667  0.253922  0.056049
1    0.311402  0.888370  0.385811  0.598123  0.731200
3    0.074488  0.500755  0.695989  0.676369  0.243483
4    0.920726  0.313844  0.319068  0.102468  0.923880
5    0.617580  0.550209  0.292646  0.110617  0.912574
"""

print(new_df.drop(['A'], axis=1)) #* Drop one column

"""
            B         C         D         E
0    2.000000  0.084667  0.253922  0.056049
1    0.888370  0.385811  0.598123  0.731200
2    0.092194  0.895521  0.348507  0.325791
3    0.500755  0.695989  0.676369  0.243483
4    0.313844  0.319068  0.102468  0.923880
"""

new_df.drop(['B', 'E'], axis=1, inplace=True) #* change in original df

new_df.drop([1, 3], axis=0, inplace=True) #* change in original df

print(new_df.head())

"""
            A         C         D
0  452.000000  0.889690  0.906158
2    0.059090  0.892896  0.581937
4    0.136717  0.337648  0.749829
5    0.624124  0.951755  0.953244
6    0.514848  0.319055  0.403498
"""

new_df.reset_index() #* Reset all index but add one index column

new_df.reset_index(drop=True) #* Reset index but no index column is created

new_df.reset_index(drop=True, inplace=True) #* Reset index and also change in original array

print(new_df.head())

"""
            A         C         D
0  452.000000  0.669383  0.896629
1    0.645785  0.692094  0.410193
2    0.107226  0.970682  0.363829
3    0.103506  0.488351  0.941832
4    0.663168  0.452766  0.891851
"""

new_df.loc[:, ['C']] = 23

print(new_df.head())

"""
            A     C         D
0  452.000000  23.0  0.628445
1    0.382378  23.0  0.751719
2    0.318183  23.0  0.458378
3    0.296166  23.0  0.043557
4    0.406131  23.0  0.912522
"""