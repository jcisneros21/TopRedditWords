import csv
import praw
import json

# Credentials to access the Reddit API
reddit = praw.Reddit(client_id='vgr0He3IMlSqVA',
                     client_secret='h0WAu-6F6cQsx3Ku0DcC9gtld24',
                     user_agent='by /u/ExtractAccount',
                     username='ExtractAccount',
                     password='reddit12345')

# Extract only 25 post from the front page
topPosts = []
for submission in reddit.front.hot(limit=25):
  topPosts.append(submission)

# Lists for comments and information about them
donaldComments = []
authorList = []
comment_ranking = []

# Extract all comments from the front page submissions
for sub in topPosts:
  submission = reddit.submission(id=sub)
  submission.comments.replace_more(limit=0)
  for comment in submission.comments.list():
    strip_comment = comment.body.replace("\n\n"," ")
    strip_comment = strip_comment.replace("\n", " ")
    if ' Donald ' or ' Donald\'s ' in comment.body:
      if 'Glover' not in comment.body:
        authorList.append(comment.author.name)
        donaldComments.append(strip_comment)
        comment_ranking.append(comment.score)
    elif ' donald ' or ' donald\'s ' in comment.body:
      if 'Glover' not in comment.body:
        authorList.append(comment.author.name)
        donaldComments.append(strip_comment)
        comment_ranking.append(comment.score)
    elif 'Trump' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)
    elif 'trump' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)

# A list of indexes
index_list = []
for i in range(0,len(comment_ranking)):
  index_list.append(i)

# Sort by ranking of each comment and allow the list of indexes to be changed accordingly
# to the rankings
def bubble_sort(items):
  for i in range(len(items)):
    for j in range(len(items)-1-i):
      if items[j] < items[j+1]:
        items[j], items[j+1] = items[j+1], items[j]
        index_list[j], index_list[j+1] = index_list[j+1], index_list[j]

bubble_sort(comment_ranking)

# Creates the JS comment file so the browser can present the comments
with open('../js/randomTrumpText.js','w+') as myfile:
  # Write a list for the comments
  myfile.write('text_list = [\n')
  for item in donaldComments:
    holder = json.dumps(item)
    myfile.write('              ' + holder + ',\n')
  myfile.write('             ];\n\n')
  # Write a list for the authors of each comment
  myfile.write('name_list = [\n')
  for name in authorList:
    holder = json.dumps(name)
    myfile.write('              ' + holder + ',\n')
  myfile.write('             ];\n\n')
  # Write the indexes of the highest rated comments
  myfile.write('rank_list = [\n')
  for i in range(0,5):
    myfile.write('              ' + str(index_list[i]) + ',\n')
  myfile.write('             ];\n\n')
  myfile.write('var amount = text_list.length;\n')
  myfile.write('$(\"#numberofComments\").text(amount + " Comments");\n\n')
  for i in range(0,5):
    myfile.write('$("#comment' + str(i+1) + '").text(text_list[rank_list[' + str(i) + ']]);\n')
  myfile.write('\n')
  for i in range(0,5):
    myfile.write('$("#author' + str(i+1) + '").text("- /u/" + name_list[rank_list[' + str(i) + ']]);\n')
  myfile.write('\n')
  myfile.write('var counter = 0\n\n')
  myfile.write('function replaceText(){\n')
  myfile.write('  text = text_list[counter];\n')
  myfile.write('  if(text.length > 80){\n')
  myfile.write('')
  myfile.write('    trump_array = ["Trump","trump","Donald","donald"];\n')
  myfile.write('    for(var i=0; i < trump_array.length; i++){\n')
  myfile.write('      index = text.indexOf(trump_array[i]);\n')
  myfile.write('      if(index > -1){\n')
  myfile.write('        if(index > 200){\n')
  myfile.write('          text = text.substring(index - 200, index) + text.substring(index,index+206);\n')
  myfile.write('          text = "... " + text + " ...";\n')
  myfile.write('        }\n')
  myfile.write('        else{\n')
  myfile.write('          diff = 200 - index;\n')
  myfile.write('          text = text.substring(0, index) + text.substring(index, index+206 + diff);\n')
  myfile.write('          text = text + " ...";\n')
  myfile.write('        }\n')
  myfile.write('      }\n')
  myfile.write('    }\n')
  myfile.write('  }\n')
  myfile.write('  $("#comment").text(text + " -/u/" + name_list[counter]);\n')
  myfile.write('  counter += 1;\n')
  myfile.write('  if((counter % amount) == 0){\n')
  myfile.write('    counter = 0;\n')
  myfile.write('  }\n')
  myfile.write('}\n\n')
  myfile.write('function reload(){\n')
  myfile.write('  location.reload();\n')
  myfile.write('}\n\n')
  myfile.write('replaceText();\n')
  myfile.write('setInterval(replaceText,10000);\n')
  myfile.write('setInterval(replaceText,600000);')
