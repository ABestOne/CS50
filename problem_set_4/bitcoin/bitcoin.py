import sys
import requests

def main():
    # 1. 检查命令行参数
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # 2. 尝试转换为 float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3. 调用 CoinCap API
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()  # 检查 HTTP 错误
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")
    except (KeyError, ValueError):
        sys.exit("Invalid API response")

    # 4. 计算并输出
    amount = n * price
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
