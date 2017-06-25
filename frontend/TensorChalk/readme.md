# TensorChalk Frontend

## Dependencies
- [NodeJS](https://nodejs.org/en/) (0.12 or greater)
- NPM
- Bower
- Zurb Foundation CLI tool


## Installing NodeJS and NPM

### Linux

You may the .tar.xz file and install it from the [nodejs.org](https://nodejs.org/) web site. Alternatively you may use your package manager to install as follows

#### Ubuntu/Linux Mint/Debian
```bash
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && sudo apt install -y nodejs
```

#### RHEL/Fedora
```bash
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - && yum -y install nodejs
```

#### Arch Linux
```bash
pacman -S nodejs npm
```

#### Gentoo
```bash
emerge nodejs
```

Other linux distrubitions may want to install the .tar.xz file as mentioned above

### macOS

You may simply download the Macintosh Installer direct from the [nodejs.org](https://nodejs.org/) web site or any of the following methods.

#### using Bash
```bash
curl "https://nodejs.org/dist/latest/node-${VERSION:-$(wget -qO- https://nodejs.org/dist/latest/ | sed -nE 's|.*>node-(.*)\.pkg</a>.*|\1|p')}.pkg" > "$HOME/Downloads/node-latest.pkg" && sudo installer -store -pkg "$HOME/Downloads/node-latest.pkg" -target "/"
```

#### using Homebrew
```bash
brew install node
```

#### using MacPorts
```bash
port install nodejs6
```

### Windows
You may simply download the Windows Installer direct from the [nodejs.org](https://nodejs.org/) web site or any of the following methods.

#### using Chocolatey:
```bash
cinst nodejs.install
```

#### using Scoop:
```bash
scoop install nodejs
```

## Installing/Updating Bower

The Foundation CLI Tool can be downloaded using the following commands

```bash
npm install -g bower
```

If you already have the CLI Tool and want to update it use this command

```bash
npm update -g bower
```

## Installing/Updating Foundation CLI Tool

The Foundation CLI Tool can be downloaded using the following commands

```bash
npm install -g foundation-cli
```

If you already have the CLI Tool and want to update it use this command

```bash
npm update -g foundation-cli
```


## Downloading Site Dependencies

A few more things need to be downloaded which will help in compiling the site (development purposes only). Issuing the following commands will install everything for you

```bash
npm install && bower install
```


## Testing the site

Issuing the following command on the command line will compile all the components and pull up `localhost:8000` in your default web browser.

```bash
foundation watch
```