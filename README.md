# SteamCase
Hello and Welcome in the SteamCase repository.

This repository is all about virtual items (more precisely, cases/containers) in a videogame known as Counter Strike Global Offensive/Counter Strike 2.

The aim of this project is to obtain raw data on existing crates/containers from a platform where these items are traded and to establish correlations between variables, as well as to gain insight into how and why the prices of said crates actually fluctuate in said platform.


Now something about files and their funtions.

First one main.py is scraper. Which means that it crawls the specified url and based on filters implemented using the python library BeautifulSoup saves raw data based on those filters.

The next file is currency_Swap.py. This file deals with the preparation of data in order to have everything ready for file #3 Analysis.py.

The purpose of the final Analysis.py file is to obtain clarifying information about this project goal based on linear regression.
