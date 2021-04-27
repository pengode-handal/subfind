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
<details open>
<summary> show helper</summary>

- ```bash
  $ python3 run.py -h/--help
  ```
<details open>
<summary> show version </summary>
- ```bash
  $ python3 run.py -v/--version
  ```
<details open>
<summary> scan a domain</summary>
- ```bash
  $ python3 run.py -d/--domain [the domain]
  Example
  $ python3 run.py -d google.com
  ```
<details open>
<summary>scan the domain and save the result</summary>
- ```bash
  $ python3 run.py -d/--domain [the domain] -s/--save [filename]
  Example
  $ python3 run.py -d google.com -s result
  ```
## Note: When usage save, dont use .txt, .html, .php, .py, etc
