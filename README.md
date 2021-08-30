# subfind
SubDomain Finder Scanner With CLI 

<p align="center">
  <a name="top" href="#">
     <img alt="aaaaaa" height="cover" width="cover" src="Screenshot_2021-04-27_06_30_02.png"/>
  </a>
</p>

# Installation
<details open>
<summary> pydroid / Linux</summary>

- ```bash
  $ apt update && apt upgrade
  ```

- ```bash
  $ apt install python git -y
  ```

- ```bash
  $ git clone https://github.com/pengode-handal/subfind
  ```

- ```bash
  $ pip3 install requests
  ```

- ```bash
  $ cd subfind
  ```

# Usage

<p>for help</p>

- ```bash
  $ python3 run.py -h/--help
  ```

<p>for see the version</p>

- ```bash
  $ python3 run.py -v/--version
  ```
<p>for scanning the web</p>

- ```bash
  $ python3 run.py -d/--domain [the domain]
  Example
  $ python3 run.py -d google.com
  ```

<p>for scanning the web and save the result in the file</p>

- ```bash
  $ python3 run.py -d/--domain [the domain] -s/--save [filename]
  Example
  $ python3 run.py -d google.com -s result
  ```
