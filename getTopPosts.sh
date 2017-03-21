rm ./comments/* 

wget "https://www.reddit.com/" -P ./comments

COMDIR="${PWD}/comments/"

echo $COMDIR

find $COMDIR -type f -exec cat {} + | egrep -o '<li class=\"first\"><a href=\"[^\"]+\"' | sed 's/^.*https/"https/' | xargs wget -P ./comments/

rm "$COMDIR/index.html"

TIMES=$(find $COMDIR -type f -exec cat {} + | egrep -o '<div class="md"><p>[^<]*</p>' | sed 's/^<div class="md"><p>//' | sed 's/<\/p>$//' | egrep -o '[^ ]+' | sort | uniq -c | sort -r -n | egrep '(Trump|trump)' | sed 's/\s*//' | sed 's/ .*//' | head -n 1)

echo $TIMES

rm -f text.html

touch text.html

echo "<HTML>" >> text.html
echo "  <HEAD>" >> text.html
echo "    <TITLE>" >> text.html
echo "      Reddit's Trump Obsession" >> text.html
echo "    </TITLE>" >> text.html
echo "  <BODY>" >> text.html
echo "    <H3> The number of times trump has been mentioned is: </H3> " >> text.html
echo "    <p>$TIMES</p>" >> text.html
echo "    <img src=\"Donald-Trump.jpg\" alt=\"The Donald\" style=\"width:500px;height:300px;\"> " >> text.html
echo "  </BODY>" >> text.html
echo "</HTML>" >> text.html
