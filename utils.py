#Data Exploration
import json

def parse_fields(line):
    data = json.loads(line)
    return {
        "book_id": data["book_id"], 
        "title": data["title_without_series"], 
        "ratings": data["ratings_count"], 
        "url": data["url"], 
        "cover_image": data["image_url"]
    }

#Visualizations
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns

def value_counts(data, feature):
    plt.figure(figsize=(16,6))
    sns.countplot(data=data, x=str(feature), palette='Pastel1')
    plt.show()