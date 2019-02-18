# call-data-count

This is a script to perform some analytics function on the provided call data for some given dates

# Analytics-output

This file will output four things with the respective UID of calls:-

1)Total Count:-No of calls total that happened after the UID is activated

2)Connected:-No of calls connected out of the total count

3)is_confirmed:-if the calls are confirmed or not value bool:- 0 or 1

4)Total Time:-Total time duration of the calls

## Installation

Need Python3 installed to run this file 

```bash
python3 createcsv.py
```

## Usage

``
Enter start date
2019-02-01
Enter end date 
2019-02-04
--FILE OPTIONS--
requirements.txt app.py 2019-02-01.csv 2019-02-04.csv 2019-02-03.csv mydatabase.db result.py test2.py 2019-02-02.csv 1-6feb.csv  
 Enter File name 
 1-6feb.csv

```
## Output

Csv file with each date and their data will be output and saved in the current dir

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
