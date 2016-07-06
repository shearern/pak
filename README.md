General Package Manager (PAK)
=============================

This project is intended to provide a lightweight tool to create custom packages for deploying files.
Many package managers exist already for different platforms, and this tool is not an alternative to those.
Rather, the example use case of this tool is packaging your own web application code to deploy to web servers.
It focuses on packaging up files, and then installing, upgrading, and removing packaged files from target hosts.

Features
--------

In the spirit of keeping things lightweight, here are some of the things that this tool *doesn't* do: 

 - Create repositories of packages
 - Retrieve packages from repositories
 - Track package dependencies

Here's what it does do:

 - *Nothing Yet :-)*

**TODO:** 

 - Package up a directory of files to be "deployed" or "installed" on another host.
 - Install a package into a directory of your choosing.
 - Remove a previously installed package, removing all installed files.
 - Remove "expired" files while upgrading when it was previously installed, but no longer in the package.
 - Won't clobber existing files should you install into an existing directory structure.
 - Usable on host where you have command line access but very limited permissions.
 - Usable for installing to hosts over FTP.
 - Usable for installing to hosts over SFTP.
 - Interactively merge changes when installed files are changed on the target host
   (e.g.: Configuration files). 
 - Set permissions on installed files
 - Map owner and group to target host UIDs and GIDs.
 - Create self-installing executable packages (for Linux at least).
 
 
Why PAK?
--------

Why develop another tool rather than use an existing package manager or just use zip/tar/rar?

That's a fair question.  I think that other tools could have sufficed, but I found that I desired a tool that was
simpler than building .debs and .rpms, but smarter than a basic file archive like tar and zip.
For my specific needs, checkout the section below entitled "Drupal Deployment Use Case."


Basic Usage
-----------

### Creating a new package

Create the source you wish to package, say under $HOME/my_app

Execute 'pack create' to Create a new package 

    $ pak create my_app/ 1.0.0 my_app-1.0.0.pak
   
   
### Installing a package

    $ pak install my_app-1.0.0.pak /var/www/my_app
   
   
### Upgrading a package

    $ pak upgrade my_app-1.1.0.pak /var/www/my_app
   

### Removing a package

    $ pak uninstall /var/www/my_app
   

Drupal Deployment Use Case
--------------------------

*TODO*