# Log Analysis Project

## Project Overview
>In this project, you will use a database to run queries and ask questions and
answer three questions.

### Installing the Virtual Machine
>The VM is a Linux server system that runs on top pf your own computer. You will
be running a web service inside the VM which you'll be able to access from your
regular browser.

#### Downloads:
  * [Python](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  * [git-scm.com](https://git-scm.com/downloads)

#### Use a terminal:
>You'll be doing these exercises using Unix-style terminal on you computer. If
you are using Mac or Linux system, your regular terminal program will do just
fine. On Windows use the Git Bash terminal that comes with the Git software.

#### Install VirtualBox:
>VirtualBox is the software that actually runs the virtual machine. Install the
platform package for your OS. You do not need the extension pack or the SDK. You
do not need to launch VirtualBox after installing it: Vagrant will hangle that

#### Install Vagrant:
>Vagrant is the software that configures the VM and lets you share files between
your host computer and the VM's file system. Install the version for you OS.
**Windows users may need to grant network permissions or make firewall
exceptions. This needs to be done!**

#### Download the VM configuration:
  * [ FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

  > You will end up with a new director containing the VM files. Change to this
  directory in your terminal with cd. inside, you will find another directory
  call vagrant. Change to the vagrant directory.

#### Starting the VM:
> From your terminal, inside the vagrant subdirectory, run the command
**vagrant up**. This will cause Vagrant to download the Linux OS and install it.
This will take awhile. When **vagrant up** is finished running you will get
your shell prompt back. At this point you can run **vagrant ssh** to log in to
the newly installed VM.

#### Running the database;
  * [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

>  To load the data, **cd** into the **vagrant** directory and use the command
**psql - d news -f newsdata.sql** Running this command will connect your
installed databse server and execute the SQL command in the downloaded file.

#### Explore the data:
> Once you have the data loaded into your database, connect to your database
using **psql -d news** and explore the tables using the **\dt** and
**\d** *then enter the table name*.

# Views that need to be re-created;

## View 1 for question 1:
'''
  CREATE VIEW most_pop as
  select title, count( * ) as views  
  from log join articles
  on log.path = concat('/article/', articles.slug)
  group by title
  order by views desc
  limit 3;
'''

## View 2 for question 2:
'''
  CREATE VIEW top_authors as
  SELECT authors.name,
  count( * ) as views
  FROM articles
  join authors on articles.author = authors.id
  join log on log.path
  like CONCAT('/article/', articles.slug)
  group by authors.name
  order by views desc;
'''  

## Views 3 for question 3:
'''
CREATE VIEW er_percent as
  select to_char(date, 'FMMonth FMDD, YYYY'),
  err/total as ratio  from (select time::date as date,
  count( * ) as total, sum((status != '200 OK')::int)::float as err
  from log  group by date) as errors where err/total > 0.01;
'''
