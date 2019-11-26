# linkedin-job-search-automation
Automation of LinkedIn's sign in and job search process using Python.

## Motivation
Sometimes you may just want to perform a quick job search without doing multiple clicks across pages and waiting for the browser to load each time or you may be multitasking. This project addresses that 'adversity' by automating the entire process with just a few fields to be filled by the user. 

(Ofcourse you can have your credentials saved with bookmarked pages or use the LinkedIn app, but I personally do not prefer saving my credentials anywhere)

## Prerequisites

1. Installing Python 3.7.3
    -> https://www.python.org/downloads/

2. Installing selenium package and interfacing with required Web Driver modules ( Project uses Chrome as the browser)
    
      ``` 
      pip install selenium 
      
      ```
   For more information -> https://selenium-python.readthedocs.io/
   

## How It Works 
On running GUI.pyw, the user is prompted with a GUI that takes in login credentials, job keywords and location as input. 


<p align="center">
<img src="https://github.com/haneef-khan/linkedin-job-search-automation/blob/master/screenshots/ezgif.com-crop.gif">
</p>

Once the user submits the form, the bot does the rest of the work by submitting these details according to the pages and landing at the required page. 

<p align="center">
<img src="https://github.com/haneef-khan/linkedin-job-search-automation/blob/master/screenshots/ezgif.com-crop-1.gif">
</p>

   
### Acknowledgements

Hat tip to the those whose tutorials were referenced for inspiration and fixes

      
    

