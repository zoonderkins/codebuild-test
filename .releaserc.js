module.exports = {
  branches: [
    {
      name: "master"
    },
    {
      name: "test", channel: "beta", prerelease: "beta"
    },
    {
      name: "dev", channel: "alpha", prerelease: "alpha"
    }
  ],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md"
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": [
          "package.json",
          "CHANGELOG.md"
        ],
        "message": "🔖 release: ${nextRelease.version} \n ${nextRelease.notes}",
      },
    ],

  ],
}