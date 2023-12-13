<h2>Running Changelog Generator allows you to </h2>
<ul>
  <li>Create test runs </li>
  <li>Generate release notes</li>
  <li>Generate the exclusion list</li>
</ul>

<h2>Before you begin</h2>
<ol>
  <li><p>Download and install Python3 (3.5.2): https://www.python.org/downloads/release/python-352/</p></li>
  <li><p>If you haven’t already set up a ‘Development’ directory for github so you can clone repositories, 
    
   - Create a Development directory 
   - Open terminal, type mkdir Development</p></li>
   _**This document assumes this is where you create this directory. You will need to adjust accordingly if you create this directory elsewhere.**_
   <li><p>Other things that might be helpful to have installed</p></li>
   <li><p>iTerm2 - alternative to the standard Terminal. Not needed, but has some nice features.</p></li>
</ol>


<h2>First time stuff - getting set up</h2>
<ol>
  <li><p>Open Terminal and navigate to your ‘Development’ directory.</p></li>
  <li><p>Type: <code>git clone git@github.com:brave/qa-resources.git</code></p></li>
  <li><p>Press Enter/Return. You have now cloned the qa-resources repo onto your machine.</p></li>
  <li><p>Next, you’ll need to install the pygithub package. This gives you the shared code needed to use github’s public api. 
    
   - Open a Terminal and type: `pip3 install PyGithub` Then select Enter/Return.</p>
   - FYI - You can get information on this pygithub package here: http://pygithub.readthedocs.io/en/latest/introduction.html <br />and the main library of packages can be found here: https://pypi.python.org/pypi </p></li>
  <li><p>In the qa-resources folder, create a file called <code>github.secret</code>. To do this in your Terminal session change directory to qa-resources if you are not already inside the directory. Then type <code>touch github.secret</code> and select Enter/Return.</p></li>
  <li><p>Next, you have to create a github key. 
  
   - Login to your github account and navigate to https://github.com/settings/profile</p>
   - Open new tab and navigate to https://github.com/settings/tokens </p>
   - Click on **Generate new token** button. Give the token a meaningful name and select the checkboxes below for your token.</p>
   - Select ‘Generate token’ button. Your token is now generated, it looks similar to an SHA. Copy the token. Do not exit this page yet.</p>
<li><p>Add this token to your github.secret file. 
  
   - To do this, in your Terminal session change directory to qa-resources if you are not already inside the directory. </p>
   - Then type <code>vi github.secret</code> and select Enter/Return.</p>
   - Since you’ve already copied your token, type <code>i</code>  and paste your token. Then hit the Esc key.</p>
   - Now type <code>:wq</code> to save and exit the file.
   - If you want to verify that the token was saved correctly, you can type <code>cat github.secret</code> and your token will display.</p></li>
  </ol>

<h2>Running the Changelog Generator</h2>
<ol>
  <li><p>Open a Terminal session.</p></li>
  <li><p>Change directory to where you have qa-resources.</p></li>
  <li><p>Determine what product you want to run the changelog-generator for (browser-laptop, Android, iOS) and if you want to create issues in github or just see the output in the terminal.
    
   - For browser-laptop:
    
    - In the terminal type <code>python3 brave_testrun_generator.py --test true</code> and select Enter/Return. This just displays the output in the terminal and does NOT create github issues. 
    - To create github issues, leave off the <code>--test true</code> flag and github issues will be created and assigned out.

  - For Android:

     - <code>python3 braveautogen-androdid.py --test true </code>(no github issues)
     - <code>python3 braveautogen-androdid.py</code>  (github issues created)
     
   - For iOS:
   
     - <code>python3 braveautogen-ios.py --test true </code>(no github issues)
     - <code>python3 braveautogen-ios.py</code>   (github issues created)
</p></li>
</ol>

<h2> Format of terminal output</h2>
<p>General format of the output in the terminal is as follows. Specific label names may vary slightly by repo. See individual .py files for details.</p>
<pre>
$ python3 braveautogen.py --test true
  Rate Limit: 5000
  Rate Remaining: <some number>
  
    <next release version>
  
    Release Notes:
    <lists issues with label ‘release-notes/include’>

    Checklist:
    <lists issues with label ‘QA/steps-specified’ and does not have label ‘QA/no-qa-needed’>

    Exclusion List:
    <lists issues with label ‘release-notes/exclude>

    Individual Product checklists

     - Contains per release specialty items
     - Uses the associated product wikitemplate file also found in qa-resources to generate the test run
</pre>

<h2> Misc Notes</h2>

  - To get updates to the changelog-generator you can open a terminal and navigate to the /Development/qa-resources folder and type: <code>git pull</code>
  - Be sure you never add your github.secret file to any git commits you do.
  - If you uninstall Python3 for any reason, any packages you install (like PyGithub) will also be uninstalled, so you will need to install them again.

