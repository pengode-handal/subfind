# subfind
SubDomain Finder Scanner With CLI 

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
  $ git clone https://github.com/BabwaXgura/subfind
  ```

- ```bash
  $ pip3 install requests
  ```

- ```bash
  $ cd subfind
  ```

# Usage

<p> show helper</p>

- ```bash
  $ python3 run.py -h/--help
  ```


<p> show version </p>
- ```bash
  $ python3 run.py -v/--version
  ```

<p> scan a domain</p>
- ```bash
  $ python3 run.py -d/--domain [the domain]
  Example
  $ python3 run.py -d google.com
  ```


<p>scan the domain and save the result</p>
- ```bash
  $ python3 run.py -d/--domain [the domain] -s/--save [filename]
  Example
  $ python3 run.py -d google.com -s result
  ```

## Note: When usage save, dont use .txt, .html, .php, .py, etc
