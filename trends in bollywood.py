import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


data = {
         'movie_title': ['Movie A','Movie B','Movie C','Movie D','Movie E','Movie F','Movie G','Movie H','Movie I','Movie J'],
         'genre':['Romance','Action','Comedy','Drama','Action','Comedy','Romance','Thriller','Drama','Action'],
         'release_year':[2023,2023,2022,2021,2022,2023,2020,2021,2022,2023],
         'box_office_crores':[150,80,90,120,100,130,125,240,100,70],
         'lead_actor':['Actor x','Actor y','Actor z','Actor x','Actor y','Actor z','Actor x','Actor y','Actor z','Actor x'],
       }

bollywood_df = pd.DataFrame(data)

print(bollywood_df.head())
print(bollywood_df.info())

# genre analysis

genre_counts = bollywood_df['genre'].value_counts()
print("\nMovie count by genre:\n",genre_counts)

#box office collection by genre

box_office_by_genre = bollywood_df.groupby('genre')['box_office_crores'].sum()
print("\nTotal box office collection by genre:\n",box_office_by_genre)

#lead actor analysis

lead_actor_box_office = bollywood_df.groupby('lead_actor')['box_office_crores'].sum()
print("\ntotal box office collection by lead actors:\n",lead_actor_box_office)

#bar chart of movie count by genre

plt.figure(figsize=(10, 6))
sns.countplot(x='genre',data=bollywood_df)
plt.title('Number of movies by genre')
plt.xlabel('Genre')
plt.ylabel('Number of movies')
plt.show()


# Pie Chart of box office collection by genre

plt.figure(figsize=(8,5))
plt.pie(box_office_by_genre, labels=box_office_by_genre.index, autopct='%1.1f%%',startangle=140)
plt.title('Box office collection by genre')
plt.show()

