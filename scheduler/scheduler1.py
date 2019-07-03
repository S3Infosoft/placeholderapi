import schedule
import time

def invoke_email_workflow():
    print("Check for pending emails in Queue and Send Email...")

def invoke_automation_workflow():
    print("Check for pending automation runs in Queue and Invoke mvr automation API...")

if __name__ == "__main__":
    try:
        schedule.every(3).seconds.do(invoke_email_workflow)
        schedule.every(5).seconds.do(invoke_automation_workflow)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Graceful Exit..")

