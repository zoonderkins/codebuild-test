module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'header-max-length': [2, 'always', 120],
    'subject-case': [0],
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'refactor',
        'test',
        'bump',
        'chore',
        'revert',
        'build',
        'ci',
        'skip',
      ]
    ],
    'scope-empty': [0]
  }
};
