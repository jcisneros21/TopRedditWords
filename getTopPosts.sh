rm ./comments/* 

wget "https://www.reddit.com/" -P ./comments

COMDIR="${PWD}/comments/"

echo $COMDIR

find $COMDIR -type f -exec cat {} + | egrep -o '<li class=\"first\"><a href=\"[^\"]+\"' | sed 's/^.*https/"https/' | xargs wget -P ./comments/

rm "$COMDIR/index.html"

find $COMDIR -type f -exec cat {} + | egrep -o '<div class="md"><p>[^<]*</p>' | sed 's/^<div class="md"><p>//' | sed 's/<\/p>$//' | egrep -o '[^ ]+' | sort | uniq -c | sort -r -n | head -n 20

