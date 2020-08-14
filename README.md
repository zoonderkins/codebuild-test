## Semantic release example

## Added from SYG-123 -- trigger test

## Install commitlint

```
npm install --save-dev husky
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```


## Reset / clear all git commit

```bash
git checkout --orphan latest_branch \
git add -A \
git commit -am "feat: init" \
git branch -D master \
git branch -m master \
git push -f origin master
git gc --aggressive --prune=all
```

## Remove all released tag

```bash
# delete all remote tags
git tag | xargs -L 1 | xargs git push origin --delete

# delete all local tags
git tag | xargs -L 1 | xargs git push origin --delete
```
## Commitizen

```
// Install commitizen first
npm install -g commitizen  OR  npm install --save-dev commitizen

// init your repo to fit into commitizen format
commitizen init cz-conventional-changelog --save-dev --save-exact
OR
npx commitizen init cz-conventional-changelog --save-dev --save-exact

// Husky config
"husky": {
  "hooks": {
    "prepare-commit-msg": "exec < /dev/tty && git cz --hook || true",
  }
}
```


## Commitlint

```
npm install --save-dev @commitlint/cli @commitlint/config-conventional

// package.json

"commitlint": {
    "extends": [
      "@commitlint/config-conventional"
    ]
  },

```

## Gitmoji

```
// Install
npm i -g gitmoji-cli

// Example
git commit -m ':bug: fix xxx'

// Other sample
1. :art: (Improve struct or format code)
2. :zap: (Improve performance)
3. :fire: (Removing files)
4. :bug: (fix a bug)
5. :ambulance: (Critical hot-fix)
6. :sparkles: (Introducing new features)
7. :pencil: (Writing docs)
8. :rocket: (Deploying stuff)
9. :tada: (Begin a project)
10. :white_check_mark: (Add or update tests)
11. :lock: (Fix security issues)
12. :bookmark: (Release version tag)
13. :rotating_light: (Remove linter warnings)
14. :construction: (work in progress)
15. :green_heart: (Fix CI Build)
16. :arrow_down: (Downgrade dependencies)
17. :arrow_up: (Upgrade dependencies)
18. :pushpin: (Pin dependencies to specific version)
19. :construction_worker: (Add or update CI build system)
20. :recycle: (Refactor code)
21. :twisted_rightwards_arrows: (Merge branches)
22. :poop: (Write bad code that need to be improved)
23. :page_facing_up: (Add or update license)
24. :boom: (Introduce breaking changes)
25. :see_no_evil: (Add or update .gitignore file)

```
