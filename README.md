# OpenFisca Aotearoa


## Get Started 

Requirements:

* Docker

```
# Using the `Dockerfile` in this repo build a docker container tagged/named `openfisca`
docker build . -t openfisca 

# to run openfisca and connect log/error output to your terminal
docker run -v ${PWD}:/openfisca -p 5000:5000 -t openfisca

# To run in background (see it running using `docker ps` and logs with `docker logs openfisca`
docker run -v ${PWD}:/openfisca -p 5000:5000 -t openfisca -d 

```

*Note that we're using -v to map the local directory inside of the container 
so you shouldn't have to rebuild the container while developing and 
testing changes in your development environment. If you have something running locally on port 5000, you can change the `-p 5000:5000` to an unocupied local port like 5005 like this: `-p 5005:5000`*


## Writing the Legislation

This is an experiment. We've coded large swathes of New Zealand's legislation, regulation, and some government policy into rules that run in the Open Fisca calculation engine. We've released all the code here, for anyone to use.

From late January 2018, the Service Innovation Lab (LabPlus) facilitated a cross-agency and multidisciplinary team in a 3 week Discovery Sprint exploring the challenges and opportunities of developing human and machine consumable legislation for effective and efficient service delivery.

Please also read [the wiki](https://github.com/ServiceInnovationLab/openfisca-aotearoa/wiki) as a way of introduction.

### The Lab Team's server

An instance of Open Fisca is running at
[http://rac.g0v.nz/](http://rac.rg0v.nz/)


## Installing this Country Package (Aotearoa New Zealand)

Supported platforms:
- GNU/Linux distributions (in particular Debian and Ubuntu);
- Mac OS X;
- Microsoft Windows (we recommend using [ConEmu](https://conemu.github.io/) instead of the default console).

Other OS should work if they can execute Python and NumPy.

Pick option (A) or (B)


### A. Minimal Installation - for users running the rules

Follow this installation if you wish to:
  - run calculations on a large population;
  - run your own instance of OpenFisca-Aotearoa
  - run your own instance of the OpenFisca-Aotearoa rules package, as an OpenFisca Web API.
  - **not** modify the rules

There are 3 documented ways to do this - Pick your tech:
  * [Run in docker](SETUP-docker.md) to run on an instance or your laptop
  * [Setup pew and install from pip](SETUP-pew.md) to manage virtualenvs
  * [Run on heroku's PaaS cloud](https://heroku.com/deploy)

### B. Advanced Installation - for devs, modifying the rules and code

Follow this tutorial if you wish to change the OpenFisca-Aotearoa rules or contribute to the source code.

Read the [Setup Aotearoa Open Fisca in pyenv](SETUP-pyenv.md) instructions to manage python runtimes and eggs

`pyenv` is simular to rbenv/rvm (for ruby) and nvm (for nodejs).

## Next Steps

- To write new legislation, read [the wiki](https://github.com/ServiceInnovationLab/openfisca-aotearoa/wiki) along with the OpenFisca [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html) section.
- To contribute to the code, read our [contribution doc](https://github.com/ServiceInnovationLab/openfisca-aotearoa/blob/master/CONTRIBUTING.md).
