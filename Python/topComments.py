# username = ExtractAccount
# password = reddit12345

import csv
import praw
import json

reddit = praw.Reddit(client_id='vgr0He3IMlSqVA',
                     client_secret='h0WAu-6F6cQsx3Ku0DcC9gtld24',
                     user_agent='by /u/ExtractAccount',
                     username='ExtractAccount',
                     password='reddit12345')

topPosts = []
for submission in reddit.front.hot(limit=25):
  topPosts.append(submission)

donaldComments = []
authorList = []
comment_ranking = []
for sub in topPosts:
  submission = reddit.submission(id=sub)
  submission.comments.replace_more(limit=0)
  for comment in submission.comments.list():
    strip_comment = comment.body.replace("\n\n"," ")
    strip_comment = strip_comment.replace("\n", " ")
    if ' Donald ' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)
    elif ' donald ' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)
    elif ' Trump ' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)
    elif ' trump ' in comment.body:
      authorList.append(comment.author.name)
      donaldComments.append(strip_comment)
      comment_ranking.append(comment.score)
    # trump's
    # donald's

index_list = []
for i in range(0,len(comment_ranking)):
  index_list.append(i)

def bubble_sort(items):
  for i in range(len(items)):
    for j in range(len(items)-1-i):
      if items[j] < items[j+1]:
        items[j], items[j+1] = items[j+1], items[j]
        index_list[j], index_list[j+1] = index_list[j+1], index_list[j]

bubble_sort(comment_ranking)
print(comment_ranking)
print(index_list)

# Creates the JS comment file so the browser can show the comments
with open('../js/randomTrumpText.js','w+') as myfile:
  myfile.write('text_list = [\n')
  for item in donaldComments:
    holder = json.dumps(item)
    myfile.write('              ' + holder + ',\n')
  myfile.write('             ];\n\n')
  myfile.write('name_list = [\n')
  for name in authorList:
    holder = json.dumps(name)
    myfile.write('              ' + holder + ',\n')
  myfile.write('             ];\n\n')
  myfile.write('rank_list = [\n')
  for i in range(0,5):
    myfile.write('              ' + str(index_list[i]) + ',\n')
  myfile.write('             ];\n\n')
  myfile.write('var amount = text_list.length;\n')
  myfile.write('$(\"#numberofComments\").text(amount);\n\n')
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
