'use strict'

const Generator = require('yeoman-generator')
const path = require('path')
const mkdirp = require('mkdirp')

class MicrolibraryGenerator extends Generator {
  constructor (args, opts) {
    super(args, opts)
    this.argument('name', {type: String, required: false})
    this.option('yarn', {
      description: 'Use Yarn as the package manager'
    })
    /*
    this.option('docker', {
      description: 'Install Docker artifacts including a Dockerfile',
    });
    */

    this.useYarn = this.options.yarn
    this.docker = this.options.docker
    this.name = this.options.name || 'micro.library.python'
    this.description = 'My cool microlibrary'
    this.version = '0.0.1'
    this.github = {username: '', repository: this.name}
    this.author = {name: '', url: '', email: ''}
    this.node = {version: '9.5.0'}
    this.coveralls = {token: ''}
  }

  initializing () {
  }

  prompting () {
    const prompts = [
      {
        type: 'input',
        name: 'description',
        message: `description [${this.description}]`
      },
      {
        type: 'input',
        name: 'version',
        message: `version [${this.version}]`
      },
      {
        type: 'input',
        name: 'githubUsername',
        message: `github username [${this.github.username}]`
      },
      {
        type: 'input',
        name: 'githubRepository',
        message: `github repository [${this.github.repository}]`
      },
      {
        type: 'input',
        name: 'authorName',
        message: `author name [${this.author.name}]`
        /*
        validate: (input) => {
          const done = this.async();
          setTimeout(() => {
            if (_.isEmpty(input)) {
              // Pass the return value in the done callback
              done('You need to provide a name');
              return;
            }
            // Pass the return value in the done callback
            done(null, true);
          }, 100)
        }
        */
      },
      {
        type: 'input',
        name: 'authorEmail',
        message: `author e-mail [${this.author.email}]`
      },
      {
        type: 'input',
        name: 'authorUrl',
        message: `author url [${this.author.url}]`
      },
      {
        type: 'input',
        name: 'coverallsToken',
        message: `coveralls token [${this.coveralls.token}]`
      }
    ]

    if (!this.options.name) {
      prompts.unshift({
        type: 'input',
        name: 'name',
        message: `microlibrary name [${this.name}]`
      })
    }

    return this.prompt(prompts).then(r => {
      this.name = r.name ? r.name : this.name
      this.description = r.description ? r.description : this.description
      this.version = r.version ? r.version : this.version
      this.github.username = r.githubUsername ? r.githubUsername : this.github.username
      this.github.repository = r.githubRepository ? r.githubRepository : this.github.repository
      this.author.name = r.authorName ? r.authorName : this.author.name
      this.author.url = r.authorUrl ? r.authorUrl : this.author.url
      this.author.email = r.authorEmail ? r.authorEmail : this.author.email
      this.coveralls.token = r.coverallsToken ? r.coverallsToken : this.coveralls.token
    })
  }

  configuring () {
  }

  default () {
  }

  get writing () {
    return {
      appStaticFiles () {
        const src = this.sourceRoot()
        const dest = this.destinationPath(this.name)

        const files = [
          './.tasks/config.yml',
          './.tasks/build.py',
          '.coveralls.yml',
          './setup.py',
          './src/__init__.py',
          './src/base.py',
          './test/__init__.py',
          './test/test_example.py',
          './docs/conf.py'
        ]

        const copyOpts = this.docker
          ? null
          : {
            globOptions: {
              ignore: '**/+(Dockerfile|.dockerignore)'
            }
          }
        this.fs.copy(src, dest, copyOpts)
        this.fs.copy(this.templatePath('.*'), dest, copyOpts)
        this.fs.copy(this.templatePath('.tasks'), path.join(dest, '.tasks'), copyOpts)
        this.fs.copy(this.templatePath('.templates'), path.join(dest, '.templates'), copyOpts)

        mkdirp.sync(path.join('src', this.name.split('.').join(path.sep)))

        const opts = {
          name: this.name,
          title: this.name,
          description: this.description,
          keywords: this.keywords,
          version: this.version,
          github: this.github,
          node: this.node,
          author: this.author,
          coveralls: this.coveralls,
          year: new Date().getFullYear()
        }

        files.forEach(f => {
          this.fs.copyTpl(
            this.templatePath(f),
            this.destinationPath(`${this.name}/${f}`),
            opts
          )
        })
      }
    }
  }

  conflicts () {
  }

  install () {
    const appDir = path.join(process.cwd(), this.name)
    process.chdir(appDir)
    if (this.useYarn) {
      this.yarnInstall()
    } else {
      this.npmInstall()
    }
  }

  end () {
  }
};

module.exports = MicrolibraryGenerator
