import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood_data = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_data = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#Inspect
print(wood_data.head())
print(steel_data.head())



# write function to plot rankings over time for 1 roller coaster here:
plt.close('all')
def ranking_over_time(coastername, parkname, df):
  data = df[(df['Name'] == coastername) & (df['Park'] == parkname)]
  y_data = data['Rank']
  x_data = data['Year of Rank']
  plt.plot(x_data, y_data)
  plt.xlabel('Year of rank')
  plt.ylabel('Rank')
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.show()

ranking_over_time('El Toro', 'Six Flags Great Adventure', wood_data)

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_coaster_ranking(coaster1, park1, coaster2, park2,
df):
  coaster1_data = df[(df['Name'] == coaster1) & (df['Park']
== park1)]
  coaster2_data = df[(df['Name'] == coaster2) & (df['Park']
== park2)]
  xdata = ['2013', '2014', '2015','2016','2017','2018']
  coaster1_rankings = coaster1_data['Rank']
  coaster2_rankings = coaster2_data['Rank']
  plt.plot(xdata, coaster1_rankings)
  plt.plot(xdata, coaster2_rankings)
  plt.xlabel('Year of rank')
  plt.ylabel('Rank')
  plt.legend([coaster1, coaster2])
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.show()

two_coaster_ranking('El Toro', 'Six Flags Great Adventure',
'Boulder Dash', 'Lake Compounce', wood_data)

plt.clf()

# write function to plot top n rankings over time here:

def top_ranked_coasters(n, df):
  coasterdata = df[df['Rank'] <= n]
  print(coasterdata)
  plt.figure()
  ax = plt.subplot()
  for coaster in set(coasterdata['Name']): #creates a unordered list, need to use in because python sets have no indices
    rank = coasterdata[coasterdata['Name'] == coaster]
    ax.plot(rank['Year of Rank'], rank['Rank'], label=coaster)
  plt.show()
  
top_ranked_coasters(10, steel_data)

plt.clf()

# load roller coaster data here:
captain_data = pd.read_csv('roller_coasters.csv')
print(captain_data.head())


# write function to plot histogram of column values here:
def hist_of_column(col_name, df):
  data = df[col_name]
  data_not_null = pd.notnull(df[col_name])
  print(data[data_not_null])
  plt.hist(data[data_not_null])
  plt.ylabel('Count')
  plt.xlabel('Speed (km/h)')
  plt.show()

hist_of_column('speed', captain_data)

plt.clf()

# write function to plot inversions by coaster at a park here:

def num_inversions(parkname, df):
  coasterdata = df[df['park'] == parkname]
  coasterdata = coasterdata.sort_values('num_inversions', ascending=False)
  coaster_names = coasterdata['name']
  number_inversion = coasterdata['num_inversions']
  xpos = list(range(len(coaster_names)))
  plt.bar(xpos, number_inversion, 1, tick_label=coaster_names)
  plt.xlabel('Name of coaster')
  plt.ylabel('Number of inversions')
  plt.xticks(list(range(len(coaster_names))),rotation=90)
  plt.show()


num_inversions('Parc Asterix', captain_data)


plt.clf()
    
# write function to plot pie chart of operating status here:
def operating_status(df):
  x = len(df[df.status == 'status.operating'])
  x2 = len(df[df.status =='status.closed.definitely'])
  ax = plt.subplot()
  ax.pie([x, x2], labels=['Operating', 'Closed'])
  ax.axis('equal')
  plt.show()

operating_status(captain_data)

plt.clf()
  
# write function to create scatter plot of any two numeric columns here:

def scatter_two_cols (df, col1, col2):
  x_data = df[col1]
  y_data = df[col2]
  plt.scatter(x_data, y_data)
  plt.ylabel(col2)
  plt.xlabel(col1)
  plt.show()

scatter_two_cols(captain_data, 'speed', 'height')

plt.clf()

#Speed of coasters vs length of coasters

def speed_against_length (df):
  woodendata = df[df.material_type == 'Wooden']
  steeldata = df[df.material_type == 'Steel']
  plt.scatter(woodendata.speed, woodendata.length, alpha=0.4)
  plt.scatter(steeldata.speed, steeldata.length, alpha=0.4)
  plt.legend(['Wooden Coasters', 'Steel Coasters'])
  plt.xlabel('Speed (km/h)')
  plt.ylabel('Length (m)')
  plt.show()

speed_against_length(captain_data)
