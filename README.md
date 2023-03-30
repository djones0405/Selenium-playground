# Selenium-playground
Selenium playground 
There are several types of options that can be used with Selenium webdrivers. Here are some of the most common ones:

    --headless: This option runs the browser in headless mode, which means that there is no GUI. This is useful for running tests or scraping data without having to interact with the browser.

    --disable-gpu: This option disables the GPU hardware acceleration in the browser, which can sometimes cause issues.

    --no-sandbox: This option disables the sandbox mode in the browser, which can sometimes cause issues on certain systems.

    --disable-extensions: This option disables any extensions or plugins that are installed in the browser.

    --start-maximized: This option starts the browser in a maximized window.

    --incognito: This option opens the browser in incognito or private browsing mode.

    --window-size: This option sets the size of the browser window, which can be useful for testing responsive designs.
    
    options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
