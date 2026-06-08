def zuri_bot():
    print("Hello, I am Zuri your safaricom assistant!")
    print("Ask me about bundles, data, mpesa, airtime and more!")
    message = input("you: ").lower()   
    if "hello" in message or "hi" in message or "hey" in message or "greetings" in message:
        print("zuri hello, how can I help you today.")
    elif "bundles" in message:
        print("Zuri: you can buy bundles using *544# or Mysafaricom app.")
    elif "mpesa" in message:
        print("Zuri: Use *334# or sim tool kit or Mpesa app for services.")
    elif "airtime" in message:
        print("Zuri: Buy airtime via *544# or Mysafaricom app.")
    elif "reverse" in message:
        print("Zuri: To initiate a refund, forward the transaction details to 456.")
    elif "agent" in message:
        print("Zuri: To talk to an agent dial 100 for customer support services.")
    else:
        print("Zuri: I did not understand your request. Ask me about bundles, mpesa, airtime, internet, refunds or agents.")

zuri_bot()
