# TopRedditWords
TopRedditWords searches through the submissions from the front page of Reddit.com and extacts all comments that relate to Donald Trump. Once extracted, a JavaScript file will be generated so that index.html can read the comments from the front page and display these comments in nicely formatted display. For this project, I access Reddit's Python API, PRAW, to grab the comments necessary for this project.

If you would like to see an example of what this program produces, please visit here:  
https://jcisneros21.github.io/

# Dependencies
You will need to install python3 and as well as pip3 and praw.

You can visit Python's website here for downloads:  
https://www.python.org/downloads/

or if you are using a Linux distro:  
sudo apt-get install python3

For downloading pip3, please refer to the pip installation guide:  
https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py

For downloading the module praw, please follow the instructions in the link below:  
https://pypi.python.org/pypi/praw

Note: Remember to use pip3 instead of pip when installing praw

# Install
If you would like to generate the JavaScript file to display current comments of Donald Trump on Reddit.com please follow the directions below:

Please clone the repository on a terminal with the command:  
git clone https://github.com/jcisneros21/TopRedditWords.git

Next please enter the repository. Once in, enter the Python directory.

Run the python command below:  
python3 topComments.py

There you go! You just generated your very own JavaScript file. Now please open index.html to see the comments
