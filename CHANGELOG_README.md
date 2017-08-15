#License MPL 2.0

# How to get autogen.py to work for your org

 - make sure the issues you wish to include in your release notes have a label of release-notes/include, are in the milestone, and are closed

 - create a github personal access token https://github.com/settings/tokens and place it in a file called 'github.secret' next to autogen.py
 - on the command line run 'pip3 install pygithub'
 - on the command line run 'python3 autogen.py -o <name of your organization> -r <name of your repo>'
