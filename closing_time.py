import webbrowser
import schedule
import time

def job():
  webbrowser.open("https://www.youtube.com/watch?v=xGytDsqkQY8")
  return


schedule.every().day.at("21:56").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
