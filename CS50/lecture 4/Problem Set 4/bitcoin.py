import sys
import requests


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


    api_key = "b4468a89e820db4f757c7dcd627e06e619bd6e0eaf3dd9e911b9017737159040"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data")


    total = n * price

    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
