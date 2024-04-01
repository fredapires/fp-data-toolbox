# useful git CLI commands

To roll back the last commit you made, especially if you haven't pushed it to the remote repository yet, you can use the following Git CLI command:

`git reset --soft HEAD~1`

This command will undo the last commit but keep the changes you made in your working directory. If you want to discard the changes made in the last commit entirely (both commit and changes), you can use:

`git reset --hard HEAD~1`

Be cautious with --hard as it will remove all changes without the possibility of recovery. If you've already pushed the commit to the remote repository, you'll need to force push after the reset, but this can affect other collaborators. Always communicate with your team before doing a force push.

If the commit has been pushed, and you want to avoid rewriting history, you might consider reverting the commit instead:

`git revert HEAD`

This will create a new commit that undoes the changes made by the last commit.