Contributing to nile-coverage
=======

We really appreciate and value contributions. Please take 5' to review the items listed below to make sure that your contributions are merged as soon as possible.

## Creating Pull Requests (PRs)

As a contributor, you are expected to fork this repository, work on your own fork and then submit pull requests. The pull requests will be reviewed and eventually merged into the main repo. See ["Fork-a-Repo"](https://help.github.com/articles/fork-a-repo/) for how this works.

## A typical workflow

1) Make sure your fork is up to date with the main repository:

```
cd nile-coverage
git remote add upstream git@github.com:ericnordelo/nile-coverage.git
git fetch upstream
git pull upstream main
```
NOTE: The directory `nile-coverage` represents your fork's local copy.

2) Branch out from `master` into `feat/some-feature-#123`:
(Postfixing #123 will associate your PR with the issue #123 and make everyone's life easier =D)
```
git checkout -b feat/some-feature-#123
```

3) Make your changes, add your files, commit, and push to your fork.

```
git add some_file.py
git commit "Add some feature"
git push origin feat/some-feature-#123
```

5) Go to [nile-coverage](https://github.com/ericnordelo/nile-coverage) in your web browser and issue a new pull request.

6) Maintainers will review your code and possibly ask for changes before your code is pulled in to the main repository. We'll check that all tests pass, review the coding style, and check for general code correctness. If everything is OK, we'll merge your pull request and your code will be part of nile-coverage.

## All set!

If you find any issues or have any suggestion, feel free to post them to [issues](https://github.com/ericnordelo/nile-coverage/issues).

Finally, if you're looking to collaborate and want to find easy tasks to start, look at the issues we marked as ["Good first issue"](https://github.com/ericnordelo/nile-coverage/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22).

Thanks for your time and code!
