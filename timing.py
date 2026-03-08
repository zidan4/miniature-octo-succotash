def wait_for_browser(browser):
    
  # wait for the browser to finish loading a page
  while browser.ReadyState != 4 and browser.ReadyState != "complete":
    time.sleep(0.1)
  
  return
