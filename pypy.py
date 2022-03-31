import numpy as np
import pandas as pd
import array
import matplotlib.pyplot as plt
df= pd.read_csv(
    'earthquakes.csv'    
)

print(
df.loc[
 df.mag.between(6.5, 7.5),
 ['alert', 'mag', 'magType','place' , 'tsunami', 'type']
 ]
)

df1 = df[df['title'].str.contains("Peru")]
print(
df1.loc[
      df1.mag.between(4,10),
      ['place','alert', 'mag', 'magType', 'place', 'tsunami', 'type']
        ]
)

print(
df.loc[
(df.place.str.contains(r'PE|Peru$'))
 & (df.mag > 3.8),
 ['alert', 'mag', 'magType', 'title', 'tsunami', 'type']
 ]
      )
plt.plot(df1.mag, df1.place)
plt.legend(('X'),loc='best')
#plt.xlabel(df1.mag,"MAGNITUD",fontsize='13')	#adds a label in the x axis
#plt.ylabel(df1.place,"Lugar",fontsize='13')
plt.show()

