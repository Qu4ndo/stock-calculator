# Stockypy
A small Python Stock Calculator for a more efficient Stock Picking Experience

![stockypy](https://user-images.githubusercontent.com/55713049/66148900-3b49c180-e612-11e9-8309-ae32e84aaf7b.png)

## Usage

Follow the Instruction given in the Terminal.

**Attention:**
Please don't input any Symbols (like %)!



## Functions

The Calculator has following options:


**Inputs:**

  - Earnings per Share (EPS) Data from the Past
  - Assumption of Future Interest (%) for Earnings per Share (EPS)
  - Assumption of Future Interest for Price-Earnings Ratio (P/E Ratio)


**Outputs:**

  - Average Interest from the Past
  - EPS in 10 Years
  - Price per Share (PPS) in 10 Years
  - Fair Price per Share (Present) - with 12% Interest/Year
  - Save Calculation into file



## Usecase

If you are using a Linux machine you can easily make this script executable.

Include following code in the first line of the stocky.py script:
```
#!/usr/bin/env python3
```

Then make the stocky.py script executable with following command in the terminal:
```
chmod +x stocky.py
```

After that you can simply add a shortcut on your desktop or start it with:
```
./stock.py
```



## Future Expansions

  - Comparison of different Stocks
  - Best-, Worst- and Normal Case Output
