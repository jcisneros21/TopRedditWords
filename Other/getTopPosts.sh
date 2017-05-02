# Will focus on just best comments
# Ex: How many top comments ( top 10 ) use Trump in the lines
# Create a five top sentences of the day


rm ./comments/* 

wget "https://www.reddit.com/" -P ./comments

COMDIR="${PWD}/comments/"

echo $COMDIR

find $COMDIR -type f -exec cat {} + | egrep -o '<li class=\"first\"><a href=\"[^\"]+\"' | sed 's/^.*https/"https/' | head -n 2 | xargs wget -P ./comments/

rm "$COMDIR/index.html"

FILES="$COMDIR/*"
echo "\n\n\n\n\n\n\n\n"

for file in $FILES; do
  echo $file
  cat $file | egrep -o '<ul class=\"flat-list buttons\"><li class=\"first\"><a href=\"[^\"]+\"' | sed 's/^.*https/"https/' | head -n 20 | xargs wget -P ./comments/
  rm $file
done


for file in $FILES; do
  cat $file | egrep -o '<div class="md"><p>[^<]*</p>' | sed 's/^<div class="md"><p>//' | sed 's/<\/p>$//' |  egrep "(Trump|trump|Donald Trump)" 
done
#TIMES=$(

#find $COMDIR -type f -exec cat {} + | egrep -o '<div class="md"><p>[^<]*</p>' | sed 's/^<div class="md"><p>//' | sed 's/<\/p>$//' | egrep "Trump" 

#echo $TIMES

#rm -f text.html

#touch text.html


#echo "<HTML>" >> text.html
#echo "  <HEAD>" >> text.html
#echo "    <TITLE>" >> text.html
#echo "      Reddit's Trump Obsession" >> text.html
#echo "    </TITLE>" >> text.html
#echo "  <BODY>" >> text.html
#echo "    <H3> The number of times trump has been mentioned is: </H3> " >> text.html
#echo "    <p>$TIMES</p>" >> text.html
#echo "    <img src=\"Donald-Trump.jpg\" alt=\"The Donald\" style=\"width:500px;height:300px;\"> " >> text.html
#echo "  </BODY>" >> text.html
#echo "</HTML>" >> text.html

