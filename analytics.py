import pandas as pd
from tqdm.notebook import tqdm_notebook
from dateutil import parser
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np
import joblib
#from profanity_check import predict, predict_prob
import warnings
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from textblob import TextBlob
import emoji
import itertools 
import matplotlib.style as style
from ipywidgets import IntProgress
# from google.colab import files
style.use('ggplot')
warnings.filterwarnings('ignore')


def vali_date(text):
    try:
        datetime.datetime.strptime(text, '%m/%d/%y')
        return True
    except Exception as e:
      return False


def valid_user(str):
  if len(str.split(' ')) < 5 and not 'left' in str and not 'added' in str and not 'removed' in str:
    return True
  elif ('+234' or '+1'  or '+27') in str and len(str.split(' ')) <= 3:
    return True
  return False
  

def get_colors_of_certain_order(names_in_certain_order):
  order = list(names_in_certain_order)
  return_list = []
  for name in order:
    return_list.append(color_dict[name])
  return return_list
  
  
lines = []
with open('itgist.txt', encoding='utf-8') as f:
  for line in f:
    if vali_date(line.split(',')[0]):
      lines.append(line.strip('\n'))
    else:
      lines[len(lines) - 1] += ' ' + line.strip('\n')


datetimes, names, msgs = ([] for i in range(3))
for line in tqdm_notebook(lines, total = len(lines), unit = 'line'):
    datetimes.append(datetime.datetime.strptime(line.split(' - ')[0], '%m/%d/%y, %I:%M %p'))
    names.append(line.split(' - ')[1].split(': ')[0])
    msgs.append(''.join(line.split(' - ')[1].split(': ')[1:]))


df2 = pd.DataFrame()
df2['datetime'] = datetimes
df2['name'] = names
df2['msg'] = msgs


df3 = df2[df2['name'].apply(valid_user)]

 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 df3.loc[df3.name ==  '<Name Redacted>', 'name'] = '<Name Redacted>'
 
uni_names = df3['name'].unique()
print(len(uni_names))


df3['date'] = df3['datetime'].apply(lambda x: x.date())
df3['day_sent'] = df3['datetime'].dt.strftime('%a')
df3['month_sent'] = df3['datetime'].dt.strftime('%b')
df3['year_sent'] = df3['datetime'].dt.year
df3['count'] = 1 # To groupby days and have a count of how many messages were sent per day
df3 = df3[~df3['msg'].apply(lambda x: True if '\xa0' in x else False)] # To remove characters with '\xa0'
print(df3.shape)


grouped_by_date = df.groupby('date').sum().reset_index()

plt.figure(figsize = (27, 6))
sns.lineplot(x = 'date', y = 'count', data = grouped_by_date)
plt.title('Messages sent per day over a time period')
#plt.savefig('msg_perday_over_period.svg', format = 'svg')



color_dict = {}
colors = ["#e52165", "#0d1137", "#efb5a3", "#f57e7e", "#315f72", "#7fc3c0", "#cfb845", "#141414", "#1fbfb8", "#05716c", "#1978a5", "#031163", "#829079", "#ede6b9", "#b9925e", "#d71b3b", "#e8d71e", "#16acea", "#4203c9", "#b85042", "#e7e8d1", "#a7beae", "#f5beb4", "#9bc472", "#cbf6db", "#79cbb8", "#500472", "#f6ead4", "#a2a595", "#b4a284", "#e3b448", "#cbd18f", "#3a6b35", "#d13ca4", "#ffea04", "#fe3a9e", "#e1dd72", "#a8c66c", "#1b6535", "#edca82", "#097770", "#e0cdbe", "#a9c0a6", "#ddc3a5", "#201e20", "#e0a96d", "#ffcce7", "#daf2dc", "#81b7d2", "#4d5198", "#d902ee", "#ffd79d", "#f162ff", "#320d3e", "#316879", "#f47a60", "#7fe7dc", "#ced7d8"]
sns.palplot(colors)
names = df['name'].unique()


for name, color in zip(names, colors):
  color_dict[name] = color

color_dict

fig, axs = plt.subplots(ncols = 2, figsize = (20, 6))
plt.xticks(rotation = 90)

# Plot 1 - Countplot of total messages sent
g = sns.countplot(x = 'name', data = df, order = df['name'].value_counts().index, ax = axs[0], palette = get_colors_of_certain_order(df['name'].value_counts().index))
axs[0].set_title('Total Messages Sent')
g.set_xticklabels(g.get_xticklabels(), rotation=90)

# Plot 2 - Barplot of average message lengths
df['msg_length'] = df['msg'].apply(lambda x: len(x))
avg_msg_lengths = df.groupby('name').mean().reset_index().sort_values(by = 'msg_length', ascending = False)
h = sns.barplot(x = 'name', y = 'msg_length', data = avg_msg_lengths, ax = axs[1], palette = get_colors_of_certain_order(avg_msg_lengths['name']))
axs[1].set_title('Average Message Lengths')
h.set_xticklabels(h.get_xticklabels(), rotation=90)

plt.savefig('msg_plots.svg', format = 'svg')
#files.download('msg_plots.svg')


# Plot 3 - Barplot of total media count
plt.figure(figsize = (8, 6))
df['is_media'] = df['msg'].apply(lambda x: 1 if '<Media omitted>' in x else 0)
df.groupby('name').sum().reset_index().sort_values(by = 'is_media', ascending = False)[['name', 'is_media']]
total_media_count = df.groupby('name').sum().reset_index().sort_values(by = 'is_media', ascending = False)[['name', 'is_media']]
g = sns.barplot(x = 'name', y = 'is_media', data = total_media_count, palette = get_colors_of_certain_order(total_media_count['name']))
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.title('Total Media Sent')
#plt.xticks(rotation = 90)

# Plot 3 - Barplot of total deleted messages count

plt.figure(figsize = (8, 6))
df['is_deleted'] = df['msg'].apply(lambda x: 1 if 'This message was deleted' in x else 0)
df.groupby('name').sum().reset_index().sort_values(by = 'is_deleted', ascending = False)[['name', 'is_deleted']]
total_deleted_count = df.groupby('name').sum().reset_index().sort_values(by = 'is_deleted', ascending = False)[['name', 'is_deleted']]
g = sns.barplot(x = 'name', y = 'is_deleted', data = total_deleted_count, palette = get_colors_of_certain_order(total_deleted_count['name']))
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.title('Total Deleted Messages')
#plt.xticks(rotation = 90)
# total_deleted_count
# plt.savefig('total_deleted_plot.svg', format = 'svg')
#files.download('total_deleted_plot.svg')


word_dict = dict.fromkeys(df['name'].unique())
for key in word_dict.keys():
  word_dict[key] = {}

for name, msg in zip(df['name'], df['msg']):
  for word in msg.split():
    # If word contains the 'media ommited' message ignore
    if word not in ['<Media', 'omitted>']: 
      if word in word_dict[name]:
        word_dict[name][word] += 1
      else:
        word_dict[name][word] = 1

# Sorting emoji dictionary in descending order of word frequency
for name in df['name'].unique():
  word_dict[name] = {k: v for k, v in sorted(word_dict[name].items(), key = lambda item: item[1], reverse = True)}

grouped_df = df.groupby('name').sum().reset_index()
grouped_df['most_used_words'] = grouped_df['name'].apply(lambda x: word_dict[x])
grouped_df[['name', 'most_used_words']]

# plt.savefig('total_media_plot.svg', format = 'svg')
#files.download('total_media_plot.svg')



fig, axs = plt.subplots(ncols = 2, figsize = (24, 6))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
grouped_by_month = df.groupby('month_sent').sum().reset_index().sort_values(by = 'count', ascending = False)
sns.barplot(x = 'count', y = 'month_sent', data = grouped_by_month, order = months, ax = axs[0], palette = sns.color_palette('cividis', 12))
axs[0].set_title('Total messages sent grouped by month')

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
grouped_by_month_and_day = df.groupby(['month_sent', 'day_sent']).sum().reset_index()[['month_sent', 'day_sent', 'count']]
pt = grouped_by_month_and_day.pivot_table(index = 'month_sent', columns = 'day_sent', values = 'count').reindex(index = months, columns = days)
sns.heatmap(pt, cmap = 'cividis', ax = axs[1])
axs[1].set_title('Heatmap of month sent and day sent')

# plt.savefig('month_activity.svg', format = 'svg')
#files.download('month_activity.svg')


fig, axs = plt.subplots(ncols = 2, figsize = (24, 6))

grouped_by_day = df.groupby('day_sent').sum().reset_index()[['day_sent', 'count']]
sns.barplot(y = 'count', x = 'day_sent', data = grouped_by_day, order = days, ax = axs[0])
axs[0].set_title('Total messages sent grouped by day')

df['hour_sent'] = df['datetime'].apply(lambda x: x.hour)
grouped_by_time = df.groupby('hour_sent').sum().reset_index().sort_values(by = 'count', ascending = False)
sns.barplot(y = 'count', x = 'hour_sent', data = grouped_by_time, ax = axs[1])
axs[1].set_title('Most Active Hours')

# plt.savefig('days_and_times.svg', format = 'svg')
#files.download('days_and_times.svg')



plt.figure(figsize = (18, 6))

grouped_by_date = df.groupby('date').sum().reset_index().sort_values(by = 'count', ascending = False).head(15)
grouped_by_date['day_sent'] = grouped_by_date['date'].apply(lambda x: x.strftime('%a'))
ax = sns.barplot(y = 'count', x = 'date', data = grouped_by_date)

# I spent way too long to get the bar annotations to work properly. Thank you again, StackOverflow.
for bar, label in zip(ax.patches, grouped_by_date['day_sent']):
    x = bar.get_x()
    width = bar.get_width()
    height = bar.get_height()
    ax.text(x + width/2., height + 10, label, ha="center") 

ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.title('Most Active Days')

plt.savefig('most_active_days.svg', format = 'svg')
#files.download('most_active_days.svg')
