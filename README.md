# Stockypy
A small Python Stock Calculator for a more efficient Stock Picking Experience


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

![Screenshot_txt](https://user-images.githubusercontent.com/55713049/66148070-692e0680-e610-11e9-911d-c88c2bb7db3b.png)



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
