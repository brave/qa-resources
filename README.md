<h2>Running Changelog Generator allows you to </h2>
<ul>
  <li>Create test runs </li>
  <li>Generate release notes</li>
  <li>Generate the exclusion list</li>
</ul>

<h2>Before you begin</h2>
<ol>
  <li><p>Download and install Python3 : <code>https://www.python.org/downloads/ </code> </p></li>
  <li><p>If you haven’t already set up a ‘Development’ directory for github so you can clone repositories, 
    
   - Create a Development directory 
   - Open terminal, type <code>mkdir Development</code></p></li>
   _**This document assumes this is where you create this directory. You will need to adjust accordingly if you create this directory elsewhere.**_
</ol>


<h2>First time stuff - getting set up</h2>
<ol>
  <li><p>Open Terminal and navigate to your <code>Development</code> directory.</p></li>
  <li><p>Type: <code>git clone git@github.com:brave/qa-resources.git</code></p></li>
  <li><p>Press Enter/Return. You have now cloned the qa-resources repo onto your machine.</p></li>
  <li><p>Next, you’ll need to install the <code>pygithub</code> package. This gives you the shared code needed to use GitHub’s public api. 
    
   - Open a Terminal and type: <code>pip3 install PyGithub</code> Then select Enter/Return.</p>
   - FYI - You can get information on this pygithub package here: <code>http://pygithub.readthedocs.io/en/latest/introduction.html</code> <br />and the main library of packages can be found here: <code>https://pypi.python.org/pypi</code> </p></li>
  <li><p>In the qa-resources folder, create a file called <code>github.secret</code>. To do this in your Terminal session change directory to qa-resources if you are not already inside the directory. Then type <code>touch github.secret</code> and select Enter/Return.</p></li>
  <li><p>Next, you have to create a github key. 
  
   - Login to your github account and navigate to <code>https://github.com/settings/profile</code></p>
   - Open new tab and navigate to <code>https://github.com/settings/tokens </code></p>
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
    
   - For simulating creation of test runs

     - In the terminal type <code>python3 brave_testrun_generator.py --test true</code> and select Enter/Return.
     - Follow options on screen to simulate generating test runs. It will just displays the output in the terminal and does NOT create GitHub issues. 

  - For Tor/IPFS:

     - Ensure milestones are created before running the test run generator.
     - Selecting the number option won't generate test runs for Tor/IPFS, need to type in `Tor/IPFS` respectively. 
     
</p></li>
</ol>

<h2> Format of terminal output</h2>
<p>General format of the output in the terminal is as follows. Enter the number for which you want to generate test runs </p>

```

Rate Limit: 5000
Rate Remaining: some number

##########################################################################################################################

For Desktop or Android minor CR bump only use the basic checks selection to generate testruns

Current open milestones for Desktop/Android
1. X.XX.x - Release
2. X.XX.x - Beta
3. X.XX.x - Nightly

Current open milestones for iOS
1. X.XX
2. X.XX
3. X.XX
4. icebox

NOTE:

For Tor Release make sure you type "Tor" or "tor" instead of the number

For IPFS Release make sure you type "IPFS/KUBO " or "ipfs/kubo" instead of the number
##########################################################################################################################

Create test runs for:

1. Desktop Release (Full manual pass)
2. Desktop Release (Basic checks for hotfix/minor Chromium bump)
3. Android Release (Full manual pass)
4. Android Release (Basic checks for hotfix/minor Chromium bump)
5. iOS Release
6. Crypto Wallet - Desktop
7. Crypto Wallet - Android
8. Crypto Wallet - iOS
9. Tor Release
10. IPFS Release

Choose the platform for which you want to generate the test run:
```

<h2> Misc Notes</h2>

  - To get updates to the changelog-generator you can open a terminal and navigate to the <Code>/Development/qa-resources</code> folder and type: <code>git pull</code>
  - Be sure you never add your <code>github.secret</code> file to any git commits you do.
  - If you uninstall Python3 for any reason, any packages you install (like PyGithub) will also be uninstalled, so you will need to install them again.

