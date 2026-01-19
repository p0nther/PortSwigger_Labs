from flask import Flask, request, redirect
import time
import threading

app = Flask(__name__)

 balance = 1000

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

# steps:
# - read
# - check    the race window between check and update  , to fix it must made it as one block and lock the threads till the block finished
# - update
@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
     amount = int(request.form.get("amount", 0))

     if balance >= amount:
         temp = balance
        print(f"[DEBUG] Thread={threading.get_ident()} READ balance={temp}")
    # here we have the bug "race.window"
         time.sleep(1)

         balance = temp - amount 
         
        print(f"[DEBUG] Thread={threading.get_ident()} WRITE balance={balance}")
        print("[+] Withdraw success")
    else:
        print("[-] Insufficient balance")
 
    return redirect("/")

if __name__ == "__main__":
    print("[*] Flask bank app started on http://127.0.0.1:5000")
    app.run(port=5000, threaded=True)
