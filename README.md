# In-Memory-Database

[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg)](https://github.com/badges/shields/stargazers)

In-Memory Database created in Python which **runs as a REPL and stores data in that session** which can also be saved as file. It also supports loading data from an existing file.

[Report Bug](https://github.com/9teen26/In-Memory-Database/issues)

---

## Features
- **Supported commands**: SET <key> <value>, GET <key>, DEL <key>, and EXISTS <key>
- **Store and Load files**: SAVE <filename> (stores current data to file) and LOAD <filename> (loads data from file)
- **Validated command parsing**: input validation, missing-key error handling and file handling
