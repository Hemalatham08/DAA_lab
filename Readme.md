Your project structure is perfectly fine. Since your GitHub repository already exists and you've successfully pushed lab1 and lab2, you only need to add lab3 and push the changes.

Your folder structure should look like this:

DAA_lab/
│
├── lab1/
│   └── app.py
│
├── lab2/
│   └── app.py
│
└── lab3/
    └── app.py
Step 1: Make sure you're inside the DAA_lab folder

In the VS Code terminal, you should see something like:

--------PS C:\Users\Hemalatha M\OneDrive\Desktop\DAA lab>

If yes, you're in the correct folder.

Step 2: Check the changes
-----------git status

You should see something similar to:

Untracked files:
    lab3/

or, if you modified files inside lab3:

Changes not staged for commit:
Step 3: Add the new folder
---------git add .
Step 4: Commit the changes
-------git commit -m "Added lab3"
Step 5: Push to GitHub
--------git push origin main

That's it. Git will upload only the new changes (the lab3 folder and its contents).

Verify

After the push completes, your GitHub repository should look like:

DAA_lab/
│
├── lab1/
│   └── app.py
│
├── lab2/
│   └── app.py
│
└── lab3/
    └── app.py


    ------------------------------ALL THE COMMANDS-----------
git status
git add .
git commit -m "Describe your changes"
git push origin main

change the wordings alone
-------------------------------------------------------------------------