from flask import Flask, request, redirect
import time
import threading

app = Flask(__name__)

 balance = 1000

 balance_lock = threading.Lock()

@app.route("/", methods=["GET"])
def index():
    global balance
    return f"""
    <h2>Bank Balance</h2>
    <p>Current Balance: <b>{balance}</b></p>
    <br>
    <form method="POST" action="/withdraw">
        <input name="amount" type="number" placeholder="Amount" value="500" />
        <button>Withdraw</button>
    </form>
    """

@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
    amount = int(request.form.get("amount", 0))

     with balance_lock:           # the bug was fixed 'cause we lock the threads
        print(f"[DEBUG] Thread {threading.get_ident()} acquired lock")
        
         if balance >= amount:
            temp = balance
            time.sleep(1)    
            balance = temp - amount
            print(f"[DEBUG] Thread {threading.get_ident()} WRITE balance={balance}")
        else:
            print(f"[-] Thread {threading.get_ident()} Insufficient balance")
            
     return redirect("/")

if __name__ == "__main__":
    app.run(port=5000, threaded=True)
