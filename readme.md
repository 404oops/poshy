<img title="Poshy" alt="Poshy" src="images/poshy.png" width="256" height="256">

## Poshy, The extensible shell
You can contact us via <a href="https://discord.gg/R5ExvA63Jz">Our Discord!</a>

Poshy is a shell similar to zsh, but written in python, so it'll have the a different functionality than zsh. It's independent of a config file, and since it's written in python, you'll have no problem mixing and matching your own Poshy-spins

## Usage
Just install it and run the `start-poshy` file. It's written in bash, so you'll know exactly what the code is

## AYP DOCUMENTATION
AYP (All your plugins) are simple plugins that run before the shell does. There's not API you need to learn before making a plugin or program.

For the file structure and installation, AYP recommends you use `bash` for the simplicity of the installation. The things you need to learn before starting are:

1. That we strictly moderate your plugins
2. That we can control them
3. That you must'nt make a virus of sort with your AYP plugin

The file structure is:

1. Using `curl` or `wget` to download the bundle
2. Extracting the bundle
3. Putting it in the `programs` dir and
4. Putting ```echo 'import bin.programs.<AYPNAME> >> ayploader.py```, while replacing \<AYPNAME> with your package name

Package manager coming soon, make sure you make `carapace` your installation hosting subdomain 
